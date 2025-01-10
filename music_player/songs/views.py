from django.shortcuts import render, get_object_or_404, redirect
from .models import Song
from .forms import SongForm
from django.db.models import Q  # برای جستجوی پیچیده
from .models import Playlist, Song
from .forms import PlaylistForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


# نمایش لیست آهنگ‌ها
def song_list(request):
    songs = Song.objects.all()  # تمام آهنگ‌ها از پایگاه داده گرفته می‌شوند
    return render(request, "songs/song_list.html", {"songs": songs})


# نمایش جزئیات یک آهنگ
def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)  # آهنگ مورد نظر پیدا می‌شود
    return render(request, "songs/song_detail.html", {"song": song})


# افزودن آهنگ جدید
def add_song(request):
    if request.method == "POST":
        form = SongForm(
            request.POST, request.FILES
        )  # داده‌های فرم و فایل‌ها دریافت می‌شوند
        if form.is_valid():
            form.save()  # آهنگ جدید ذخیره می‌شود
            return redirect("song_list")  # بازگشت به لیست آهنگ‌ها
    else:
        form = SongForm()  # فرم خالی برای افزودن آهنگ جدید
    return render(request, "songs/add_song.html", {"form": form})


# View برای ویرایش یک آهنگ
def edit_song(request, song_id):
    # دریافت آهنگ بر اساس شناسه، اگر پیدا نشد خطای 404 برمی‌گرداند
    song = get_object_or_404(Song, id=song_id)

    if request.method == "POST":
        # ایجاد فرم با داده‌های ارسال شده توسط کاربر و فایل‌ها
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            # ذخیره تغییرات در پایگاه داده
            form.save()
            return redirect(
                "song_detail", song_id=song.id
            )  # بازگشت به صفحه جزئیات آهنگ
    else:
        # نمایش فرم با داده‌های موجود در آهنگ
        form = SongForm(instance=song)

    # ارسال فرم به قالب
    return render(request, "songs/edit_song.html", {"form": form, "song": song})


# View برای حذف یک آهنگ
def delete_song(request, song_id):
    # دریافت آهنگ بر اساس شناسه، اگر پیدا نشد خطای 404 برمی‌گرداند
    song = get_object_or_404(Song, id=song_id)

    if request.method == "POST":
        # حذف آهنگ از پایگاه داده
        song.delete()
        return redirect("song_list")  # بازگشت به صفحه لیست آهنگ‌ها

    # نمایش صفحه تأیید حذف
    return render(request, "songs/delete_song.html", {"song": song})


# View برای جستجو در لیست آهنگ‌ها
def search_songs(request):
    query = request.GET.get("q")  # دریافت عبارت جستجو از URL
    if query:
        # جستجو در عنوان و نام خواننده
        songs = Song.objects.filter(
            Q(title__icontains=query) | Q(artist__icontains=query)
        )
    else:
        songs = Song.objects.all()  # اگر جستجو انجام نشده، تمام آهنگ‌ها نمایش داده شوند

    return render(
        request, "songs/search_results.html", {"songs": songs, "query": query}
    )

    # نمایش تمام لیست‌های پخش


def playlist_list(request):
    playlists = Playlist.objects.all()  # تمام لیست‌های پخش
    return render(request, "songs/playlist_list.html", {"playlists": playlists})


# نمایش جزئیات یک لیست پخش
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(
        Playlist, id=playlist_id
    )  # پیدا کردن لیست پخش با شناسه
    return render(request, "songs/playlist_detail.html", {"playlist": playlist})


# افزودن لیست پخش جدید
def add_playlist(request):
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("playlist_list")
    else:
        form = PlaylistForm()
    return render(request, "playlists/add_playlist.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ورود خودکار پس از ثبت‌نام
            return redirect("song_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def custom_logout_view(request):
    """
    سفارشی کردن عملکرد لاگ‌اوت برای هدایت کاربر به صفحه اصلی یا هر صفحه دیگر
    """
    logout(request)
    return redirect("song_list")  # هدایت به لیست آهنگ‌ها یا صفحه اصلی
