# Generated by Django 4.0.3 on 2022-05-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]
