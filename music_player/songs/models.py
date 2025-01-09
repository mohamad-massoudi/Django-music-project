from django.db import models  # برای استفاده از کلاس‌های مرتبط با پایگاه داده

# مدل مربوط به آهنگ‌ها
class Song(models.Model):
    title = models.CharField(max_length=200)  # عنوان آهنگ (رشته‌ای با حداکثر 200 کاراکتر)
    artist = models.CharField(max_length=100)  # نام خواننده یا هنرمند (رشته‌ای با حداکثر 100 کاراکتر)
    album = models.CharField(max_length=100, blank=True, null=True)  
    # نام آلبوم. این فیلد اختیاری است (می‌تواند خالی یا Null باشد)
    release_date = models.DateField(blank=True, null=True)  
    # تاریخ انتشار آهنگ. این فیلد هم اختیاری است.
    file = models.FileField(upload_to='songs/')  
    # فیلدی برای آپلود فایل آهنگ. فایل‌ها در پوشه‌ای به نام `songs/` ذخیره می‌شوند.
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)  
    # فیلدی برای آپلود تصویر جلد آهنگ. تصویرها در پوشه‌ای به نام `covers/` ذخیره می‌شوند. این فیلد اختیاری است.

    def __str__(self):
        """
        متدی که مشخص می‌کند هنگام نمایش آبجکت مدل در رابط کاربری
        یا در چاپ، چه چیزی نمایش داده شود.
        """
        return self.title  # عنوان آهنگ را به‌عنوان نمایش اصلی برمی‌گرداند


# مدل مربوط به لیست‌های پخش (Playlist)
class Playlist(models.Model):
    name = models.CharField(max_length=100)  # نام لیست پخش (رشته‌ای با حداکثر 100 کاراکتر)
    songs = models.ManyToManyField(Song, related_name='playlists')  
    # رابطه چند به چند با مدل `Song`. هر لیست پخش می‌تواند چندین آهنگ داشته باشد و هر آهنگ می‌تواند در چند لیست پخش باشد.
    created_at = models.DateTimeField(auto_now_add=True)  
    # تاریخ ایجاد لیست پخش. به‌طور خودکار زمان ایجاد را ثبت می‌کند.

    def __str__(self):
        """
        متدی که مشخص می‌کند هنگام نمایش آبجکت مدل در رابط کاربری
        یا در چاپ، چه چیزی نمایش داده شود.
        """
        return self.name  # نام لیست پخش را به‌عنوان نمایش اصلی برمی‌گرداند
