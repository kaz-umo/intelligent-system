from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # ← чтобы работал редирект

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analyzer/', include('analyzer.urls')),
    path('', lambda request: redirect('analyzer/', permanent=False)),  # ← редирект с / на /analyzer/
]
