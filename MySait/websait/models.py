from django.db import models


class Webdev(models.Model):
    title = models.CharField('Textname', max_length=50)
    task = models.TextField('Undertext')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
