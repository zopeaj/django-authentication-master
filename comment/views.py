from django.shortcuts import render
from rest_framework.views.decorator import api_view
from rest_framework.response import Response
from rest_framework import status
from comment.models import Comment
from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET'])
def get_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment is not None:
        return Response(comment, status=status.HTTP_200_OK)
    return Response({"error": f"Comment with {comment_id} not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_comment(request):
    user = User.objects.get(username=request.user.username)
    if not user:
        return Response({"detail": f"{request.user.username} not found"}, status=status.HTTP_404_NOT_FOUND)

    serializers = CommentSerializer(user=user, data=request.POST)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_comment(request, comment_id, account_id):
    user = User.objects.get(id=account_id)
    if not user:
        return Response({"detail": f"user with {account_id} not found"}, status=status.HTTP_404_NOT_FOUND)

    comment = Comment.objects.get(id=comment_id)
    if not comment:
        return Response({"detail": f"comment with {comment_id} not found"}, status=status.HTTP_404_NOT_FOUND)

    serializers = CommentSerializer(user=user, data=request.POST)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment is not None:
        comment.delete()
        return Response({"detail": "Success"}, status=status.HTTP_204_NO_CONTENT)
    return Response({"error": f"{comment_id} not found"})


