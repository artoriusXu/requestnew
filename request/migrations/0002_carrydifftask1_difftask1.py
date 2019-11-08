# Generated by Django 2.0.2 on 2019-07-29 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarryDiffTask1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diff_task_name', models.CharField(max_length=200)),
                ('candidate', models.CharField(max_length=200)),
                ('master', models.CharField(max_length=200)),
                ('test', models.CharField(default='', max_length=200)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiffTask1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diff_task_name', models.CharField(max_length=200)),
                ('remark', models.CharField(max_length=200)),
                ('db_remark', models.CharField(default='', max_length=100)),
                ('status', models.BooleanField()),
                ('test', models.CharField(default='', max_length=200)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Case')),
            ],
        ),
    ]