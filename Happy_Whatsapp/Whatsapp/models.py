from django.db import models

class Login(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=20)
    
    
  