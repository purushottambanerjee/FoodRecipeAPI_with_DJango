# Generated by Django 3.1.2 on 2020-11-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('ingriedient', models.CharField(max_length=1000)),
                ('time', models.IntegerField()),
                ('process', models.CharField(max_length=2000)),
            ],
        ),
    ]
