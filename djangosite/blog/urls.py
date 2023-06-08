from django.urls import path
from . import views
 
urlpatterns = [
    path('',views.index,name='home'),
    path('<int:pk>', views.news_info, name='news_info'),
    path('new',views.new,name='new'),
]
