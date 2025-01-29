from django.urls import path
from .views import TemplateListCreateAPIView, TemplateDetailAPIView, ContentDetailAPIView, ContentListCreateAPIView

urlpatterns = [
    path('templates/', TemplateListCreateAPIView.as_view(), name='template-list-create'),
    path('templates/<int:pk>/', TemplateDetailAPIView.as_view(), name='template-detail'), 


    path('templates/<int:template_id>/content/', ContentListCreateAPIView.as_view(), name='content-list-create'),
    path('content/<int:pk>/', ContentDetailAPIView.as_view(), name='content-detail'),


]
