# Generated by Django 4.2.3 on 2023-07-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='good',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='read',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='readtext',
            field=models.TextField(blank=True, null=True),
        ),
    ]
