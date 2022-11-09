# Generated by Django 4.1.3 on 2022-11-09 07:33

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
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=100)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('discount', models.IntegerField()),
                ('serving_time_period', models.TimeField()),
                ('estimated_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.PositiveIntegerField()),
                ('cafe_space_position', models.PositiveIntegerField()),
                ('use', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField()),
                ('final_price', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ureceipts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('status', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('menu_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='morders', to='orders.menuitem')),
                ('receipts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rorders', to='orders.receipt')),
                ('tables', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='torders', to='orders.table')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uorders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]