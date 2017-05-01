# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 14:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('dateActivated', models.DateTimeField(blank=True, null=True, verbose_name='Date activated')),
                ('dateCompleted', models.DateTimeField(blank=True, null=True, verbose_name='Date completed')),
                ('dateRetired', models.DateTimeField(blank=True, null=True, verbose_name='Date retired')),
                ('activated', models.BooleanField(default=False, verbose_name='Activated?')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed?')),
                ('retired', models.BooleanField(default=False, verbose_name='Retired?')),
                ('marketID', models.CharField(editable=False, max_length=42, unique=True)),
                ('sourceLanguageCode', models.CharField(help_text='(max. 10 characters)', max_length=10, verbose_name='Source language')),
                ('targetLanguageCode', models.CharField(help_text='(max. 10 characters)', max_length=10, verbose_name='Target language')),
                ('domainName', models.CharField(help_text='(max. 20 characters)', max_length=20, verbose_name='Domain name')),
                ('activatedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_market_activated_by', related_query_name='evaldata_markets', to=settings.AUTH_USER_MODEL, verbose_name='Activated by')),
                ('completedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_market_completed_by', related_query_name='evaldata_markets', to=settings.AUTH_USER_MODEL, verbose_name='Completed by')),
                ('createdBy', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_market_created_by', related_query_name='evaldata_markets', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('retiredBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_market_retired_by', related_query_name='evaldata_markets', to=settings.AUTH_USER_MODEL, verbose_name='Retired by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('dateActivated', models.DateTimeField(blank=True, null=True, verbose_name='Date activated')),
                ('dateCompleted', models.DateTimeField(blank=True, null=True, verbose_name='Date completed')),
                ('dateRetired', models.DateTimeField(blank=True, null=True, verbose_name='Date retired')),
                ('activated', models.BooleanField(default=False, verbose_name='Activated?')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed?')),
                ('retired', models.BooleanField(default=False, verbose_name='Retired?')),
                ('corpusName', models.CharField(help_text='(max. 100 characters)', max_length=100, verbose_name='Corpus name')),
                ('versionInfo', models.CharField(help_text='(max. 20 characters)', max_length=20, verbose_name='Version info')),
                ('source', models.CharField(help_text='(max. 250 characters)', max_length=250, verbose_name='Source')),
                ('activatedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_metadata_activated_by', related_query_name='evaldata_metadatas', to=settings.AUTH_USER_MODEL, verbose_name='Activated by')),
                ('completedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_metadata_completed_by', related_query_name='evaldata_metadatas', to=settings.AUTH_USER_MODEL, verbose_name='Completed by')),
                ('createdBy', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_metadata_created_by', related_query_name='evaldata_metadatas', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='EvalData.Market')),
                ('retiredBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_metadata_retired_by', related_query_name='evaldata_metadatas', to=settings.AUTH_USER_MODEL, verbose_name='Retired by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('dateActivated', models.DateTimeField(blank=True, null=True, verbose_name='Date activated')),
                ('dateCompleted', models.DateTimeField(blank=True, null=True, verbose_name='Date completed')),
                ('dateRetired', models.DateTimeField(blank=True, null=True, verbose_name='Date retired')),
                ('activated', models.BooleanField(default=False, verbose_name='Activated?')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed?')),
                ('retired', models.BooleanField(default=False, verbose_name='Retired?')),
                ('itemID', models.PositiveIntegerField(help_text='(1-based)', verbose_name='Item ID')),
                ('sourceText', models.CharField(help_text='(max. 250 characters)', max_length=250, verbose_name='Source text')),
                ('targetText', models.CharField(help_text='(max. 250 characters)', max_length=250, verbose_name='Target text')),
                ('activatedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_textpair_activated_by', related_query_name='evaldata_textpairs', to=settings.AUTH_USER_MODEL, verbose_name='Activated by')),
                ('completedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_textpair_completed_by', related_query_name='evaldata_textpairs', to=settings.AUTH_USER_MODEL, verbose_name='Completed by')),
                ('createdBy', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_textpair_created_by', related_query_name='evaldata_textpairs', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('metadata', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='EvalData.Metadata')),
                ('retiredBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_textpair_retired_by', related_query_name='evaldata_textpairs', to=settings.AUTH_USER_MODEL, verbose_name='Retired by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextSegment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('dateActivated', models.DateTimeField(blank=True, null=True, verbose_name='Date activated')),
                ('dateCompleted', models.DateTimeField(blank=True, null=True, verbose_name='Date completed')),
                ('dateRetired', models.DateTimeField(blank=True, null=True, verbose_name='Date retired')),
                ('activated', models.BooleanField(default=False, verbose_name='Activated?')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed?')),
                ('retired', models.BooleanField(default=False, verbose_name='Retired?')),
                ('itemID', models.PositiveIntegerField(help_text='(1-based)', verbose_name='Item ID')),
                ('segmentText', models.CharField(help_text='(max. 250 characters)', max_length=250, verbose_name='Segment text')),
                ('activatedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_textsegment_activated_by', related_query_name='evaldata_textsegments', to=settings.AUTH_USER_MODEL, verbose_name='Activated by')),
                ('completedBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_textsegment_completed_by', related_query_name='evaldata_textsegments', to=settings.AUTH_USER_MODEL, verbose_name='Completed by')),
                ('createdBy', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_textsegment_created_by', related_query_name='evaldata_textsegments', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('metadata', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='EvalData.Metadata')),
                ('retiredBy', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_textsegment_retired_by', related_query_name='evaldata_textsegments', to=settings.AUTH_USER_MODEL, verbose_name='Retired by')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
