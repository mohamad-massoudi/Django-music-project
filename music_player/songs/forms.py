from django import forms
from .models import Song
from .models import Playlist


class SongForm(forms.ModelForm):
    class Meta:
        model = Song  # مدل مرتبط با این فرم
        fields = [
            "title",
            "artist",
            "album",
            "release_date",
            "file",
            "cover",
        ]  # فیلدهایی که در فرم نمایش داده می‌شوند

    def clean_file(self):
        """
        بررسی نوع فایل صوتی و اعتبارسنجی آن
        """
        file = self.cleaned_data.get("file")
        if file:
            # بررسی فرمت فایل
            if not file.name.endswith((".mp3", ".wav", ".aac")):
                raise forms.ValidationError(
                    "Only MP3, WAV, and AAC files are supported."
                )
        return file


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = [
            "name",
            "description",
            "songs",
        ]  # فیلدهایی که در فرم نمایش داده می‌شوند
        widgets = {
            "songs": forms.CheckboxSelectMultiple(),  # نمایش آهنگ‌ها به صورت چک‌باکس
        }
