# Generated by Django 3.1.14 on 2022-04-26 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0095_auto_20220407_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.asset')),
                ('db_name', models.CharField(blank=True, max_length=1024, verbose_name='Database')),
            ],
            options={
                'verbose_name': 'Database',
            },
            bases=('assets.asset',),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.asset')),
            ],
            options={
                'abstract': False,
            },
            bases=('assets.asset',),
        ),
        migrations.CreateModel(
            name='Cloud',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.asset')),
                ('url', models.CharField(max_length=4096, verbose_name='Cluster')),
            ],
            options={
                'abstract': False,
            },
            bases=('assets.asset',),
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.asset')),
                ('url', models.CharField(max_length=1024, verbose_name='url')),
                ('autofill', models.CharField(default='basic', max_length=16)),
                ('password_selector', models.CharField(blank=True, default='', max_length=128)),
                ('submit_selector', models.CharField(blank=True, default='', max_length=128)),
                ('username_selector', models.CharField(blank=True, default='', max_length=128))
            ],
            options={
                'abstract': False,
            },
            bases=('assets.asset',),
        ),
    ]
