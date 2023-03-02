from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    
    class Meta:
        verbose_name = ("UserModel")
        verbose_name_plural = ("UserModels")

    def __str__(self):
        return self.name
