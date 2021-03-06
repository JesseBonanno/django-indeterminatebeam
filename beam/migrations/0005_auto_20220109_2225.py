# Generated by Django 3.2.4 on 2022-01-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beam', '0004_auto_20211128_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitoptionsmodel',
            name='A',
            field=models.CharField(choices=[('mm2', 'mm2'), ('cm2', 'cm2'), ('m2', 'm2'), ('in2', 'in2'), ('ft2', 'ft2')], default='m2', max_length=10),
        ),
        migrations.AlterField(
            model_name='unitoptionsmodel',
            name='E',
            field=models.CharField(choices=[('Pa', 'Pa'), ('kPa', 'kPa'), ('MPa', 'MPa'), ('kip/in2', 'kip/in2'), ('kip/ft2', 'kip/ft2'), ('lbf/in2', 'lbf/in2'), ('lbf/ft2', 'lbf/ft2')], default='Pa', max_length=10),
        ),
        migrations.AlterField(
            model_name='unitoptionsmodel',
            name='I',
            field=models.CharField(choices=[('mm4', 'mm4'), ('cm4', 'cm4'), ('m4', 'm4'), ('in4', 'in4'), ('ft4', 'ft4')], default='m4', max_length=10),
        ),
        migrations.AlterField(
            model_name='unitoptionsmodel',
            name='deflection',
            field=models.CharField(choices=[('mm', 'mm'), ('cm', 'cm'), ('m', 'm'), ('in', 'in'), ('ft', 'ft')], default='m', max_length=10),
        ),
        migrations.AlterField(
            model_name='unitoptionsmodel',
            name='distributed',
            field=models.CharField(choices=[('N/mm', 'N/mm'), ('kN/mm', 'kN/mm'), ('N/m', 'N/m'), ('kN/m', 'kN/m'), ('kip/ft', 'kip/ft'), ('kip/in', 'kip/in'), ('lbf/ft', 'lbf/ft'), ('lbf/in', 'lbf/in')], default='N/m', max_length=10),
        ),
        migrations.AlterField(
            model_name='unitoptionsmodel',
            name='force',
            field=models.CharField(choices=[('N', 'N'), ('kN', 'kN'), ('lbf', 'lbf'), ('kip', 'kip')], default='N', max_length=10),
        ),
        migrations.AlterField(
            model_name='unitoptionsmodel',
            name='length',
            field=models.CharField(choices=[('mm', 'mm'), ('cm', 'cm'), ('m', 'm'), ('in', 'in'), ('ft', 'ft')], default='m', max_length=10),
        ),
        migrations.AlterField(
            model_name='unitoptionsmodel',
            name='moment',
            field=models.CharField(choices=[('N.mm', 'N.mm'), ('kN.mm', 'kN.mm'), ('N.m', 'N.m'), ('kN.m', 'kN.m'), ('lbf.ft', 'lbf.ft'), ('kip.ft', 'kip.ft'), ('lbf.in', 'lbf.in'), ('kip.in', 'kip.in')], default='N.m', max_length=10),
        ),
        migrations.AlterField(
            model_name='unitoptionsmodel',
            name='stiffness',
            field=models.CharField(choices=[('N/mm', 'N/mm'), ('kN/mm', 'kN/mm'), ('N/m', 'N/m'), ('kN/m', 'kN/m'), ('kip/ft', 'kip/ft'), ('kip/in', 'kip/in'), ('lbf/ft', 'lbf/ft'), ('lbf/in', 'lbf/in')], default='N/m', max_length=10),
        ),
        migrations.AlterField(
            model_name='unitoptionsmodel',
            name='units',
            field=models.CharField(choices=[('SI', 'SI'), ('metric', 'metric'), ('imperial', 'imperial')], default='SI', max_length=64),
        ),
    ]
