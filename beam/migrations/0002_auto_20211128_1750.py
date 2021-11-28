# Generated by Django 3.2.4 on 2021-11-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beammodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='beammodel',
            name='length',
            field=models.FloatField(default=5.0),
        ),
    ]