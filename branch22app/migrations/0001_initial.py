# Generated by Django 5.0.1 on 2024-12-25 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accounts_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accounts_book_name', models.CharField(max_length=200)),
                ('created_by', models.CharField(max_length=200)),
                ('cb_date', models.CharField(max_length=200)),
                ('updated_by', models.CharField(max_length=200)),
                ('ub_date', models.CharField(max_length=200)),
                ('deleted_by', models.CharField(max_length=200)),
                ('db_date', models.CharField(max_length=200)),
                ('ub_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='background_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('flag', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='br2test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('br2test_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='branch_closing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=200)),
                ('jan', models.CharField(max_length=200)),
                ('feb', models.CharField(max_length=200)),
                ('mar', models.CharField(max_length=200)),
                ('apr', models.CharField(max_length=200)),
                ('may', models.CharField(max_length=200)),
                ('jun', models.CharField(max_length=200)),
                ('jul', models.CharField(max_length=200)),
                ('aug', models.CharField(max_length=200)),
                ('sep', models.CharField(max_length=200)),
                ('oct', models.CharField(max_length=200)),
                ('nov', models.CharField(max_length=200)),
                ('dec', models.CharField(max_length=200)),
                ('flag', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('enter_by', models.CharField(max_length=200)),
                ('cb_date', models.CharField(max_length=200)),
                ('updated_by', models.CharField(max_length=200)),
                ('ub_date', models.CharField(max_length=200)),
                ('deleted_by', models.CharField(max_length=200)),
                ('db_date', models.CharField(max_length=200)),
                ('ub_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='in_exp_items_daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particulars', models.CharField(max_length=200)),
                ('amount', models.FloatField()),
                ('ledger', models.CharField(max_length=200)),
                ('accounts_book_name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('item_catergory', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('day', models.CharField(max_length=200)),
                ('month', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('enter_by', models.CharField(max_length=200)),
                ('cb_date', models.CharField(max_length=200)),
                ('updated_by', models.CharField(max_length=200)),
                ('ub_date', models.CharField(max_length=200)),
                ('deleted_by', models.CharField(max_length=200)),
                ('db_date', models.CharField(max_length=200)),
                ('ub_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_name', models.CharField(max_length=200)),
                ('contact_person_name', models.CharField(max_length=200)),
                ('contact_person_mob', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('created_by', models.CharField(max_length=200)),
                ('cb_date', models.CharField(max_length=200)),
                ('updated_by', models.CharField(max_length=200)),
                ('ub_date', models.CharField(max_length=200)),
                ('deleted_by', models.CharField(max_length=200)),
                ('db_date', models.CharField(max_length=200)),
                ('ub_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='opening_balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_no', models.CharField(max_length=200)),
                ('month_name', models.CharField(max_length=200)),
                ('month_amount', models.FloatField()),
                ('date', models.CharField(max_length=200)),
                ('enter_by', models.CharField(max_length=200)),
                ('cb_date', models.CharField(max_length=200)),
                ('updated_by', models.CharField(max_length=200)),
                ('ub_date', models.CharField(max_length=200)),
                ('deleted_by', models.CharField(max_length=200)),
                ('db_date', models.CharField(max_length=200)),
                ('ub_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pg1_new_beds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roon_no', models.IntegerField()),
                ('room_name', models.CharField(max_length=100)),
                ('bed_no', models.IntegerField()),
                ('created_by', models.CharField(max_length=100)),
                ('bed_code', models.IntegerField()),
                ('guest_code', models.IntegerField()),
                ('guest_join_date', models.CharField(max_length=50)),
                ('guest_join_month', models.CharField(max_length=50)),
                ('guest_vacated_date', models.CharField(max_length=50)),
                ('guest_vacate_month', models.CharField(max_length=50)),
                ('share_type', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('advance', models.CharField(max_length=15)),
                ('monthly_rent', models.CharField(max_length=12)),
                ('self_mob', models.CharField(max_length=12)),
                ('age', models.IntegerField(null=True)),
                ('remark', models.CharField(max_length=100)),
                ('narration', models.CharField(max_length=250)),
                ('parent_name', models.CharField(max_length=200)),
                ('parent_mob', models.BigIntegerField(null=True)),
                ('permanent_address', models.TextField()),
                ('jan_rent', models.FloatField(null=True)),
                ('jan_advance', models.CharField(max_length=200)),
                ('jan_due_amt', models.CharField(max_length=200)),
                ('jan_dis_amt', models.CharField(max_length=200)),
                ('jan_rent_rec_date', models.CharField(max_length=200)),
                ('jan_rent_flag', models.IntegerField()),
                ('feb_rent', models.FloatField()),
                ('feb_advance', models.CharField(max_length=200)),
                ('feb_due_amt', models.CharField(max_length=200)),
                ('feb_dis_amt', models.CharField(max_length=200)),
                ('feb_rent_rec_date', models.CharField(max_length=200)),
                ('feb_rent_flag', models.IntegerField()),
                ('march_rent', models.FloatField()),
                ('march_advance', models.CharField(max_length=200)),
                ('march_due_amt', models.CharField(max_length=200)),
                ('march_dis_amt', models.CharField(max_length=200)),
                ('march_rent_rec_date', models.CharField(max_length=200)),
                ('march_rent_flag', models.IntegerField()),
                ('april_rent', models.FloatField()),
                ('april_advance', models.CharField(max_length=200)),
                ('april_due_amt', models.CharField(max_length=200)),
                ('april_dis_amt', models.CharField(max_length=200)),
                ('april_rent_rec_date', models.CharField(max_length=200)),
                ('april_rent_flag', models.IntegerField()),
                ('may_rent', models.FloatField()),
                ('may_advance', models.CharField(max_length=200)),
                ('may_due_amt', models.CharField(max_length=200)),
                ('may_dis_amt', models.CharField(max_length=200)),
                ('may_rent_rec_date', models.CharField(max_length=200)),
                ('may_rent_flag', models.IntegerField()),
                ('june_rent', models.FloatField()),
                ('june_advance', models.CharField(max_length=200)),
                ('june_due_amt', models.CharField(max_length=200)),
                ('june_dis_amt', models.CharField(max_length=200)),
                ('june_rent_rec_date', models.CharField(max_length=200)),
                ('june_rent_flag', models.IntegerField()),
                ('july_rent', models.FloatField()),
                ('july_advance', models.CharField(max_length=200)),
                ('july_due_amt', models.CharField(max_length=200)),
                ('july_dis_amt', models.CharField(max_length=200)),
                ('july_rent_rec_date', models.CharField(max_length=200)),
                ('july_rent_flag', models.IntegerField()),
                ('auguest_rent', models.FloatField()),
                ('auguest_advance', models.CharField(max_length=200)),
                ('auguest_due_amt', models.CharField(max_length=200)),
                ('auguest_dis_amt', models.CharField(max_length=200)),
                ('auguest_rent_rec_date', models.CharField(max_length=200)),
                ('auguest_rent_flag', models.IntegerField()),
                ('sept_rent', models.FloatField()),
                ('sept_advance', models.CharField(max_length=200)),
                ('sept_due_amt', models.CharField(max_length=200)),
                ('sept_dis_amt', models.CharField(max_length=200)),
                ('sept_rent_rec_date', models.CharField(max_length=200)),
                ('sept_rent_flag', models.IntegerField()),
                ('october_rent', models.FloatField()),
                ('october_advance', models.CharField(max_length=200)),
                ('october_due_amt', models.CharField(max_length=200)),
                ('october_dis_amt', models.CharField(max_length=200)),
                ('october_rent_rec_date', models.CharField(max_length=200)),
                ('october_rent_flag', models.IntegerField()),
                ('nov_rent', models.FloatField()),
                ('nov_advance', models.CharField(max_length=200)),
                ('nov_due_amt', models.CharField(max_length=200)),
                ('nov_dis_amt', models.CharField(max_length=200)),
                ('nov_rent_rec_date', models.CharField(max_length=200)),
                ('nov_rent_flag', models.IntegerField()),
                ('dec_rent', models.FloatField()),
                ('dec_advance', models.CharField(max_length=200)),
                ('dec_due_amt', models.CharField(max_length=200)),
                ('dec_dis_amt', models.CharField(max_length=200)),
                ('dec_rent_rec_date', models.CharField(max_length=200)),
                ('dec_rent_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pg1_new_guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roon_no', models.IntegerField()),
                ('room_name', models.CharField(max_length=100)),
                ('bed_no', models.IntegerField()),
                ('created_by', models.CharField(max_length=100)),
                ('bed_code', models.IntegerField()),
                ('guest_code', models.IntegerField()),
                ('guest_join_date', models.CharField(max_length=50)),
                ('guest_join_month', models.CharField(max_length=50)),
                ('guest_vacated_date', models.CharField(max_length=50)),
                ('guest_vacate_month', models.CharField(max_length=50)),
                ('share_type', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('advance', models.CharField(max_length=15)),
                ('monthly_rent', models.CharField(max_length=12)),
                ('self_mob', models.CharField(max_length=12)),
                ('age', models.IntegerField(null=True)),
                ('remark', models.CharField(max_length=100)),
                ('narration', models.CharField(max_length=250)),
                ('parent_name', models.CharField(max_length=200)),
                ('parent_mob', models.BigIntegerField(null=True)),
                ('permanent_address', models.TextField()),
                ('jan_rent', models.FloatField()),
                ('jan_advance', models.CharField(max_length=200)),
                ('jan_due_amt', models.CharField(max_length=200)),
                ('jan_dis_amt', models.CharField(max_length=200)),
                ('jan_rent_rec_date', models.CharField(max_length=200)),
                ('jan_rent_flag', models.IntegerField()),
                ('feb_rent', models.FloatField()),
                ('feb_advance', models.CharField(max_length=200)),
                ('feb_due_amt', models.CharField(max_length=200)),
                ('feb_dis_amt', models.CharField(max_length=200)),
                ('feb_rent_rec_date', models.CharField(max_length=200)),
                ('feb_rent_flag', models.IntegerField()),
                ('march_rent', models.FloatField()),
                ('march_advance', models.CharField(max_length=200)),
                ('march_due_amt', models.CharField(max_length=200)),
                ('march_dis_amt', models.CharField(max_length=200)),
                ('march_rent_rec_date', models.CharField(max_length=200)),
                ('march_rent_flag', models.IntegerField()),
                ('april_rent', models.FloatField()),
                ('april_advance', models.CharField(max_length=200)),
                ('april_due_amt', models.CharField(max_length=200)),
                ('april_dis_amt', models.CharField(max_length=200)),
                ('april_rent_rec_date', models.CharField(max_length=200)),
                ('april_rent_flag', models.IntegerField()),
                ('may_rent', models.FloatField()),
                ('may_advance', models.CharField(max_length=200)),
                ('may_due_amt', models.CharField(max_length=200)),
                ('may_dis_amt', models.CharField(max_length=200)),
                ('may_rent_rec_date', models.CharField(max_length=200)),
                ('may_rent_flag', models.IntegerField()),
                ('june_rent', models.FloatField()),
                ('june_advance', models.CharField(max_length=200)),
                ('june_due_amt', models.CharField(max_length=200)),
                ('june_dis_amt', models.CharField(max_length=200)),
                ('june_rent_rec_date', models.CharField(max_length=200)),
                ('june_rent_flag', models.IntegerField()),
                ('july_rent', models.FloatField()),
                ('july_advance', models.CharField(max_length=200)),
                ('july_due_amt', models.CharField(max_length=200)),
                ('july_dis_amt', models.CharField(max_length=200)),
                ('july_rent_rec_date', models.CharField(max_length=200)),
                ('july_rent_flag', models.IntegerField()),
                ('auguest_rent', models.FloatField()),
                ('auguest_advance', models.CharField(max_length=200)),
                ('auguest_due_amt', models.CharField(max_length=200)),
                ('auguest_dis_amt', models.CharField(max_length=200)),
                ('auguest_rent_rec_date', models.CharField(max_length=200)),
                ('auguest_rent_flag', models.IntegerField()),
                ('sept_rent', models.FloatField()),
                ('sept_advance', models.CharField(max_length=200)),
                ('sept_due_amt', models.CharField(max_length=200)),
                ('sept_dis_amt', models.CharField(max_length=200)),
                ('sept_rent_rec_date', models.CharField(max_length=200)),
                ('sept_rent_flag', models.IntegerField()),
                ('october_rent', models.FloatField()),
                ('october_advance', models.CharField(max_length=200)),
                ('october_due_amt', models.CharField(max_length=200)),
                ('october_dis_amt', models.CharField(max_length=200)),
                ('october_rent_rec_date', models.CharField(max_length=200)),
                ('october_rent_flag', models.IntegerField()),
                ('nov_rent', models.FloatField()),
                ('nov_advance', models.CharField(max_length=200)),
                ('nov_due_amt', models.CharField(max_length=200)),
                ('nov_dis_amt', models.CharField(max_length=200)),
                ('nov_rent_rec_date', models.CharField(max_length=200)),
                ('nov_rent_flag', models.IntegerField()),
                ('dec_rent', models.FloatField()),
                ('dec_advance', models.CharField(max_length=200)),
                ('dec_due_amt', models.CharField(max_length=200)),
                ('dec_dis_amt', models.CharField(max_length=200)),
                ('dec_rent_rec_date', models.CharField(max_length=200)),
                ('dec_rent_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='room_pg1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roon_no', models.IntegerField()),
                ('room_name', models.CharField(max_length=100)),
                ('share_type', models.IntegerField()),
                ('created_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='share_holders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_holders_name', models.CharField(max_length=200)),
                ('share_holders_percentage', models.CharField(max_length=200)),
                ('share_holders_amt', models.CharField(max_length=200)),
                ('created_by', models.CharField(max_length=200)),
                ('cb_date', models.CharField(max_length=200)),
                ('updated_by', models.CharField(max_length=200)),
                ('ub_date', models.CharField(max_length=200)),
                ('deleted_by', models.CharField(max_length=200)),
                ('db_date', models.CharField(max_length=200)),
                ('ub_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='table1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('item_category', models.CharField(max_length=200)),
                ('created_by', models.CharField(max_length=200)),
                ('cb_date', models.CharField(max_length=200)),
                ('updated_bys', models.CharField(max_length=200)),
                ('ub_date', models.CharField(max_length=200)),
                ('deleted_by', models.CharField(max_length=200)),
                ('db_date', models.CharField(max_length=200)),
                ('ub_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
    ]