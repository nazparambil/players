from django.db import models

# Create your models here.
class players(models.Model):
    id=models.AutoField(primary_key=True)
    player_name=models.CharField(max_length=20)
    def __str__(self):
        return self.player_name
    player_email=models.EmailField()
    country=models.CharField(max_length=20)
    games=models.IntegerField()
    total=models.IntegerField()
