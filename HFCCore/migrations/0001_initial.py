# Generated by Django 2.2.4 on 2020-05-01 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TFC', '0003_auto_20200501_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('organization_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='TFC.Organization')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
            },
            bases=('TFC.organization',),
        ),
    ]