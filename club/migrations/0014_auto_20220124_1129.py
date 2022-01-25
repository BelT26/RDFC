# Generated by Django 3.2 on 2022-01-24 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0013_alter_matchplayer_registration_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Result',
        ),
        migrations.AlterField(
            model_name='match',
            name='time',
            field=models.TimeField(default='20:00'),
        ),
        migrations.AlterField(
            model_name='matchplayer',
            name='match_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='club.match'),
        ),
        migrations.AlterField(
            model_name='matchplayer',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]