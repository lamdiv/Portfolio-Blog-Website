# Generated by Django 3.1.5 on 2021-01-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='images',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]