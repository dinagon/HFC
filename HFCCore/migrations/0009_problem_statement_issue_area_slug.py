# Generated by Django 2.2.13 on 2020-06-22 04:25

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HFCCore', '0008_problem_statement_title_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem_statement',
            name='issue_area_slug',
            field=autoslug.fields.AutoSlugField(default='Civic_Empowerment', editable=False, populate_from='issue_area'),
            preserve_default=False,
        ),
    ]