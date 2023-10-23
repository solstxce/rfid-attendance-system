
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Student',
        ),
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 4, 16, 38, 23, 751714)),
        ),
        migrations.AlterField(
            model_name='log',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2020, 5, 4, 16, 38, 23, 751777)),
        ),
    ]
