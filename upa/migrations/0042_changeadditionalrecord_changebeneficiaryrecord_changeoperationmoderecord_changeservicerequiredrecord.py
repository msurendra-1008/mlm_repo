# Generated by Django 3.2.5 on 2021-09-22 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_profile_initial_form_status'),
        ('upa', '0041_auto_20210921_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeServiceRequiredRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upa_id_no', models.CharField(blank=True, max_length=100, null=True)),
                ('request_no', models.IntegerField(blank=True, null=True)),
                ('royal_green_card', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('green_card_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('royal_yellow_card', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('yellow_card_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('royal_red_card', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('red_card_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('sms_alert', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('home_delevery', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('product_display', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('book_new_update', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('general_color_card', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('general_color_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('pvc_color_card', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('pvc_color_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('accouont_passbook', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('account_passbook_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('e_account_statement', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('e_account_statement_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('royal_green_atm', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('green_atm_card_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('royal_yellow_atm', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('yellow_atm_card_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('royal_red_atm', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('red_atm_card_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('royal_blue_atm', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('blue_atm_card_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('modification_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('upa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='change_service_details', to='accounts.profile')),
                ('user_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeOperationModeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upa_id_no', models.CharField(blank=True, max_length=100, null=True)),
                ('request_no', models.IntegerField(blank=True, null=True)),
                ('total_amount', models.IntegerField(blank=True, null=True)),
                ('amount_in_figure', models.CharField(blank=True, max_length=250, null=True)),
                ('transaction_mode', models.CharField(blank=True, choices=[('CARD', 'CARD'), ('CASH', 'CASH'), ('ONLINE TRANSFER', 'ONLINE TRANSFER')], max_length=20, null=True)),
                ('upa_account_operation_mode', models.CharField(blank=True, choices=[('SELF', 'SELF'), ('JOINTLY', 'JOINTLY')], max_length=10, null=True)),
                ('joint_account', models.CharField(blank=True, choices=[('1', '1'), ('2', '2')], max_length=10, null=True)),
                ('uid_no_f', models.CharField(blank=True, max_length=20, null=True)),
                ('name_f', models.CharField(blank=True, max_length=100, null=True)),
                ('relation_upa_f', models.CharField(blank=True, choices=[('WIFE', 'WIFE'), ('SON', 'SON'), ('DAUGHTER', 'DAUGHTER'), ('OTHER', 'OTHER')], max_length=100, null=True)),
                ('aadhar_card_f', models.CharField(blank=True, max_length=16, null=True)),
                ('account_no_f', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile_no_f', models.PositiveIntegerField(blank=True, null=True)),
                ('email_f', models.EmailField(blank=True, max_length=254, null=True)),
                ('address_one_f', models.CharField(blank=True, max_length=100, null=True)),
                ('address_two_f', models.CharField(blank=True, max_length=100, null=True)),
                ('dob_f', models.DateField(blank=True, null=True)),
                ('gender_f', models.CharField(blank=True, max_length=10, null=True)),
                ('marital_status_f', models.CharField(blank=True, max_length=6, null=True)),
                ('extra_detail_f', models.TextField(blank=True, null=True)),
                ('uid_no_s', models.CharField(blank=True, max_length=20, null=True)),
                ('name_s', models.CharField(blank=True, max_length=100, null=True)),
                ('relation_upa_s', models.CharField(blank=True, choices=[('WIFE', 'WIFE'), ('SON', 'SON'), ('DAUGHTER', 'DAUGHTER'), ('OTHER', 'OTHER')], max_length=100, null=True)),
                ('aadhar_card_s', models.CharField(blank=True, max_length=16, null=True)),
                ('account_no_s', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile_no_s', models.PositiveIntegerField(blank=True, null=True)),
                ('email_s', models.EmailField(blank=True, max_length=254, null=True)),
                ('address_one_s', models.CharField(blank=True, max_length=100, null=True)),
                ('address_two_s', models.CharField(blank=True, max_length=100, null=True)),
                ('dob_s', models.DateField(blank=True, null=True)),
                ('gender_s', models.CharField(blank=True, max_length=10, null=True)),
                ('marital_status_s', models.CharField(blank=True, max_length=6, null=True)),
                ('extra_detail_s', models.TextField(blank=True, null=True)),
                ('modification_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('upa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='change_operation_details', to='accounts.profile')),
                ('user_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeBeneficiaryRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upa_id_no', models.CharField(blank=True, max_length=100, null=True)),
                ('request_no', models.IntegerField(blank=True, null=True)),
                ('beneficiary_name', models.CharField(blank=True, max_length=100, null=True)),
                ('beneficiary_id_no', models.CharField(blank=True, max_length=100, null=True)),
                ('relation_upa', models.CharField(blank=True, choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Daughter', 'Daughter'), ('Son', 'Son')], max_length=20, null=True)),
                ('other', models.CharField(blank=True, max_length=100, null=True)),
                ('ben_first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ben_middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ben_last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('f_g_first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('f_g_middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('f_g_last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('m_m_first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('m_m_middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('m_m_last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('update_age_dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Married', 'Married'), ('Unmarried', 'Unmarried')], max_length=100, null=True)),
                ('nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line_one', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line_two', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line_three', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line_four', models.CharField(blank=True, max_length=200, null=True)),
                ('landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('town', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.PositiveIntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('telephone', models.PositiveIntegerField(blank=True, null=True)),
                ('mobile', models.PositiveIntegerField(blank=True, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('identity_proof', models.CharField(blank=True, choices=[('Aadhar Card', 'Aadhar Card'), ('Voter ID Card', 'Voter ID Card'), ('PAN Card', 'PAN Card'), ('Passport', 'Passport'), ('Driving License', 'Driving License')], max_length=20, null=True)),
                ('address_proof', models.CharField(blank=True, choices=[('Aadhar Card', 'Aadhar Card'), ('Voter ID Card', 'Voter ID Card'), ('PAN Card', 'PAN Card'), ('Passport', 'Passport'), ('Driving License', 'Driving License')], max_length=20, null=True)),
                ('id_proof_no', models.CharField(blank=True, max_length=100, null=True)),
                ('id_issued_at', models.DateField(blank=True, null=True)),
                ('id_issued_by', models.CharField(blank=True, max_length=100, null=True)),
                ('add_proof_no', models.CharField(blank=True, max_length=100, null=True)),
                ('add_issued_at', models.DateField(blank=True, null=True)),
                ('add_issued_by', models.CharField(blank=True, max_length=100, null=True)),
                ('modification_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('upa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='change_beneficiary_details', to='accounts.profile')),
                ('user_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeAdditionalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upa_id_no', models.CharField(blank=True, max_length=100, null=True)),
                ('request_no', models.IntegerField(blank=True, null=True)),
                ('educational_qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation_type', models.CharField(blank=True, max_length=100, null=True)),
                ('employer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('self_employeed', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('monthly_income', models.CharField(blank=True, max_length=100, null=True)),
                ('assets', models.CharField(blank=True, help_text='Approximate Value', max_length=20, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('bussiness_nature', models.CharField(blank=True, max_length=100, null=True)),
                ('modification_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('upa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='change_additional_details', to='accounts.profile')),
                ('user_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]