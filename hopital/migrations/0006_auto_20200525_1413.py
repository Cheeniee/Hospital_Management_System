# Generated by Django 2.2.6 on 2020-05-25 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hopital', '0005_super_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hopital.Doc_Status'),
        ),
    ]
