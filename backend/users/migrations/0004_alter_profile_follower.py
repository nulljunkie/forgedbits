# Generated by Django 5.1 on 2024-09-08 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_profile_follower"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="follower",
            field=models.ManyToManyField(blank=True, to="users.profile"),
        ),
    ]
