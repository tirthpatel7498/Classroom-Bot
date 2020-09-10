# Generated by Django 3.1 on 2020-09-06 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_deptmanager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='log_course_id',
            new_name='log_course_id',
        ),
        migrations.RenameField(
            model_name='dept',
            old_name='log_department_id',
            new_name='log_department_id',
        ),
        migrations.AlterModelTable(
            name='course',
            table='log_course',
        ),
        migrations.AlterModelTable(
            name='dept',
            table='log_department',
        ),
    ]
