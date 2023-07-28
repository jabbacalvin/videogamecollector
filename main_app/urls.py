from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('videogames/', views.videogames_index, name='index'),
  path('videogames/<int:videogame_id>/', views.videogames_detail, name='detail'),
  path('videogames/create/', views.VideoGameCreate.as_view(), name='videogames_create'),
  path('videogames/<int:pk>/update', views.VideoGameUpdate.as_view(), name='videogames_update'),
  path('videogames/<int:pk>/delete', views.VideoGameDelete.as_view(), name='videogames_delete'),
  path('videogames/<int:videogame_id>/add_stream/', views.add_stream, name='add_stream'),
  path('videogames/<int:videogame_id>/assoc_platform/<int:platform_id>/', views.assoc_platform, name='assoc_platform'),
  path('videogames/<int:videogame_id>/unassoc_platform/<int:platform_id>/', views.unassoc_platform, name='unassoc_platform'),
  path('platforms/', views.PlatformList.as_view(), name='platforms_index'),
  path('platforms/<int:pk>/', views.PlatformDetail.as_view(), name='platforms_detail'),
  path('platforms/create/', views.PlatformCreate.as_view(), name='platforms_create'),
  path('platforms/<int:pk>/update/', views.PlatformUpdate.as_view(), name='platforms_update'),
  path('platforms/<int:pk>/delete/', views.PlatformDelete.as_view(), name='platforms_delete'),
]