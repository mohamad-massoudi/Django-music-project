from django.urls import path  # این خط را اضافه کنید
from . import views

urlpatterns = [
    path("", views.song_list, name="song_list"),  # لیست آهنگ‌ها
    path("<int:song_id>/", views.song_detail, name="song_detail"),  # جزئیات آهنگ
    path("add/", views.add_song, name="add_song"),  # افزودن آهنگ جدید
    path("<int:song_id>/edit/", views.edit_song, name="edit_song"),  # ویرایش آهنگ
    path("<int:song_id>/delete/", views.delete_song, name="delete_song"),  # حذف آهنگ
    path("search/", views.search_songs, name="search_songs"),  # جستجوی آهنگ‌ها
    path("playlists/", views.playlist_list, name="playlist_list"),  # لیست لیست‌های پخش
    path(
        "playlists/<int:playlist_id>/", views.playlist_detail, name="playlist_detail"
    ),  # جزئیات لیست پخش
    path("playlists/add/", views.add_playlist, name="add_playlist"),
    path("signup/", views.signup, name="signup"),  # ثبت‌نام# افزودن لیست پخش
    path("accounts/logout/", views.custom_logout_view, name="logout"),  # لاگ‌اوت سفارشی
]
