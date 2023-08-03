# Generated by Django 4.2.2 on 2023-06-13 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('query', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reply', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactUs',
        ),
    ]
