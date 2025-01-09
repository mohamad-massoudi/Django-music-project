from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL پنل مدیریت
    path('', include('songs.urls')),  # اتصال URLهای اپلیکیشن songs
]
