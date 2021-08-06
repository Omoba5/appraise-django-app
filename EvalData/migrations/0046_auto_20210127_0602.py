# Generated by Django 2.2.12 on 2021-01-27 06:02
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('EvalData', '0045_merge_20210112_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textpairwithdomain',
            name='documentURL',
        ),
        migrations.AddField(
            model_name='textpairwithdomain',
            name='sourceURL',
            field=models.TextField(blank=True, verbose_name='Source URL'),
        ),
        migrations.AddField(
            model_name='textpairwithdomain',
            name='targetURL',
            field=models.TextField(blank=True, verbose_name='Target URL'),
        ),
    ]
