# Generated by Django 4.0.4 on 2022-06-17 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_author_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='category',
            name='canonical',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='keyword',
        ),
        migrations.RemoveField(
            model_name='category',
            name='og_card',
        ),
        migrations.RemoveField(
            model_name='category',
            name='og_site',
        ),
        migrations.RemoveField(
            model_name='category',
            name='og_type',
        ),
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
    ]
