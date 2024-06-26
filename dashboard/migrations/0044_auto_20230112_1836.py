# Generated by Django 3.2.5 on 2023-01-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0043_auto_20220924_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomesetting',
            name='child_one',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('Normal', 'Normal'), ('BPL', 'BPL'), ('Handicap', 'Handicap')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='incomesetting',
            name='child_three',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('Normal', 'Normal'), ('BPL', 'BPL'), ('Handicap', 'Handicap')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='incomesetting',
            name='child_two',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('Normal', 'Normal'), ('BPL', 'BPL'), ('Handicap', 'Handicap')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='incomesettingforwomenold',
            name='category_type',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('BPL', 'BPL'), ('Handicap', 'Handicap'), ('Child Below 18', 'Child Below 18'), ('Mature Female', 'Mature Female'), ('Senior Citizen', 'Senior Citizen')], max_length=15, null=True),
        ),
    ]
