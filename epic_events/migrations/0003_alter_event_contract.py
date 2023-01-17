# Generated by Django 4.1.3 on 2023-01-17 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epic_events', '0002_remove_event_customer_event_contract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contract',
            field=models.ForeignKey(default='3', on_delete=django.db.models.deletion.RESTRICT, related_name='event_contract', to='epic_events.contract'),
        ),
    ]
