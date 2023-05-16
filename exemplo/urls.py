from django.urls import path
from exemplo import views

app_name = 'exemplo'

urlpatterns = [
    path('',views.AdminList.as_view(), name=app_name)
]
