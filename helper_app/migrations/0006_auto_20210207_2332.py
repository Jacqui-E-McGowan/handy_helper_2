# Generated by Django 2.2 on 2021-02-08 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper_app', '0005_auto_20210207_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(choices=[('Pet Care', 'Pet Care'), ('Electrical', 'Electrical'), ('Garden', 'Garden')], default=2, max_length=50, null=True),
        ),
    ]
