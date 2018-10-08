# Generated by Django 2.1 on 2018-08-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('classid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ClassTable',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=30)),
                ('chour', models.IntegerField(default=0)),
                ('ctime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('cid', models.IntegerField()),
                ('score', models.IntegerField(default=0)),
                ('score0', models.IntegerField(default=0)),
                ('score1', models.IntegerField(default=0)),
                ('score2', models.IntegerField(default=0)),
                ('score3', models.IntegerField(default=0)),
                ('score4', models.IntegerField(default=0)),
                ('score5', models.IntegerField(default=0)),
                ('stime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Root',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('aname', models.CharField(max_length=30)),
                ('apwd', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=20)),
                ('spwd', models.CharField(max_length=15)),
                ('sbirth', models.DateTimeField()),
                ('ssex', models.BooleanField(default=False)),
                ('semail', models.EmailField(max_length=100)),
                ('saddress', models.CharField(max_length=100)),
                ('sdepart', models.CharField(max_length=30)),
                ('sclass', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=20)),
                ('tpwd', models.CharField(max_length=15)),
                ('tsex', models.BooleanField(default=True)),
                ('tpost', models.CharField(max_length=30)),
                ('tphone', models.CharField(max_length=20)),
                ('tquestion', models.CharField(default='', max_length=50)),
                ('tanswer', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
