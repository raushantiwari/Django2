# Generated by Django 2.1.7 on 2019-02-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20190224_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_category',
            field=models.CharField(choices=[('Pl', 'Political'), ('Mv', 'Movies'), ('WW', 'World War')], db_index=True, default='World_War', max_length=2),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='delete',
            field=models.BooleanField(choices=[('1', 'Delete'), ('0', 'Alive')], default='0', max_length=2),
        ),
    ]
