from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name="index"),
    path('blogs/<int:id>',views.blogs,name = "blogs"),
    path('old_url',views.old_url, name="old_url" ),
    path('new_view',views.new_view,name='new_url'),
]