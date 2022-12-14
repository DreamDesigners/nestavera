# Generated by Django 3.2 on 2022-12-12 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.job')),
            ],
        ),
    ]
