# Generated by Django 2.2.5 on 2021-01-31 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20210131_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='contact',
            field=models.CharField(max_length=15),
        ),
    ]
