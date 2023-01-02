# Generated by Django 4.1.3 on 2022-12-12 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=64, unique=True)),
                ('mobile', models.CharField(max_length=64, unique=True)),
                ('company_name', models.CharField(max_length=64)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('sales_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_sales_contact', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('event_status', models.CharField(choices=[('IN PROGRESS', 'In progress'), ('RESOLVED', 'Resolved')], default='IN PROGRESS', max_length=64)),
                ('attendees', models.IntegerField()),
                ('event_date', models.DateTimeField()),
                ('notes', models.CharField(max_length=2048)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_customer', to='epic_events.customer')),
                ('support_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_support_staff', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('amount', models.FloatField()),
                ('payment_due', models.DateField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_customer', to='epic_events.customer')),
                ('sales_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_sales_contact', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
