# Generated by Django 3.1.7 on 2021-03-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='prix',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
