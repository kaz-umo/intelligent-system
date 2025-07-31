from django.urls import path
from . import views

urlpatterns = [
    path('', views.rocket_view, name='rocket'),  # http://127.0.0.1:8000/analyzer/
    path('analyze/', views.upload_text, name='upload_text'),  # http://127.0.0.1:8000/analyzer/analyze/
]
