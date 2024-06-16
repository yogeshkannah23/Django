from . import views
from django.urls import path

app_name = "myblog"


urlpatterns = [
    path('',views.index,name="index"),
    path('blogs/<int:id>',views.blogs,name = "blogs"),
    path('blog/<int:id>',views.detail,name="detail"),
    path('old_url',views.old_url, name="old_url" ),
    path('new_view_da',views.new_view,name='new_page_url'),
]