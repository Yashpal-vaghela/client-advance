# Generated by Django 4.0.4 on 2022-06-17 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_category_banner_remove_category_canonical_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
