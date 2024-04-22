from django.db import models
from django.contrib.auth.models import User


class S3File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    category = models.CharField(max_length=255)
