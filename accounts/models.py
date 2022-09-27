# accounts - models.py

from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class ServiceUser(AbstractUser):

    KeywordChoices = (
            ("적금", "적금"),
            ("주거", "주거"),
            ("창업", "창업"),
            ("교육", "교육"),
            ("장학", "장학"),
            ("재테크", "재테크"),
            ("주식", "주식"),
            ("교통", "교통")
        )

    keyword1 = models.CharField(max_length=20, choices=KeywordChoices, default="적금", null=True)
    keyword2 = models.CharField(max_length=20, choices=KeywordChoices, default="주거", null=True)