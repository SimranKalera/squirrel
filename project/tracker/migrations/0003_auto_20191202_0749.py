# Generated by Django 2.2.7 on 2019-12-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20191202_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='approaches',
            field=models.BooleanField(default=False, help_text='Whether the squirrel was seen approaching human, seeking foodl'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='chasing',
            field=models.BooleanField(default=False, help_text='Whether squirrel was seen chasing another squirrel.'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='climbing',
            field=models.BooleanField(default=False, help_text='Whether Squirrel was seen climbing a tree or other environmental landmark.'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='eating',
            field=models.BooleanField(default=False, help_text='Whether squirrel was seen eating'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='foraging',
            field=models.BooleanField(default=False, help_text='Whether squirrel was seen foraging for food'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='indifferent',
            field=models.BooleanField(default=False, help_text='Whether the Squirrel was indifferent to human presence'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='kuks',
            field=models.BooleanField(default=False, help_text='Whether squirrel was heard kukking'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='moans',
            field=models.BooleanField(default=False, help_text='Whether the squirrel was heard moaning'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='quaas',
            field=models.BooleanField(default=False, help_text='Whether the squirrel was heard quaaing'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='running',
            field=models.BooleanField(default=False, help_text='Whether squirrel was seen running'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='runs_from',
            field=models.BooleanField(default=False, help_text='Whether the Squirrel was seen running from humans, seeing them as a threat'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_flags',
            field=models.BooleanField(default=False, help_text='Whether the squirrel was seen flagging its tail'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_twitches',
            field=models.BooleanField(default=False, help_text='Whether the squirrel was seen twitching its tail'),
        ),
    ]
