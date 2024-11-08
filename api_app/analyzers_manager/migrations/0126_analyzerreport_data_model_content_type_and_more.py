# Generated by Django 4.2.16 on 2024-11-08 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('analyzers_manager', '0125_alter_analyzerconfig_mapping_data_model_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyzerreport',
            name='data_model_content_type',
            field=models.ForeignKey(editable=False, limit_choices_to={'app_label': 'data_model'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='analyzerreport',
            name='data_model_object_id',
            field=models.IntegerField(editable=False, null=True),
        ),
    ]
