# Generated by Django 3.1.2 on 2021-07-24 19:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('contributors', models.ManyToManyField(blank=True, to='user.Profile')),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(2021, 7, 25, 19, 0, 56, 745673, tzinfo=utc))),
                ('announced', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='defaulst.png', null=True, upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.workspace')),
            ],
        ),
    ]
