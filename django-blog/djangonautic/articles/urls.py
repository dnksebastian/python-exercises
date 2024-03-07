from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<slug:slug>/', views.article_detail), #re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail),
    
]
