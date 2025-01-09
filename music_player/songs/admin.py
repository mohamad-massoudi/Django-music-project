from django.contrib import admin  # برای ثبت مدل‌ها در پنل مدیریت
from .models import Song, Playlist  # ایمپورت مدل‌های Song و Playlist

# ثبت مدل Song در پنل مدیریت
admin.site.register(Song)

# ثبت مدل Playlist در پنل مدیریت
admin.site.register(Playlist)
