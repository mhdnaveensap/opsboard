# Generated by Django 2.0 on 2017-12-28 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commonpage', '0003_userprofile_team_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='team_name',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
