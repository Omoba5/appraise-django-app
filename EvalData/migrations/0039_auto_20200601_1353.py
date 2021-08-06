# Generated by Django 2.2.12 on 2020-06-01 13:53
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('EvalData', '0038_pairwiseassessmentresult_pairwiseassessmenttask_textsegmentwithtwotargets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pairwiseassessmentresult',
            name='score2',
            field=models.PositiveSmallIntegerField(blank=True, help_text='(value in range=[1,100])', null=True, verbose_name='Score (2)'),
        ),
    ]
