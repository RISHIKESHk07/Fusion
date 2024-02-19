# Generated by Django 3.1.5 on 2024-02-19 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0010_auto_20240219_1316'),
        ('hostel_management', '0012_merge_20240219_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffschedule',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.staff'),
        ),
        migrations.DeleteModel(
            name='HostelAllottment',
        ),
    ]
