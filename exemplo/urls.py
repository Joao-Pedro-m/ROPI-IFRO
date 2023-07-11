from django.urls import path
from exemplo import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'exemplo'

urlpatterns = [
    path('',views.ProjetosIntegradoresList.as_view(), name='list'),
    path('create/',views.ProjetosIntegradoresCreate.as_view(), name='create'),
    path('update/<int:pk>/',views.ProjetosIntegradoresUpdate.as_view(), name='update'),
    path('detail/<int:pk>/',views.ProjetosIntegradoresDetail.as_view(), name='detail'),
    path('uploadimages/', views.upload, name='upload')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
