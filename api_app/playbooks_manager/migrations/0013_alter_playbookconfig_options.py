# Generated by Django 4.1.9 on 2023-06-21 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playbooks_manager', '0012_ip_reputation_playbook'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playbookconfig',
            options={'ordering': ['name', 'disabled']},
        ),
    ]
