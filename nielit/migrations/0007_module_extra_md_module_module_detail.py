# Generated by Django 4.2.2 on 2023-06-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nielit', '0006_remove_syllabus_extra_md_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='extra_md',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='module',
            name='module_detail',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]