from django.db import models
#from django.contrib.auth import get_user_model
# Create your models here.

#User=get_user_model()

class todo(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=300)
    date_add =models.DateTimeField(auto_now_add=True)
    date_todo = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.desc
