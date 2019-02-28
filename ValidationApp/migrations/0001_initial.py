# Generated by Django 2.0.6 on 2019-02-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=20)),
                ('password', models.CharField(default='', max_length=200)),
                ('age', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
