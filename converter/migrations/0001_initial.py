# Generated by Django 3.0.7 on 2020-06-11 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('rollNo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('marks_subject1', models.IntegerField()),
                ('marks_subject2', models.IntegerField()),
                ('marks_subject3', models.IntegerField()),
            ],
        ),
    ]
