# Generated by Django 2.0.7 on 2018-07-09 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20180708_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='age_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Event', to='activities.Age_Group'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_subtype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Event', to='activities.Event_Subtype'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Event', to='activities.Event_Type'),
        ),
        migrations.AlterField(
            model_name='event',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Event', to='activities.Level'),
        ),
        migrations.AlterField(
            model_name='event',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Event', to='activities.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='venue',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Room', to='activities.Venue'),
        ),
    ]
