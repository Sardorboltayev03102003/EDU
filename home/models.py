from django.db import models

from base.models import Basemodel


class HomePopularCourses(Basemodel):
    image = models.ImageField(upload_to="home", verbose_name="popular courses ")
    title = models.CharField(max_length=100, verbose_name="kurs haqida ")
    name = models.CharField(max_length=100, verbose_name="kurs nomi")
    views = models.IntegerField()
    old_price = models.IntegerField(verbose_name="Eski narxi ")
    new_price = models.IntegerField(verbose_name="Yangi narxi ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mashhur kurslar "




