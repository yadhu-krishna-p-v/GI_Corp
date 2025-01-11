from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    
    
    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
