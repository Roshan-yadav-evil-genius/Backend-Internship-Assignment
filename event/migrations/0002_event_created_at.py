# Generated by Django 4.1.7 on 2023-05-23 16:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At'),
            preserve_default=False,
        ),
    ]