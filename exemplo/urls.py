from django.urls import path
from exemplo import views

app_name = 'exemplo'

urlpatterns = [
    path('',views.ProjetosIntegradoresList.as_view(), name='list'),
    path('create/',views.ProjetosIntegradoresCreate.as_view(), name='create'),
    path('update/<int:pk>/',views.ProjetosIntegradoresUpdate.as_view(), name='update')
]
