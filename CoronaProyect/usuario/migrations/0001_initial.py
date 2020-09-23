# Generated by Django 3.1.1 on 2020-09-23 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('nacimiento', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=20)),
                ('ciudad', models.CharField(max_length=100)),
                ('codigopostal', models.IntegerField(max_length=6)),
            ],
        ),
    ]
