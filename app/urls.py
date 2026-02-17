from django.urls import path
from app import views

urlpatterns = [
    path('task/',views.task_view, name = 'task'),
    path('delete/<int:id>/',views.delete_view, name = 'delete'),
    path('add/',views.add_view,name='add'),
    path('edit/<int:id>/',views.edit_view,name='edit'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout')
]
