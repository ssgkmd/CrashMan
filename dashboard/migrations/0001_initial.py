# Generated by Django 2.0.6 on 2018-06-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Crash_Name', models.CharField(max_length=30)),
                ('Exploitable', models.CharField(max_length=30)),
                ('Date', models.DateTimeField(blank=True, null=True)),
                ('Program', models.CharField(max_length=30)),
                ('VM_ip', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VM_Name', models.CharField(max_length=30)),
                ('VM_ip', models.CharField(max_length=20)),
                ('Program', models.CharField(max_length=30)),
                ('Port', models.CharField(max_length=10)),
                ('Fuzzer', models.CharField(max_length=30)),
            ],
        ),
    ]