# Generated by Django 4.0.6 on 2022-08-02 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rollnum', models.IntegerField()),
                ('rank', models.IntegerField()),
            ],
        ),
    ]