# Generated by Django 2.1.5 on 2019-02-27 22:21
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign', '0008_auto_20171006_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campaign',
            options={'ordering': ['_str_name']},
        ),
        migrations.AlterModelOptions(
            name='campaigndata',
            options={'ordering': ['_str_name'], 'verbose_name': 'Batch', 'verbose_name_plural': 'Batches'},
        ),
        migrations.AlterModelOptions(
            name='campaignteam',
            options={'ordering': ['_str_name'], 'verbose_name': 'Team', 'verbose_name_plural': 'Teams'},
        ),
        migrations.AlterField(
            model_name='campaign',
            name='activated',
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Activated?'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='completed',
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Completed?'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='retired',
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Retired?'),
        ),
        migrations.AlterField(
            model_name='campaigndata',
            name='activated',
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Activated?'),
        ),
        migrations.AlterField(
            model_name='campaigndata',
            name='completed',
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Completed?'),
        ),
        migrations.AlterField(
            model_name='campaigndata',
            name='dataReady',
            field=models.BooleanField(blank=True, default=False, editable=False, verbose_name='Data ready?'),
        ),
        migrations.AlterField(
            model_name='campaigndata',
            name='dataValid',
            field=models.BooleanField(blank=True, default=False, editable=False, verbose_name='Data valid?'),
        ),
        migrations.AlterField(
            model_name='campaigndata',
            name='retired',
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Retired?'),
        ),
        migrations.AlterField(
            model_name='campaignteam',
            name='activated',
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Activated?'),
        ),
        migrations.AlterField(
            model_name='campaignteam',
            name='completed',
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Completed?'),
        ),
        migrations.AlterField(
            model_name='campaignteam',
            name='owner',
            field=models.ForeignKey(help_text='(must be staff member)', limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.PROTECT, related_name='campaign_campaignteam_owner', related_query_name='campaign_campaignteams', to=settings.AUTH_USER_MODEL, verbose_name='Team owner'),
        ),
        migrations.AlterField(
            model_name='campaignteam',
            name='retired',
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Retired?'),
        ),
        migrations.AlterField(
            model_name='trusteduser',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Campaign.Campaign', verbose_name='Campaign'),
        ),
        migrations.AlterField(
            model_name='trusteduser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
