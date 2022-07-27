from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Person(User):

    class Meta:
        proxy = True

    def characterstics(self):
        return CharacteristicsUser.objects.filter(user_id=self.id).select_related(rbCharacteristics)

    def actions(self):
        return ActionUser.objects.filter(user_id=self.id).select_related(rbAction)


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CharacteristicsUser(TimeStampMixin):
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='user_dinamic')
    characteristic_id = models.ForeignKey('rbCharacteristics', verbose_name='Характеристика', on_delete=models.CASCADE)
    value = models.FloatField('Значение')
    visible = models.BooleanField('Показывать', default=True)

    class Meta:
        verbose_name_plural = 'Характеристики пользователя'
        verbose_name = 'Характеристика пользователя'

    def __str__(self):
        return self.user_id.last_name + self.characteristic_id.name


class ActionUser(TimeStampMixin):
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE,
                                related_name='user_action')
    action_id = models.ForeignKey('rbAction', verbose_name='Действие', on_delete=models.CASCADE)
    value = models.CharField('Значение', max_length=200)
    visible = models.BooleanField('Показывать', default=True)
    start_datetime = models.DateTimeField('Время начала действия', default=datetime.today)
    end_datetime = models.DateTimeField('Время окончания действия', default=datetime.today)

    class Meta:
        verbose_name_plural = 'Действия пользователя'
        verbose_name = 'Действие пользователя'

    def get_str_value(self):
        result = ''
        if self.action_id.is_vector:
            values = self.value.split(',')
            units = self.action_id.unit.split(',')
            for value, unit in zip(values, units):
                result += value + ' ' + unit + ','
        return result[:-1]

    def __str__(self):
        return self.user_id.last_name + ',' + self.action_id.name


class rbCharacteristics(TimeStampMixin):
    name = models.CharField('Название', max_length=50)
    code = models.CharField('Код', max_length=50)
    unit = models.CharField('Eд.изм.', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Характеристики'
        verbose_name = 'Характеристика'


class rbAction(TimeStampMixin):
    Type = (
        ('I', 'Integer'),
        ('F', 'Float'),
        ('C', 'Char'),
    )
    name = models.CharField('Название', max_length=50)
    code = models.CharField('Код', max_length=50)
    unit = models.CharField('Eд.изм.', max_length=20)
    type = models.CharField('Тип данных', choices=Type, max_length=10)
    is_vector = models.BooleanField('Вектор', default=False)

    @property
    def get_number_args(self):
        return len(self.unit.split(','))

    def __str__(self):
        return self.name + ','+ str(self.unit)

    class Meta:
        verbose_name_plural = 'Действия'
        verbose_name = 'Действие'


class rbEvent(TimeStampMixin):
    name = models.CharField('Название', max_length=50)
    code = models.CharField('Код', max_length=50)

    class Meta:
        verbose_name_plural = 'События'
        verbose_name = 'Событие'