from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.authors, name='authors'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('research/', views.research_list, name='research'),  # Research page route
    path('research/<int:research_id>/', views.research_detail, name='research_detail'),
]
