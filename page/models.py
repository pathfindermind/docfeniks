# -*- coding: utf-8 -*-
from django.db import models

CHOISES = (
    (u'Все', 'Все'),
    (u'Гарантии', 'Гарантии'),
    (u'IT - консалтинг', 'IT - консалтинг'),
    (u'Оценка','Оценка'),
)

class Category(models.Model):
    name = models.CharField('Name (Eng, в нижнем регистре)', max_length=255)
    slug = models.SlugField('Slug')
    title = models.CharField('Передача названия категории в фильтр пример: .category1', max_length=255)
    section = models.CharField(u'Выберите категорию', choices=CHOISES, default="Все", max_length=255)


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'категорию'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return u'%s' % self.name


class Slider(models.Model):
    title = models.CharField(u'Заголовок', max_length=255)
    after_title = models.CharField(u'Подзаголовок', max_length=255)
    text = models.TextField(u'Текст')
    image = models.ImageField(upload_to='img/', blank=True, verbose_name='image')
    detail_url = models.CharField(u'Ссылка на детальное описание', max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'слайд'
        verbose_name_plural = u'Слайды'

class Service(models.Model):
    title = models.CharField(u'Заголовок', max_length=255)
    text = models.TextField(u'Текст')
    image = models.ImageField(upload_to='img/', blank=True, verbose_name='image')
    align = models.CharField(u'Выравнивание left или right', max_length=255)

    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = u'услугу'
        verbose_name_plural = u'Услуги'

class Project(models.Model):
    title = models.CharField(u'Заголовок', max_length=255)
    text = models.TextField(u'Текст')
    image = models.ImageField(upload_to='img/', blank=True, verbose_name='image')
    detail_url = models.CharField(u'Ссылка на страницу проекта', max_length=255)
    category = models.ForeignKey(Category, related_name='project', verbose_name = "Категория")


    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'проект'
        verbose_name_plural = u'Проекты'

class Worker(models.Model):
    name = models.CharField(u'Имя', max_length=255)
    position = models.TextField(u'Должность')
    text = models.TextField(u'Текст')
    image = models.ImageField(upload_to='img/', blank=True, verbose_name='image')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'сотрудника'
        verbose_name_plural = u'Сотрудники'

class Client(models.Model):
    name = models.CharField(u'Имя', max_length = 250)
    image = models.ImageField(upload_to='img/', blank=True, verbose_name='image')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'клиента'
        verbose_name_plural = u'Клиенты'
