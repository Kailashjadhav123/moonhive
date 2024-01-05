# Generated by Django 4.2.4 on 2024-01-04 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=255)),
                ('property_address', models.TextField()),
                ('property_location', models.CharField(max_length=255)),
                ('property_features', models.TextField()),
                ('unit_type', models.CharField(choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')], max_length=4)),
                ('rent_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('document_proofs', models.CharField(max_length=255)),
                ('agreement_end_date', models.DateField()),
                ('monthly_rent_date', models.PositiveIntegerField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.property')),
            ],
        ),
    ]
