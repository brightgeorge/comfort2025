from django.urls import path, include

from . import admin_branch24
from . import admin_branch24
from . import branch24
from . import reports24
from . import payment24
from . import admin_dashboard_calculations_br24
from . import accounts24
from . import branch_settings24

urlpatterns = [

    path('branch1_dashboard_ob_ch24/', branch24.branch1_dashboard_ob_ch24, name='branch1_dashboard_ob_ch24'),
    path('branch1_dashboard24/',branch24.branch1_dashboard24,name='branch1_dashboard24'),
    path('user_dashboard_calculations_ob_ch24/',branch24.user_dashboard_calculations_ob_ch24,name='user_dashboard_calculations_ob_ch24'),

    path('background_ob_ch24',branch24.background_ob_ch24,name='background_ob_ch24'),
    path('background_regi_ob_ch24',branch24.background_regi_ob_ch24,name='background_regi_ob_ch24'),
    path('custom_background_regi_ob_ch24',branch24.custom_background_regi_ob_ch24,name='custom_background_regi_ob_ch24'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch24/',admin_branch24.branch1_room_create_regi_ob_ch24,name='branch1_room_create_regi_ob_ch24'),
    path('view_all_room_ob_ch24/',admin_branch24.view_all_room_ob_ch24,name='view_all_room_ob_ch24'),
    path('delete_room_ob_ch24/<id>',admin_branch24.delete_room_ob_ch24,name='delete_room_ob_ch24'),

    path('branch1_room_create_ob_ch24/',admin_branch24.branch1_room_create_ob_ch24,name='branch1_room_create_ob_ch24'),

    path('multiple_branch1_room_create_regi24/',admin_branch24.multiple_branch1_room_create_regi24,name='multiple_branch1_room_create_regi24'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch24/', admin_branch24.pg1_bed_create_regi_ob_ch24, name='pg1_bed_create_regi_ob_ch24'),
    path('pg1_view_all_beds_ob_ch24/', admin_branch24.pg1_view_all_beds_ob_ch24, name='pg1_view_all_beds_ob_ch24'),
    path('delete_bed_ob_ch24/<id>', admin_branch24.delete_bed_ob_ch24, name='delete_bed_ob_ch24'),

    path('pg1_bed_create_ob_ch24/', admin_branch24.pg1_bed_create_ob_ch24, name='pg1_bed_create_ob_ch24'),

    path('single_pg1_bed_create_regi_ob_ch24/',admin_branch24.single_pg1_bed_create_regi_ob_ch24,name='single_pg1_bed_create_regi_ob_ch24'),
    path('update_bed_basic_details_ob_ch24/<id>',admin_branch24.update_bed_basic_details_ob_ch24, name='update_bed_basic_details_ob_ch24'),

    path('multiple_single_pg1_bed_create_regi24/',admin_branch24.multiple_single_pg1_bed_create_regi24,name='multiple_single_pg1_bed_create_regi24'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch24/<id>',branch24.br1_admit_guest_ob_ch24,name='br1_admit_guest_ob_ch24'),
    path('view_all_new_guest_ob_ch24/',branch24.view_all_new_guest_ob_ch24,name='view_all_new_guest_ob_ch24'),
    path('update_br1_admit_guest_ob_ch24/<id>',branch24.update_br1_admit_guest_ob_ch24,name='update_br1_admit_guest_ob_ch24'),
    path('vacate_br1_guest_ob_ch24/<id>',branch24.vacate_br1_guest_ob_ch24,name='vacate_br1_guest_ob_ch24'),

    path('active_guest_details_ob_ch24/<guest_code>',branch24.active_guest_details_ob_ch24,name='active_guest_details_ob_ch24'),
    path('view_all_guest_ob_ch24/',branch24.view_all_guest_ob_ch24,name='view_all_guest_ob_ch24'),
    path('shift_guest_ob_ch24/<id>',branch24.shift_guest_ob_ch24,name='shift_guest_ob_ch24'),
    path('shift_guest_regi_ob_ch24/',branch24.shift_guest_regi_ob_ch24,name='shift_guest_regi_ob_ch24'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch24/',branch24.update_all_rent_ob_ch24,name='update_all_rent_ob_ch24'),

    path('multiple_br1_admit_guest24/<id>',branch24.multiple_br1_admit_guest24,name='multiple_br1_admit_guest24'),

#guest end here


##################################
#_ADVANCE_ob_ch24 START HERE
################################


    path('choose_months_advance_ob_ch24/',branch24.choose_months_advance_ob_ch24,name='choose_months_advance_ob_ch24'),

    path('jan_advance_ob_ch24/', branch24.jan_advance_ob_ch24, name='jan_advance_ob_ch24'),
    path('jan_make_payments_advance_ob_ch24/<id>', branch24.jan_make_payments_advance_ob_ch24,name='jan_make_payments_advance_ob_ch24'),
    path('feb_advance_ob_ch24/', branch24.feb_advance_ob_ch24, name='feb_advance_ob_ch24'),
    path('feb_make_payments_advance_ob_ch24/<id>', branch24.feb_make_payments_advance_ob_ch24,name='feb_make_payments_advance_ob_ch24'),
    path('march_advance_ob_ch24/', branch24.march_advance_ob_ch24, name='march_advance_ob_ch24'),
    path('march_make_payments_advance_ob_ch24/<id>', branch24.march_make_payments_advance_ob_ch24,name='march_make_payments_advance_ob_ch24'),
    path('april_advance_ob_ch24/', branch24.april_advance_ob_ch24, name='april_advance_ob_ch24'),
    path('april_make_payments_advance_ob_ch24/<id>', branch24.april_make_payments_advance_ob_ch24, name='april_make_payments_advance_ob_ch24'),

    path('may_advance_ob_ch24/',branch24.may_advance_ob_ch24,name='may_advance_ob_ch24'),
    path('may_make_payments_advance_ob_ch24/<id>', branch24.may_make_payments_advance_ob_ch24, name='may_make_payments_advance_ob_ch24'),
    path('june_advance_ob_ch24/',branch24.june_advance_ob_ch24,name='june_advance_ob_ch24'),
    path('june_make_payments_advance_ob_ch24/<id>', branch24.june_make_payments_advance_ob_ch24, name='june_make_payments_advance_ob_ch24'),
    path('july_advance_ob_ch24/',branch24.july_advance_ob_ch24,name='july_advance_ob_ch24'),
    path('july_make_payments_advance_ob_ch24/<id>', branch24.july_make_payments_advance_ob_ch24, name='july_make_payments_advance_ob_ch24'),
    path('auguest_advance_ob_ch24/', branch24.auguest_advance_ob_ch24, name='auguest_advance_ob_ch24'),
    path('auguest_make_payments_advance_ob_ch24/<id>', branch24.auguest_make_payments_advance_ob_ch24, name='auguest_make_payments_advance_ob_ch24'),

    path('sept_advance_ob_ch24/', branch24.sept_advance_ob_ch24, name='sept_advance_ob_ch24'),
    path('sept_make_payments_advance_ob_ch24/<id>', branch24.sept_make_payments_advance_ob_ch24,name='sept_make_payments_advance_ob_ch24'),
    path('october_advance_ob_ch24/', branch24.october_advance_ob_ch24, name='october_advance_ob_ch24'),
    path('october_make_payments_advance_ob_ch24/<id>', branch24.october_make_payments_advance_ob_ch24, name='october_make_payments_advance_ob_ch24'),
    path('nov_advance_ob_ch24/', branch24.nov_advance_ob_ch24, name='nov_advance_ob_ch24'),
    path('nov_make_payments_advance_ob_ch24/<id>', branch24.nov_make_payments_advance_ob_ch24,name='nov_make_payments_advance_ob_ch24'),
    path('dec_advance_ob_ch24/', branch24.dec_advance_ob_ch24, name='dec_advance_ob_ch24'),
    path('dec_make_payments_advance_ob_ch24/<id>', branch24.dec_make_payments_advance_ob_ch24, name='dec_make_payments_advance_ob_ch24'),



##################################
#_ADVANCE_ob_ch24 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch24/',branch24.choose_months_ob_ch24,name='choose_months_ob_ch24'),

    path('jan_ob_ch24/',branch24.jan_ob_ch24,name='jan_ob_ch24'),
    path('jan_manke_payments_ob_ch24/<id>',branch24.jan_manke_payments_ob_ch24,name='jan_manke_payments_ob_ch24'),

    path('feb_ob_ch24/',branch24.feb_ob_ch24,name='feb_ob_ch24'),
    path('feb_manke_payments_ob_ch24/<id>',branch24.feb_manke_payments_ob_ch24,name='feb_manke_payments_ob_ch24'),

    path('march_ob_ch24/',branch24.march_ob_ch24,name='march_ob_ch24'),
    path('march_manke_payments_ob_ch24/<id>',branch24.march_manke_payments_ob_ch24,name='march_manke_payments_ob_ch24'),

    path('april_ob_ch24/',branch24.april_ob_ch24,name='april_ob_ch24'),
    path('april_make_payments_ob_ch24/<id>',branch24.april_make_payments_ob_ch24,name='april_make_payments_ob_ch24'),

    path('may_ob_ch24/',branch24.may_ob_ch24,name='may_ob_ch24'),
    path('may_make_payments_ob_ch24/<id>',branch24.may_make_payments_ob_ch24,name='may_make_payments_ob_ch24'),

    path('june_ob_ch24/',branch24.june_ob_ch24,name='june_ob_ch24'),
    path('june_make_payments_ob_ch24/<id>',branch24.june_make_payments_ob_ch24,name='june_make_payments_ob_ch24'),

    path('july_ob_ch24/',branch24.july_ob_ch24,name='july_ob_ch24'),
    path('july_make_payments_ob_ch24/<id>',branch24.july_make_payments_ob_ch24,name='july_make_payments_ob_ch24'),

    path('aug_ob_ch24/',branch24.aug_ob_ch24,name='aug_ob_ch24'),
    path('aug_make_payments_ob_ch24/<id>',branch24.aug_make_payments_ob_ch24,name='aug_make_payments_ob_ch24'),

    path('sept_ob_ch24/',branch24.sept_ob_ch24,name='sept_ob_ch24'),
    path('sept_make_payments_ob_ch24/<id>',branch24.sept_make_payments_ob_ch24,name='sept_make_payments_ob_ch24'),

    path('oct_ob_ch24/',branch24.oct_ob_ch24,name='oct_ob_ch24'),
    path('oct_make_payments_ob_ch24/<id>',branch24.oct_make_payments_ob_ch24,name='oct_make_payments_ob_ch24'),

    path('nov_ob_ch24/',branch24.nov_ob_ch24,name='nov_ob_ch24'),
    path('nov_make_payments_ob_ch24/<id>',branch24.nov_make_payments_ob_ch24,name='nov_make_payments_ob_ch24'),

    path('dec_ob_ch24/',branch24.dec_ob_ch24,name='dec_ob_ch24'),
    path('dec_make_payments_ob_ch24/<id>',branch24.dec_make_payments_ob_ch24,name='dec_make_payments_ob_ch24'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch24/', payment24.choose_user_ob_ch24, name='choose_user_ob_ch24'),
    path('payment_user_details_ob_ch24/<id>', payment24.payment_user_details_ob_ch24, name='payment_user_details_ob_ch24'),
    path('close_choose_user_ob_ch24/<id>',payment24.close_choose_user_ob_ch24,name='close_choose_user_ob_ch24'),

    path('monthly_jan_make_payments_ob_ch24/<id>', payment24.monthly_jan_make_payments_ob_ch24, name='monthly_jan_make_payments_ob_ch24'),
    path('monthly_feb_make_payments_ob_ch24/<id>', payment24.monthly_feb_make_payments_ob_ch24, name='monthly_feb_make_payments_ob_ch24'),
    path('monthly_march_make_payments_ob_ch24/<id>', payment24.monthly_march_make_payments_ob_ch24, name='monthly_march_make_payments_ob_ch24'),
    path('monthly_april_make_payments_ob_ch24/<id>', payment24.monthly_april_make_payments_ob_ch24, name='monthly_april_make_payments_ob_ch24'),
    path('monthly_may_make_payments_ob_ch24/<id>', payment24.monthly_may_make_payments_ob_ch24, name='monthly_may_make_payments_ob_ch24'),
    path('monthly_june_make_payments_ob_ch24/<id>', payment24.monthly_june_make_payments_ob_ch24, name='monthly_june_make_payments_ob_ch24'),

    path('monthly_july_make_payments_ob_ch24/<id>', payment24.monthly_july_make_payments_ob_ch24, name='monthly_july_make_payments_ob_ch24'),
    path('monthly_aug_make_payments_ob_ch24/<id>', payment24.monthly_aug_make_payments_ob_ch24, name='monthly_aug_make_payments_ob_ch24'),
    path('monthly_sept_make_payments_ob_ch24/<id>', payment24.monthly_sept_make_payments_ob_ch24, name='monthly_sept_make_payments_ob_ch24'),
    path('monthly_oct_make_payments_ob_ch24/<id>', payment24.monthly_oct_make_payments_ob_ch24, name='monthly_oct_make_payments_ob_ch24'),
    path('monthly_nov_make_payments_ob_ch24/<id>', payment24.monthly_nov_make_payments_ob_ch24, name='monthly_nov_make_payments_ob_ch24'),
    path('monthly_dec_make_payments_ob_ch24/<id>', payment24.monthly_dec_make_payments_ob_ch24, name='monthly_dec_make_payments_ob_ch24'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch24/',branch24.unpaid_rent_choose_months_ob_ch24,name='unpaid_rent_choose_months_ob_ch24'),

    path('jan_unpaid_rent_ob_ch24/', branch24.jan_unpaid_rent_ob_ch24, name='jan_unpaid_rent_ob_ch24'),
    path('table_jan_unpaid_rent_ob_ch24/', branch24.table_jan_unpaid_rent_ob_ch24, name='table_jan_unpaid_rent_ob_ch24'),
    path('feb_unpaid_rent_ob_ch24/', branch24.feb_unpaid_rent_ob_ch24, name='feb_unpaid_rent_ob_ch24'),
    path('table_feb_unpaid_rent_ob_ch24/', branch24.table_feb_unpaid_rent_ob_ch24, name='table_feb_unpaid_rent_ob_ch24'),
    path('mar_unpaid_rent_ob_ch24/', branch24.mar_unpaid_rent_ob_ch24, name='mar_unpaid_rent_ob_ch24'),
    path('table_mar_unpaid_rent_ob_ch24/', branch24.table_mar_unpaid_rent_ob_ch24, name='table_mar_unpaid_rent_ob_ch24'),
    path('april_unpaid_rent_ob_ch24/', branch24.april_unpaid_rent_ob_ch24, name='april_unpaid_rent_ob_ch24'),
    path('table_april_unpaid_rent_ob_ch24/', branch24.table_april_unpaid_rent_ob_ch24, name='table_april_unpaid_rent_ob_ch24'),

    path('may_unpaid_rent_ob_ch24/', branch24.may_unpaid_rent_ob_ch24, name='may_unpaid_rent_ob_ch24'),
    path('table_may_unpaid_rent_ob_ch24/', branch24.table_may_unpaid_rent_ob_ch24, name='table_may_unpaid_rent_ob_ch24'),
    path('june_unpaid_rent_ob_ch24/', branch24.june_unpaid_rent_ob_ch24, name='june_unpaid_rent_ob_ch24'),
    path('table_june_unpaid_rent_ob_ch24/', branch24.table_june_unpaid_rent_ob_ch24, name='table_june_unpaid_rent_ob_ch24'),
    path('july_unpaid_rent_ob_ch24/', branch24.july_unpaid_rent_ob_ch24, name='july_unpaid_rent_ob_ch24'),
    path('table_july_unpaid_rent_ob_ch24',branch24.table_july_unpaid_rent_ob_ch24,name='table_july_unpaid_rent_ob_ch24'),
    path('aug_unpaid_rent_ob_ch24/', branch24.aug_unpaid_rent_ob_ch24, name='aug_unpaid_rent_ob_ch24'),
    path('table_aug_unpaid_rent_ob_ch24/',branch24.table_aug_unpaid_rent_ob_ch24,name='table_aug_unpaid_rent_ob_ch24'),

    path('sept_unpaid_rent_ob_ch24/', branch24.sept_unpaid_rent_ob_ch24, name='sept_unpaid_rent_ob_ch24'),
    path('table_sept_unpaid_rent_ob_ch24/', branch24.table_sept_unpaid_rent_ob_ch24, name='table_sept_unpaid_rent_ob_ch24'),
    path('oct_unpaid_rent_ob_ch24/', branch24.oct_unpaid_rent_ob_ch24, name='oct_unpaid_rent_ob_ch24'),
    path('table_oct_unpaid_rent_ob_ch24/', branch24.table_oct_unpaid_rent_ob_ch24, name='table_oct_unpaid_rent_ob_ch24'),
    path('nov_unpaid_rent_ob_ch24/', branch24.nov_unpaid_rent_ob_ch24, name='nov_unpaid_rent_ob_ch24'),
    path('table_nov_unpaid_rent_ob_ch24/', branch24.table_nov_unpaid_rent_ob_ch24, name='table_nov_unpaid_rent_ob_ch24'),
    path('dec_unpaid_rent_ob_ch24/', branch24.dec_unpaid_rent_ob_ch24, name='dec_unpaid_rent_ob_ch24'),
    path('table_dec_unpaid_rent_ob_ch24/', branch24.table_dec_unpaid_rent_ob_ch24, name='table_dec_unpaid_rent_ob_ch24'),

    path('details_of_unpaid_guests_ob_ch24/<id>',branch24.details_of_unpaid_guests_ob_ch24,name='details_of_unpaid_guests_ob_ch24'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch24/',branch24.paid_rent_choose_months_ob_ch24,name='paid_rent_choose_months_ob_ch24'),
    path('partially_paid_guest_choose_months_ob_ch24/',reports24.partially_paid_guest_choose_months_ob_ch24,name='partially_paid_guest_choose_months_ob_ch24'),

    path('jan_paid_rent_ob_ch24/', branch24.jan_paid_rent_ob_ch24, name='jan_paid_rent_ob_ch24'),
    path('table_jan_paid_rent_ob_ch24/', branch24.table_jan_paid_rent_ob_ch24, name='table_jan_paid_rent_ob_ch24'),
    path('jan_full_paid_guest_ob_ch24/', reports24.jan_full_paid_guest_ob_ch24, name='jan_full_paid_guest_ob_ch24'),
    path('jan_partially_paid_guest_ob_ch24/', reports24.jan_partially_paid_guest_ob_ch24, name='jan_partially_paid_guest_ob_ch24'),
    path('table_jan_partially_paid_guest_ob_ch24/', reports24.table_jan_partially_paid_guest_ob_ch24,name='table_jan_partially_paid_guest_ob_ch24'),

    path('feb_paid_rent_ob_ch24/', branch24.feb_paid_rent_ob_ch24, name='feb_paid_rent_ob_ch24'),
    path('table_feb_paid_rent_ob_ch24/', branch24.table_feb_paid_rent_ob_ch24, name='table_feb_paid_rent_ob_ch24'),
    path('feb_full_paid_guest_ob_ch24/', reports24.feb_full_paid_guest_ob_ch24, name='feb_full_paid_guest_ob_ch24'),
    path('feb_partially_paid_guest_ob_ch24/', reports24.feb_partially_paid_guest_ob_ch24, name='feb_partially_paid_guest_ob_ch24'),
    path('table_feb_partially_paid_guest_ob_ch24/', reports24.table_feb_partially_paid_guest_ob_ch24,name='table_feb_partially_paid_guest_ob_ch24'),

    path('mar_paid_rent_ob_ch24/', branch24.mar_paid_rent_ob_ch24, name='mar_paid_rent_ob_ch24'),
    path('table_mar_paid_rent_ob_ch24/', branch24.table_mar_paid_rent_ob_ch24, name='table_mar_paid_rent_ob_ch24'),
    path('march_full_paid_guest_ob_ch24/', reports24.march_full_paid_guest_ob_ch24, name='march_full_paid_guest_ob_ch24'),
    path('march_partially_paid_guest_ob_ch24/', reports24.march_partially_paid_guest_ob_ch24, name='march_partially_paid_guest_ob_ch24'),
    path('table_march_partially_paid_guest_ob_ch24/', reports24.table_march_partially_paid_guest_ob_ch24,name='table_march_partially_paid_guest_ob_ch24'),

    path('april_paid_rent_ob_ch24/', branch24.april_paid_rent_ob_ch24, name='april_paid_rent_ob_ch24'),
    path('table_april_paid_rent_ob_ch24/', branch24.table_april_paid_rent_ob_ch24, name='table_april_paid_rent_ob_ch24'),
    path('april_full_paid_guest_ob_ch24/', reports24.april_full_paid_guest_ob_ch24, name='april_full_paid_guest_ob_ch24'),
    path('april_partially_paid_guest_ob_ch24/', reports24.april_partially_paid_guest_ob_ch24, name='april_partially_paid_guest_ob_ch24'),
    path('table_april_partially_paid_guest_ob_ch24/', reports24.table_april_partially_paid_guest_ob_ch24,name='table_april_partially_paid_guest_ob_ch24'),

    path('may_paid_rent_ob_ch24/', branch24.may_paid_rent_ob_ch24, name='may_paid_rent_ob_ch24'),
    path('table_may_paid_rent_ob_ch24/', branch24.table_may_paid_rent_ob_ch24, name='table_may_paid_rent_ob_ch24'),
    path('may_full_paid_guest_ob_ch24/', reports24.may_full_paid_guest_ob_ch24, name='may_full_paid_guest_ob_ch24'),
    path('may_partially_paid_guest_ob_ch24/', reports24.may_partially_paid_guest_ob_ch24, name='may_partially_paid_guest_ob_ch24'),
    path('table_may_partially_paid_guest_ob_ch24/', reports24.table_may_partially_paid_guest_ob_ch24, name='table_may_partially_paid_guest_ob_ch24'),

    path('june_paid_rent_ob_ch24/', branch24.june_paid_rent_ob_ch24, name='june_paid_rent_ob_ch24'),
    path('table_june_paid_rent_ob_ch24/', branch24.table_june_paid_rent_ob_ch24, name='table_june_paid_rent_ob_ch24'),
    path('june_full_paid_guest_ob_ch24/', reports24.june_full_paid_guest_ob_ch24, name='june_full_paid_guest_ob_ch24'),
    path('june_partially_paid_guest_ob_ch24/', reports24.june_partially_paid_guest_ob_ch24, name='june_partially_paid_guest_ob_ch24'),
    path('table_june_partially_paid_guest_ob_ch24/', reports24.table_june_partially_paid_guest_ob_ch24, name='table_june_partially_paid_guest_ob_ch24'),

    path('july_paid_rent_ob_ch24/', branch24.july_paid_rent_ob_ch24, name='july_paid_rent_ob_ch24'),
    path('table_july_paid_rent_ob_ch24/', branch24.table_july_paid_rent_ob_ch24, name='table_july_paid_rent_ob_ch24'),
    path('july_full_paid_guest_ob_ch24/', reports24.july_full_paid_guest_ob_ch24, name='july_full_paid_guest_ob_ch24'),
    path('july_partially_paid_guest_ob_ch24/', reports24.july_partially_paid_guest_ob_ch24, name='july_partially_paid_guest_ob_ch24'),
    path('table_july_partially_paid_guest_ob_ch24/', reports24.table_july_partially_paid_guest_ob_ch24, name='table_july_partially_paid_guest_ob_ch24'),

    path('aug_paid_rent_ob_ch24/', branch24.aug_paid_rent_ob_ch24, name='aug_paid_rent_ob_ch24'),
    path('table_aug_paid_rent_ob_ch24/', branch24.table_aug_paid_rent_ob_ch24, name='table_aug_paid_rent_ob_ch24'),
    path('auguest_full_paid_guest_ob_ch24/', reports24.auguest_full_paid_guest_ob_ch24, name='auguest_full_paid_guest_ob_ch24'),
    path('auguest_partially_paid_guest_ob_ch24/', reports24.auguest_partially_paid_guest_ob_ch24,name='auguest_partially_paid_guest_ob_ch24'),
    path('table_auguest_partially_paid_guest_ob_ch24/', reports24.table_auguest_partially_paid_guest_ob_ch24,name='table_auguest_partially_paid_guest_ob_ch24'),

    path('sept_paid_rent_ob_ch24/', branch24.sept_paid_rent_ob_ch24, name='sept_paid_rent_ob_ch24'),
    path('table_sept_paid_rent_ob_ch24/', branch24.table_sept_paid_rent_ob_ch24, name='table_sept_paid_rent_ob_ch24'),
    path('sept_full_paid_guest_ob_ch24/', reports24.sept_full_paid_guest_ob_ch24, name='sept_full_paid_guest_ob_ch24'),
    path('sept_partially_paid_guest_ob_ch24/', reports24.sept_partially_paid_guest_ob_ch24, name='sept_partially_paid_guest_ob_ch24'),
    path('table_sept_partially_paid_guest_ob_ch24/', reports24.table_sept_partially_paid_guest_ob_ch24,name='table_sept_partially_paid_guest_ob_ch24'),

    path('oct_paid_rent_ob_ch24/', branch24.oct_paid_rent_ob_ch24, name='oct_paid_rent_ob_ch24'),
    path('table_oct_paid_rent_ob_ch24/', branch24.table_oct_paid_rent_ob_ch24, name='table_oct_paid_rent_ob_ch24'),
    path('october_full_paid_guest_ob_ch24/', reports24.october_full_paid_guest_ob_ch24, name='october_full_paid_guest_ob_ch24'),
    path('october_partially_paid_guest_ob_ch24/', reports24.october_partially_paid_guest_ob_ch24,name='october_partially_paid_guest_ob_ch24'),
    path('table_october_partially_paid_guest_ob_ch24/', reports24.table_october_partially_paid_guest_ob_ch24,name='table_october_partially_paid_guest_ob_ch24'),

    path('nov_paid_rent_ob_ch24/', branch24.nov_paid_rent_ob_ch24, name='nov_paid_rent_ob_ch24'),
    path('table_nov_paid_rent_ob_ch24/', branch24.table_nov_paid_rent_ob_ch24, name='table_nov_paid_rent_ob_ch24'),
    path('nov_full_paid_guest_ob_ch24/', reports24.nov_full_paid_guest_ob_ch24, name='nov_full_paid_guest_ob_ch24'),
    path('nov_partially_paid_guest_ob_ch24/', reports24.nov_partially_paid_guest_ob_ch24, name='nov_partially_paid_guest_ob_ch24'),
    path('table_nov_partially_paid_guest_ob_ch24/', reports24.table_nov_partially_paid_guest_ob_ch24,name='table_nov_partially_paid_guest_ob_ch24'),

    path('dec_paid_rent_ob_ch24/', branch24.dec_paid_rent_ob_ch24, name='dec_paid_rent_ob_ch24'),
    path('table_dec_paid_rent_ob_ch24/', branch24.table_dec_paid_rent_ob_ch24, name='table_dec_paid_rent_ob_ch24'),
    path('dec_full_paid_guest_ob_ch24/', reports24.dec_full_paid_guest_ob_ch24, name='dec_full_paid_guest_ob_ch24'),
    path('dec_partially_paid_guest_ob_ch24/', reports24.dec_partially_paid_guest_ob_ch24, name='dec_partially_paid_guest_ob_ch24'),
    path('table_dec_partially_paid_guest_ob_ch24/', reports24.table_dec_partially_paid_guest_ob_ch24,name='table_dec_partially_paid_guest_ob_ch24'),

    path('details_of_paid_guests_ob_ch24/<id>',branch24.details_of_paid_guests_ob_ch24,name='details_of_paid_guests_ob_ch24'),
    path('full_paid_guest_ob_ch24/',reports24.full_paid_guest_ob_ch24,name='full_paid_guest_ob_ch24'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch24/',branch24.viewall_vacate_guest_ob_ch24,name='viewall_vacate_guest_ob_ch24'),
    path('details_of_vacate_guest_ob_ch24/<id>',branch24.details_of_vacate_guest_ob_ch24,name='details_of_vacate_guest_ob_ch24'),
    path('full_vacated_guest_details_ob_ch24',branch24.full_vacated_guest_details_ob_ch24,name='full_vacated_guest_details_ob_ch24'),
    path('full_vacated_guest_table_ob_ch24',branch24.full_vacated_guest_table_ob_ch24,name='full_vacated_guest_table_ob_ch24'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch24/<id>', branch24.jan_manke_payments_vacate_ob_ch24, name='jan_manke_payments_vacate_ob_ch24'),
    path('feb_manke_payments_vacate_ob_ch24/<id>', branch24.feb_manke_payments_vacate_ob_ch24, name='feb_manke_payments_vacate_ob_ch24'),
    path('march_manke_payments_vacate_ob_ch24/<id>', branch24.march_manke_payments_vacate_ob_ch24, name='march_manke_payments_vacate_ob_ch24'),
    path('april_make_payments_vacate_ob_ch24/<id>', branch24.april_make_payments_vacate_ob_ch24, name='april_make_payments_vacate_ob_ch24'),

    path('may_make_payments_vacate_ob_ch24/<id>', branch24.may_make_payments_vacate_ob_ch24, name='may_make_payments_vacate_ob_ch24'),
    path('june_make_payments_vacate_ob_ch24/<id>', branch24.june_make_payments_vacate_ob_ch24, name='june_make_payments_vacate_ob_ch24'),
    path('july_make_payments_vacate_ob_ch24/<id>', branch24.july_make_payments_vacate_ob_ch24, name='july_make_payments_vacate_ob_ch24'),
    path('aug_make_payments_vacate_ob_ch24/<id>', branch24.aug_make_payments_vacate_ob_ch24, name='aug_make_payments_vacate_ob_ch24'),

    path('sept_make_payments_vacate_ob_ch24/<id>', branch24.sept_make_payments_vacate_ob_ch24, name='sept_make_payments_vacate_ob_ch24'),
    path('oct_make_payments_vacate_ob_ch24/<id>', branch24.oct_make_payments_vacate_ob_ch24, name='oct_make_payments_vacate_ob_ch24'),
    path('nov_make_payments_vacate_ob_ch24/<id>', branch24.nov_make_payments_vacate_ob_ch24, name='nov_make_payments_vacate_ob_ch24'),
    path('dec_make_payments_vacate_ob_ch24/<id>', branch24.dec_make_payments_vacate_ob_ch24, name='dec_make_payments_vacate_ob_ch24'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch24/',branch24.detail_guest_general_ob_ch24,name='detail_guest_general_ob_ch24'),

    path('jan_print_ob_ch24/',branch24.jan_print_ob_ch24,name='jan_print_ob_ch24'),
    path('feb_print_ob_ch24/',branch24.feb_print_ob_ch24,name='feb_print_ob_ch24'),
    path('march_print_ob_ch24/',branch24.march_print_ob_ch24,name='march_print_ob_ch24'),
    path('april_print_ob_ch24/',branch24.april_print_ob_ch24,name='april_print_ob_ch24'),

    path('may_print_ob_ch24/',branch24.may_print_ob_ch24,name='may_print_ob_ch24'),
    path('june_print_ob_ch24/',branch24.june_print_ob_ch24,name='june_print_ob_ch24'),
    path('july_print_ob_ch24/', branch24.july_print_ob_ch24, name='july_print_ob_ch24'),
    path('aug_print_ob_ch24/', branch24.aug_print_ob_ch24, name='aug_print_ob_ch24'),

    path('sept_print_ob_ch24/', branch24.sept_print_ob_ch24, name='sept_print_ob_ch24'),
    path('oct_print_ob_ch24/', branch24.oct_print_ob_ch24, name='oct_print_ob_ch24'),
    path('nov_print_ob_ch24/', branch24.nov_print_ob_ch24, name='nov_print_ob_ch24'),
    path('dec_print_ob_ch24/', branch24.dec_print_ob_ch24, name='dec_print_ob_ch24'),

    path('new_year_jan_print_ob_ch24/', branch24.new_year_jan_print_ob_ch24, name='new_year_jan_print_ob_ch24'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch24/', branch24.jan_close_ob_ch24, name='jan_close_ob_ch24'),
    path('jan_close_decision_page_ob_ch24/', branch24.jan_close_decision_page_ob_ch24, name='jan_close_decision_page_ob_ch24'),
    path('feb_close/', branch24.feb_close_ob_ch24, name='feb_close_ob_ch24'),
    path('feb_close_decision_page_ob_ch24/', branch24.feb_close_decision_page_ob_ch24, name='feb_close_decision_page_ob_ch24'),
    path('mar_close_ob_ch24/', branch24.mar_close_ob_ch24, name='mar_close_ob_ch24'),
    path('mar_close_decision_page/', branch24.mar_close_decision_page_ob_ch24, name='mar_close_decision_page_ob_ch24'),
    path('apr_close_ob_ch24/', branch24.apr_close_ob_ch24, name='apr_close_ob_ch24'),
    path('apr_close_decision_page_ob_ch24/', branch24.apr_close_decision_page_ob_ch24, name='apr_close_decision_page_ob_ch24'),

    path('may_close_ob_ch24/', branch24.may_close_ob_ch24, name='may_close_ob_ch24'),
    path('may_close_decision_page_ob_ch24/', branch24.may_close_decision_page_ob_ch24, name='may_close_decision_page_ob_ch24'),
    path('jun_close_ob_ch24/', branch24.jun_close_ob_ch24, name='jun_close_ob_ch24'),
    path('jun_close_decision_page_ob_ch24/', branch24.jun_close_decision_page_ob_ch24, name='jun_close_decision_page_ob_ch24'),
    path('jul_close_ob_ch24/', branch24.jul_close_ob_ch24, name='jul_close_ob_ch24'),
    path('jul_close_decision_page_ob_ch24/', branch24.jul_close_decision_page_ob_ch24, name='jul_close_decision_page_ob_ch24'),
    path('aug_close_ob_ch24/', branch24.aug_close_ob_ch24, name='aug_close_ob_ch24'),
    path('aug_close_decision_page_ob_ch24/', branch24.aug_close_decision_page_ob_ch24, name='aug_close_decision_page_ob_ch24'),

    path('sep_close_ob_ch24/', branch24.sep_close_ob_ch24, name='sep_close_ob_ch24'),
    path('sep_close_decision_page_ob_ch24/', branch24.sep_close_decision_page_ob_ch24, name='sep_close_decision_page_ob_ch24'),
    path('oct_close_ob_ch24/', branch24.oct_close_ob_ch24, name='oct_close_ob_ch24'),
    path('oct_close_decision_page_ob_ch24/', branch24.oct_close_decision_page_ob_ch24, name='oct_close_decision_page_ob_ch24'),
    path('nov_close_ob_ch24/', branch24.nov_close_ob_ch24, name='nov_close_ob_ch24'),
    path('nov_close_decision_page_ob_ch24/', branch24.nov_close_decision_page_ob_ch24, name='nov_close_decision_page_ob_ch24'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch24/',reports24.detailed_report_choose_months_ob_ch24,name='detailed_report_choose_months_ob_ch24'),

    path('jan_details_live_ob_ch24/', reports24.jan_details_live_ob_ch24, name='jan_details_live_ob_ch24'),
    path('jan_print_live_ob_ch24/', reports24.jan_print_live_ob_ch24, name='jan_print_live_ob_ch24'),
    path('feb_details_live_ob_ch24/', reports24.feb_details_live_ob_ch24, name='feb_details_live_ob_ch24'),
    path('feb_print_live_ob_ch24/', reports24.feb_print_live_ob_ch24, name='feb_print_live_ob_ch24'),
    path('march_details_live_ob_ch24/', reports24.march_details_live_ob_ch24, name='march_details_live_ob_ch24'),
    path('march_print_live_ob_ch24/', reports24.march_print_live_ob_ch24, name='march_print_live_ob_ch24'),

    path('april_details_live_ob_ch24/', reports24.april_details_live_ob_ch24, name='april_details_live_ob_ch24'),
    path('april_print_live_ob_ch24/', reports24.april_print_live_ob_ch24, name='april_print_live_ob_ch24'),
    path('may_details_live_ob_ch24/', reports24.may_details_live_ob_ch24, name='may_details_live_ob_ch24'),
    path('may_print_live_ob_ch24/', reports24.may_print_live_ob_ch24, name='may_print_live_ob_ch24'),
    path('june_details_live_ob_ch24/',reports24.june_details_live_ob_ch24,name='june_details_live_ob_ch24'),
    path('june_print_live_ob_ch24/', reports24.june_print_live_ob_ch24, name='june_print_live_ob_ch24'),

    path('july_details_live_ob_ch24/', reports24.july_details_live_ob_ch24, name='july_details_live_ob_ch24'),
    path('july_print_live_ob_ch24/', reports24.july_print_live_ob_ch24, name='july_print_live_ob_ch24'),
    path('auguest_details_live_ob_ch24/', reports24.auguest_details_live_ob_ch24, name='auguest_details_live_ob_ch24'),
    path('auguest_print_live_ob_ch24/', reports24.auguest_print_live_ob_ch24, name='auguest_print_live_ob_ch24'),
    path('sept_details_live_ob_ch24/', reports24.sept_details_live_ob_ch24, name='sept_details_live_ob_ch24'),
    path('sept_print_live_ob_ch24/', reports24.sept_print_live_ob_ch24, name='sept_print_live_ob_ch24'),

    path('october_details_live_ob_ch24/', reports24.october_details_live_ob_ch24, name='october_details_live_ob_ch24'),
    path('october_print_live_ob_ch24/', reports24.october_print_live_ob_ch24, name='october_print_live_ob_ch24'),
    path('nov_details_live_ob_ch24/', reports24.nov_details_live_ob_ch24, name='nov_details_live_ob_ch24'),
    path('nov_print_live_ob_ch24/', reports24.nov_print_live_ob_ch24, name='nov_print_live_ob_ch24'),
    path('dec_details_live_ob_ch24/', reports24.dec_details_live_ob_ch24, name='dec_details_live_ob_ch24'),
    path('dec_print_live_ob_ch24/', reports24.dec_print_live_ob_ch24, name='dec_print_live_ob_ch24'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch24/', reports24.viewall_vaccant_room_ob_ch24, name='viewall_vaccant_room_ob_ch24'),

    path('d_ob_ch24/', branch24.dynamic, name='dynamic'),

    path('manage_bed_ob_ch24/', branch24.manage_bed_ob_ch24, name='manage_bed_ob_ch24'),
    path('manage_new_guest_ob_ch24/', branch24.manage_new_guest_ob_ch24, name='manage_new_guest_ob_ch24'),
    path('manage_update_new_guest_ob_ch24/<id>', branch24.manage_update_new_guest_ob_ch24, name='manage_update_new_guest_ob_ch24'),
    path('manage_update_beds_ob_ch24/<id>', branch24.manage_update_beds_ob_ch24, name='manage_update_beds_ob_ch24'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch24/', branch24.view_all_due_amt_ob_ch24, name='view_all_due_amt_ob_ch24'),
    path('due_amt_mgt_choose_months_ob_ch24/', branch24.due_amt_mgt_choose_months_ob_ch24, name='due_amt_mgt_choose_months_ob_ch24'),

    path('view_jan_account_details_ob_ch24/', branch24.view_jan_account_details_ob_ch24, name='view_jan_account_details_ob_ch24'),
    path('jan_account_mgt_ob_ch24/<id>',branch24.jan_account_mgt_ob_ch24,name='jan_account_mgt_ob_ch24'),
    path('view_feb_account_details_ob_ch24/', branch24.view_feb_account_details_ob_ch24, name='view_feb_account_details_ob_ch24'),
    path('feb_account_mgt_ob_ch24/<id>',branch24.feb_account_mgt_ob_ch24,name='feb_account_mgt_ob_ch24'),
    path('view_march_account_details_ob_ch24/', branch24.view_march_account_details_ob_ch24, name='view_march_account_details_ob_ch24'),
    path('march_account_mgt_ob_ch24/<id>',branch24.march_account_mgt_ob_ch24,name='march_account_mgt_ob_ch24'),
    path('view_april_account_details_ob_ch24/', branch24.view_april_account_details_ob_ch24, name='view_april_account_details_ob_ch24'),
    path('april_account_mgt_ob_ch24/<id>',branch24.april_account_mgt_ob_ch24,name='april_account_mgt_ob_ch24'),

    path('view_may_account_details_ob_ch24/',branch24.view_may_account_details_ob_ch24,name='view_may_account_details_ob_ch24'),
    path('may_account_mgt_ob_ch24/<id>', branch24.may_account_mgt_ob_ch24, name='may_account_mgt_ob_ch24'),
    path('view_june_account_details_ob_ch24/', branch24.view_june_account_details_ob_ch24, name='view_june_account_details_ob_ch24'),
    path('june_account_mgt_ob_ch24/<id>',branch24.june_account_mgt_ob_ch24,name='june_account_mgt_ob_ch24'),
    path('view_july_account_details_ob_ch24/', branch24.view_july_account_details_ob_ch24, name='view_july_account_details_ob_ch24'),
    path('july_account_mgt_ob_ch24/<id>',branch24.july_account_mgt_ob_ch24,name='july_account_mgt_ob_ch24'),
    path('view_auguest_account_details_ob_ch24/', branch24.view_auguest_account_details_ob_ch24, name='view_auguest_account_details_ob_ch24'),
    path('auguest_account_mgt_ob_ch24/<id>',branch24.auguest_account_mgt_ob_ch24,name='auguest_account_mgt_ob_ch24'),

    path('view_sept_account_details_ob_ch24/', branch24.view_sept_account_details_ob_ch24, name='view_sept_account_details_ob_ch24'),
    path('sept_account_mgt_ob_ch24/<id>',branch24.sept_account_mgt_ob_ch24,name='sept_account_mgt_ob_ch24'),
    path('view_october_account_details_ob_ch24/', branch24.view_october_account_details_ob_ch24, name='view_october_account_details_ob_ch24'),
    path('october_account_mgt_ob_ch24/<id>',branch24.october_account_mgt_ob_ch24,name='october_account_mgt_ob_ch24'),
    path('view_nov_account_details_ob_ch24/', branch24.view_nov_account_details_ob_ch24, name='view_nov_account_details_ob_ch24'),
    path('nov_account_mgt_ob_ch24/<id>',branch24.nov_account_mgt_ob_ch24,name='nov_account_mgt_ob_ch24'),
    path('view_dec_account_details_ob_ch24/', branch24.view_dec_account_details_ob_ch24, name='view_dec_account_details_ob_ch24'),
    path('dec_account_mgt_ob_ch24/<id>',branch24.dec_account_mgt_ob_ch24,name='dec_account_mgt_ob_ch24'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch24', admin_dashboard_calculations_br24.monthly_details_due_ob_ch24, name='monthly_details_due_ob_ch24'),
    path('monthly_collection_details_ob_ch24/', admin_dashboard_calculations_br24.monthly_collection_details_ob_ch24, name='monthly_collection_details_ob_ch24'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch24/',branch24.guest_all_ob_ch24,name='guest_all_ob_ch24'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category24/', accounts24.view_all_category24, name='view_all_category24'),
    path('create_new_category24/', accounts24.create_new_category24, name='create_new_category24'),
    path('regi_new_category24/', accounts24.regi_new_category24, name='regi_new_category24'),
    path('update_category24/<id>',accounts24.update_category24,name='update_category24'),

    path('delete_category24/<id>', accounts24.delete_category24, name='delete_category24'),
    path('view_all_category_delete24/', accounts24.view_all_category_delete24, name='view_all_category_delete24'),

    path('regi_multiple_new_category24/', accounts24.regi_multiple_new_category24, name='regi_multiple_new_category24'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items24/', accounts24.view_all_items24, name='view_all_items24'),
    path('create_new_item24/', accounts24.create_new_item24, name='create_new_item24'),
    path('regi_new_item24/', accounts24.regi_new_item24, name='regi_new_item24'),
    path('delete_item24/<id>',accounts24.delete_item24,name='delete_item24'),
    path('update_item24/<id>', accounts24.update_item24, name='update_item24'),
    path('view_all_items_delete24/',accounts24.view_all_items_delete24,name='view_all_items_delete24'),

    path('regi_multiple_new_item24/', accounts24.regi_multiple_new_item24, name='regi_multiple_new_item24'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger24/', accounts24.view_all_ledger24, name='view_all_ledger24'),
    path('create_new_ledger24/', accounts24.create_new_ledger24, name='create_new_ledger24'),
    path('regi_new_ledger24/', accounts24.regi_new_ledger24, name='regi_new_ledger24'),
    path('delete_ledger24/<id>',accounts24.delete_ledger24,name='delete_ledger24'),
    path('update_ledger24/<id>',accounts24.update_ledger24,name='update_ledger24'),
    path('view_all_ledger_delete24/',accounts24.view_all_ledger_delete24,name='view_all_ledger_delete24'),

    path('regi_multiple_new_ledger24/', accounts24.regi_multiple_new_ledger24, name='regi_multiple_new_ledger24'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book24/', accounts24.view_all_accounts_book24, name='view_all_accounts_book24'),
    path('create_new_accounts_book24/', accounts24.create_new_accounts_book24, name='create_new_accounts_book24'),
    path('regi_new_accounts_book24/', accounts24.regi_new_accounts_book24, name='regi_new_accounts_book24'),
    path('update_accounts_book24/<id>',accounts24.update_accounts_book24,name='update_accounts_book24'),
    path('delete_accounts_book24/<id>',accounts24.delete_accounts_book24,name='delete_accounts_book24'),
    path('view_all_accounts_book_delete24/',accounts24.view_all_accounts_book_delete24,name='view_all_accounts_book_delete24'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries24/', accounts24.get_countries24, name='get_countries24'),

    path('in_exp_items_entry24/', accounts24.in_exp_items_entry24, name='in_exp_items_entry24'),
    path('reg_in_exp_items_entry24/', accounts24.reg_in_exp_items_entry24, name='reg_in_exp_items_entry24'),
    path('delete_journal24/<id>',accounts24.delete_journal24,name='delete_journal24'),
    path('update_in_exp_items_entry24/<id>',accounts24.update_in_exp_items_entry24,name='update_in_exp_items_entry24'),
    path('detailed_journal_report24/',accounts24.detailed_journal_report24,name='detailed_journal_report24'),
    path('journal_report_deleted24/',accounts24.journal_report_deleted24,name='journal_report_deleted24'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise24/', accounts24.daily_category_wise24, name='daily_category_wise24'),
    path('monthly_category_based_reports24/',accounts24.monthly_category_based_reports24,name='monthly_category_based_reports24'),
    path('yearly_category_based_reports24/', accounts24.yearly_category_based_reports24,name='yearly_category_based_reports24'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed24/', accounts24.daily_detailed24, name='daily_detailed24'),
    path('monthly_detailed24/',accounts24.monthly_detailed24,name='monthly_detailed24'),
    path('yearly_detailed24/',accounts24.yearly_detailed24,name='yearly_detailed24'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports24/', accounts24.item_based_reports24, name='item_based_reports24'),
    path('daily_item_based_reports24/',accounts24.daily_item_based_reports24,name='daily_item_based_reports24'),
    path('monthly_item_based_reports24/',accounts24.monthly_item_based_reports24,name='monthly_item_based_reports24'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports24/', accounts24.ledger_based_reports24, name='ledger_based_reports24'),
    path('monthly_ledger_based_reports24/', accounts24.monthly_ledger_based_reports24, name='monthly_ledger_based_reports24'),
    path('daily_ledger_based_reports24/',accounts24.daily_ledger_based_reports24,name='daily_ledger_based_reports24'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports24/', accounts24.accounts_book_based_reports24, name='accounts_book_based_reports24'),
    path('daily_accounts_book_based_reports24/',accounts24.daily_accounts_book_based_reports24,name='daily_accounts_book_based_reports24'),
    path('monthly_accounts_book_based_reports24/',accounts24.monthly_accounts_book_based_reports24,name='monthly_accounts_book_based_reports24'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months24/', accounts24.monthly_reports_choose_months24, name='monthly_reports_choose_months24'),
    path('monthly_detailed_daily_in_exp_items_report24/<mo>',accounts24.monthly_detailed_daily_in_exp_items_report24,name='monthly_detailed_daily_in_exp_items_report24'),

    path('single_monthly_reports_choose_months24/', accounts24.single_monthly_reports_choose_months24,name='single_monthly_reports_choose_months24'),
    path('single_monthly_daily_in_exp_items_report24/<mo>',accounts24.single_monthly_daily_in_exp_items_report24,name='single_monthly_daily_in_exp_items_report24'),

    path('accounts_dash_board_ob_ch24/',accounts24.accounts_dash_board_ob_ch24,name='accounts_dash_board_ob_ch24'),
    path('accounts_dash_board24/',accounts24.accounts_dash_board24,name='accounts_dash_board24'),

    path('profit_sharing_choose_months24', accounts24.profit_sharing_choose_months24,name='profit_sharing_choose_months24'),
    path('profit_sharing24/<mo>', accounts24.profit_sharing24, name='profit_sharing24'),
    path('view_share_holders24', accounts24.view_share_holders24, name='view_share_holders24'),
    path('create_share_holders24', accounts24.create_share_holders24, name='create_share_holders24'),
    path('regi_share_holders24', accounts24.regi_share_holders24, name='regi_share_holders24'),
    path('update_share_holders24/<id>', accounts24.update_share_holders24, name='update_share_holders24'),
    path('delete_share_holders24/<id>', accounts24.delete_share_holders24, name='delete_share_holders24'),
    path('view_deleted_share_holders24', accounts24.view_deleted_share_holders24, name='view_deleted_share_holders24'),

    path('regi_multiple_share_holders24', accounts24.regi_multiple_share_holders24, name='regi_multiple_share_holders24'),

    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch24/', branch_settings24.guest_rent_update_ob_ch24, name='guest_rent_update_ob_ch24'),

    ############BRANCH SETTINGS END HERE ############################

]

