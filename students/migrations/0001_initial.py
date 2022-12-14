# Generated by Django 3.1 on 2022-09-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField()),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('full_name', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
                ('section', models.CharField(choices=[('A', 'SectionA'), ('B', 'SectionB')], max_length=1)),
            ],
        ),
    ]
