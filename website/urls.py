from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('media-gallery/', views.media_gallery, name='media_gallery'),
    path('membership/', views.membership, name='membership'),
    path('partners/', views.partners, name='partners'),
    path('contact/', views.contact, name='contact'),
]
