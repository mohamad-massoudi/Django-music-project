from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),  # لیست آهنگ‌ها
    path('<int:song_id>/', views.song_detail, name='song_detail'),  # جزئیات آهنگ
]
