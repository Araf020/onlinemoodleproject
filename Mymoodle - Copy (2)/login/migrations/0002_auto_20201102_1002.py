# Generated by Django 3.1.2 on 2020-11-02 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSession',
            fields=[
                ('course_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('session_id', models.CharField(max_length=20)),
                ('course_title', models.CharField(max_length=100)),
                ('credit_hour', models.IntegerField()),
            ],
            options={
                'db_table': 'COURSE',
            },
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]