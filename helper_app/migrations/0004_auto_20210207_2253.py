# Generated by Django 2.2 on 2021-02-08 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper_app', '0003_job_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(choices=[('1', 'Pet Care'), ('2', 'Electrical'), ('3', 'Garden')], max_length=50, null=True),
        ),
    ]
