# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-06 00:14
from __future__ import unicode_literals

import contentcuration.models
from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0084_auto_20180329_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentnode',
            name='aggregator',
            field=models.CharField(blank=True, default=b'', help_text='Who gathered this content together?', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contentnode',
            name='provider',
            field=models.CharField(blank=True, default=b'', help_text='Who distributed this content?', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='content_defaults',
            field=jsonfield.fields.JSONField(default={b'aggregator': None, b'author': None, b'auto_derive_audio_thumbnail': True, b'auto_derive_document_thumbnail': True, b'auto_derive_exercise_thumbnail': True, b'auto_derive_html5_thumbnail': True, b'auto_derive_video_thumbnail': True, b'auto_randomize_questions': True, b'copyright_holder': None, b'language': None, b'license': None, b'license_description': None, b'm_value': 5, b'mastery_model': b'num_correct_in_a_row_5', b'n_value': 5, b'provider': None}),
        ),
        migrations.AlterField(
            model_name='channel',
            name='preferences',
            field=models.TextField(default=b'{"auto_derive_exercise_thumbnail": true, "auto_derive_video_thumbnail": true, "m_value": 5, "language": null, "license": null, "author": null, "aggregator": null, "auto_randomize_questions": true, "auto_derive_document_thumbnail": true, "copyright_holder": null, "auto_derive_html5_thumbnail": true, "provider": null, "auto_derive_audio_thumbnail": true, "license_description": null, "n_value": 5, "mastery_model": "num_correct_in_a_row_5"}'),
        ),
        migrations.AlterField(
            model_name='contentnode',
            name='author',
            field=models.CharField(blank=True, default=b'', help_text='Who created this content?', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='content_defaults',
            field=jsonfield.fields.JSONField(default={b'aggregator': None, b'author': None, b'auto_derive_audio_thumbnail': True, b'auto_derive_document_thumbnail': True, b'auto_derive_exercise_thumbnail': True, b'auto_derive_html5_thumbnail': True, b'auto_derive_video_thumbnail': True, b'auto_randomize_questions': True, b'copyright_holder': None, b'language': None, b'license': None, b'license_description': None, b'm_value': 5, b'mastery_model': b'num_correct_in_a_row_5', b'n_value': 5, b'provider': None}),
        ),
        migrations.AlterField(
            model_name='user',
            name='preferences',
            field=models.TextField(default=b'{"auto_derive_exercise_thumbnail": true, "auto_derive_video_thumbnail": true, "m_value": 5, "language": null, "license": null, "author": null, "aggregator": null, "auto_randomize_questions": true, "auto_derive_document_thumbnail": true, "copyright_holder": null, "auto_derive_html5_thumbnail": true, "provider": null, "auto_derive_audio_thumbnail": true, "license_description": null, "n_value": 5, "mastery_model": "num_correct_in_a_row_5"}'),
        ),
    ]