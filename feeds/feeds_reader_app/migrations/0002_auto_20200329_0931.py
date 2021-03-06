# Generated by Django 3.0.4 on 2020-03-29 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds_reader_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('category', models.CharField(max_length=1000)),
                ('copyright', models.TextField()),
                ('docs', models.TextField()),
                ('languages', models.CharField(max_length=1000)),
                ('last_build_date', models.DateTimeField()),
                ('managing_editor', models.EmailField(max_length=254)),
                ('pub_date', models.DateTimeField()),
                ('web_master', models.EmailField(max_length=254)),
                ('generator', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='channel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feeds_reader_app.Channel'),
            preserve_default=False,
        ),
    ]
