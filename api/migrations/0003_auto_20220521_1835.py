# Generated by Django 3.2.5 on 2022-05-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220503_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='imperialUnitMain',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='imperialUnitSub',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='isRequired',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='metricUnitMain',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='metricUnitSub',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='subQuestions',
            field=models.ManyToManyField(blank=True, related_name='subQuestions_list', to='api.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answerType',
            field=models.CharField(blank=True, choices=[('mcq', 'mcq'), ('text', 'text'), ('bool', 'bool'), ('number', 'number'), ('float', 'float'), ('date', 'date'), ('file', 'file'), ('photo', 'photo'), ('answerMCQ_dropDown', 'answerMCQ_dropDown')], max_length=50, null=True),
        ),
        migrations.RemoveField(
            model_name='question',
            name='answersMCQ',
        ),
        migrations.AddField(
            model_name='question',
            name='answersMCQ',
            field=models.ManyToManyField(blank=True, related_name='mcq_answerID_set', to='api.Answer'),
        ),
    ]