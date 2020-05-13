# Generated by Django 2.2.4 on 2020-04-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screeningapp', '0002_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='qtype',
            field=models.CharField(choices=[('multiple choice', 'Multiple Choice'), ('yes/no', 'Yes/No')], max_length=30),
        ),
    ]