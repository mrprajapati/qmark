# Generated by Django 3.0.6 on 2020-07-21 10:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuizCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'QuizCategories',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('quiz_name', models.CharField(max_length=200)),
                ('no_of_question', models.PositiveIntegerField(default=0)),
                ('publish_date', models.DateTimeField()),
                ('is_published', models.BooleanField()),
                ('quiz_duration', models.DurationField(default='00:00:00')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_category', to='quiz.QuizCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=1000)),
                ('mark', models.PositiveIntegerField(default=1)),
                ('option_A', models.CharField(max_length=200)),
                ('option_B', models.CharField(max_length=200)),
                ('option_C', models.CharField(max_length=200)),
                ('option_D', models.CharField(max_length=200)),
                ('answer', models.CharField(choices=[('A', 'option_A'), ('B', 'option_B'), ('C', 'option_C'), ('D', 'option_D')], max_length=1)),
                ('quiz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_question', to='quiz.Quiz')),
            ],
        ),
    ]
