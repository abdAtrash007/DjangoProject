from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:post_id>',views.getPost,name='post'),
    path('category',views.getCategory,name='getCategory'),
    path('category/<int:category_id>',views.findCategory,name='findCategory')
    
]