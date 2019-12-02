# Generated by Django 2.2.7 on 2019-12-02 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='squirrel',
            name='age',
            field=models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile'), ('other', 'Other')], default='other', help_text='Value is either Adult or Juvenile', max_length=50),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='approaches',
            field=models.BooleanField(default='Other', help_text='Whether the squirrel was seen approaching human, seeking foodl'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='chasing',
            field=models.BooleanField(default='Other', help_text='Whether squirrel was seen chasing another squirrel.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='climbing',
            field=models.BooleanField(default='Other', help_text='Whether Squirrel was seen climbing a tree or other environmental landmark.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='eating',
            field=models.BooleanField(default='Other', help_text='Whether squirrel was seen eating'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='foraging',
            field=models.BooleanField(default='Other', help_text='Whether squirrel was seen foraging for food'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='indifferent',
            field=models.BooleanField(default='Other', help_text='Whether the Squirrel was indifferent to human presence'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='kuks',
            field=models.BooleanField(default='Other', help_text='Whether squirrel was heard kukking'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='latitude',
            field=models.FloatField(default='Other', help_text='Latitude coordinate for squirrel sighting point'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='location',
            field=models.CharField(choices=[('ground plane', 'Ground Plane'), ('above ground', 'Above Ground'), ('other', 'Other')], default='other', help_text='Location of where the squirrel was when first sighted', max_length=50),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='longitude',
            field=models.FloatField(default='Other', help_text='Longitude coordinate for squirrel sighting point'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='moans',
            field=models.BooleanField(default='Other', help_text='Whether the squirrel was heard moaning'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='other_activities',
            field=models.CharField(default='Other', help_text='Whether squirrel was seen engaged in any other activity', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='primary_fur_color',
            field=models.CharField(choices=[('gray', 'Gray'), ('cinnamon', 'Cinnamon'), ('black', 'Black'), ('other', 'Other')], default='other', help_text='Value is either "Gray," "Cinnamon" or "Black."', max_length=50),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='quaas',
            field=models.BooleanField(default='Other', help_text='Whether the squirrel was heard quaaing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='running',
            field=models.BooleanField(default='Other', help_text='Whether squirrel was seen running'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='runs_from',
            field=models.BooleanField(default='Other', help_text='Whether the Squirrel was seen running from humans, seeing them as a threat'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='shift',
            field=models.CharField(choices=[('am', 'AM'), ('pm', 'PM'), ('other', 'Other')], default='other', help_text='Sighting occurred in the morning or late afternoon', max_length=5),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='specific_location',
            field=models.CharField(default='Other', help_text='Additional commentary on the squirrel location', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='tail_flags',
            field=models.BooleanField(default='Other', help_text='Whether the squirrel was seen flagging its tail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='tail_twitches',
            field=models.BooleanField(default='Other', help_text='Whether the squirrel was seen twitching its tail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squirrel',
            name='unique_id',
            field=models.CharField(default='Other', help_text='Identification tag for each squirrel sighting', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='date',
            field=models.CharField(help_text='Concatenation of the sighting session day and month', max_length=8),
        ),
    ]