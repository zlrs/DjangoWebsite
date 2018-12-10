# Generated by Django 2.1.2 on 2018-12-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesFinished',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=20)),
                ('courseCode', models.CharField(max_length=20)),
                ('courseSerial', models.CharField(max_length=20)),
                ('courseName', models.CharField(max_length=150)),
                ('courseType', models.CharField(max_length=100)),
                ('credit', models.IntegerField()),
                ('grade', models.CharField(max_length=20)),
                ('finalGrade', models.CharField(max_length=20)),
            ],
        ),
    ]