from django.shortcuts import render
from rest_framework.views import viewsets
from django.views.decorator import api_view
from rest_framework.response import Response
from rest_framework import status
from movie.serializers import MovieSerializer
from movie.models import Model
# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

@api_view(['GET'])
def get_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if movie is not None:
        return Response(movie, status=status.HTTP_200_OK)
    return Response({"error": f"{movie_id} not found"})

@api_view(['POST'])
def save_movie(request):
    serializers = MovieSerializer(request.POST or None, request.FILES or None)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if movie is not None:
        serializers = MovieSerializer(data=request.POST, instance=movie)
        if serializers.is_valid():
            serializers.save()
            return Response({"detail": "Movie updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id):
    if movie is not None:
        movie.delete()
        return Response({"detail": "successfully deleted movie"}, status=status.HTTP_204_NO_CONTENT)
    return Response({"detail": f"{movie_id} not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_movie_by_category(request, category):
    movie = Movie.objects.filter(category=category).all()
    if len(movie) > 1:
        return Response({'data': movie}, status=status.HTTP_200_OK)
    return Response({'data': 'no movies for this category'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_movie_by_category_detail(request, category, movie_id):
    movie = Movie.objects.filter(category=category, id=movie_id).first()
    if not movie:
        return Response({"detail": "No Movie found"}, status=status.HTTP_404_NOT_FOUND)
    return Response({'data': movie}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_movie(request):
    all_movies = Movie.objects.all()
    if len(all_movies) > 1:
        return Response({'data': all_movies}, status=status.HTTP_200_OK)
    return Response({'detail': 'No moie found'}, status=status.HTTP_404_NOT_FOUND)




