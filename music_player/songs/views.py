from django.shortcuts import render, get_object_or_404
from .models import Song

# View برای نمایش لیست آهنگ‌ها
def song_list(request):
    songs = Song.objects.all()  # تمام آهنگ‌ها را از پایگاه داده می‌گیرد
    return render(request, 'songs/song_list.html', {'songs': songs})  # به قالب ارسال می‌کند

# View برای نمایش جزئیات یک آهنگ
def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)  # آهنگ مشخص شده را پیدا می‌کند یا 404 برمی‌گرداند
    return render(request, 'songs/song_detail.html', {'song': song})  # به قالب ارسال می‌کند
