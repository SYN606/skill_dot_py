# Generated by Django 4.2.2 on 2023-06-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nielit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='c_intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50)),
                ('c_detail', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='O_level',
        ),
    ]