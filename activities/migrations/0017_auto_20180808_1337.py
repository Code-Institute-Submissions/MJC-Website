# Generated by Django 2.0.7 on 2018-08-08 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0016_auto_20180808_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Event', to='activities.Weekday'),
        ),
    ]
