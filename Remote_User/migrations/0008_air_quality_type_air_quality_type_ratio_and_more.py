# Generated by Django 4.2 on 2024-02-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Remote_User', '0007_clientposts_model_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='air_quality_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.CharField(max_length=30000)),
                ('City', models.CharField(max_length=300)),
                ('Date', models.CharField(max_length=300)),
                ('PM2andhalf', models.CharField(max_length=300)),
                ('PM10', models.CharField(max_length=300)),
                ('NO', models.CharField(max_length=300)),
                ('NO2', models.CharField(max_length=300)),
                ('Nox', models.CharField(max_length=300)),
                ('NH3', models.CharField(max_length=300)),
                ('CO', models.CharField(max_length=300)),
                ('SO2', models.CharField(max_length=300)),
                ('O3', models.CharField(max_length=300)),
                ('Benzene', models.CharField(max_length=300)),
                ('Toluene', models.CharField(max_length=300)),
                ('Xylene', models.CharField(max_length=300)),
                ('AQI', models.CharField(max_length=300)),
                ('Prediction', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='air_quality_type_ratio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=300)),
                ('ratio', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='detection_accuracy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=300)),
                ('ratio', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='clientposts_model',
            name='userId',
        ),
        migrations.DeleteModel(
            name='review_Model',
        ),
        migrations.AddField(
            model_name='clientregister_model',
            name='address',
            field=models.CharField(default='Default Address', max_length=30),
        ),
        migrations.AddField(
            model_name='clientregister_model',
            name='gender',
            field=models.CharField(default='Male', max_length=30),
        ),
        migrations.AlterField(
            model_name='clientregister_model',
            name='phoneno',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='ClientPosts_Model',
        ),
    ]
