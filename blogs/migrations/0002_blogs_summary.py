# Generated by Django 2.1.7 on 2019-02-27 07:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_squashed_0005_auto_20190224_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='summary',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
