# Generated by Django 3.2 on 2023-06-22 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_contactformessage_contactformmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactformmessage',
            name='subject',
        ),
        migrations.AddField(
            model_name='contactformmessage',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
