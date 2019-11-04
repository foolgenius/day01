from django.db import models

# Create your models here.
class User_module(models.Model):
    SEX = (
        ('male', 'male'),
        ('female', 'female')
    )
    LOCATION = (
        ('Shanghai', 'shanghai'),
        ('Beijing', 'beijing'),
        ('Guangdong', 'guangdong'),
        ('Jiangsu', 'jiangsu'),
        ('Anhui', 'anhui'),
        ('Hunan', 'hunan'),
        ('Henan', 'hunan')

    )
    u_name = models.CharField(max_length=32, verbose_name='name')
    u_phonenum = models.CharField(max_length=20, unique=True,verbose_name='phone')
    u_sex = models.CharField(max_length=8, choices=SEX, default='male', verbose_name='sex')
    u_birthday = models.DateField(default='1990-1-1', verbose_name='birthday')
    u_avatar = models.CharField(max_length=256, verbose_name='avatar')
    u_location = models.CharField(max_length=16, choices=LOCATION, default='Beijing',verbose_name='location')

    class Meta:
        db_table = 'user_module'