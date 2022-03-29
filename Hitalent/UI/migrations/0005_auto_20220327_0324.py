# Generated by Django 3.0.6 on 2022-03-27 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0004_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar.svg', upload_to='avatars'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]