# Generated by Django 3.2.12 on 2022-04-19 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='everyName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='eventreservation',
            name='purposeDescribe',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='iscreated',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='isupdated',
            field=models.DateField(blank=True, null=True),
        ),
    ]
