from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('events/', views.events, name='events'),
    path('news/', views.news, name='news'),
    path('leadership/', views.leadership, name='leadership'),
    path('resources/', views.resources, name='resources'),
    path('media-gallery/', views.media_gallery, name='media_gallery'),
    path('membership/', views.membership, name='membership'),
    path('partners/', views.partners, name='partners'),
    path('contact/', views.contact, name='contact'),
]
