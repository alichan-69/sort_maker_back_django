from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator


class User(models.Model):
    id = models.CharField(
        primary_key=True, editable=False, max_length=255, validators=[MinLengthValidator(1)])
    name = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    access_token = models.CharField(
        max_length=255, validators=[MinLengthValidator(1)])
    secret = models.CharField(max_length=255, validators=[
                              MinLengthValidator(1)])
    delete_flg = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Sort(models.Model):
    id = models.AutoField(
        primary_key=True, auto_created=True, editable=False, validators=[MinValueValidator(1), MaxValueValidator(99999999999)])
    name = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    description = models.CharField(
        max_length=255, validators=[MinLengthValidator(1)])
    play_count = models.IntegerField(default=0,
                                     validators=[MinValueValidator(1), MaxValueValidator(99999999999)])
    user = models.ForeignKey(
        User, related_name='sorts', on_delete=models.CASCADE)
    delete_flg = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class SortItem(models.Model):
    id = models.AutoField(
        primary_key=True, auto_created=True, editable=False, validators=[MinValueValidator(1), MaxValueValidator(99999999999)])
    name = models.CharField(max_length=255, validators=[
        MinLengthValidator(1)])
    sort = models.ForeignKey(
        Sort, related_name='sort_items', on_delete=models.CASCADE)
    delete_flg = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Like(models.Model):
    id = models.AutoField(
        primary_key=True, auto_created=True, editable=False, validators=[MinValueValidator(1), MaxValueValidator(99999999999)])
    sort = models.ForeignKey(
        Sort, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='likes', on_delete=models.CASCADE)
    delete_flg = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
