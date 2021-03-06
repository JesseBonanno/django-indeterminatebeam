# Generated by Django 3.2.4 on 2022-01-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beam', '0005_auto_20220109_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unitoptionsmodel',
            name='A',
        ),
        migrations.RemoveField(
            model_name='unitoptionsmodel',
            name='E',
        ),
        migrations.RemoveField(
            model_name='unitoptionsmodel',
            name='I',
        ),
        migrations.RemoveField(
            model_name='unitoptionsmodel',
            name='deflection',
        ),
        migrations.RemoveField(
            model_name='unitoptionsmodel',
            name='distributed',
        ),
        migrations.RemoveField(
            model_name='unitoptionsmodel',
            name='force',
        ),
        migrations.RemoveField(
            model_name='unitoptionsmodel',
            name='length',
        ),
        migrations.RemoveField(
            model_name='unitoptionsmodel',
            name='moment',
        ),
        migrations.RemoveField(
            model_name='unitoptionsmodel',
            name='stiffness',
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='A_i',
            field=models.CharField(choices=[('in2', 'in2'), ('ft2', 'ft2')], default='in2', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='A_m',
            field=models.CharField(choices=[('mm2', 'mm2'), ('cm2', 'cm2'), ('m2', 'm2')], default='mm2', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='E_i',
            field=models.CharField(choices=[('kip/in2', 'kip/in2'), ('kip/ft2', 'kip/ft2'), ('lbf/in2', 'lbf/in2'), ('lbf/ft2', 'lbf/ft2')], default='kip/in2', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='E_m',
            field=models.CharField(choices=[('Pa', 'Pa'), ('kPa', 'kPa'), ('MPa', 'MPa')], default='MPa', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='I_i',
            field=models.CharField(choices=[('in4', 'in4'), ('ft4', 'ft4')], default='in4', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='I_m',
            field=models.CharField(choices=[('mm4', 'mm4'), ('cm4', 'cm4'), ('m4', 'm4')], default='mm4', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='deflection_i',
            field=models.CharField(choices=[('in', 'in'), ('ft', 'ft')], default='in', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='deflection_m',
            field=models.CharField(choices=[('mm', 'mm'), ('cm', 'cm'), ('m', 'm')], default='mm', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='distributed_i',
            field=models.CharField(choices=[('kip/ft', 'kip/ft'), ('kip/in', 'kip/in'), ('lbf/ft', 'lbf/ft'), ('lbf/in', 'lbf/in')], default='kip/ft', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='distributed_m',
            field=models.CharField(choices=[('N/mm', 'N/mm'), ('kN/mm', 'kN/mm'), ('N/m', 'N/m'), ('kN/m', 'kN/m')], default='kN/m', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='force_i',
            field=models.CharField(choices=[('lbf', 'lbf'), ('kip', 'kip')], default='kip', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='force_m',
            field=models.CharField(choices=[('N', 'N'), ('kN', 'kN')], default='kN', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='length_i',
            field=models.CharField(choices=[('in', 'in'), ('ft', 'ft')], default='ft', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='length_m',
            field=models.CharField(choices=[('mm', 'mm'), ('cm', 'cm'), ('m', 'm')], default='m', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='moment_i',
            field=models.CharField(choices=[('lbf.ft', 'lbf.ft'), ('kip.ft', 'kip.ft'), ('lbf.in', 'lbf.in'), ('kip.in', 'kip.in')], default='kip.ft', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='moment_m',
            field=models.CharField(choices=[('N.mm', 'N.mm'), ('kN.mm', 'kN.mm'), ('N.m', 'N.m'), ('kN.m', 'kN.m')], default='kN.m', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='stiffness_i',
            field=models.CharField(choices=[('kip/ft', 'kip/ft'), ('kip/in', 'kip/in'), ('lbf/ft', 'lbf/ft'), ('lbf/in', 'lbf/in')], default='kip/ft', max_length=10),
        ),
        migrations.AddField(
            model_name='unitoptionsmodel',
            name='stiffness_m',
            field=models.CharField(choices=[('N/mm', 'N/mm'), ('kN/mm', 'kN/mm'), ('N/m', 'N/m'), ('kN/m', 'kN/m')], default='kN/mm', max_length=10),
        ),
    ]
