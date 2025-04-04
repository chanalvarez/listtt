# Generated by Django 3.2.7 on 2021-09-29 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_rename_title_task_section_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=200)),
                ('ID_no', models.CharField(max_length=11)),
                ('Course_code', models.CharField(max_length=10)),
                ('Attendance', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Late'), ('E', 'Excused'), ('D', 'Drop'), ('W', 'Withdraw')], max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
