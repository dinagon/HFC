# Generated by Django 2.2.4 on 2020-04-18 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidate_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('level_of_expertise', models.CharField(choices=[('Entry Level', 'Entry Level'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Expert', 'Expert')], max_length=100)),
                ('area_of_expertise', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Candidate',
                'verbose_name_plural': 'Candidates',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=300, unique=True)),
                ('area', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Screenings',
            fields=[
                ('screening_id', models.AutoField(primary_key=True, serialize=False)),
                ('screening_uuid', models.CharField(blank=True, max_length=50)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Candidate')),
            ],
            options={
                'verbose_name': 'Screening',
                'verbose_name_plural': 'Screenings',
            },
        ),
        migrations.CreateModel(
            name='Sub_category',
            fields=[
                ('sub_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_category_name', models.CharField(max_length=300, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Category')),
            ],
            options={
                'verbose_name': 'Sub_Category',
                'verbose_name_plural': 'Sub_Categories',
            },
        ),
        migrations.CreateModel(
            name='Screenings_Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True)),
                ('candidate_ans', models.CharField(blank=True, max_length=50)),
                ('correct_ans', models.CharField(blank=True, max_length=50)),
                ('answer_correctness', models.CharField(blank=True, max_length=10)),
                ('screening_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Screenings')),
            ],
            options={
                'verbose_name': 'Screening_Question',
                'verbose_name_plural': 'Screenings_Questions',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('qtype', models.CharField(choices=[('multiple choice', 'Multiple Choice'), ('yes/no', 'Yes/No')], max_length=100)),
                ('option_1', models.TextField(blank=True)),
                ('option_2', models.TextField(blank=True)),
                ('option_3', models.TextField(blank=True)),
                ('option_4', models.TextField(blank=True)),
                ('answer', models.TextField(blank=True)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Category')),
                ('sub_category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Sub_category')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
    ]
