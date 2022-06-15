from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField("Savol", max_length=255)

    def __str__(self):
        return self.question


class Choice(models.Model):
    # ForeignKey - Many To One relation - Bir nechta -> bittaga
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField("Variant", max_length=255)
    is_correct = models.BooleanField("To'g'ri", default=False)

    def __str__(self):
        return self.choice
