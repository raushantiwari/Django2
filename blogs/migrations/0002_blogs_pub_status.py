# Generated by Django 2.1.7 on 2019-02-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='pub_status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
