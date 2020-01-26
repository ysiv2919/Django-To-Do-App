from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'todo'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),

    #todo urls
    path('', views.index, name='index'),
    path('new-item/', views.new_item, name='new-item'),
    path('delete/<int:item>', views.delete_item, name='delete-item/>')
]
