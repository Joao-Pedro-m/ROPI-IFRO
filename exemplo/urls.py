from django.urls import path
from exemplo import views

app_name = 'exemplo'

urlpatterns = [
    path('',views.AdministradoresList.as_view(), name='list'),
    path('create/',views.AdministradoresCreate.as_view(), name='create'),
    path('update/<int:pk>/',views.AdministradoresUpdate.as_view(), name='update')
]
