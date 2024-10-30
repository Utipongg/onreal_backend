# Generated by Django 5.1 on 2024-09-29 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('instructor_name', models.CharField(max_length=255)),
                ('instructor_image', models.ImageField(blank=True, null=True, upload_to='instructor_images/')),
                ('category', models.CharField(blank=True, max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='course_covers/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]