# Generated by Django 3.2.6 on 2021-08-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210814_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Password',
            field=models.CharField(max_length=150),
        ),
    ]