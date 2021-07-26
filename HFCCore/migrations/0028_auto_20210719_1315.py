# Generated by Django 3.2 on 2021-07-19 07:45

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HFCCore', '0027_alter_issue_area_issue_brief'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='website_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]