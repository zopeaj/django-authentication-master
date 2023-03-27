from django.urls import path
from movie.views import

urlpatterns = [
    path('', name='home'),
    path('/movie/<str:category/all', name='category-all'),
    path('/movie/<str:category>/detail/<int:id', name='detail'),
    path('/movie/<int:id>/', name='delete'),
]

