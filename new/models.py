from django.db import models
from django.contrib.auth.models import User

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
