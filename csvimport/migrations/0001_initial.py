# Generated by Django 3.0.5 on 2020-04-26 16:22

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField(default=0, null=True)),
                ('longitude', models.FloatField(default=0, null=True)),
                ('alias', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': '"csvtests_country"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CSVImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(choices=[], default='csvimport.Item', help_text='Please specify the app_label.model_name', max_length=255)),
                ('field_list', models.TextField(blank=True, help_text='Enter list of fields in order only if\n                                     you dont have a header row with matching field names, eg.\n                                     "column1=shared_code,column2=org(Organisation|name)"')),
                ('upload_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=''), upload_to='csv')),
                ('file_name', models.CharField(blank=True, max_length=255)),
                ('encoding', models.CharField(blank=True, max_length=32)),
                ('upload_method', models.CharField(choices=[('manual', 'manual'), ('cronjob', 'cronjob')], default='manual', max_length=50)),
                ('error_log', models.TextField(help_text='Each line is an import error')),
                ('import_date', models.DateField(auto_now=True)),
                ('import_user', models.CharField(blank=True, default='anonymous', help_text='User id as text', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'csvtests_organisation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'csvtests_unitofmeasure',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TYPE', models.PositiveIntegerField(default=0)),
                ('code_share', models.CharField(help_text='Cross-organization item code', max_length=32)),
                ('code_org', models.CharField(help_text='Organization-specfific item code', max_length=32)),
                ('description', models.TextField(null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(max_length=10, null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='csvimport.Country')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csvimport.Organisation')),
                ('uom', models.ForeignKey(help_text='Unit of Measure', on_delete=django.db.models.deletion.CASCADE, to='csvimport.UnitOfMeasure')),
            ],
            options={
                'db_table': 'csvtests_item',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeric_id', models.PositiveIntegerField()),
                ('natural_key', models.CharField(max_length=100)),
                ('csvimport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csvimport.CSVImport')),
            ],
        ),
    ]
