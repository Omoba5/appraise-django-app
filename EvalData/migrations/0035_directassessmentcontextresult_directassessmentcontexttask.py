# Generated by Django 2.2 on 2019-05-17 17:07
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign', '0010_merge_20190517_0925'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EvalData', '0034_textpairwithcontext'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectAssessmentContextTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('dateActivated', models.DateTimeField(blank=True, null=True, verbose_name='Date activated')),
                ('dateCompleted', models.DateTimeField(blank=True, null=True, verbose_name='Date completed')),
                ('dateRetired', models.DateTimeField(blank=True, null=True, verbose_name='Date retired')),
                ('dateModified', models.DateTimeField(blank=True, null=True, verbose_name='Date modified')),
                ('activated', models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Activated?')),
                ('completed', models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Completed?')),
                ('retired', models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Retired?')),
                ('rawData', models.TextField(blank=True, editable=False, verbose_name='Raw data')),
                ('_str_name', models.TextField(blank=True, default='', editable=False)),
                ('requiredAnnotations', models.PositiveSmallIntegerField(help_text='(value in range=[1,50])', verbose_name='Required annotations')),
                ('batchNo', models.PositiveIntegerField(help_text='(1-based)', verbose_name='Batch number')),
                ('activatedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontexttask_activated_by', related_query_name='evaldata_directassessmentcontexttasks', to=settings.AUTH_USER_MODEL, verbose_name='Activated by')),
                ('assignedTo', models.ManyToManyField(blank=True, db_index=True, help_text='(users working on this task)', related_name='evaldata_directassessmentcontexttask_assignedTo', related_query_name='evaldata_directassessmentcontexttasks', to=settings.AUTH_USER_MODEL, verbose_name='Assigned to')),
                ('batchData', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontexttask_batchData', related_query_name='evaldata_directassessmentcontexttasks', to='Campaign.CampaignData', verbose_name='Batch data')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontexttask_campaign', related_query_name='evaldata_directassessmentcontexttasks', to='Campaign.Campaign', verbose_name='Campaign')),
                ('completedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontexttask_completed_by', related_query_name='evaldata_directassessmentcontexttasks', to=settings.AUTH_USER_MODEL, verbose_name='Completed by')),
                ('createdBy', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontexttask_created_by', related_query_name='evaldata_directassessmentcontexttasks', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('items', models.ManyToManyField(related_name='evaldata_directassessmentcontexttask_items', related_query_name='evaldata_directassessmentcontexttasks', to='EvalData.TextPairWithContext', verbose_name='Items')),
                ('modifiedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontexttask_modified_by', related_query_name='evaldata_directassessmentcontexttasks', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
                ('retiredBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontexttask_retired_by', related_query_name='evaldata_directassessmentcontexttasks', to=settings.AUTH_USER_MODEL, verbose_name='Retired by')),
            ],
            options={
                'ordering': ['_str_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DirectAssessmentContextResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('dateActivated', models.DateTimeField(blank=True, null=True, verbose_name='Date activated')),
                ('dateCompleted', models.DateTimeField(blank=True, null=True, verbose_name='Date completed')),
                ('dateRetired', models.DateTimeField(blank=True, null=True, verbose_name='Date retired')),
                ('dateModified', models.DateTimeField(blank=True, null=True, verbose_name='Date modified')),
                ('activated', models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Activated?')),
                ('completed', models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Completed?')),
                ('retired', models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Retired?')),
                ('rawData', models.TextField(blank=True, editable=False, verbose_name='Raw data')),
                ('_str_name', models.TextField(blank=True, default='', editable=False)),
                ('score', models.PositiveSmallIntegerField(help_text='(value in range=[1,100])', verbose_name='Score')),
                ('start_time', models.FloatField(help_text='(in seconds)', verbose_name='Start time')),
                ('end_time', models.FloatField(help_text='(in seconds)', verbose_name='End time')),
                ('activatedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontextresult_activated_by', related_query_name='evaldata_directassessmentcontextresults', to=settings.AUTH_USER_MODEL, verbose_name='Activated by')),
                ('completedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontextresult_completed_by', related_query_name='evaldata_directassessmentcontextresults', to=settings.AUTH_USER_MODEL, verbose_name='Completed by')),
                ('createdBy', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontextresult_created_by', related_query_name='evaldata_directassessmentcontextresults', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontextresult_item', related_query_name='evaldata_directassessmentcontextresults', to='EvalData.TextPairWithContext', verbose_name='Item')),
                ('modifiedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontextresult_modified_by', related_query_name='evaldata_directassessmentcontextresults', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
                ('retiredBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontextresult_retired_by', related_query_name='evaldata_directassessmentcontextresults', to=settings.AUTH_USER_MODEL, verbose_name='Retired by')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentcontextresult_task', related_query_name='evaldata_directassessmentcontextresults', to='EvalData.DirectAssessmentContextTask', verbose_name='Task')),
            ],
            options={
                'ordering': ['_str_name'],
                'abstract': False,
            },
        ),
    ]
