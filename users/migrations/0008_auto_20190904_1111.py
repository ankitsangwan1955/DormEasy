# Generated by Django 2.2.4 on 2019-09-04 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190903_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_students',
            name='Fullname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reg_students',
            name='Gender',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='reg_students',
            name='Regno',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='reg_students',
            name='Sem',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]