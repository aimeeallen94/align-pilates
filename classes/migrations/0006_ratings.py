# Generated by Django 3.2.25 on 2024-06-11 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_class_type_day_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=254)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('review', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class_type')),
            ],
        ),
    ]