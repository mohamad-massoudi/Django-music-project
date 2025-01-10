from django.contrib import admin
from django.urls import path, include  # برای مدیریت مسیرهای اپلیکیشن‌ها
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),  # مسیر پنل مدیریت
    path("", include("songs.urls")),  # اتصال مسیرهای اپلیکیشن songs به پروژه
    path("accounts/", include("django.contrib.auth.urls")),
    # مسیرهای پیش‌فرض احراز هویت
]

# ارائه فایل‌های رسانه‌ای در حالت توسعه
if settings.DEBUG:  # اگر حالت DEBUG فعال باشد
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
