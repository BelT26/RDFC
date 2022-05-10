# Generated by Django 3.2 on 2022-05-10 10:07

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('played', models.IntegerField(default=0)),
                ('won', models.IntegerField(default=0)),
                ('drawn', models.IntegerField(default=0)),
                ('lost', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('is_approved', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.DateField()),
                ('time', models.TimeField(default='20:00')),
                ('location', models.CharField(max_length=200)),
                ('blue_goals', models.IntegerField(default=0)),
                ('white_goals', models.IntegerField(default=0)),
                ('results_added', models.BooleanField(default=False)),
                ('registrations_open', models.BooleanField(default=False)),
                ('next_fixture', models.BooleanField(default=False)),
                ('teams_allocated', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
        migrations.CreateModel(
            name='MatchPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(blank=True, max_length=6, null=True)),
                ('reserve', models.BooleanField(default=False)),
                ('registration_time', models.DateTimeField(auto_now_add=True)),
                ('win', models.BooleanField(default=False)),
                ('loss', models.BooleanField(default=False)),
                ('draw', models.BooleanField(default=False)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchplayer', to='club.match')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchmember', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
