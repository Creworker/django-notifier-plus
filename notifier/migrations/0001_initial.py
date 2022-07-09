# Generated by Django 4.0.6 on 2022-07-09 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('display_name', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('enabled', models.BooleanField(default=True)),
                ('klass', models.CharField(help_text='Example: notifier.backends.EmailBackend', max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('display_name', models.CharField(max_length=200)),
                ('public', models.BooleanField(default=True)),
                ('backends', models.ManyToManyField(blank=True, to='notifier.backend')),
                ('permissions', models.ManyToManyField(blank=True, to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SentNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('success', models.BooleanField()),
                ('read', models.BooleanField(default=False)),
                ('backend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifier.backend')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifier.notification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPrefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('notify', models.BooleanField(default=True)),
                ('backend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifier.backend')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifier.notification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'notification', 'backend')},
            },
        ),
        migrations.CreateModel(
            name='GroupPrefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('notify', models.BooleanField(default=True)),
                ('backend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifier.backend')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifier.notification')),
            ],
            options={
                'unique_together': {('group', 'notification', 'backend')},
            },
        ),
    ]
