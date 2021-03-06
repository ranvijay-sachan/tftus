# Generated by Django 3.1.4 on 2021-02-25 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('my_free_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='SalesMan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'db_table': 'salesman',
            },
        ),
        migrations.CreateModel(
            name='CustomerCallHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_start', models.DateTimeField()),
                ('call_end', models.DateTimeField()),
                ('note', models.TextField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='call_history', to='cms.customer')),
                ('sales_man', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attendee', to='cms.salesman')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='sales_man',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_salesman', to='cms.salesman'),
        ),
    ]
