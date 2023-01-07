from django.db import models
from django.conf import settings
# Create your models here.

class Word(models.Model):
    name = models.CharField(max_length=100)
    faTranslate = models.TextField()
    enTranslate = models.TextField()
    voice = models.FileField()
    image = models.FileField()
    def __str__(self):
        return self.name


class WordDescription(models.Model):
    wordId = models.ForeignKey(Word, null=True, on_delete=models.CASCADE)
    # مهم
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    image = models.FileField(blank=True)
    text = models.TextField(blank=True)