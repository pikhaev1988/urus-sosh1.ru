
from django.db import models
from django.urls import reverse
class Pedagog(models.Model):
    fio = models.CharField(max_length=200, verbose_name='ФИО')
    data_roj = models.DateField(verbose_name='Дата')
    adres = models.TextField(verbose_name='Адрес')
    snils = models.CharField(verbose_name='СНИЛС', max_length=100)
    telefon = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    ser_pas = models.CharField(max_length=200, verbose_name='Серия паспорта')
    nom_pas = models.CharField(max_length=200, verbose_name='Номер паспорта')
    mesto_rab = models.CharField(max_length=200, verbose_name='Место работы')
    staj = models.CharField(max_length=200, verbose_name='Общий стаж')
    ped_staj = models.CharField(max_length=200, verbose_name='Пед. Стаж')
    kate_gor = models.CharField(max_length=200, verbose_name='Категория')
    doljnost = models.CharField(max_length=200, verbose_name='Должность')
    uch_zav = models.CharField(max_length=200, verbose_name='ВО СПО Учебное заведения')
    spec_po_dip = models.CharField(max_length=200, verbose_name='Спец по диплому')
    sroc_ob = models.CharField(max_length=200, verbose_name='Сроки обучения')
    ser_dip = models.CharField(max_length=200, verbose_name='Серия диплома')
    nom_dip = models.CharField(max_length=200, verbose_name='Номер диплота')
    kpk_god_proh = models.CharField(max_length=200, verbose_name='КПК (год прохождения последних КПК)')
    mesto_ob = models.CharField(max_length=200, verbose_name='Место обучения и тема КПК')
    photo = models.ImageField(verbose_name='Фото', upload_to='madia')
    cet = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'user'
    def __str__(self):
        return self.fio




class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')

    def __str__(self):
        return self.name

class ucheniki(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    data = models.CharField(max_length=100, verbose_name='Дата роджения')
    snils = models.CharField(max_length=100, verbose_name='СНИЛС')
    adres = models.CharField(max_length=100, verbose_name='Адрес место жительство')
    fio_ot = models.CharField(max_length=100, verbose_name='ФИО Отца')
    tel_ot = models.CharField(max_length=100, verbose_name='Телефон отца')
    mesto_rab_ot = models.CharField(max_length=100, verbose_name='Место работы отца')
    fio_mat = models.CharField(max_length=100, verbose_name='ФИО Матери')
    tel_mat = models.CharField(max_length=100, verbose_name='Телефон Матери')
    mesto_rab_mat = models.CharField(max_length=100, verbose_name='Место работы Матери')
    status = models.CharField(max_length=100, null=True, verbose_name='Социальный статус семьи')
    foto = models.ImageField(upload_to='media/ucheniki', verbose_name='Фото')
    uch = models.ForeignKey('cat_uch', on_delete=models.CASCADE, null=True, verbose_name='Класс')

    class Meta:
        db_table = 'urus_sosh1_ucheniki'

    def __str__(self):
        return self.fio


class cat_uch(models.Model):
    klass = models.CharField(max_length=20, verbose_name='Класс')
    foto = models.ImageField(upload_to='media/class', verbose_name='Фото класса' )
    klass_ruk = models.CharField(max_length=50, verbose_name='Классный руоводитель')
    opis_klass = models.TextField(blank=True)

    def __str__(self):
        return self.klass

class doc(models.Model):
    mane = models.CharField(max_length=100, verbose_name='имя')
    docs = models.FileField(upload_to='doks/')
    admini  = models.ForeignKey('adminis', on_delete=models.CASCADE, null=True, verbose_name='Группа')

    def __str__(self):
        return self.mane

class adminis(models.Model):
    name = models.CharField(max_length=200, verbose_name='администрация')

    def __str__(self):
        return self.name