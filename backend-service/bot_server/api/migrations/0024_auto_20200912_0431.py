# Generated by Django 3.1 on 2020-09-12 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_delete_partof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_number',
            field=models.IntegerField(),
        ),
    ]