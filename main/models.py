from django.db import models
from django.urls import reverse


class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название предмета')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Subject', args=[self.slug])

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class Lectures(models.Model):
    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, verbose_name='Название леции')
    video = models.CharField(max_length=255, blank=True, verbose_name='Код видео')
    text = models.TextField(blank=True, verbose_name='Примечание')
    file = models.FileField(blank=True, verbose_name='Файл лекции')
    date = models.DateTimeField(blank=True, verbose_name='Дата леции')

    def __str__(self):
        return "{}: {}".format(self.subject, self.title)

    def get_absolute_url(self):
        return reverse('Lectures', args=[self.id])

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'