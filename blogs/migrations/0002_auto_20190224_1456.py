# Generated by Django 2.1.7 on 2019-02-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='delete',
            field=models.BooleanField(choices=[('1', 'Delete'), ('0', 'Alive')], default='0'),
        ),
    ]
