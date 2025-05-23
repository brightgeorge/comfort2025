from django.urls import path, include

from . import admin_branch23
from . import admin_branch23
from . import branch23
from . import reports23
from . import payment23
from . import admin_dashboard_calculations_br23
from . import accounts23
from . import branch_settings23

urlpatterns = [

    path('branch1_dashboard_ob_ch23/', branch23.branch1_dashboard_ob_ch23, name='branch1_dashboard_ob_ch23'),
    path('branch1_dashboard23/',branch23.branch1_dashboard23,name='branch1_dashboard23'),
    path('user_dashboard_calculations_ob_ch23/',branch23.user_dashboard_calculations_ob_ch23,name='user_dashboard_calculations_ob_ch23'),

    path('background_ob_ch23',branch23.background_ob_ch23,name='background_ob_ch23'),
    path('background_regi_ob_ch23',branch23.background_regi_ob_ch23,name='background_regi_ob_ch23'),
    path('custom_background_regi_ob_ch23',branch23.custom_background_regi_ob_ch23,name='custom_background_regi_ob_ch23'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch23/',admin_branch23.branch1_room_create_regi_ob_ch23,name='branch1_room_create_regi_ob_ch23'),
    path('view_all_room_ob_ch23/',admin_branch23.view_all_room_ob_ch23,name='view_all_room_ob_ch23'),
    path('delete_room_ob_ch23/<id>',admin_branch23.delete_room_ob_ch23,name='delete_room_ob_ch23'),

    path('branch1_room_create_ob_ch23/',admin_branch23.branch1_room_create_ob_ch23,name='branch1_room_create_ob_ch23'),

    path('multiple_branch1_room_create_regi23/',admin_branch23.multiple_branch1_room_create_regi23,name='multiple_branch1_room_create_regi23'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch23/', admin_branch23.pg1_bed_create_regi_ob_ch23, name='pg1_bed_create_regi_ob_ch23'),
    path('pg1_view_all_beds_ob_ch23/', admin_branch23.pg1_view_all_beds_ob_ch23, name='pg1_view_all_beds_ob_ch23'),
    path('delete_bed_ob_ch23/<id>', admin_branch23.delete_bed_ob_ch23, name='delete_bed_ob_ch23'),

    path('pg1_bed_create_ob_ch23/', admin_branch23.pg1_bed_create_ob_ch23, name='pg1_bed_create_ob_ch23'),

    path('single_pg1_bed_create_regi_ob_ch23/',admin_branch23.single_pg1_bed_create_regi_ob_ch23,name='single_pg1_bed_create_regi_ob_ch23'),
    path('update_bed_basic_details_ob_ch23/<id>',admin_branch23.update_bed_basic_details_ob_ch23, name='update_bed_basic_details_ob_ch23'),

    path('multiple_single_pg1_bed_create_regi23/',admin_branch23.multiple_single_pg1_bed_create_regi23,name='multiple_single_pg1_bed_create_regi23'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch23/<id>',branch23.br1_admit_guest_ob_ch23,name='br1_admit_guest_ob_ch23'),
    path('view_all_new_guest_ob_ch23/',branch23.view_all_new_guest_ob_ch23,name='view_all_new_guest_ob_ch23'),
    path('update_br1_admit_guest_ob_ch23/<id>',branch23.update_br1_admit_guest_ob_ch23,name='update_br1_admit_guest_ob_ch23'),
    path('vacate_br1_guest_ob_ch23/<id>',branch23.vacate_br1_guest_ob_ch23,name='vacate_br1_guest_ob_ch23'),

    path('active_guest_details_ob_ch23/<guest_code>',branch23.active_guest_details_ob_ch23,name='active_guest_details_ob_ch23'),
    path('view_all_guest_ob_ch23/',branch23.view_all_guest_ob_ch23,name='view_all_guest_ob_ch23'),
    path('shift_guest_ob_ch23/<id>',branch23.shift_guest_ob_ch23,name='shift_guest_ob_ch23'),
    path('shift_guest_regi_ob_ch23/',branch23.shift_guest_regi_ob_ch23,name='shift_guest_regi_ob_ch23'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch23/',branch23.update_all_rent_ob_ch23,name='update_all_rent_ob_ch23'),

    path('multiple_br1_admit_guest23/<id>',branch23.multiple_br1_admit_guest23,name='multiple_br1_admit_guest23'),

#guest end here


##################################
#_ADVANCE_ob_ch23 START HERE
################################


    path('choose_months_advance_ob_ch23/',branch23.choose_months_advance_ob_ch23,name='choose_months_advance_ob_ch23'),

    path('jan_advance_ob_ch23/', branch23.jan_advance_ob_ch23, name='jan_advance_ob_ch23'),
    path('jan_make_payments_advance_ob_ch23/<id>', branch23.jan_make_payments_advance_ob_ch23,name='jan_make_payments_advance_ob_ch23'),
    path('feb_advance_ob_ch23/', branch23.feb_advance_ob_ch23, name='feb_advance_ob_ch23'),
    path('feb_make_payments_advance_ob_ch23/<id>', branch23.feb_make_payments_advance_ob_ch23,name='feb_make_payments_advance_ob_ch23'),
    path('march_advance_ob_ch23/', branch23.march_advance_ob_ch23, name='march_advance_ob_ch23'),
    path('march_make_payments_advance_ob_ch23/<id>', branch23.march_make_payments_advance_ob_ch23,name='march_make_payments_advance_ob_ch23'),
    path('april_advance_ob_ch23/', branch23.april_advance_ob_ch23, name='april_advance_ob_ch23'),
    path('april_make_payments_advance_ob_ch23/<id>', branch23.april_make_payments_advance_ob_ch23, name='april_make_payments_advance_ob_ch23'),

    path('may_advance_ob_ch23/',branch23.may_advance_ob_ch23,name='may_advance_ob_ch23'),
    path('may_make_payments_advance_ob_ch23/<id>', branch23.may_make_payments_advance_ob_ch23, name='may_make_payments_advance_ob_ch23'),
    path('june_advance_ob_ch23/',branch23.june_advance_ob_ch23,name='june_advance_ob_ch23'),
    path('june_make_payments_advance_ob_ch23/<id>', branch23.june_make_payments_advance_ob_ch23, name='june_make_payments_advance_ob_ch23'),
    path('july_advance_ob_ch23/',branch23.july_advance_ob_ch23,name='july_advance_ob_ch23'),
    path('july_make_payments_advance_ob_ch23/<id>', branch23.july_make_payments_advance_ob_ch23, name='july_make_payments_advance_ob_ch23'),
    path('auguest_advance_ob_ch23/', branch23.auguest_advance_ob_ch23, name='auguest_advance_ob_ch23'),
    path('auguest_make_payments_advance_ob_ch23/<id>', branch23.auguest_make_payments_advance_ob_ch23, name='auguest_make_payments_advance_ob_ch23'),

    path('sept_advance_ob_ch23/', branch23.sept_advance_ob_ch23, name='sept_advance_ob_ch23'),
    path('sept_make_payments_advance_ob_ch23/<id>', branch23.sept_make_payments_advance_ob_ch23,name='sept_make_payments_advance_ob_ch23'),
    path('october_advance_ob_ch23/', branch23.october_advance_ob_ch23, name='october_advance_ob_ch23'),
    path('october_make_payments_advance_ob_ch23/<id>', branch23.october_make_payments_advance_ob_ch23, name='october_make_payments_advance_ob_ch23'),
    path('nov_advance_ob_ch23/', branch23.nov_advance_ob_ch23, name='nov_advance_ob_ch23'),
    path('nov_make_payments_advance_ob_ch23/<id>', branch23.nov_make_payments_advance_ob_ch23,name='nov_make_payments_advance_ob_ch23'),
    path('dec_advance_ob_ch23/', branch23.dec_advance_ob_ch23, name='dec_advance_ob_ch23'),
    path('dec_make_payments_advance_ob_ch23/<id>', branch23.dec_make_payments_advance_ob_ch23, name='dec_make_payments_advance_ob_ch23'),



##################################
#_ADVANCE_ob_ch23 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch23/',branch23.choose_months_ob_ch23,name='choose_months_ob_ch23'),

    path('jan_ob_ch23/',branch23.jan_ob_ch23,name='jan_ob_ch23'),
    path('jan_manke_payments_ob_ch23/<id>',branch23.jan_manke_payments_ob_ch23,name='jan_manke_payments_ob_ch23'),

    path('feb_ob_ch23/',branch23.feb_ob_ch23,name='feb_ob_ch23'),
    path('feb_manke_payments_ob_ch23/<id>',branch23.feb_manke_payments_ob_ch23,name='feb_manke_payments_ob_ch23'),

    path('march_ob_ch23/',branch23.march_ob_ch23,name='march_ob_ch23'),
    path('march_manke_payments_ob_ch23/<id>',branch23.march_manke_payments_ob_ch23,name='march_manke_payments_ob_ch23'),

    path('april_ob_ch23/',branch23.april_ob_ch23,name='april_ob_ch23'),
    path('april_make_payments_ob_ch23/<id>',branch23.april_make_payments_ob_ch23,name='april_make_payments_ob_ch23'),

    path('may_ob_ch23/',branch23.may_ob_ch23,name='may_ob_ch23'),
    path('may_make_payments_ob_ch23/<id>',branch23.may_make_payments_ob_ch23,name='may_make_payments_ob_ch23'),

    path('june_ob_ch23/',branch23.june_ob_ch23,name='june_ob_ch23'),
    path('june_make_payments_ob_ch23/<id>',branch23.june_make_payments_ob_ch23,name='june_make_payments_ob_ch23'),

    path('july_ob_ch23/',branch23.july_ob_ch23,name='july_ob_ch23'),
    path('july_make_payments_ob_ch23/<id>',branch23.july_make_payments_ob_ch23,name='july_make_payments_ob_ch23'),

    path('aug_ob_ch23/',branch23.aug_ob_ch23,name='aug_ob_ch23'),
    path('aug_make_payments_ob_ch23/<id>',branch23.aug_make_payments_ob_ch23,name='aug_make_payments_ob_ch23'),

    path('sept_ob_ch23/',branch23.sept_ob_ch23,name='sept_ob_ch23'),
    path('sept_make_payments_ob_ch23/<id>',branch23.sept_make_payments_ob_ch23,name='sept_make_payments_ob_ch23'),

    path('oct_ob_ch23/',branch23.oct_ob_ch23,name='oct_ob_ch23'),
    path('oct_make_payments_ob_ch23/<id>',branch23.oct_make_payments_ob_ch23,name='oct_make_payments_ob_ch23'),

    path('nov_ob_ch23/',branch23.nov_ob_ch23,name='nov_ob_ch23'),
    path('nov_make_payments_ob_ch23/<id>',branch23.nov_make_payments_ob_ch23,name='nov_make_payments_ob_ch23'),

    path('dec_ob_ch23/',branch23.dec_ob_ch23,name='dec_ob_ch23'),
    path('dec_make_payments_ob_ch23/<id>',branch23.dec_make_payments_ob_ch23,name='dec_make_payments_ob_ch23'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch23/', payment23.choose_user_ob_ch23, name='choose_user_ob_ch23'),
    path('payment_user_details_ob_ch23/<id>', payment23.payment_user_details_ob_ch23, name='payment_user_details_ob_ch23'),
    path('close_choose_user_ob_ch23/<id>',payment23.close_choose_user_ob_ch23,name='close_choose_user_ob_ch23'),

    path('monthly_jan_make_payments_ob_ch23/<id>', payment23.monthly_jan_make_payments_ob_ch23, name='monthly_jan_make_payments_ob_ch23'),
    path('monthly_feb_make_payments_ob_ch23/<id>', payment23.monthly_feb_make_payments_ob_ch23, name='monthly_feb_make_payments_ob_ch23'),
    path('monthly_march_make_payments_ob_ch23/<id>', payment23.monthly_march_make_payments_ob_ch23, name='monthly_march_make_payments_ob_ch23'),
    path('monthly_april_make_payments_ob_ch23/<id>', payment23.monthly_april_make_payments_ob_ch23, name='monthly_april_make_payments_ob_ch23'),
    path('monthly_may_make_payments_ob_ch23/<id>', payment23.monthly_may_make_payments_ob_ch23, name='monthly_may_make_payments_ob_ch23'),
    path('monthly_june_make_payments_ob_ch23/<id>', payment23.monthly_june_make_payments_ob_ch23, name='monthly_june_make_payments_ob_ch23'),

    path('monthly_july_make_payments_ob_ch23/<id>', payment23.monthly_july_make_payments_ob_ch23, name='monthly_july_make_payments_ob_ch23'),
    path('monthly_aug_make_payments_ob_ch23/<id>', payment23.monthly_aug_make_payments_ob_ch23, name='monthly_aug_make_payments_ob_ch23'),
    path('monthly_sept_make_payments_ob_ch23/<id>', payment23.monthly_sept_make_payments_ob_ch23, name='monthly_sept_make_payments_ob_ch23'),
    path('monthly_oct_make_payments_ob_ch23/<id>', payment23.monthly_oct_make_payments_ob_ch23, name='monthly_oct_make_payments_ob_ch23'),
    path('monthly_nov_make_payments_ob_ch23/<id>', payment23.monthly_nov_make_payments_ob_ch23, name='monthly_nov_make_payments_ob_ch23'),
    path('monthly_dec_make_payments_ob_ch23/<id>', payment23.monthly_dec_make_payments_ob_ch23, name='monthly_dec_make_payments_ob_ch23'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch23/',branch23.unpaid_rent_choose_months_ob_ch23,name='unpaid_rent_choose_months_ob_ch23'),

    path('jan_unpaid_rent_ob_ch23/', branch23.jan_unpaid_rent_ob_ch23, name='jan_unpaid_rent_ob_ch23'),
    path('table_jan_unpaid_rent_ob_ch23/', branch23.table_jan_unpaid_rent_ob_ch23, name='table_jan_unpaid_rent_ob_ch23'),
    path('feb_unpaid_rent_ob_ch23/', branch23.feb_unpaid_rent_ob_ch23, name='feb_unpaid_rent_ob_ch23'),
    path('table_feb_unpaid_rent_ob_ch23/', branch23.table_feb_unpaid_rent_ob_ch23, name='table_feb_unpaid_rent_ob_ch23'),
    path('mar_unpaid_rent_ob_ch23/', branch23.mar_unpaid_rent_ob_ch23, name='mar_unpaid_rent_ob_ch23'),
    path('table_mar_unpaid_rent_ob_ch23/', branch23.table_mar_unpaid_rent_ob_ch23, name='table_mar_unpaid_rent_ob_ch23'),
    path('april_unpaid_rent_ob_ch23/', branch23.april_unpaid_rent_ob_ch23, name='april_unpaid_rent_ob_ch23'),
    path('table_april_unpaid_rent_ob_ch23/', branch23.table_april_unpaid_rent_ob_ch23, name='table_april_unpaid_rent_ob_ch23'),

    path('may_unpaid_rent_ob_ch23/', branch23.may_unpaid_rent_ob_ch23, name='may_unpaid_rent_ob_ch23'),
    path('table_may_unpaid_rent_ob_ch23/', branch23.table_may_unpaid_rent_ob_ch23, name='table_may_unpaid_rent_ob_ch23'),
    path('june_unpaid_rent_ob_ch23/', branch23.june_unpaid_rent_ob_ch23, name='june_unpaid_rent_ob_ch23'),
    path('table_june_unpaid_rent_ob_ch23/', branch23.table_june_unpaid_rent_ob_ch23, name='table_june_unpaid_rent_ob_ch23'),
    path('july_unpaid_rent_ob_ch23/', branch23.july_unpaid_rent_ob_ch23, name='july_unpaid_rent_ob_ch23'),
    path('table_july_unpaid_rent_ob_ch23',branch23.table_july_unpaid_rent_ob_ch23,name='table_july_unpaid_rent_ob_ch23'),
    path('aug_unpaid_rent_ob_ch23/', branch23.aug_unpaid_rent_ob_ch23, name='aug_unpaid_rent_ob_ch23'),
    path('table_aug_unpaid_rent_ob_ch23/',branch23.table_aug_unpaid_rent_ob_ch23,name='table_aug_unpaid_rent_ob_ch23'),

    path('sept_unpaid_rent_ob_ch23/', branch23.sept_unpaid_rent_ob_ch23, name='sept_unpaid_rent_ob_ch23'),
    path('table_sept_unpaid_rent_ob_ch23/', branch23.table_sept_unpaid_rent_ob_ch23, name='table_sept_unpaid_rent_ob_ch23'),
    path('oct_unpaid_rent_ob_ch23/', branch23.oct_unpaid_rent_ob_ch23, name='oct_unpaid_rent_ob_ch23'),
    path('table_oct_unpaid_rent_ob_ch23/', branch23.table_oct_unpaid_rent_ob_ch23, name='table_oct_unpaid_rent_ob_ch23'),
    path('nov_unpaid_rent_ob_ch23/', branch23.nov_unpaid_rent_ob_ch23, name='nov_unpaid_rent_ob_ch23'),
    path('table_nov_unpaid_rent_ob_ch23/', branch23.table_nov_unpaid_rent_ob_ch23, name='table_nov_unpaid_rent_ob_ch23'),
    path('dec_unpaid_rent_ob_ch23/', branch23.dec_unpaid_rent_ob_ch23, name='dec_unpaid_rent_ob_ch23'),
    path('table_dec_unpaid_rent_ob_ch23/', branch23.table_dec_unpaid_rent_ob_ch23, name='table_dec_unpaid_rent_ob_ch23'),

    path('details_of_unpaid_guests_ob_ch23/<id>',branch23.details_of_unpaid_guests_ob_ch23,name='details_of_unpaid_guests_ob_ch23'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch23/',branch23.paid_rent_choose_months_ob_ch23,name='paid_rent_choose_months_ob_ch23'),
    path('partially_paid_guest_choose_months_ob_ch23/',reports23.partially_paid_guest_choose_months_ob_ch23,name='partially_paid_guest_choose_months_ob_ch23'),

    path('jan_paid_rent_ob_ch23/', branch23.jan_paid_rent_ob_ch23, name='jan_paid_rent_ob_ch23'),
    path('table_jan_paid_rent_ob_ch23/', branch23.table_jan_paid_rent_ob_ch23, name='table_jan_paid_rent_ob_ch23'),
    path('jan_full_paid_guest_ob_ch23/', reports23.jan_full_paid_guest_ob_ch23, name='jan_full_paid_guest_ob_ch23'),
    path('jan_partially_paid_guest_ob_ch23/', reports23.jan_partially_paid_guest_ob_ch23, name='jan_partially_paid_guest_ob_ch23'),
    path('table_jan_partially_paid_guest_ob_ch23/', reports23.table_jan_partially_paid_guest_ob_ch23,name='table_jan_partially_paid_guest_ob_ch23'),

    path('feb_paid_rent_ob_ch23/', branch23.feb_paid_rent_ob_ch23, name='feb_paid_rent_ob_ch23'),
    path('table_feb_paid_rent_ob_ch23/', branch23.table_feb_paid_rent_ob_ch23, name='table_feb_paid_rent_ob_ch23'),
    path('feb_full_paid_guest_ob_ch23/', reports23.feb_full_paid_guest_ob_ch23, name='feb_full_paid_guest_ob_ch23'),
    path('feb_partially_paid_guest_ob_ch23/', reports23.feb_partially_paid_guest_ob_ch23, name='feb_partially_paid_guest_ob_ch23'),
    path('table_feb_partially_paid_guest_ob_ch23/', reports23.table_feb_partially_paid_guest_ob_ch23,name='table_feb_partially_paid_guest_ob_ch23'),

    path('mar_paid_rent_ob_ch23/', branch23.mar_paid_rent_ob_ch23, name='mar_paid_rent_ob_ch23'),
    path('table_mar_paid_rent_ob_ch23/', branch23.table_mar_paid_rent_ob_ch23, name='table_mar_paid_rent_ob_ch23'),
    path('march_full_paid_guest_ob_ch23/', reports23.march_full_paid_guest_ob_ch23, name='march_full_paid_guest_ob_ch23'),
    path('march_partially_paid_guest_ob_ch23/', reports23.march_partially_paid_guest_ob_ch23, name='march_partially_paid_guest_ob_ch23'),
    path('table_march_partially_paid_guest_ob_ch23/', reports23.table_march_partially_paid_guest_ob_ch23,name='table_march_partially_paid_guest_ob_ch23'),

    path('april_paid_rent_ob_ch23/', branch23.april_paid_rent_ob_ch23, name='april_paid_rent_ob_ch23'),
    path('table_april_paid_rent_ob_ch23/', branch23.table_april_paid_rent_ob_ch23, name='table_april_paid_rent_ob_ch23'),
    path('april_full_paid_guest_ob_ch23/', reports23.april_full_paid_guest_ob_ch23, name='april_full_paid_guest_ob_ch23'),
    path('april_partially_paid_guest_ob_ch23/', reports23.april_partially_paid_guest_ob_ch23, name='april_partially_paid_guest_ob_ch23'),
    path('table_april_partially_paid_guest_ob_ch23/', reports23.table_april_partially_paid_guest_ob_ch23,name='table_april_partially_paid_guest_ob_ch23'),

    path('may_paid_rent_ob_ch23/', branch23.may_paid_rent_ob_ch23, name='may_paid_rent_ob_ch23'),
    path('table_may_paid_rent_ob_ch23/', branch23.table_may_paid_rent_ob_ch23, name='table_may_paid_rent_ob_ch23'),
    path('may_full_paid_guest_ob_ch23/', reports23.may_full_paid_guest_ob_ch23, name='may_full_paid_guest_ob_ch23'),
    path('may_partially_paid_guest_ob_ch23/', reports23.may_partially_paid_guest_ob_ch23, name='may_partially_paid_guest_ob_ch23'),
    path('table_may_partially_paid_guest_ob_ch23/', reports23.table_may_partially_paid_guest_ob_ch23, name='table_may_partially_paid_guest_ob_ch23'),

    path('june_paid_rent_ob_ch23/', branch23.june_paid_rent_ob_ch23, name='june_paid_rent_ob_ch23'),
    path('table_june_paid_rent_ob_ch23/', branch23.table_june_paid_rent_ob_ch23, name='table_june_paid_rent_ob_ch23'),
    path('june_full_paid_guest_ob_ch23/', reports23.june_full_paid_guest_ob_ch23, name='june_full_paid_guest_ob_ch23'),
    path('june_partially_paid_guest_ob_ch23/', reports23.june_partially_paid_guest_ob_ch23, name='june_partially_paid_guest_ob_ch23'),
    path('table_june_partially_paid_guest_ob_ch23/', reports23.table_june_partially_paid_guest_ob_ch23, name='table_june_partially_paid_guest_ob_ch23'),

    path('july_paid_rent_ob_ch23/', branch23.july_paid_rent_ob_ch23, name='july_paid_rent_ob_ch23'),
    path('table_july_paid_rent_ob_ch23/', branch23.table_july_paid_rent_ob_ch23, name='table_july_paid_rent_ob_ch23'),
    path('july_full_paid_guest_ob_ch23/', reports23.july_full_paid_guest_ob_ch23, name='july_full_paid_guest_ob_ch23'),
    path('july_partially_paid_guest_ob_ch23/', reports23.july_partially_paid_guest_ob_ch23, name='july_partially_paid_guest_ob_ch23'),
    path('table_july_partially_paid_guest_ob_ch23/', reports23.table_july_partially_paid_guest_ob_ch23, name='table_july_partially_paid_guest_ob_ch23'),

    path('aug_paid_rent_ob_ch23/', branch23.aug_paid_rent_ob_ch23, name='aug_paid_rent_ob_ch23'),
    path('table_aug_paid_rent_ob_ch23/', branch23.table_aug_paid_rent_ob_ch23, name='table_aug_paid_rent_ob_ch23'),
    path('auguest_full_paid_guest_ob_ch23/', reports23.auguest_full_paid_guest_ob_ch23, name='auguest_full_paid_guest_ob_ch23'),
    path('auguest_partially_paid_guest_ob_ch23/', reports23.auguest_partially_paid_guest_ob_ch23,name='auguest_partially_paid_guest_ob_ch23'),
    path('table_auguest_partially_paid_guest_ob_ch23/', reports23.table_auguest_partially_paid_guest_ob_ch23,name='table_auguest_partially_paid_guest_ob_ch23'),

    path('sept_paid_rent_ob_ch23/', branch23.sept_paid_rent_ob_ch23, name='sept_paid_rent_ob_ch23'),
    path('table_sept_paid_rent_ob_ch23/', branch23.table_sept_paid_rent_ob_ch23, name='table_sept_paid_rent_ob_ch23'),
    path('sept_full_paid_guest_ob_ch23/', reports23.sept_full_paid_guest_ob_ch23, name='sept_full_paid_guest_ob_ch23'),
    path('sept_partially_paid_guest_ob_ch23/', reports23.sept_partially_paid_guest_ob_ch23, name='sept_partially_paid_guest_ob_ch23'),
    path('table_sept_partially_paid_guest_ob_ch23/', reports23.table_sept_partially_paid_guest_ob_ch23,name='table_sept_partially_paid_guest_ob_ch23'),

    path('oct_paid_rent_ob_ch23/', branch23.oct_paid_rent_ob_ch23, name='oct_paid_rent_ob_ch23'),
    path('table_oct_paid_rent_ob_ch23/', branch23.table_oct_paid_rent_ob_ch23, name='table_oct_paid_rent_ob_ch23'),
    path('october_full_paid_guest_ob_ch23/', reports23.october_full_paid_guest_ob_ch23, name='october_full_paid_guest_ob_ch23'),
    path('october_partially_paid_guest_ob_ch23/', reports23.october_partially_paid_guest_ob_ch23,name='october_partially_paid_guest_ob_ch23'),
    path('table_october_partially_paid_guest_ob_ch23/', reports23.table_october_partially_paid_guest_ob_ch23,name='table_october_partially_paid_guest_ob_ch23'),

    path('nov_paid_rent_ob_ch23/', branch23.nov_paid_rent_ob_ch23, name='nov_paid_rent_ob_ch23'),
    path('table_nov_paid_rent_ob_ch23/', branch23.table_nov_paid_rent_ob_ch23, name='table_nov_paid_rent_ob_ch23'),
    path('nov_full_paid_guest_ob_ch23/', reports23.nov_full_paid_guest_ob_ch23, name='nov_full_paid_guest_ob_ch23'),
    path('nov_partially_paid_guest_ob_ch23/', reports23.nov_partially_paid_guest_ob_ch23, name='nov_partially_paid_guest_ob_ch23'),
    path('table_nov_partially_paid_guest_ob_ch23/', reports23.table_nov_partially_paid_guest_ob_ch23,name='table_nov_partially_paid_guest_ob_ch23'),

    path('dec_paid_rent_ob_ch23/', branch23.dec_paid_rent_ob_ch23, name='dec_paid_rent_ob_ch23'),
    path('table_dec_paid_rent_ob_ch23/', branch23.table_dec_paid_rent_ob_ch23, name='table_dec_paid_rent_ob_ch23'),
    path('dec_full_paid_guest_ob_ch23/', reports23.dec_full_paid_guest_ob_ch23, name='dec_full_paid_guest_ob_ch23'),
    path('dec_partially_paid_guest_ob_ch23/', reports23.dec_partially_paid_guest_ob_ch23, name='dec_partially_paid_guest_ob_ch23'),
    path('table_dec_partially_paid_guest_ob_ch23/', reports23.table_dec_partially_paid_guest_ob_ch23,name='table_dec_partially_paid_guest_ob_ch23'),

    path('details_of_paid_guests_ob_ch23/<id>',branch23.details_of_paid_guests_ob_ch23,name='details_of_paid_guests_ob_ch23'),
    path('full_paid_guest_ob_ch23/',reports23.full_paid_guest_ob_ch23,name='full_paid_guest_ob_ch23'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch23/',branch23.viewall_vacate_guest_ob_ch23,name='viewall_vacate_guest_ob_ch23'),
    path('details_of_vacate_guest_ob_ch23/<id>',branch23.details_of_vacate_guest_ob_ch23,name='details_of_vacate_guest_ob_ch23'),
    path('full_vacated_guest_details_ob_ch23',branch23.full_vacated_guest_details_ob_ch23,name='full_vacated_guest_details_ob_ch23'),
    path('full_vacated_guest_table_ob_ch23',branch23.full_vacated_guest_table_ob_ch23,name='full_vacated_guest_table_ob_ch23'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch23/<id>', branch23.jan_manke_payments_vacate_ob_ch23, name='jan_manke_payments_vacate_ob_ch23'),
    path('feb_manke_payments_vacate_ob_ch23/<id>', branch23.feb_manke_payments_vacate_ob_ch23, name='feb_manke_payments_vacate_ob_ch23'),
    path('march_manke_payments_vacate_ob_ch23/<id>', branch23.march_manke_payments_vacate_ob_ch23, name='march_manke_payments_vacate_ob_ch23'),
    path('april_make_payments_vacate_ob_ch23/<id>', branch23.april_make_payments_vacate_ob_ch23, name='april_make_payments_vacate_ob_ch23'),

    path('may_make_payments_vacate_ob_ch23/<id>', branch23.may_make_payments_vacate_ob_ch23, name='may_make_payments_vacate_ob_ch23'),
    path('june_make_payments_vacate_ob_ch23/<id>', branch23.june_make_payments_vacate_ob_ch23, name='june_make_payments_vacate_ob_ch23'),
    path('july_make_payments_vacate_ob_ch23/<id>', branch23.july_make_payments_vacate_ob_ch23, name='july_make_payments_vacate_ob_ch23'),
    path('aug_make_payments_vacate_ob_ch23/<id>', branch23.aug_make_payments_vacate_ob_ch23, name='aug_make_payments_vacate_ob_ch23'),

    path('sept_make_payments_vacate_ob_ch23/<id>', branch23.sept_make_payments_vacate_ob_ch23, name='sept_make_payments_vacate_ob_ch23'),
    path('oct_make_payments_vacate_ob_ch23/<id>', branch23.oct_make_payments_vacate_ob_ch23, name='oct_make_payments_vacate_ob_ch23'),
    path('nov_make_payments_vacate_ob_ch23/<id>', branch23.nov_make_payments_vacate_ob_ch23, name='nov_make_payments_vacate_ob_ch23'),
    path('dec_make_payments_vacate_ob_ch23/<id>', branch23.dec_make_payments_vacate_ob_ch23, name='dec_make_payments_vacate_ob_ch23'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch23/',branch23.detail_guest_general_ob_ch23,name='detail_guest_general_ob_ch23'),

    path('jan_print_ob_ch23/',branch23.jan_print_ob_ch23,name='jan_print_ob_ch23'),
    path('feb_print_ob_ch23/',branch23.feb_print_ob_ch23,name='feb_print_ob_ch23'),
    path('march_print_ob_ch23/',branch23.march_print_ob_ch23,name='march_print_ob_ch23'),
    path('april_print_ob_ch23/',branch23.april_print_ob_ch23,name='april_print_ob_ch23'),

    path('may_print_ob_ch23/',branch23.may_print_ob_ch23,name='may_print_ob_ch23'),
    path('june_print_ob_ch23/',branch23.june_print_ob_ch23,name='june_print_ob_ch23'),
    path('july_print_ob_ch23/', branch23.july_print_ob_ch23, name='july_print_ob_ch23'),
    path('aug_print_ob_ch23/', branch23.aug_print_ob_ch23, name='aug_print_ob_ch23'),

    path('sept_print_ob_ch23/', branch23.sept_print_ob_ch23, name='sept_print_ob_ch23'),
    path('oct_print_ob_ch23/', branch23.oct_print_ob_ch23, name='oct_print_ob_ch23'),
    path('nov_print_ob_ch23/', branch23.nov_print_ob_ch23, name='nov_print_ob_ch23'),
    path('dec_print_ob_ch23/', branch23.dec_print_ob_ch23, name='dec_print_ob_ch23'),

    path('new_year_jan_print_ob_ch23/', branch23.new_year_jan_print_ob_ch23, name='new_year_jan_print_ob_ch23'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch23/', branch23.jan_close_ob_ch23, name='jan_close_ob_ch23'),
    path('jan_close_decision_page_ob_ch23/', branch23.jan_close_decision_page_ob_ch23, name='jan_close_decision_page_ob_ch23'),
    path('feb_close/', branch23.feb_close_ob_ch23, name='feb_close_ob_ch23'),
    path('feb_close_decision_page_ob_ch23/', branch23.feb_close_decision_page_ob_ch23, name='feb_close_decision_page_ob_ch23'),
    path('mar_close_ob_ch23/', branch23.mar_close_ob_ch23, name='mar_close_ob_ch23'),
    path('mar_close_decision_page/', branch23.mar_close_decision_page_ob_ch23, name='mar_close_decision_page_ob_ch23'),
    path('apr_close_ob_ch23/', branch23.apr_close_ob_ch23, name='apr_close_ob_ch23'),
    path('apr_close_decision_page_ob_ch23/', branch23.apr_close_decision_page_ob_ch23, name='apr_close_decision_page_ob_ch23'),

    path('may_close_ob_ch23/', branch23.may_close_ob_ch23, name='may_close_ob_ch23'),
    path('may_close_decision_page_ob_ch23/', branch23.may_close_decision_page_ob_ch23, name='may_close_decision_page_ob_ch23'),
    path('jun_close_ob_ch23/', branch23.jun_close_ob_ch23, name='jun_close_ob_ch23'),
    path('jun_close_decision_page_ob_ch23/', branch23.jun_close_decision_page_ob_ch23, name='jun_close_decision_page_ob_ch23'),
    path('jul_close_ob_ch23/', branch23.jul_close_ob_ch23, name='jul_close_ob_ch23'),
    path('jul_close_decision_page_ob_ch23/', branch23.jul_close_decision_page_ob_ch23, name='jul_close_decision_page_ob_ch23'),
    path('aug_close_ob_ch23/', branch23.aug_close_ob_ch23, name='aug_close_ob_ch23'),
    path('aug_close_decision_page_ob_ch23/', branch23.aug_close_decision_page_ob_ch23, name='aug_close_decision_page_ob_ch23'),

    path('sep_close_ob_ch23/', branch23.sep_close_ob_ch23, name='sep_close_ob_ch23'),
    path('sep_close_decision_page_ob_ch23/', branch23.sep_close_decision_page_ob_ch23, name='sep_close_decision_page_ob_ch23'),
    path('oct_close_ob_ch23/', branch23.oct_close_ob_ch23, name='oct_close_ob_ch23'),
    path('oct_close_decision_page_ob_ch23/', branch23.oct_close_decision_page_ob_ch23, name='oct_close_decision_page_ob_ch23'),
    path('nov_close_ob_ch23/', branch23.nov_close_ob_ch23, name='nov_close_ob_ch23'),
    path('nov_close_decision_page_ob_ch23/', branch23.nov_close_decision_page_ob_ch23, name='nov_close_decision_page_ob_ch23'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch23/',reports23.detailed_report_choose_months_ob_ch23,name='detailed_report_choose_months_ob_ch23'),

    path('jan_details_live_ob_ch23/', reports23.jan_details_live_ob_ch23, name='jan_details_live_ob_ch23'),
    path('jan_print_live_ob_ch23/', reports23.jan_print_live_ob_ch23, name='jan_print_live_ob_ch23'),
    path('feb_details_live_ob_ch23/', reports23.feb_details_live_ob_ch23, name='feb_details_live_ob_ch23'),
    path('feb_print_live_ob_ch23/', reports23.feb_print_live_ob_ch23, name='feb_print_live_ob_ch23'),
    path('march_details_live_ob_ch23/', reports23.march_details_live_ob_ch23, name='march_details_live_ob_ch23'),
    path('march_print_live_ob_ch23/', reports23.march_print_live_ob_ch23, name='march_print_live_ob_ch23'),

    path('april_details_live_ob_ch23/', reports23.april_details_live_ob_ch23, name='april_details_live_ob_ch23'),
    path('april_print_live_ob_ch23/', reports23.april_print_live_ob_ch23, name='april_print_live_ob_ch23'),
    path('may_details_live_ob_ch23/', reports23.may_details_live_ob_ch23, name='may_details_live_ob_ch23'),
    path('may_print_live_ob_ch23/', reports23.may_print_live_ob_ch23, name='may_print_live_ob_ch23'),
    path('june_details_live_ob_ch23/',reports23.june_details_live_ob_ch23,name='june_details_live_ob_ch23'),
    path('june_print_live_ob_ch23/', reports23.june_print_live_ob_ch23, name='june_print_live_ob_ch23'),

    path('july_details_live_ob_ch23/', reports23.july_details_live_ob_ch23, name='july_details_live_ob_ch23'),
    path('july_print_live_ob_ch23/', reports23.july_print_live_ob_ch23, name='july_print_live_ob_ch23'),
    path('auguest_details_live_ob_ch23/', reports23.auguest_details_live_ob_ch23, name='auguest_details_live_ob_ch23'),
    path('auguest_print_live_ob_ch23/', reports23.auguest_print_live_ob_ch23, name='auguest_print_live_ob_ch23'),
    path('sept_details_live_ob_ch23/', reports23.sept_details_live_ob_ch23, name='sept_details_live_ob_ch23'),
    path('sept_print_live_ob_ch23/', reports23.sept_print_live_ob_ch23, name='sept_print_live_ob_ch23'),

    path('october_details_live_ob_ch23/', reports23.october_details_live_ob_ch23, name='october_details_live_ob_ch23'),
    path('october_print_live_ob_ch23/', reports23.october_print_live_ob_ch23, name='october_print_live_ob_ch23'),
    path('nov_details_live_ob_ch23/', reports23.nov_details_live_ob_ch23, name='nov_details_live_ob_ch23'),
    path('nov_print_live_ob_ch23/', reports23.nov_print_live_ob_ch23, name='nov_print_live_ob_ch23'),
    path('dec_details_live_ob_ch23/', reports23.dec_details_live_ob_ch23, name='dec_details_live_ob_ch23'),
    path('dec_print_live_ob_ch23/', reports23.dec_print_live_ob_ch23, name='dec_print_live_ob_ch23'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch23/', reports23.viewall_vaccant_room_ob_ch23, name='viewall_vaccant_room_ob_ch23'),

    path('d_ob_ch23/', branch23.dynamic, name='dynamic'),

    path('manage_bed_ob_ch23/', branch23.manage_bed_ob_ch23, name='manage_bed_ob_ch23'),
    path('manage_new_guest_ob_ch23/', branch23.manage_new_guest_ob_ch23, name='manage_new_guest_ob_ch23'),
    path('manage_update_new_guest_ob_ch23/<id>', branch23.manage_update_new_guest_ob_ch23, name='manage_update_new_guest_ob_ch23'),
    path('manage_update_beds_ob_ch23/<id>', branch23.manage_update_beds_ob_ch23, name='manage_update_beds_ob_ch23'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch23/', branch23.view_all_due_amt_ob_ch23, name='view_all_due_amt_ob_ch23'),
    path('due_amt_mgt_choose_months_ob_ch23/', branch23.due_amt_mgt_choose_months_ob_ch23, name='due_amt_mgt_choose_months_ob_ch23'),

    path('view_jan_account_details_ob_ch23/', branch23.view_jan_account_details_ob_ch23, name='view_jan_account_details_ob_ch23'),
    path('jan_account_mgt_ob_ch23/<id>',branch23.jan_account_mgt_ob_ch23,name='jan_account_mgt_ob_ch23'),
    path('view_feb_account_details_ob_ch23/', branch23.view_feb_account_details_ob_ch23, name='view_feb_account_details_ob_ch23'),
    path('feb_account_mgt_ob_ch23/<id>',branch23.feb_account_mgt_ob_ch23,name='feb_account_mgt_ob_ch23'),
    path('view_march_account_details_ob_ch23/', branch23.view_march_account_details_ob_ch23, name='view_march_account_details_ob_ch23'),
    path('march_account_mgt_ob_ch23/<id>',branch23.march_account_mgt_ob_ch23,name='march_account_mgt_ob_ch23'),
    path('view_april_account_details_ob_ch23/', branch23.view_april_account_details_ob_ch23, name='view_april_account_details_ob_ch23'),
    path('april_account_mgt_ob_ch23/<id>',branch23.april_account_mgt_ob_ch23,name='april_account_mgt_ob_ch23'),

    path('view_may_account_details_ob_ch23/',branch23.view_may_account_details_ob_ch23,name='view_may_account_details_ob_ch23'),
    path('may_account_mgt_ob_ch23/<id>', branch23.may_account_mgt_ob_ch23, name='may_account_mgt_ob_ch23'),
    path('view_june_account_details_ob_ch23/', branch23.view_june_account_details_ob_ch23, name='view_june_account_details_ob_ch23'),
    path('june_account_mgt_ob_ch23/<id>',branch23.june_account_mgt_ob_ch23,name='june_account_mgt_ob_ch23'),
    path('view_july_account_details_ob_ch23/', branch23.view_july_account_details_ob_ch23, name='view_july_account_details_ob_ch23'),
    path('july_account_mgt_ob_ch23/<id>',branch23.july_account_mgt_ob_ch23,name='july_account_mgt_ob_ch23'),
    path('view_auguest_account_details_ob_ch23/', branch23.view_auguest_account_details_ob_ch23, name='view_auguest_account_details_ob_ch23'),
    path('auguest_account_mgt_ob_ch23/<id>',branch23.auguest_account_mgt_ob_ch23,name='auguest_account_mgt_ob_ch23'),

    path('view_sept_account_details_ob_ch23/', branch23.view_sept_account_details_ob_ch23, name='view_sept_account_details_ob_ch23'),
    path('sept_account_mgt_ob_ch23/<id>',branch23.sept_account_mgt_ob_ch23,name='sept_account_mgt_ob_ch23'),
    path('view_october_account_details_ob_ch23/', branch23.view_october_account_details_ob_ch23, name='view_october_account_details_ob_ch23'),
    path('october_account_mgt_ob_ch23/<id>',branch23.october_account_mgt_ob_ch23,name='october_account_mgt_ob_ch23'),
    path('view_nov_account_details_ob_ch23/', branch23.view_nov_account_details_ob_ch23, name='view_nov_account_details_ob_ch23'),
    path('nov_account_mgt_ob_ch23/<id>',branch23.nov_account_mgt_ob_ch23,name='nov_account_mgt_ob_ch23'),
    path('view_dec_account_details_ob_ch23/', branch23.view_dec_account_details_ob_ch23, name='view_dec_account_details_ob_ch23'),
    path('dec_account_mgt_ob_ch23/<id>',branch23.dec_account_mgt_ob_ch23,name='dec_account_mgt_ob_ch23'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch23', admin_dashboard_calculations_br23.monthly_details_due_ob_ch23, name='monthly_details_due_ob_ch23'),
    path('monthly_collection_details_ob_ch23/', admin_dashboard_calculations_br23.monthly_collection_details_ob_ch23, name='monthly_collection_details_ob_ch23'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch23/',branch23.guest_all_ob_ch23,name='guest_all_ob_ch23'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category23/', accounts23.view_all_category23, name='view_all_category23'),
    path('create_new_category23/', accounts23.create_new_category23, name='create_new_category23'),
    path('regi_new_category23/', accounts23.regi_new_category23, name='regi_new_category23'),
    path('update_category23/<id>',accounts23.update_category23,name='update_category23'),

    path('delete_category23/<id>', accounts23.delete_category23, name='delete_category23'),
    path('view_all_category_delete23/', accounts23.view_all_category_delete23, name='view_all_category_delete23'),

    path('regi_multiple_new_category23/', accounts23.regi_multiple_new_category23, name='regi_multiple_new_category23'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items23/', accounts23.view_all_items23, name='view_all_items23'),
    path('create_new_item23/', accounts23.create_new_item23, name='create_new_item23'),
    path('regi_new_item23/', accounts23.regi_new_item23, name='regi_new_item23'),
    path('delete_item23/<id>',accounts23.delete_item23,name='delete_item23'),
    path('update_item23/<id>', accounts23.update_item23, name='update_item23'),
    path('view_all_items_delete23/',accounts23.view_all_items_delete23,name='view_all_items_delete23'),

    path('regi_multiple_new_item23/', accounts23.regi_multiple_new_item23, name='regi_multiple_new_item23'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger23/', accounts23.view_all_ledger23, name='view_all_ledger23'),
    path('create_new_ledger23/', accounts23.create_new_ledger23, name='create_new_ledger23'),
    path('regi_new_ledger23/', accounts23.regi_new_ledger23, name='regi_new_ledger23'),
    path('delete_ledger23/<id>',accounts23.delete_ledger23,name='delete_ledger23'),
    path('update_ledger23/<id>',accounts23.update_ledger23,name='update_ledger23'),
    path('view_all_ledger_delete23/',accounts23.view_all_ledger_delete23,name='view_all_ledger_delete23'),

    path('regi_multiple_new_ledger23/', accounts23.regi_multiple_new_ledger23, name='regi_multiple_new_ledger23'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book23/', accounts23.view_all_accounts_book23, name='view_all_accounts_book23'),
    path('create_new_accounts_book23/', accounts23.create_new_accounts_book23, name='create_new_accounts_book23'),
    path('regi_new_accounts_book23/', accounts23.regi_new_accounts_book23, name='regi_new_accounts_book23'),
    path('update_accounts_book23/<id>',accounts23.update_accounts_book23,name='update_accounts_book23'),
    path('delete_accounts_book23/<id>',accounts23.delete_accounts_book23,name='delete_accounts_book23'),
    path('view_all_accounts_book_delete23/',accounts23.view_all_accounts_book_delete23,name='view_all_accounts_book_delete23'),

    path('regi_multiple_new_accounts_book23/', accounts23.regi_multiple_new_accounts_book23,name='regi_multiple_new_accounts_book23'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries23/', accounts23.get_countries23, name='get_countries23'),

    path('in_exp_items_entry23/', accounts23.in_exp_items_entry23, name='in_exp_items_entry23'),
    path('reg_in_exp_items_entry23/', accounts23.reg_in_exp_items_entry23, name='reg_in_exp_items_entry23'),
    path('delete_journal23/<id>',accounts23.delete_journal23,name='delete_journal23'),
    path('update_in_exp_items_entry23/<id>',accounts23.update_in_exp_items_entry23,name='update_in_exp_items_entry23'),
    path('detailed_journal_report23/',accounts23.detailed_journal_report23,name='detailed_journal_report23'),
    path('journal_report_deleted23/',accounts23.journal_report_deleted23,name='journal_report_deleted23'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise23/', accounts23.daily_category_wise23, name='daily_category_wise23'),
    path('monthly_category_based_reports23/',accounts23.monthly_category_based_reports23,name='monthly_category_based_reports23'),
    path('yearly_category_based_reports23/', accounts23.yearly_category_based_reports23,name='yearly_category_based_reports23'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed23/', accounts23.daily_detailed23, name='daily_detailed23'),
    path('monthly_detailed23/',accounts23.monthly_detailed23,name='monthly_detailed23'),
    path('yearly_detailed23/',accounts23.yearly_detailed23,name='yearly_detailed23'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports23/', accounts23.item_based_reports23, name='item_based_reports23'),
    path('daily_item_based_reports23/',accounts23.daily_item_based_reports23,name='daily_item_based_reports23'),
    path('monthly_item_based_reports23/',accounts23.monthly_item_based_reports23,name='monthly_item_based_reports23'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports23/', accounts23.ledger_based_reports23, name='ledger_based_reports23'),
    path('monthly_ledger_based_reports23/', accounts23.monthly_ledger_based_reports23, name='monthly_ledger_based_reports23'),
    path('daily_ledger_based_reports23/',accounts23.daily_ledger_based_reports23,name='daily_ledger_based_reports23'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports23/', accounts23.accounts_book_based_reports23, name='accounts_book_based_reports23'),
    path('daily_accounts_book_based_reports23/',accounts23.daily_accounts_book_based_reports23,name='daily_accounts_book_based_reports23'),
    path('monthly_accounts_book_based_reports23/',accounts23.monthly_accounts_book_based_reports23,name='monthly_accounts_book_based_reports23'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months23/', accounts23.monthly_reports_choose_months23, name='monthly_reports_choose_months23'),
    path('monthly_detailed_daily_in_exp_items_report23/<mo>',accounts23.monthly_detailed_daily_in_exp_items_report23,name='monthly_detailed_daily_in_exp_items_report23'),

    path('single_monthly_reports_choose_months23/', accounts23.single_monthly_reports_choose_months23,name='single_monthly_reports_choose_months23'),
    path('single_monthly_daily_in_exp_items_report23/<mo>',accounts23.single_monthly_daily_in_exp_items_report23,name='single_monthly_daily_in_exp_items_report23'),

    path('accounts_dash_board_ob_ch23/',accounts23.accounts_dash_board_ob_ch23,name='accounts_dash_board_ob_ch23'),
    path('accounts_dash_board23/',accounts23.accounts_dash_board23,name='accounts_dash_board23'),

    path('profit_sharing_choose_months23', accounts23.profit_sharing_choose_months23,name='profit_sharing_choose_months23'),
    path('profit_sharing23/<mo>', accounts23.profit_sharing23, name='profit_sharing23'),
    path('view_share_holders23', accounts23.view_share_holders23, name='view_share_holders23'),
    path('create_share_holders23', accounts23.create_share_holders23, name='create_share_holders23'),
    path('regi_share_holders23', accounts23.regi_share_holders23, name='regi_share_holders23'),
    path('update_share_holders23/<id>', accounts23.update_share_holders23, name='update_share_holders23'),
    path('delete_share_holders23/<id>', accounts23.delete_share_holders23, name='delete_share_holders23'),
    path('view_deleted_share_holders23', accounts23.view_deleted_share_holders23, name='view_deleted_share_holders23'),

    path('regi_multiple_share_holders23', accounts23.regi_multiple_share_holders23, name='regi_multiple_share_holders23'),

    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch23/', branch_settings23.guest_rent_update_ob_ch23, name='guest_rent_update_ob_ch23'),

    ############BRANCH SETTINGS END HERE ############################

]

