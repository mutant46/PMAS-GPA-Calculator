# Generated by Django 3.1.1 on 2021-02-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality_points', '0004_point_cre_hr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='numbers',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Number',
        ),
    ]