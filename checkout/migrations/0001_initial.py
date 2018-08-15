# Generated by Django 2.0.7 on 2018-08-12 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0026_auto_20180810_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('paid_fare', models.DecimalField(decimal_places=2, max_digits=6)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RegistrationOrder', to='activities.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RegistrationOrder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]