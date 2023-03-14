# Generated by Django 4.1.6 on 2023-03-01 23:21

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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_name', models.CharField(max_length=255)),
                ('course_image', models.ImageField(null=True, upload_to='courses/image')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='course_outlines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_module_name', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(null=True, upload_to='user/profile_pic')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('student', 'Student'), ('teacher', 'Teacher')], default='student', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('courseoutlines', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course_outlines')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('code', models.TextField(null=True)),
                ('weight', models.IntegerField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course')),
                ('courseoutlines', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course_outlines')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Course_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('text_content', models.TextField(blank=True, null=True)),
                ('code_content', models.TextField(blank=True, null=True)),
                ('image_content', models.ImageField(blank=True, null=True, upload_to='course/contentimage')),
                ('courseoutlinee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course_outlines')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='Teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.profile'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField()),
                ('is_correct', models.BooleanField(default='false')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.question')),
            ],
        ),
        migrations.CreateModel(
            name='Quizcompleted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_completed', models.DateTimeField(auto_now=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.profile')),
            ],
            options={
                'unique_together': {('user', 'quiz')},
            },
        ),
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.profile')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.CreateModel(
            name='Completed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_completed', models.DateTimeField(auto_now=True)),
                ('courseoutlinee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course_outlines')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.profile')),
            ],
            options={
                'unique_together': {('user', 'courseoutlinee')},
            },
        ),
    ]