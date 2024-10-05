from django.conf import settings
from django.db import models

'''
    name: notify if comment on my post
    user: 

'''

class Setting(models.Model):

    name = models.CharField(max_length=128)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



