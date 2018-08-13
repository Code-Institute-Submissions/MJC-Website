# Generated by Django 2.0.7 on 2018-08-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0026_auto_20180810_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_subtype',
            name='img_src',
        ),
        migrations.RemoveField(
            model_name='event_type',
            name='img_src',
        ),
        migrations.AddField(
            model_name='event_subtype',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/event_subtype'),
        ),
        migrations.AddField(
            model_name='event_type',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/event_type'),
        ),
    ]
