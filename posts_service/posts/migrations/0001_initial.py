# Generated by Django 3.2.19 on 2023-06-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userId', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
    ]