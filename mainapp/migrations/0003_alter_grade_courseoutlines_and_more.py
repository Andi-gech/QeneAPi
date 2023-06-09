# Generated by Django 4.1.6 on 2023-03-14 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_answer_is_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='courseoutlines',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course_outlines'),
        ),
        migrations.AlterUniqueTogether(
            name='grade',
            unique_together={('user', 'courseoutlines')},
        ),
    ]
