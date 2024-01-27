# urls.py

from django.urls import path
from neighborhoods_api import views

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    # List all Blog1 instances for a neighborhood
    path('api/blog1/neighborhood/<str:neighborhood_name>/', views.Blog1ListByNeighborhood.as_view(), name='blog1-neighborhood'),

    # List all Blog1 categories for a neighborhood
    path('api/blog1/category/neighborhood/<str:neighborhood_name>/', views.Blog1CategoryListByNeighborhood.as_view(), name='blog1-category-neighborhood'),

    # List all Blog2 instances for a neighborhood
    path('api/blog2/neighborhood/<str:neighborhood_name>/', views.Blog2ListByNeighborhood.as_view(), name='blog2-neighborhood'),

    # List all Blog2 categories for a neighborhood
    path('api/blog2/category/neighborhood/<str:neighborhood_name>/', views.Blog2CategoryListByNeighborhood.as_view(), name='blog2-category-neighborhood'),

    # List all BoardMinutes for a neighborhood
    path('api/board-minutes/neighborhood/<str:neighborhood_name>/', views.BoardMinutesListByNeighborhood.as_view(), name='board-minutes-neighborhood'),

    # List all Blog1 instances by category and neighborhood
    path('api/blog1/neighborhood/<str:neighborhood_name>/category/<str:category_name>/', views.Blog1ListByCategoryAndNeighborhood.as_view(), name='blog1-category-neighborhood'),

    # List all Blog2 instances by category and neighborhood
    path('api/blog2/neighborhood/<str:neighborhood_name>/category/<str:category_name>/', views.Blog2ListByCategoryAndNeighborhood.as_view(), name='blog2-category-neighborhood'),

]
