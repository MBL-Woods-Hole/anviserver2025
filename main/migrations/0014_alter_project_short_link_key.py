# Generated by Django 5.2.1 on 2025-05-31 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_project_short_link_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='short_link_key',
            field=models.CharField(default='7QyVjP', max_length=32),
        ),
    ]
