# Generated by Django 3.0.2 on 2020-02-02 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userSearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media', models.CharField(default='twitter', max_length=200)),
                ('social_media_id', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userSearch.User_Account')),
            ],
        ),
        migrations.DeleteModel(
            name='User_Target',
        ),
    ]
