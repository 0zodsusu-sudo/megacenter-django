from django.db import models
from django.contrib.auth.models import User

# --- Модель для этажей ---
class Floor(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Этаж {self.number} — {self.name}"


# --- Модель ответов ---
class Review(models.Model):
    floor = models.ForeignKey('Floor', on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.author.username} (Этаж {self.floor.number})"

# --- Модель для фотографий этажей ---
class FloorImage(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='floor_photos/')

    def __str__(self):
        return f"Фото для {self.floor.name}"

# --- Профиль пользователя ---
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_language = models.CharField(
        max_length=10,
        choices=[
            ('ru', 'Русский'),
            ('uz', 'Oʻzbekcha'),
            ('en', 'English'),
        ],
        default='ru'
    )

    def __str__(self):
        return f"Профиль {self.user.username}"
