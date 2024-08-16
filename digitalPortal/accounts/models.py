from django.db import models


class UserAccount(models.Model):
    USERNAME_MAX_LENGTH = 50
    PASSWORD_MAX_LENGTH = 50

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
    )

    email = models.EmailField(
        unique=True,
    )

    creation_date = models.DateField(
        auto_now_add=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
