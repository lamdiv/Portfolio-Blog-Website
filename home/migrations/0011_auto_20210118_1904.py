# Generated by Django 3.1.5 on 2021-01-18 13:19

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210118_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='home.BlogCategories', to='home.Categories', verbose_name='category'),
        ),
    ]
