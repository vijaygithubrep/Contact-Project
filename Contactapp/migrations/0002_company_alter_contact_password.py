# Generated by Django 4.0.4 on 2022-05-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contactapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
