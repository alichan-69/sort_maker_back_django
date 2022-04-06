from audioop import minmax
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator


class Sort(models.Model):
    id = models.AutoField(
        primary_key=True, auto_created=True, editable=False, validators=[MinValueValidator(1), MaxValueValidator(99999999999)])
    name = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    description = models.CharField(
        max_length=255, validators=[MinLengthValidator(1)])
    image = models.CharField(max_length=2083,  validators=[
                             MinLengthValidator(1)])
    user_id = models.CharField(max_length=255,  validators=[
                               MinLengthValidator(1)])
    delete_flg = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
