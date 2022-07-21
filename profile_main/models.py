from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class DinamicChUser(models.Model):
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='user_dinamic')
    characteristic_id = models.ForeignKey('rbCharacteristics', verbose_name='Характеристика', on_delete=models.CASCADE)
    value = models.FloatField('Значение')
    visible = models.BooleanField('Показывать', default=True)

    def __str__(self):
        return self.user_id.last_name + self.characteristic_id.name

class rbCharacteristics(models.Model):
    name = models.CharField('Название', max_length=50)
    code = models.CharField('Код', max_length=50)
    unit = models.CharField('Eд.изм.', max_length=20)
    create_date = models.DateTimeField('Дата создания', default=datetime.today)

    def __str__(self):
        return self.name

class rbEvent(models.Model):
    name = models.CharField('Название', max_length=50)
    code = models.CharField('Код', max_length=50)
    create_date = models.DateTimeField('Дата создания', default=datetime.today)