from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('market', views.market, name='market'),
    path('about', views.about,name='aboutUS')
]