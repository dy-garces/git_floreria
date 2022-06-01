# Generated by Django 4.0.4 on 2022-05-31 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('imgen', models.ImageField(null=True, upload_to='productos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='floreriaWeb.categoria')),
            ],
        ),
    ]