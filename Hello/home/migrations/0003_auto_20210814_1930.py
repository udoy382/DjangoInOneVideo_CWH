# Generated by Django 3.2.6 on 2021-08-14 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210813_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Re_Password',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Password',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
