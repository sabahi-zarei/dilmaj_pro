# Generated by Django 4.1.5 on 2023-01-04 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='voice',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='WordDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to='')),
                ('text', models.TextField(blank=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wordId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.word')),
            ],
        ),
    ]
