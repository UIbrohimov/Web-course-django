from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# bu class Model histoblanadi django tilida
# baza dannix tilida tablitsa hisoblanadi
class New(models.Model):
    # Many To One Relation
    author = models.ForeignKey(
        User,
        verbose_name="Muallif",
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    title = models.CharField("Sarlavha", max_length=255)
    body = models.TextField("Asosiy qism")
    image = models.ImageField("Rasm", upload_to="news/", blank=True, null=True)
    created = models.DateTimeField("Sana", auto_now=True)

    class Meta:
        verbose_name = "yangilik"
        verbose_name_plural = "Yangiliklar"

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name="Muallif",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )
    post = models.ForeignKey(
        New,
        verbose_name="Post",
        on_delete=models.SET_NULL,
        related_name="comments",
        null=True,
        blank=True
        )
    body = models.TextField("Izoh")
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.body[:20]}..."

    class Meta:
        verbose_name = "izoh"
        verbose_name_plural = "Izohlar"
