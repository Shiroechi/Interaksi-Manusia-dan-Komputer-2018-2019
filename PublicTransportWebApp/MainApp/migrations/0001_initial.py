# Generated by Django 2.1.1 on 2018-10-14 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('descriptions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.City')),
                ('infrastructure_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Infrastructure')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('departure_time', models.TimeField()),
                ('depart_status', models.CharField(max_length=16)),
                # ('transportation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transportation_id', to='MainApp.Transportation')),
                ('place_destination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_destination', to='MainApp.Place')),
                ('place_from_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_from', to='MainApp.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('cost', models.IntegerField()),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Schedule')),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.CharField(max_length=16)),
                ('description', models.TextField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Category')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='transportation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Transportation'),
        ),
    ]
