from django.db import models


class API(models.Model):
    name = models.CharField(max_length=255, null=True)
    photo = models.ImageField(upload_to='images/', null=True)
    role = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True)
    specialization = models.TextField(null=True)
    institution = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name