# Generated by Django 3.1.2 on 2020-11-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0016_delete_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Least Important', '⭐ 1'), ('Somewhat Important', '⭐ 2'), ('Mandatory', '⭐ 3')], max_length=200, null=True),
        ),
    ]