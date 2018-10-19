# Generated by Django 2.1.1 on 2018-10-19 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0008_auto_20181017_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlannedAccountingEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=13)),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Account')),
                ('compensation_account', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.CompensationAccount')),
                ('counterparty_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planned_accounting_entry_counterparty', to='accounting.Account')),
                ('recurring_accounting_entry', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.RecurringAccountingEntry')),
            ],
        ),
        migrations.RemoveField(
            model_name='forecastedaccountingentry',
            name='account',
        ),
        migrations.RemoveField(
            model_name='forecastedaccountingentry',
            name='compensation_account',
        ),
        migrations.RemoveField(
            model_name='forecastedaccountingentry',
            name='counterparty_account',
        ),
        migrations.RemoveField(
            model_name='forecastedaccountingentry',
            name='recurring_accounting_entry',
        ),
        migrations.AlterModelOptions(
            name='budget',
            options={'ordering': ('id',)},
        ),
        migrations.DeleteModel(
            name='ForecastedAccountingEntry',
        ),
    ]