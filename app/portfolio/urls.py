# portfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('stats/', views.stats, name='stats'),
    path('portfolio/', views.portfolio_page, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('currents/', views.currents, name='currents'),
    path('misc/', views.misc, name='misc'),
]
