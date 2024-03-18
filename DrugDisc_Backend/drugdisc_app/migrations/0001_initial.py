# Generated by Django 4.1.7 on 2024-03-18 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='InputData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compound_name', models.CharField(max_length=100)),
                ('smiles_notation', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Protein',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gene_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GeneratedMolecule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drugdisc_app.compound')),
                ('protein', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drugdisc_app.protein')),
            ],
        ),
        migrations.CreateModel(
            name='Bioactivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pChEMBL_value', models.FloatField()),
                ('compound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drugdisc_app.compound')),
                ('protein', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drugdisc_app.protein')),
            ],
        ),
    ]
