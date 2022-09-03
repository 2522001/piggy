# Generated by Django 4.1 on 2022-09-03 04:57

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag5',
        ),
        migrations.AddField(
            model_name='post',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('지원 정책', '지원 정책'), ('금융 상품', '금융 상품'), ('팁', '팁')], default='지원정책', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='income',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('무소득', '무소득'), ('1~100만원', '1~100만원'), ('101~200만원', '101~200만원'), ('201~300만원', '201~300만원'), ('301만원~400만원', '301만원~400만원'), ('401만원초과', '401만원초과')], default='무소득', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='loc1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='loc2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='target',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('대학생', '대학생'), ('군인', '군인'), ('청년', '청년')], default='대학생', max_length=60, null=True),
        ),
    ]
