# Generated by Django 4.1.4 on 2022-12-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0014_stlfile_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stlfile',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
