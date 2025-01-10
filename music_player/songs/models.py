from django.db import models

# مدل برای آهنگ‌ها
class Song(models.Model):
    title = models.CharField(max_length=200)  # عنوان آهنگ
    artist = models.CharField(max_length=100)  # نام خواننده
    album = models.CharField(max_length=100, blank=True, null=True)  # نام آلبوم (اختیاری)
    release_date = models.DateField(blank=True, null=True)  # تاریخ انتشار آهنگ
    file = models.FileField(upload_to='songs/')  # فایل آهنگ (آپلود شده در media/songs/)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)  # تصویر جلد آهنگ (اختیاری)

    def __str__(self):
        return self.title  # نمایش عنوان آهنگ در پنل مدیریت


# مدل برای لیست‌های پخش
class Playlist(models.Model):
    name = models.CharField(max_length=100)  # نام لیست پخش
    description = models.TextField(blank=True, null=True)  # توضیحات (اختیاری)
    songs = models.ManyToManyField('Song', related_name='playlists')  # رابطه چند به چند با مدل Song
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد لیست پخش

    def __str__(self):
        return self.name  # نمایش نام لیست پخش در پنل مدیریت
