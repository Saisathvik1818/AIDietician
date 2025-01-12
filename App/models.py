from django.db import models


class onlineuser(models.Model):
    name = models.CharField(max_length=100);
    email = models.CharField(max_length=100);
    pwd = models.CharField(max_length=100);
    gender = models.CharField(max_length=100);
    phone = models.CharField(max_length=100);


class performance(models.Model):
    alg_name = models.CharField(max_length=100)
    sc1 = models.FloatField()
    sc2 = models.FloatField()
    sc3 = models.FloatField()
    sc4 = models.FloatField()


class chat(models.Model):
    name=models.CharField(max_length=100);
    email=models.CharField(max_length=100);
    message=models.TextField();


class cal_dataset(models.Model):
    cal = models.FloatField();
    label = models.CharField(max_length=100);


class food_cal_dataset(models.Model):
    food = models.CharField(max_length=100);
    serve = models.CharField(max_length=100);
    cal = models.FloatField();
    

    

