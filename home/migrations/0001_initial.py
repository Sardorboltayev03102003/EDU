# Generated by Django 5.0.1 on 2024-01-30 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePopularCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='home', verbose_name='popular courses ')),
                ('title', models.CharField(max_length=100, verbose_name='kurs haqida ')),
                ('name', models.CharField(max_length=100, verbose_name='kurs nomi')),
                ('views', models.IntegerField()),
                ('old_price', models.IntegerField(verbose_name='Eski narxi ')),
                ('new_price', models.IntegerField(verbose_name='Yangi narxi ')),
            ],
            options={
                'verbose_name': 'Mashhur kurslar ',
            },
        ),
    ]
