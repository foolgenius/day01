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

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.u_name,
            'phonenum': self.u_phonenum,
            'sex': self.u_sex,
            'birthday': self.u_birthday,
            'avatar': self.u_avatar,
            'location': self.u_location,
        }

    class Meta:
        db_table = 'user_module'




class Profile(models.Model):
    uid = id
    dating_sex = models.CharField(max_length=8, choices=User_module.SEX)
    locations = models.CharField(max_length=16, choices=User_module.LOCATION)

    min_distance = models.IntegerField(default=1)
    max_distance = models.IntegerField(default=30)

    min_dating_age = models.IntegerField(default=18)
    max_dating_age = models.IntegerField(default=50)

    vibration = models.BooleanField(default=True)
    only_matche = models.BooleanField(default=True)
    auto_play = models.BooleanField(default=True)
#
    def to_dict(self):
        return {
        'id': self.id,
        'dating_sex': self.dating_sex,
        'dating_location': self.locations,
        'min_distance': self.min_distance,
        'max_distance': self.max_distance,
        'min_dating_age': self.min_dating_age,
        'max_dating_age': self.max_dating_age,
        'vibration': self.vibration,
        'only_matche': self.only_matche,
        'auto_play': self.auto_play,
    }