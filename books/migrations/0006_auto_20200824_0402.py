# Generated by Django 3.1 on 2020-08-24 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200824_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(choices=[('SBクリエイティブ', 'SBクリエイティブ'), ('秀和システム', '秀和システム'), ('技術評論社', '技術評論社'), ('日経BP', '日経BP'), ('翔泳社', '翔泳社')], max_length=50, verbose_name='出版社'),
        ),
    ]
