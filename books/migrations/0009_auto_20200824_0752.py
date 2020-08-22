# Generated by Django 3.1 on 2020-08-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20200824_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(choices=[('翔泳社', 'Shoeisha'), ('技術評論社', 'Gijyutsu Hyoronsha'), ('秀和システム', 'Shuwa System'), ('SBクリエイティブ', 'Sb Creative'), ('日経BP', 'Nikke Bp')], max_length=50, verbose_name='出版社'),
        ),
    ]
