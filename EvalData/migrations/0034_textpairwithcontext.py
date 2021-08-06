# Generated by Django 2.2 on 2019-05-17 16:39
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('EvalData', '0033_auto_20190228_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextPairWithContext',
            fields=[
                ('textpair_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='EvalData.TextPair')),
                ('documentID', models.CharField(help_text='(max. 100 characters)', max_length=100, verbose_name='Document ID')),
                ('isCompleteDocument', models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Complete document?')),
                ('sourceContextLeft', models.CharField(help_text='(max. 2000 characters)', max_length=2000, verbose_name='Source context (left)')),
                ('sourceContextRight', models.CharField(help_text='(max. 2000 characters)', max_length=2000, verbose_name='Source context (right)')),
                ('targetContextLeft', models.CharField(help_text='(max. 2000 characters)', max_length=2000, verbose_name='Target context (left)')),
                ('targetContextRight', models.CharField(help_text='(max. 2000 characters)', max_length=2000, verbose_name='Target context (right)')),
            ],
            options={
                'ordering': ['_str_name'],
                'abstract': False,
            },
            bases=('EvalData.textpair',),
        ),
    ]
