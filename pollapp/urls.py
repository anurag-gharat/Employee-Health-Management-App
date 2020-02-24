from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('poll/',include('poll.urls')),
    path('admin/', admin.site.urls),
]
