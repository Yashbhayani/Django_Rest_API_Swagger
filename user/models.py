from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)

    class Meta:
        db_table='users'


