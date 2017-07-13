# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrollmotion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompressedImageOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default=b'', max_length=300)),
                ('name', models.CharField(default=b'', max_length=300)),
                ('size', models.IntegerField(default=0)),
                ('image_type', models.CharField(choices=[(b'jpg', b'jpg'), (b'png', b'png')], default=b'jpg', max_length=5)),
                ('original_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compressedimageone', to='scrollmotion.Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='image',
            name='compressed_one',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scrollmotion.CompressedImageOne'),
        ),
    ]
