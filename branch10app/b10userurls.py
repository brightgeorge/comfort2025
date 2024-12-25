from django.urls import path, include

from . import admin_branch10
from . import admin_branch10
from . import branch10
from . import reports10
from . import payment10
from . import admin_dashboard_calculations_br10
from . import accounts10

urlpatterns = [

    path('branch1_dashboard_ob_ch10/', branch10.branch1_dashboard_ob_ch10, name='branch1_dashboard_ob_ch10'),
    path('branch1_dashboard10/',branch10.branch1_dashboard10,name='branch1_dashboard10'),
    path('user_dashboard_calculations_ob_ch10/',branch10.user_dashboard_calculations_ob_ch10,name='user_dashboard_calculations_ob_ch10'),

    path('background_ob_ch10',branch10.background_ob_ch10,name='background_ob_ch10'),
    path('background_regi_ob_ch10',branch10.background_regi_ob_ch10,name='background_regi_ob_ch10'),
    path('custom_background_regi_ob_ch10',branch10.custom_background_regi_ob_ch10,name='custom_background_regi_ob_ch10'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch10/',admin_branch10.branch1_room_create_regi_ob_ch10,name='branch1_room_create_regi_ob_ch10'),
    path('view_all_room_ob_ch10/',admin_branch10.view_all_room_ob_ch10,name='view_all_room_ob_ch10'),
    path('delete_room_ob_ch10/<id>',admin_branch10.delete_room_ob_ch10,name='delete_room_ob_ch10'),

    path('branch1_room_create_ob_ch10/',admin_branch10.branch1_room_create_ob_ch10,name='branch1_room_create_ob_ch10'),

    path('multiple_branch1_room_create_regi10/',admin_branch10.multiple_branch1_room_create_regi10,name='multiple_branch1_room_create_regi10'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch10/', admin_branch10.pg1_bed_create_regi_ob_ch10, name='pg1_bed_create_regi_ob_ch10'),
    path('pg1_view_all_beds_ob_ch10/', admin_branch10.pg1_view_all_beds_ob_ch10, name='pg1_view_all_beds_ob_ch10'),
    path('delete_bed_ob_ch10/<id>', admin_branch10.delete_bed_ob_ch10, name='delete_bed_ob_ch10'),

    path('pg1_bed_create_ob_ch10/', admin_branch10.pg1_bed_create_ob_ch10, name='pg1_bed_create_ob_ch10'),

    path('single_pg1_bed_create_regi_ob_ch10/',admin_branch10.single_pg1_bed_create_regi_ob_ch10,name='single_pg1_bed_create_regi_ob_ch10'),
    path('update_bed_basic_details_ob_ch10/<id>',admin_branch10.update_bed_basic_details_ob_ch10, name='update_bed_basic_details_ob_ch10'),

    path('multiple_single_pg1_bed_create_regi10/',admin_branch10.multiple_single_pg1_bed_create_regi10,name='multiple_single_pg1_bed_create_regi10'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch10/<id>',branch10.br1_admit_guest_ob_ch10,name='br1_admit_guest_ob_ch10'),
    path('view_all_new_guest_ob_ch10/',branch10.view_all_new_guest_ob_ch10,name='view_all_new_guest_ob_ch10'),
    path('update_br1_admit_guest_ob_ch10/<id>',branch10.update_br1_admit_guest_ob_ch10,name='update_br1_admit_guest_ob_ch10'),
    path('vacate_br1_guest_ob_ch10/<id>',branch10.vacate_br1_guest_ob_ch10,name='vacate_br1_guest_ob_ch10'),

    path('active_guest_details_ob_ch10/<guest_code>',branch10.active_guest_details_ob_ch10,name='active_guest_details_ob_ch10'),
    path('view_all_guest_ob_ch10/',branch10.view_all_guest_ob_ch10,name='view_all_guest_ob_ch10'),
    path('shift_guest_ob_ch10/<id>',branch10.shift_guest_ob_ch10,name='shift_guest_ob_ch10'),
    path('shift_guest_regi_ob_ch10/',branch10.shift_guest_regi_ob_ch10,name='shift_guest_regi_ob_ch10'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch10/',branch10.update_all_rent_ob_ch10,name='update_all_rent_ob_ch10'),

    path('multiple_br1_admit_guest10/<id>',branch10.multiple_br1_admit_guest10,name='multiple_br1_admit_guest10'),

#guest end here


##################################
#_ADVANCE_ob_ch10 START HERE
################################


    path('choose_months_advance_ob_ch10/',branch10.choose_months_advance_ob_ch10,name='choose_months_advance_ob_ch10'),

    path('jan_advance_ob_ch10/', branch10.jan_advance_ob_ch10, name='jan_advance_ob_ch10'),
    path('jan_make_payments_advance_ob_ch10/<id>', branch10.jan_make_payments_advance_ob_ch10,name='jan_make_payments_advance_ob_ch10'),
    path('feb_advance_ob_ch10/', branch10.feb_advance_ob_ch10, name='feb_advance_ob_ch10'),
    path('feb_make_payments_advance_ob_ch10/<id>', branch10.feb_make_payments_advance_ob_ch10,name='feb_make_payments_advance_ob_ch10'),
    path('march_advance_ob_ch10/', branch10.march_advance_ob_ch10, name='march_advance_ob_ch10'),
    path('march_make_payments_advance_ob_ch10/<id>', branch10.march_make_payments_advance_ob_ch10,name='march_make_payments_advance_ob_ch10'),
    path('april_advance_ob_ch10/', branch10.april_advance_ob_ch10, name='april_advance_ob_ch10'),
    path('april_make_payments_advance_ob_ch10/<id>', branch10.april_make_payments_advance_ob_ch10, name='april_make_payments_advance_ob_ch10'),

    path('may_advance_ob_ch10/',branch10.may_advance_ob_ch10,name='may_advance_ob_ch10'),
    path('may_make_payments_advance_ob_ch10/<id>', branch10.may_make_payments_advance_ob_ch10, name='may_make_payments_advance_ob_ch10'),
    path('june_advance_ob_ch10/',branch10.june_advance_ob_ch10,name='june_advance_ob_ch10'),
    path('june_make_payments_advance_ob_ch10/<id>', branch10.june_make_payments_advance_ob_ch10, name='june_make_payments_advance_ob_ch10'),
    path('july_advance_ob_ch10/',branch10.july_advance_ob_ch10,name='july_advance_ob_ch10'),
    path('july_make_payments_advance_ob_ch10/<id>', branch10.july_make_payments_advance_ob_ch10, name='july_make_payments_advance_ob_ch10'),
    path('auguest_advance_ob_ch10/', branch10.auguest_advance_ob_ch10, name='auguest_advance_ob_ch10'),
    path('auguest_make_payments_advance_ob_ch10/<id>', branch10.auguest_make_payments_advance_ob_ch10, name='auguest_make_payments_advance_ob_ch10'),

    path('sept_advance_ob_ch10/', branch10.sept_advance_ob_ch10, name='sept_advance_ob_ch10'),
    path('sept_make_payments_advance_ob_ch10/<id>', branch10.sept_make_payments_advance_ob_ch10,name='sept_make_payments_advance_ob_ch10'),
    path('october_advance_ob_ch10/', branch10.october_advance_ob_ch10, name='october_advance_ob_ch10'),
    path('october_make_payments_advance_ob_ch10/<id>', branch10.october_make_payments_advance_ob_ch10, name='october_make_payments_advance_ob_ch10'),
    path('nov_advance_ob_ch10/', branch10.nov_advance_ob_ch10, name='nov_advance_ob_ch10'),
    path('nov_make_payments_advance_ob_ch10/<id>', branch10.nov_make_payments_advance_ob_ch10,name='nov_make_payments_advance_ob_ch10'),
    path('dec_advance_ob_ch10/', branch10.dec_advance_ob_ch10, name='dec_advance_ob_ch10'),
    path('dec_make_payments_advance_ob_ch10/<id>', branch10.dec_make_payments_advance_ob_ch10, name='dec_make_payments_advance_ob_ch10'),



##################################
#_ADVANCE_ob_ch10 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch10/',branch10.choose_months_ob_ch10,name='choose_months_ob_ch10'),

    path('jan_ob_ch10/',branch10.jan_ob_ch10,name='jan_ob_ch10'),
    path('jan_manke_payments_ob_ch10/<id>',branch10.jan_manke_payments_ob_ch10,name='jan_manke_payments_ob_ch10'),

    path('feb_ob_ch10/',branch10.feb_ob_ch10,name='feb_ob_ch10'),
    path('feb_manke_payments_ob_ch10/<id>',branch10.feb_manke_payments_ob_ch10,name='feb_manke_payments_ob_ch10'),

    path('march_ob_ch10/',branch10.march_ob_ch10,name='march_ob_ch10'),
    path('march_manke_payments_ob_ch10/<id>',branch10.march_manke_payments_ob_ch10,name='march_manke_payments_ob_ch10'),

    path('april_ob_ch10/',branch10.april_ob_ch10,name='april_ob_ch10'),
    path('april_make_payments_ob_ch10/<id>',branch10.april_make_payments_ob_ch10,name='april_make_payments_ob_ch10'),

    path('may_ob_ch10/',branch10.may_ob_ch10,name='may_ob_ch10'),
    path('may_make_payments_ob_ch10/<id>',branch10.may_make_payments_ob_ch10,name='may_make_payments_ob_ch10'),

    path('june_ob_ch10/',branch10.june_ob_ch10,name='june_ob_ch10'),
    path('june_make_payments_ob_ch10/<id>',branch10.june_make_payments_ob_ch10,name='june_make_payments_ob_ch10'),

    path('july_ob_ch10/',branch10.july_ob_ch10,name='july_ob_ch10'),
    path('july_make_payments_ob_ch10/<id>',branch10.july_make_payments_ob_ch10,name='july_make_payments_ob_ch10'),

    path('aug_ob_ch10/',branch10.aug_ob_ch10,name='aug_ob_ch10'),
    path('aug_make_payments_ob_ch10/<id>',branch10.aug_make_payments_ob_ch10,name='aug_make_payments_ob_ch10'),

    path('sept_ob_ch10/',branch10.sept_ob_ch10,name='sept_ob_ch10'),
    path('sept_make_payments_ob_ch10/<id>',branch10.sept_make_payments_ob_ch10,name='sept_make_payments_ob_ch10'),

    path('oct_ob_ch10/',branch10.oct_ob_ch10,name='oct_ob_ch10'),
    path('oct_make_payments_ob_ch10/<id>',branch10.oct_make_payments_ob_ch10,name='oct_make_payments_ob_ch10'),

    path('nov_ob_ch10/',branch10.nov_ob_ch10,name='nov_ob_ch10'),
    path('nov_make_payments_ob_ch10/<id>',branch10.nov_make_payments_ob_ch10,name='nov_make_payments_ob_ch10'),

    path('dec_ob_ch10/',branch10.dec_ob_ch10,name='dec_ob_ch10'),
    path('dec_make_payments_ob_ch10/<id>',branch10.dec_make_payments_ob_ch10,name='dec_make_payments_ob_ch10'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch10/', payment10.choose_user_ob_ch10, name='choose_user_ob_ch10'),
    path('payment_user_details_ob_ch10/<id>', payment10.payment_user_details_ob_ch10, name='payment_user_details_ob_ch10'),
    path('close_choose_user_ob_ch10/<id>',payment10.close_choose_user_ob_ch10,name='close_choose_user_ob_ch10'),

    path('monthly_jan_make_payments_ob_ch10/<id>', payment10.monthly_jan_make_payments_ob_ch10, name='monthly_jan_make_payments_ob_ch10'),
    path('monthly_feb_make_payments_ob_ch10/<id>', payment10.monthly_feb_make_payments_ob_ch10, name='monthly_feb_make_payments_ob_ch10'),
    path('monthly_march_make_payments_ob_ch10/<id>', payment10.monthly_march_make_payments_ob_ch10, name='monthly_march_make_payments_ob_ch10'),
    path('monthly_april_make_payments_ob_ch10/<id>', payment10.monthly_april_make_payments_ob_ch10, name='monthly_april_make_payments_ob_ch10'),
    path('monthly_may_make_payments_ob_ch10/<id>', payment10.monthly_may_make_payments_ob_ch10, name='monthly_may_make_payments_ob_ch10'),
    path('monthly_june_make_payments_ob_ch10/<id>', payment10.monthly_june_make_payments_ob_ch10, name='monthly_june_make_payments_ob_ch10'),

    path('monthly_july_make_payments_ob_ch10/<id>', payment10.monthly_july_make_payments_ob_ch10, name='monthly_july_make_payments_ob_ch10'),
    path('monthly_aug_make_payments_ob_ch10/<id>', payment10.monthly_aug_make_payments_ob_ch10, name='monthly_aug_make_payments_ob_ch10'),
    path('monthly_sept_make_payments_ob_ch10/<id>', payment10.monthly_sept_make_payments_ob_ch10, name='monthly_sept_make_payments_ob_ch10'),
    path('monthly_oct_make_payments_ob_ch10/<id>', payment10.monthly_oct_make_payments_ob_ch10, name='monthly_oct_make_payments_ob_ch10'),
    path('monthly_nov_make_payments_ob_ch10/<id>', payment10.monthly_nov_make_payments_ob_ch10, name='monthly_nov_make_payments_ob_ch10'),
    path('monthly_dec_make_payments_ob_ch10/<id>', payment10.monthly_dec_make_payments_ob_ch10, name='monthly_dec_make_payments_ob_ch10'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch10/',branch10.unpaid_rent_choose_months_ob_ch10,name='unpaid_rent_choose_months_ob_ch10'),

    path('jan_unpaid_rent_ob_ch10/', branch10.jan_unpaid_rent_ob_ch10, name='jan_unpaid_rent_ob_ch10'),
    path('table_jan_unpaid_rent_ob_ch10/', branch10.table_jan_unpaid_rent_ob_ch10, name='table_jan_unpaid_rent_ob_ch10'),
    path('feb_unpaid_rent_ob_ch10/', branch10.feb_unpaid_rent_ob_ch10, name='feb_unpaid_rent_ob_ch10'),
    path('table_feb_unpaid_rent_ob_ch10/', branch10.table_feb_unpaid_rent_ob_ch10, name='table_feb_unpaid_rent_ob_ch10'),
    path('mar_unpaid_rent_ob_ch10/', branch10.mar_unpaid_rent_ob_ch10, name='mar_unpaid_rent_ob_ch10'),
    path('table_mar_unpaid_rent_ob_ch10/', branch10.table_mar_unpaid_rent_ob_ch10, name='table_mar_unpaid_rent_ob_ch10'),
    path('april_unpaid_rent_ob_ch10/', branch10.april_unpaid_rent_ob_ch10, name='april_unpaid_rent_ob_ch10'),
    path('table_april_unpaid_rent_ob_ch10/', branch10.table_april_unpaid_rent_ob_ch10, name='table_april_unpaid_rent_ob_ch10'),

    path('may_unpaid_rent_ob_ch10/', branch10.may_unpaid_rent_ob_ch10, name='may_unpaid_rent_ob_ch10'),
    path('table_may_unpaid_rent_ob_ch10/', branch10.table_may_unpaid_rent_ob_ch10, name='table_may_unpaid_rent_ob_ch10'),
    path('june_unpaid_rent_ob_ch10/', branch10.june_unpaid_rent_ob_ch10, name='june_unpaid_rent_ob_ch10'),
    path('table_june_unpaid_rent_ob_ch10/', branch10.table_june_unpaid_rent_ob_ch10, name='table_june_unpaid_rent_ob_ch10'),
    path('july_unpaid_rent_ob_ch10/', branch10.july_unpaid_rent_ob_ch10, name='july_unpaid_rent_ob_ch10'),
    path('table_july_unpaid_rent_ob_ch10',branch10.table_july_unpaid_rent_ob_ch10,name='table_july_unpaid_rent_ob_ch10'),
    path('aug_unpaid_rent_ob_ch10/', branch10.aug_unpaid_rent_ob_ch10, name='aug_unpaid_rent_ob_ch10'),
    path('table_aug_unpaid_rent_ob_ch10/',branch10.table_aug_unpaid_rent_ob_ch10,name='table_aug_unpaid_rent_ob_ch10'),

    path('sept_unpaid_rent_ob_ch10/', branch10.sept_unpaid_rent_ob_ch10, name='sept_unpaid_rent_ob_ch10'),
    path('table_sept_unpaid_rent_ob_ch10/', branch10.table_sept_unpaid_rent_ob_ch10, name='table_sept_unpaid_rent_ob_ch10'),
    path('oct_unpaid_rent_ob_ch10/', branch10.oct_unpaid_rent_ob_ch10, name='oct_unpaid_rent_ob_ch10'),
    path('table_oct_unpaid_rent_ob_ch10/', branch10.table_oct_unpaid_rent_ob_ch10, name='table_oct_unpaid_rent_ob_ch10'),
    path('nov_unpaid_rent_ob_ch10/', branch10.nov_unpaid_rent_ob_ch10, name='nov_unpaid_rent_ob_ch10'),
    path('table_nov_unpaid_rent_ob_ch10/', branch10.table_nov_unpaid_rent_ob_ch10, name='table_nov_unpaid_rent_ob_ch10'),
    path('dec_unpaid_rent_ob_ch10/', branch10.dec_unpaid_rent_ob_ch10, name='dec_unpaid_rent_ob_ch10'),
    path('table_dec_unpaid_rent_ob_ch10/', branch10.table_dec_unpaid_rent_ob_ch10, name='table_dec_unpaid_rent_ob_ch10'),

    path('details_of_unpaid_guests_ob_ch10/<id>',branch10.details_of_unpaid_guests_ob_ch10,name='details_of_unpaid_guests_ob_ch10'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch10/',branch10.paid_rent_choose_months_ob_ch10,name='paid_rent_choose_months_ob_ch10'),
    path('partially_paid_guest_choose_months_ob_ch10/',reports10.partially_paid_guest_choose_months_ob_ch10,name='partially_paid_guest_choose_months_ob_ch10'),

    path('jan_paid_rent_ob_ch10/', branch10.jan_paid_rent_ob_ch10, name='jan_paid_rent_ob_ch10'),
    path('table_jan_paid_rent_ob_ch10/', branch10.table_jan_paid_rent_ob_ch10, name='table_jan_paid_rent_ob_ch10'),
    path('jan_full_paid_guest_ob_ch10/', reports10.jan_full_paid_guest_ob_ch10, name='jan_full_paid_guest_ob_ch10'),
    path('jan_partially_paid_guest_ob_ch10/', reports10.jan_partially_paid_guest_ob_ch10, name='jan_partially_paid_guest_ob_ch10'),
    path('table_jan_partially_paid_guest_ob_ch10/', reports10.table_jan_partially_paid_guest_ob_ch10,name='table_jan_partially_paid_guest_ob_ch10'),

    path('feb_paid_rent_ob_ch10/', branch10.feb_paid_rent_ob_ch10, name='feb_paid_rent_ob_ch10'),
    path('table_feb_paid_rent_ob_ch10/', branch10.table_feb_paid_rent_ob_ch10, name='table_feb_paid_rent_ob_ch10'),
    path('feb_full_paid_guest_ob_ch10/', reports10.feb_full_paid_guest_ob_ch10, name='feb_full_paid_guest_ob_ch10'),
    path('feb_partially_paid_guest_ob_ch10/', reports10.feb_partially_paid_guest_ob_ch10, name='feb_partially_paid_guest_ob_ch10'),
    path('table_feb_partially_paid_guest_ob_ch10/', reports10.table_feb_partially_paid_guest_ob_ch10,name='table_feb_partially_paid_guest_ob_ch10'),

    path('mar_paid_rent_ob_ch10/', branch10.mar_paid_rent_ob_ch10, name='mar_paid_rent_ob_ch10'),
    path('table_mar_paid_rent_ob_ch10/', branch10.table_mar_paid_rent_ob_ch10, name='table_mar_paid_rent_ob_ch10'),
    path('march_full_paid_guest_ob_ch10/', reports10.march_full_paid_guest_ob_ch10, name='march_full_paid_guest_ob_ch10'),
    path('march_partially_paid_guest_ob_ch10/', reports10.march_partially_paid_guest_ob_ch10, name='march_partially_paid_guest_ob_ch10'),
    path('table_march_partially_paid_guest_ob_ch10/', reports10.table_march_partially_paid_guest_ob_ch10,name='table_march_partially_paid_guest_ob_ch10'),

    path('april_paid_rent_ob_ch10/', branch10.april_paid_rent_ob_ch10, name='april_paid_rent_ob_ch10'),
    path('table_april_paid_rent_ob_ch10/', branch10.table_april_paid_rent_ob_ch10, name='table_april_paid_rent_ob_ch10'),
    path('april_full_paid_guest_ob_ch10/', reports10.april_full_paid_guest_ob_ch10, name='april_full_paid_guest_ob_ch10'),
    path('april_partially_paid_guest_ob_ch10/', reports10.april_partially_paid_guest_ob_ch10, name='april_partially_paid_guest_ob_ch10'),
    path('table_april_partially_paid_guest_ob_ch10/', reports10.table_april_partially_paid_guest_ob_ch10,name='table_april_partially_paid_guest_ob_ch10'),

    path('may_paid_rent_ob_ch10/', branch10.may_paid_rent_ob_ch10, name='may_paid_rent_ob_ch10'),
    path('table_may_paid_rent_ob_ch10/', branch10.table_may_paid_rent_ob_ch10, name='table_may_paid_rent_ob_ch10'),
    path('may_full_paid_guest_ob_ch10/', reports10.may_full_paid_guest_ob_ch10, name='may_full_paid_guest_ob_ch10'),
    path('may_partially_paid_guest_ob_ch10/', reports10.may_partially_paid_guest_ob_ch10, name='may_partially_paid_guest_ob_ch10'),
    path('table_may_partially_paid_guest_ob_ch10/', reports10.table_may_partially_paid_guest_ob_ch10, name='table_may_partially_paid_guest_ob_ch10'),

    path('june_paid_rent_ob_ch10/', branch10.june_paid_rent_ob_ch10, name='june_paid_rent_ob_ch10'),
    path('table_june_paid_rent_ob_ch10/', branch10.table_june_paid_rent_ob_ch10, name='table_june_paid_rent_ob_ch10'),
    path('june_full_paid_guest_ob_ch10/', reports10.june_full_paid_guest_ob_ch10, name='june_full_paid_guest_ob_ch10'),
    path('june_partially_paid_guest_ob_ch10/', reports10.june_partially_paid_guest_ob_ch10, name='june_partially_paid_guest_ob_ch10'),
    path('table_june_partially_paid_guest_ob_ch10/', reports10.table_june_partially_paid_guest_ob_ch10, name='table_june_partially_paid_guest_ob_ch10'),

    path('july_paid_rent_ob_ch10/', branch10.july_paid_rent_ob_ch10, name='july_paid_rent_ob_ch10'),
    path('table_july_paid_rent_ob_ch10/', branch10.table_july_paid_rent_ob_ch10, name='table_july_paid_rent_ob_ch10'),
    path('july_full_paid_guest_ob_ch10/', reports10.july_full_paid_guest_ob_ch10, name='july_full_paid_guest_ob_ch10'),
    path('july_partially_paid_guest_ob_ch10/', reports10.july_partially_paid_guest_ob_ch10, name='july_partially_paid_guest_ob_ch10'),
    path('table_july_partially_paid_guest_ob_ch10/', reports10.table_july_partially_paid_guest_ob_ch10, name='table_july_partially_paid_guest_ob_ch10'),

    path('aug_paid_rent_ob_ch10/', branch10.aug_paid_rent_ob_ch10, name='aug_paid_rent_ob_ch10'),
    path('table_aug_paid_rent_ob_ch10/', branch10.table_aug_paid_rent_ob_ch10, name='table_aug_paid_rent_ob_ch10'),
    path('auguest_full_paid_guest_ob_ch10/', reports10.auguest_full_paid_guest_ob_ch10, name='auguest_full_paid_guest_ob_ch10'),
    path('auguest_partially_paid_guest_ob_ch10/', reports10.auguest_partially_paid_guest_ob_ch10,name='auguest_partially_paid_guest_ob_ch10'),
    path('table_auguest_partially_paid_guest_ob_ch10/', reports10.table_auguest_partially_paid_guest_ob_ch10,name='table_auguest_partially_paid_guest_ob_ch10'),

    path('sept_paid_rent_ob_ch10/', branch10.sept_paid_rent_ob_ch10, name='sept_paid_rent_ob_ch10'),
    path('table_sept_paid_rent_ob_ch10/', branch10.table_sept_paid_rent_ob_ch10, name='table_sept_paid_rent_ob_ch10'),
    path('sept_full_paid_guest_ob_ch10/', reports10.sept_full_paid_guest_ob_ch10, name='sept_full_paid_guest_ob_ch10'),
    path('sept_partially_paid_guest_ob_ch10/', reports10.sept_partially_paid_guest_ob_ch10, name='sept_partially_paid_guest_ob_ch10'),
    path('table_sept_partially_paid_guest_ob_ch10/', reports10.table_sept_partially_paid_guest_ob_ch10,name='table_sept_partially_paid_guest_ob_ch10'),

    path('oct_paid_rent_ob_ch10/', branch10.oct_paid_rent_ob_ch10, name='oct_paid_rent_ob_ch10'),
    path('table_oct_paid_rent_ob_ch10/', branch10.table_oct_paid_rent_ob_ch10, name='table_oct_paid_rent_ob_ch10'),
    path('october_full_paid_guest_ob_ch10/', reports10.october_full_paid_guest_ob_ch10, name='october_full_paid_guest_ob_ch10'),
    path('october_partially_paid_guest_ob_ch10/', reports10.october_partially_paid_guest_ob_ch10,name='october_partially_paid_guest_ob_ch10'),
    path('table_october_partially_paid_guest_ob_ch10/', reports10.table_october_partially_paid_guest_ob_ch10,name='table_october_partially_paid_guest_ob_ch10'),

    path('nov_paid_rent_ob_ch10/', branch10.nov_paid_rent_ob_ch10, name='nov_paid_rent_ob_ch10'),
    path('table_nov_paid_rent_ob_ch10/', branch10.table_nov_paid_rent_ob_ch10, name='table_nov_paid_rent_ob_ch10'),
    path('nov_full_paid_guest_ob_ch10/', reports10.nov_full_paid_guest_ob_ch10, name='nov_full_paid_guest_ob_ch10'),
    path('nov_partially_paid_guest_ob_ch10/', reports10.nov_partially_paid_guest_ob_ch10, name='nov_partially_paid_guest_ob_ch10'),
    path('table_nov_partially_paid_guest_ob_ch10/', reports10.table_nov_partially_paid_guest_ob_ch10,name='table_nov_partially_paid_guest_ob_ch10'),

    path('dec_paid_rent_ob_ch10/', branch10.dec_paid_rent_ob_ch10, name='dec_paid_rent_ob_ch10'),
    path('table_dec_paid_rent_ob_ch10/', branch10.table_dec_paid_rent_ob_ch10, name='table_dec_paid_rent_ob_ch10'),
    path('dec_full_paid_guest_ob_ch10/', reports10.dec_full_paid_guest_ob_ch10, name='dec_full_paid_guest_ob_ch10'),
    path('dec_partially_paid_guest_ob_ch10/', reports10.dec_partially_paid_guest_ob_ch10, name='dec_partially_paid_guest_ob_ch10'),
    path('table_dec_partially_paid_guest_ob_ch10/', reports10.table_dec_partially_paid_guest_ob_ch10,name='table_dec_partially_paid_guest_ob_ch10'),

    path('details_of_paid_guests_ob_ch10/<id>',branch10.details_of_paid_guests_ob_ch10,name='details_of_paid_guests_ob_ch10'),
    path('full_paid_guest_ob_ch10/',reports10.full_paid_guest_ob_ch10,name='full_paid_guest_ob_ch10'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch10/',branch10.viewall_vacate_guest_ob_ch10,name='viewall_vacate_guest_ob_ch10'),
    path('details_of_vacate_guest_ob_ch10/<id>',branch10.details_of_vacate_guest_ob_ch10,name='details_of_vacate_guest_ob_ch10'),
    path('full_vacated_guest_details_ob_ch10',branch10.full_vacated_guest_details_ob_ch10,name='full_vacated_guest_details_ob_ch10'),
    path('full_vacated_guest_table_ob_ch10',branch10.full_vacated_guest_table_ob_ch10,name='full_vacated_guest_table_ob_ch10'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch10/<id>', branch10.jan_manke_payments_vacate_ob_ch10, name='jan_manke_payments_vacate_ob_ch10'),
    path('feb_manke_payments_vacate_ob_ch10/<id>', branch10.feb_manke_payments_vacate_ob_ch10, name='feb_manke_payments_vacate_ob_ch10'),
    path('march_manke_payments_vacate_ob_ch10/<id>', branch10.march_manke_payments_vacate_ob_ch10, name='march_manke_payments_vacate_ob_ch10'),
    path('april_make_payments_vacate_ob_ch10/<id>', branch10.april_make_payments_vacate_ob_ch10, name='april_make_payments_vacate_ob_ch10'),

    path('may_make_payments_vacate_ob_ch10/<id>', branch10.may_make_payments_vacate_ob_ch10, name='may_make_payments_vacate_ob_ch10'),
    path('june_make_payments_vacate_ob_ch10/<id>', branch10.june_make_payments_vacate_ob_ch10, name='june_make_payments_vacate_ob_ch10'),
    path('july_make_payments_vacate_ob_ch10/<id>', branch10.july_make_payments_vacate_ob_ch10, name='july_make_payments_vacate_ob_ch10'),
    path('aug_make_payments_vacate_ob_ch10/<id>', branch10.aug_make_payments_vacate_ob_ch10, name='aug_make_payments_vacate_ob_ch10'),

    path('sept_make_payments_vacate_ob_ch10/<id>', branch10.sept_make_payments_vacate_ob_ch10, name='sept_make_payments_vacate_ob_ch10'),
    path('oct_make_payments_vacate_ob_ch10/<id>', branch10.oct_make_payments_vacate_ob_ch10, name='oct_make_payments_vacate_ob_ch10'),
    path('nov_make_payments_vacate_ob_ch10/<id>', branch10.nov_make_payments_vacate_ob_ch10, name='nov_make_payments_vacate_ob_ch10'),
    path('dec_make_payments_vacate_ob_ch10/<id>', branch10.dec_make_payments_vacate_ob_ch10, name='dec_make_payments_vacate_ob_ch10'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch10/',branch10.detail_guest_general_ob_ch10,name='detail_guest_general_ob_ch10'),

    path('jan_print_ob_ch10/',branch10.jan_print_ob_ch10,name='jan_print_ob_ch10'),
    path('feb_print_ob_ch10/',branch10.feb_print_ob_ch10,name='feb_print_ob_ch10'),
    path('march_print_ob_ch10/',branch10.march_print_ob_ch10,name='march_print_ob_ch10'),
    path('april_print_ob_ch10/',branch10.april_print_ob_ch10,name='april_print_ob_ch10'),

    path('may_print_ob_ch10/',branch10.may_print_ob_ch10,name='may_print_ob_ch10'),
    path('june_print_ob_ch10/',branch10.june_print_ob_ch10,name='june_print_ob_ch10'),
    path('july_print_ob_ch10/', branch10.july_print_ob_ch10, name='july_print_ob_ch10'),
    path('aug_print_ob_ch10/', branch10.aug_print_ob_ch10, name='aug_print_ob_ch10'),

    path('sept_print_ob_ch10/', branch10.sept_print_ob_ch10, name='sept_print_ob_ch10'),
    path('oct_print_ob_ch10/', branch10.oct_print_ob_ch10, name='oct_print_ob_ch10'),
    path('nov_print_ob_ch10/', branch10.nov_print_ob_ch10, name='nov_print_ob_ch10'),
    path('dec_print_ob_ch10/', branch10.dec_print_ob_ch10, name='dec_print_ob_ch10'),

    path('new_year_jan_print_ob_ch10/', branch10.new_year_jan_print_ob_ch10, name='new_year_jan_print_ob_ch10'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch10/', branch10.jan_close_ob_ch10, name='jan_close_ob_ch10'),
    path('jan_close_decision_page_ob_ch10/', branch10.jan_close_decision_page_ob_ch10, name='jan_close_decision_page_ob_ch10'),
    path('feb_close/', branch10.feb_close_ob_ch10, name='feb_close_ob_ch10'),
    path('feb_close_decision_page_ob_ch10/', branch10.feb_close_decision_page_ob_ch10, name='feb_close_decision_page_ob_ch10'),
    path('mar_close_ob_ch10/', branch10.mar_close_ob_ch10, name='mar_close_ob_ch10'),
    path('mar_close_decision_page/', branch10.mar_close_decision_page_ob_ch10, name='mar_close_decision_page_ob_ch10'),
    path('apr_close_ob_ch10/', branch10.apr_close_ob_ch10, name='apr_close_ob_ch10'),
    path('apr_close_decision_page_ob_ch10/', branch10.apr_close_decision_page_ob_ch10, name='apr_close_decision_page_ob_ch10'),

    path('may_close_ob_ch10/', branch10.may_close_ob_ch10, name='may_close_ob_ch10'),
    path('may_close_decision_page_ob_ch10/', branch10.may_close_decision_page_ob_ch10, name='may_close_decision_page_ob_ch10'),
    path('jun_close_ob_ch10/', branch10.jun_close_ob_ch10, name='jun_close_ob_ch10'),
    path('jun_close_decision_page_ob_ch10/', branch10.jun_close_decision_page_ob_ch10, name='jun_close_decision_page_ob_ch10'),
    path('jul_close_ob_ch10/', branch10.jul_close_ob_ch10, name='jul_close_ob_ch10'),
    path('jul_close_decision_page_ob_ch10/', branch10.jul_close_decision_page_ob_ch10, name='jul_close_decision_page_ob_ch10'),
    path('aug_close_ob_ch10/', branch10.aug_close_ob_ch10, name='aug_close_ob_ch10'),
    path('aug_close_decision_page_ob_ch10/', branch10.aug_close_decision_page_ob_ch10, name='aug_close_decision_page_ob_ch10'),

    path('sep_close_ob_ch10/', branch10.sep_close_ob_ch10, name='sep_close_ob_ch10'),
    path('sep_close_decision_page_ob_ch10/', branch10.sep_close_decision_page_ob_ch10, name='sep_close_decision_page_ob_ch10'),
    path('oct_close_ob_ch10/', branch10.oct_close_ob_ch10, name='oct_close_ob_ch10'),
    path('oct_close_decision_page_ob_ch10/', branch10.oct_close_decision_page_ob_ch10, name='oct_close_decision_page_ob_ch10'),
    path('nov_close_ob_ch10/', branch10.nov_close_ob_ch10, name='nov_close_ob_ch10'),
    path('nov_close_decision_page_ob_ch10/', branch10.nov_close_decision_page_ob_ch10, name='nov_close_decision_page_ob_ch10'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch10/',reports10.detailed_report_choose_months_ob_ch10,name='detailed_report_choose_months_ob_ch10'),

    path('jan_details_live_ob_ch10/', reports10.jan_details_live_ob_ch10, name='jan_details_live_ob_ch10'),
    path('jan_print_live_ob_ch10/', reports10.jan_print_live_ob_ch10, name='jan_print_live_ob_ch10'),
    path('feb_details_live_ob_ch10/', reports10.feb_details_live_ob_ch10, name='feb_details_live_ob_ch10'),
    path('feb_print_live_ob_ch10/', reports10.feb_print_live_ob_ch10, name='feb_print_live_ob_ch10'),
    path('march_details_live_ob_ch10/', reports10.march_details_live_ob_ch10, name='march_details_live_ob_ch10'),
    path('march_print_live_ob_ch10/', reports10.march_print_live_ob_ch10, name='march_print_live_ob_ch10'),

    path('april_details_live_ob_ch10/', reports10.april_details_live_ob_ch10, name='april_details_live_ob_ch10'),
    path('april_print_live_ob_ch10/', reports10.april_print_live_ob_ch10, name='april_print_live_ob_ch10'),
    path('may_details_live_ob_ch10/', reports10.may_details_live_ob_ch10, name='may_details_live_ob_ch10'),
    path('may_print_live_ob_ch10/', reports10.may_print_live_ob_ch10, name='may_print_live_ob_ch10'),
    path('june_details_live_ob_ch10/',reports10.june_details_live_ob_ch10,name='june_details_live_ob_ch10'),
    path('june_print_live_ob_ch10/', reports10.june_print_live_ob_ch10, name='june_print_live_ob_ch10'),

    path('july_details_live_ob_ch10/', reports10.july_details_live_ob_ch10, name='july_details_live_ob_ch10'),
    path('july_print_live_ob_ch10/', reports10.july_print_live_ob_ch10, name='july_print_live_ob_ch10'),
    path('auguest_details_live_ob_ch10/', reports10.auguest_details_live_ob_ch10, name='auguest_details_live_ob_ch10'),
    path('auguest_print_live_ob_ch10/', reports10.auguest_print_live_ob_ch10, name='auguest_print_live_ob_ch10'),
    path('sept_details_live_ob_ch10/', reports10.sept_details_live_ob_ch10, name='sept_details_live_ob_ch10'),
    path('sept_print_live_ob_ch10/', reports10.sept_print_live_ob_ch10, name='sept_print_live_ob_ch10'),

    path('october_details_live_ob_ch10/', reports10.october_details_live_ob_ch10, name='october_details_live_ob_ch10'),
    path('october_print_live_ob_ch10/', reports10.october_print_live_ob_ch10, name='october_print_live_ob_ch10'),
    path('nov_details_live_ob_ch10/', reports10.nov_details_live_ob_ch10, name='nov_details_live_ob_ch10'),
    path('nov_print_live_ob_ch10/', reports10.nov_print_live_ob_ch10, name='nov_print_live_ob_ch10'),
    path('dec_details_live_ob_ch10/', reports10.dec_details_live_ob_ch10, name='dec_details_live_ob_ch10'),
    path('dec_print_live_ob_ch10/', reports10.dec_print_live_ob_ch10, name='dec_print_live_ob_ch10'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch10/', reports10.viewall_vaccant_room_ob_ch10, name='viewall_vaccant_room_ob_ch10'),

    path('d_ob_ch10/', branch10.dynamic, name='dynamic'),

    path('manage_bed_ob_ch10/', branch10.manage_bed_ob_ch10, name='manage_bed_ob_ch10'),
    path('manage_new_guest_ob_ch10/', branch10.manage_new_guest_ob_ch10, name='manage_new_guest_ob_ch10'),
    path('manage_update_new_guest_ob_ch10/<id>', branch10.manage_update_new_guest_ob_ch10, name='manage_update_new_guest_ob_ch10'),
    path('manage_update_beds_ob_ch10/<id>', branch10.manage_update_beds_ob_ch10, name='manage_update_beds_ob_ch10'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch10/', branch10.view_all_due_amt_ob_ch10, name='view_all_due_amt_ob_ch10'),
    path('due_amt_mgt_choose_months_ob_ch10/', branch10.due_amt_mgt_choose_months_ob_ch10, name='due_amt_mgt_choose_months_ob_ch10'),

    path('view_jan_account_details_ob_ch10/', branch10.view_jan_account_details_ob_ch10, name='view_jan_account_details_ob_ch10'),
    path('jan_account_mgt_ob_ch10/<id>',branch10.jan_account_mgt_ob_ch10,name='jan_account_mgt_ob_ch10'),
    path('view_feb_account_details_ob_ch10/', branch10.view_feb_account_details_ob_ch10, name='view_feb_account_details_ob_ch10'),
    path('feb_account_mgt_ob_ch10/<id>',branch10.feb_account_mgt_ob_ch10,name='feb_account_mgt_ob_ch10'),
    path('view_march_account_details_ob_ch10/', branch10.view_march_account_details_ob_ch10, name='view_march_account_details_ob_ch10'),
    path('march_account_mgt_ob_ch10/<id>',branch10.march_account_mgt_ob_ch10,name='march_account_mgt_ob_ch10'),
    path('view_april_account_details_ob_ch10/', branch10.view_april_account_details_ob_ch10, name='view_april_account_details_ob_ch10'),
    path('april_account_mgt_ob_ch10/<id>',branch10.april_account_mgt_ob_ch10,name='april_account_mgt_ob_ch10'),

    path('view_may_account_details_ob_ch10/',branch10.view_may_account_details_ob_ch10,name='view_may_account_details_ob_ch10'),
    path('may_account_mgt_ob_ch10/<id>', branch10.may_account_mgt_ob_ch10, name='may_account_mgt_ob_ch10'),
    path('view_june_account_details_ob_ch10/', branch10.view_june_account_details_ob_ch10, name='view_june_account_details_ob_ch10'),
    path('june_account_mgt_ob_ch10/<id>',branch10.june_account_mgt_ob_ch10,name='june_account_mgt_ob_ch10'),
    path('view_july_account_details_ob_ch10/', branch10.view_july_account_details_ob_ch10, name='view_july_account_details_ob_ch10'),
    path('july_account_mgt_ob_ch10/<id>',branch10.july_account_mgt_ob_ch10,name='july_account_mgt_ob_ch10'),
    path('view_auguest_account_details_ob_ch10/', branch10.view_auguest_account_details_ob_ch10, name='view_auguest_account_details_ob_ch10'),
    path('auguest_account_mgt_ob_ch10/<id>',branch10.auguest_account_mgt_ob_ch10,name='auguest_account_mgt_ob_ch10'),

    path('view_sept_account_details_ob_ch10/', branch10.view_sept_account_details_ob_ch10, name='view_sept_account_details_ob_ch10'),
    path('sept_account_mgt_ob_ch10/<id>',branch10.sept_account_mgt_ob_ch10,name='sept_account_mgt_ob_ch10'),
    path('view_october_account_details_ob_ch10/', branch10.view_october_account_details_ob_ch10, name='view_october_account_details_ob_ch10'),
    path('october_account_mgt_ob_ch10/<id>',branch10.october_account_mgt_ob_ch10,name='october_account_mgt_ob_ch10'),
    path('view_nov_account_details_ob_ch10/', branch10.view_nov_account_details_ob_ch10, name='view_nov_account_details_ob_ch10'),
    path('nov_account_mgt_ob_ch10/<id>',branch10.nov_account_mgt_ob_ch10,name='nov_account_mgt_ob_ch10'),
    path('view_dec_account_details_ob_ch10/', branch10.view_dec_account_details_ob_ch10, name='view_dec_account_details_ob_ch10'),
    path('dec_account_mgt_ob_ch10/<id>',branch10.dec_account_mgt_ob_ch10,name='dec_account_mgt_ob_ch10'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch10', admin_dashboard_calculations_br10.monthly_details_due_ob_ch10, name='monthly_details_due_ob_ch10'),
    path('monthly_collection_details_ob_ch10/', admin_dashboard_calculations_br10.monthly_collection_details_ob_ch10, name='monthly_collection_details_ob_ch10'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch10/',branch10.guest_all_ob_ch10,name='guest_all_ob_ch10'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category10/', accounts10.view_all_category10, name='view_all_category10'),
    path('create_new_category10/', accounts10.create_new_category10, name='create_new_category10'),
    path('regi_new_category10/', accounts10.regi_new_category10, name='regi_new_category10'),
    path('update_category10/<id>',accounts10.update_category10,name='update_category10'),

    path('delete_category10/<id>', accounts10.delete_category10, name='delete_category10'),
    path('view_all_category_delete10/', accounts10.view_all_category_delete10, name='view_all_category_delete10'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items10/', accounts10.view_all_items10, name='view_all_items10'),
    path('create_new_item10/', accounts10.create_new_item10, name='create_new_item10'),
    path('regi_new_item10/', accounts10.regi_new_item10, name='regi_new_item10'),
    path('delete_item10/<id>',accounts10.delete_item10,name='delete_item10'),
    path('update_item10/<id>', accounts10.update_item10, name='update_item10'),
    path('view_all_items_delete10/',accounts10.view_all_items_delete10,name='view_all_items_delete10'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger10/', accounts10.view_all_ledger10, name='view_all_ledger10'),
    path('create_new_ledger10/', accounts10.create_new_ledger10, name='create_new_ledger10'),
    path('regi_new_ledger10/', accounts10.regi_new_ledger10, name='regi_new_ledger10'),
    path('delete_ledger10/<id>',accounts10.delete_ledger10,name='delete_ledger10'),
    path('update_ledger10/<id>',accounts10.update_ledger10,name='update_ledger10'),
    path('view_all_ledger_delete10/',accounts10.view_all_ledger_delete10,name='view_all_ledger_delete10'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book10/', accounts10.view_all_accounts_book10, name='view_all_accounts_book10'),
    path('create_new_accounts_book10/', accounts10.create_new_accounts_book10, name='create_new_accounts_book10'),
    path('regi_new_accounts_book10/', accounts10.regi_new_accounts_book10, name='regi_new_accounts_book10'),
    path('update_accounts_book10/<id>',accounts10.update_accounts_book10,name='update_accounts_book10'),
    path('delete_accounts_book10/<id>',accounts10.delete_accounts_book10,name='delete_accounts_book10'),
    path('view_all_accounts_book_delete10/',accounts10.view_all_accounts_book_delete10,name='view_all_accounts_book_delete10'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries10/', accounts10.get_countries10, name='get_countries10'),

    path('in_exp_items_entry10/', accounts10.in_exp_items_entry10, name='in_exp_items_entry10'),
    path('reg_in_exp_items_entry10/', accounts10.reg_in_exp_items_entry10, name='reg_in_exp_items_entry10'),
    path('delete_journal10/<id>',accounts10.delete_journal10,name='delete_journal10'),
    path('update_in_exp_items_entry10/<id>',accounts10.update_in_exp_items_entry10,name='update_in_exp_items_entry10'),
    path('detailed_journal_report10/',accounts10.detailed_journal_report10,name='detailed_journal_report10'),
    path('journal_report_deleted10/',accounts10.journal_report_deleted10,name='journal_report_deleted10'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise10/', accounts10.daily_category_wise10, name='daily_category_wise10'),
    path('monthly_category_based_reports10/',accounts10.monthly_category_based_reports10,name='monthly_category_based_reports10'),
    path('yearly_category_based_reports10/', accounts10.yearly_category_based_reports10,name='yearly_category_based_reports10'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed10/', accounts10.daily_detailed10, name='daily_detailed10'),
    path('monthly_detailed10/',accounts10.monthly_detailed10,name='monthly_detailed10'),
    path('yearly_detailed10/',accounts10.yearly_detailed10,name='yearly_detailed10'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports10/', accounts10.item_based_reports10, name='item_based_reports10'),
    path('daily_item_based_reports10/',accounts10.daily_item_based_reports10,name='daily_item_based_reports10'),
    path('monthly_item_based_reports10/',accounts10.monthly_item_based_reports10,name='monthly_item_based_reports10'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports10/', accounts10.ledger_based_reports10, name='ledger_based_reports10'),
    path('monthly_ledger_based_reports10/', accounts10.monthly_ledger_based_reports10, name='monthly_ledger_based_reports10'),
    path('daily_ledger_based_reports10/',accounts10.daily_ledger_based_reports10,name='daily_ledger_based_reports10'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports10/', accounts10.accounts_book_based_reports10, name='accounts_book_based_reports10'),
    path('daily_accounts_book_based_reports10/',accounts10.daily_accounts_book_based_reports10,name='daily_accounts_book_based_reports10'),
    path('monthly_accounts_book_based_reports10/',accounts10.monthly_accounts_book_based_reports10,name='monthly_accounts_book_based_reports10'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months10/', accounts10.monthly_reports_choose_months10, name='monthly_reports_choose_months10'),
    path('monthly_detailed_daily_in_exp_items_report10/<mo>',accounts10.monthly_detailed_daily_in_exp_items_report10,name='monthly_detailed_daily_in_exp_items_report10'),

    path('single_monthly_reports_choose_months10/', accounts10.single_monthly_reports_choose_months10,name='single_monthly_reports_choose_months10'),
    path('single_monthly_daily_in_exp_items_report10/<mo>',accounts10.single_monthly_daily_in_exp_items_report10,name='single_monthly_daily_in_exp_items_report10'),

    path('accounts_dash_board_ob_ch10/',accounts10.accounts_dash_board_ob_ch10,name='accounts_dash_board_ob_ch10'),
    path('accounts_dash_board10/',accounts10.accounts_dash_board10,name='accounts_dash_board10'),

    path('profit_sharing_choose_months10', accounts10.profit_sharing_choose_months10,name='profit_sharing_choose_months10'),
    path('profit_sharing10/<mo>', accounts10.profit_sharing10, name='profit_sharing10'),
    path('view_share_holders10', accounts10.view_share_holders10, name='view_share_holders10'),
    path('create_share_holders10', accounts10.create_share_holders10, name='create_share_holders10'),
    path('regi_share_holders10', accounts10.regi_share_holders10, name='regi_share_holders10'),
    path('update_share_holders10/<id>', accounts10.update_share_holders10, name='update_share_holders10'),
    path('delete_share_holders10/<id>', accounts10.delete_share_holders10, name='delete_share_holders10'),
    path('view_deleted_share_holders10', accounts10.view_deleted_share_holders10, name='view_deleted_share_holders10'),


]

