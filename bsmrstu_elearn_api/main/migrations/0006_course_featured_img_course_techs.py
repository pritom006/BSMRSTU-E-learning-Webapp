# Generated by Django 4.1.5 on 2023-07-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_adress_teacher_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='featured_img',
            field=models.ImageField(null=True, upload_to='course_imgs/'),
        ),
        migrations.AddField(
            model_name='course',
            name='techs',
            field=models.TextField(null=True),
        ),
    ]
