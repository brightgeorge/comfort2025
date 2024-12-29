#admin_branch_ob_ch23
import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

from branch23app.models import *
import datetime

#***branch1 rooms start here

def branch1_room_create_ob_ch23(request):
    if 'username' in request.session:

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,

        }
        return render(request,'branches/branch23/rooms/create_room.html',context)
    return render(request, 'index.html')

def branch1_room_create_regi_ob_ch23(request):
    if 'username' in request.session:
        if request.method == 'POST':
            chk_room_no = request.POST.get('roonno')
            chk_room = room_pg1.objects.all().filter(roon_no=chk_room_no).exists()
            if chk_room == True:

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'br': room_pg1.objects.all().order_by('roon_no'),

                }
                messages.info(request, 'BRANCH no already exists')
                return render(request, 'branches/branch23/rooms/view_all_rooms.html', context)
            else:
                room_no = request.POST.get('roonno')
                room_name = request.POST.get('roomname')
                share_type = request.POST.get('sharetype')
                ic=room_pg1()
                ic.roon_no = room_no
                ic.room_name = room_name
                ic.share_type = share_type
                ic.created_by = request.session['username']
                ic.save()

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'br' : room_pg1.objects.all().order_by('roon_no'),
                }
                messages.info(request, 'BRANCH room created sucessfully')
                return render(request,'branches/branch23/rooms/view_all_rooms.html',context)
    return render(request, 'index.html')












def multiple_branch1_room_create_regi23(request):
    if 'username' in request.session:
        if request.method == 'POST':
            chk_room_no = request.POST.get('roonno')
            chk_room = room_pg1.objects.all().filter(roon_no=chk_room_no).exists()
            if chk_room == True:

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'brname': 'BRANCH 23 Room Creation Form',
                    'br': room_pg1.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 23'
                }
                messages.info(request, 'BRANCH9 roon no already exists')
                return render(request, 'branches/branch23/rooms/view_all_rooms.html', context)
            else:
                rnum = [

                    '1',
                    '2',
                    '3',
                    '4',
                    '5',
                    '6',
                    '7',
                    '8',
                    '9',
                    '10',
                    '11',
                    '12',
                    '13',
                    '14',
                    '15',
                    '16',
                    '17',
                    '18',
                    '19',
                    '20',
                    '21',
                    '22',

                ]

                rnam = [

                    '1',
                    '2',
                    '3',
                    '4',
                    '5',
                    '6',
                    '7',
                    '8',
                    '9',
                    '10',
                    '11',
                    '12',
                    '13',
                    '14',
                    '15',
                    '16',
                    '17',
                    '18',
                    '19',
                    '20',
                    '21',
                    '22',

                ]

                styp = [

                    '2',
                    '4',
                    '3',
                    '2',
                    '4',
                    '4',
                    '4',
                    '4',
                    '3',
                    '4',
                    '4',
                    '4',
                    '4',
                    '4',
                    '2',
                    '4',
                    '4',
                    '4',
                    '4',
                    '4',
                    '2',
                    '4',

                ]

                print(len(rnum))
                print(len(rnam))
                print(len(styp))

                #room_no = request.POST.get('roonno')
                #room_name = request.POST.get('roomname')
                #share_type = request.POST.get('sharetype')

                for i in range(len(rnum)):
                    ic = room_pg1()
                    ic.roon_no = rnum[i]
                    ic.room_name = rnam[i]
                    ic.share_type = styp[i]
                    ic.created_by = request.session['username']
                    ic.save()

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'brname': 'BRANCH 23 Room Creation Form',
                    'br': room_pg1.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 23'
                }
                messages.info(request, 'BRANCH23 room created sucessfully')
                return render(request, 'branches/branch23/rooms/view_all_rooms.html', context)
    return render(request, 'index.html')













def view_all_room_ob_ch23(request):
    if 'username' in request.session:

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,

            'br': room_pg1.objects.all().order_by('roon_no').values(),
        }
        return render(request,'branches/branch23/rooms/view_all_rooms.html',context)
    return render(request,'index.html')

def delete_room_ob_ch23(request,id):
    if 'username' in request.session:
        dr = room_pg1.objects.get(id=id)
        dr.delete()

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,

            'br': room_pg1.objects.all().order_by('roon_no')
        }
        messages.info(request, 'BRANCH Room Updated sucessfully')
        return render(request, 'branches/branch23/rooms/view_all_rooms.html', context)
    return render(request, 'index.html')

#***branch1 rooms end here
#bed creation start here


def pg1_bed_create_ob_ch23(request):
    if 'username' in request.session:

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,

            'roomno' : room_pg1.objects.all(),
            'roomtype': set(room_pg1.objects.values_list('share_type')),
        }
        return render(request,'branches/branch23/beds/create_beds.html',context)
    return render(request, 'index.html')

def pg1_bed_create_regi_ob_ch23(request):
    if 'username' in request.session:
        if request.method == 'POST':

            chk_bed_no = request.POST.get('bedno')
            print('chk_bed_no', chk_bed_no)
            chk_room_no = request.POST.get('roomno')
            print('chk_room_no', chk_room_no)

            bd_code = chk_bed_no + chk_room_no
            int_bd_code = int(bd_code)
            chk_bd_code = pg1_new_beds.objects.all().filter(bed_code=int_bd_code).exists()

            if chk_bd_code == True:

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'br': pg1_new_beds.objects.all().order_by('roon_no'),
                }
                messages.info(request, ' Bed no Already Exists')
                return render(request, 'branches/branch23/beds/view_all_beds.html', context)
            else:
                room_no = request.POST.get('roomno')
                room_name = request.POST.get('roomname')
                bed_no = request.POST.get('bedno')
                room_type = request.POST.get('roomtype')

                c = 0
                for i in range(int(room_type)):
                    ic = pg1_new_beds()
                    ic.roon_no = room_no
                    ic.room_name = room_name
                    c = c + 1
                    ic.bed_no = c

                    ic.created_by = request.session['username']
                    ic.bed_code = int_bd_code
                    ic.share_type = room_type

                    ic.guest_code = 0

                    ic.jan_rent = 0
                    ic.jan_advance = 0
                    ic.jan_due_amt = 0
                    ic.jan_dis_amt = 0
                    ic.jan_rent_flag = 33

                    ic.feb_rent = 0
                    ic.feb_advance = 0
                    ic.feb_due_amt = 0
                    ic.feb_dis_amt = 0
                    ic.feb_rent_flag = 33

                    ic.march_rent = 0
                    ic.march_advance = 0
                    ic.march_due_amt = 0
                    ic.march_dis_amt = 0
                    ic.march_rent_flag = 33

                    ic.april_rent = 0
                    ic.april_advance = 0
                    ic.april_due_amt = 0
                    ic.april_dis_amt = 0
                    ic.april_rent_flag = 33

                    ic.may_rent = 0
                    ic.may_advance = 0
                    ic.may_due_amt = 0
                    ic.may_dis_amt = 0
                    ic.may_rent_flag = 33

                    ic.june_rent = 0
                    ic.june_advance = 0
                    ic.june_due_amt = 0
                    ic.june_dis_amt = 0
                    ic.june_rent_flag = 33

                    ic.july_rent = 0
                    ic.july_advance = 0
                    ic.july_due_amt = 0
                    ic.july_dis_amt = 0
                    ic.july_rent_flag = 33

                    ic.auguest_rent = 0
                    ic.auguest_advance = 0
                    ic.auguest_due_amt = 0
                    ic.auguest_dis_amt = 0
                    ic.auguest_rent_flag = 33

                    ic.sept_rent = 0
                    ic.sept_advance = 0
                    ic.sept_due_amt = 0
                    ic.sept_dis_amt = 0
                    ic.sept_rent_flag = 33

                    ic.october_rent = 0
                    ic.october_advance = 0
                    ic.october_due_amt = 0
                    ic.october_dis_amt = 0
                    ic.october_rent_flag = 33

                    ic.nov_rent = 0
                    ic.nov_advance = 0
                    ic.nov_due_amt = 0
                    ic.nov_dis_amt = 0
                    ic.nov_rent_flag = 33

                    ic.dec_rent = 0
                    ic.dec_advance = 0
                    ic.dec_due_amt = 0
                    ic.dec_dis_amt = 0
                    ic.dec_rent_flag = 33

                    ic.flag = 1

                    ic.save()

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'brname': ' Room Creation Form',
                    'br': pg1_new_beds.objects.all().order_by('roon_no'),
                }
                messages.info(request, ' Room Created Sucessfully')
                return render(request, 'branches/branch23/beds/view_all_beds.html', context)
    return render(request, 'index.html')




def single_pg1_bed_create_regi_ob_ch23(request):
    if 'username' in request.session:
        if request.method == 'POST':

            chk_bed_no = request.POST.get('bedno')
            print('chk_bed_no', chk_bed_no)
            chk_room_no = request.POST.get('roomno')
            print('chk_room_no', chk_room_no)

            bd_code = chk_bed_no + chk_room_no
            int_bd_code = int(bd_code)
            chk_bd_code = pg1_new_beds.objects.all().filter(bed_code=int_bd_code).exists()

            if chk_bd_code == True:

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'brname': ' Room Creation Form',
                    'br': pg1_new_beds.objects.all().order_by('roon_no'),
                }
                messages.info(request, ' Bed no Already Exists')
                return render(request, 'branches/branch23/beds/view_all_beds.html', context)
            else:
                room_no = request.POST.get('roomno')
                room_name = request.POST.get('roomname')
                bed_no = request.POST.get('bedno')
                room_type = request.POST.get('roomtype')

                ic = pg1_new_beds()
                ic.roon_no = room_no
                ic.room_name = room_name

                ic.bed_no = bed_no

                ic.created_by = request.session['username']
                ic.bed_code = int_bd_code
                ic.share_type = room_type

                ic.guest_code = 0
                ic.jan_rent = 0
                ic.jan_advance = 0
                ic.jan_due_amt = 0
                ic.jan_dis_amt = 0
                ic.jan_rent_flag = 33

                ic.feb_rent = 0
                ic.feb_advance = 0
                ic.feb_due_amt = 0
                ic.feb_dis_amt = 0
                ic.feb_rent_flag = 33

                ic.march_rent = 0
                ic.march_advance = 0
                ic.march_due_amt = 0
                ic.march_dis_amt = 0
                ic.march_rent_flag = 33

                ic.april_rent = 0
                ic.april_advance = 0
                ic.april_due_amt = 0
                ic.april_dis_amt = 0
                ic.april_rent_flag = 33

                ic.may_rent = 0
                ic.may_advance = 0
                ic.may_due_amt = 0
                ic.may_dis_amt = 0
                ic.may_rent_flag = 33

                ic.june_rent = 0
                ic.june_advance = 0
                ic.june_due_amt = 0
                ic.june_dis_amt = 0
                ic.june_rent_flag = 33

                ic.july_rent = 0
                ic.july_advance = 0
                ic.july_due_amt = 0
                ic.july_dis_amt = 0
                ic.july_rent_flag = 33

                ic.auguest_rent = 0
                ic.auguest_advance = 0
                ic.auguest_due_amt = 0
                ic.auguest_dis_amt = 0
                ic.auguest_rent_flag = 33

                ic.sept_rent = 0
                ic.sept_advance = 0
                ic.sept_due_amt = 0
                ic.sept_dis_amt = 0
                ic.sept_rent_flag = 33

                ic.october_rent = 0
                ic.october_advance = 0
                ic.october_due_amt = 0
                ic.october_dis_amt = 0
                ic.october_rent_flag = 33

                ic.nov_rent = 0
                ic.nov_advance = 0
                ic.nov_due_amt = 0
                ic.nov_dis_amt = 0
                ic.nov_rent_flag = 33

                ic.dec_rent = 0
                ic.dec_advance = 0
                ic.dec_due_amt = 0
                ic.dec_dis_amt = 0
                ic.dec_rent_flag = 33

                ic.flag = 1

                ic.save()

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
            a = []
            if bg == True:
                a.append(us)
            else:
                a.append('f')

            context = {
                'bg': bgs,
                'us': us,
                'th_us': a[0],
                'name': us,

                'brname': ' Room Creation Form',
                'br': pg1_new_beds.objects.all().order_by('roon_no'),
            }
            messages.info(request, ' Room Created Sucessfully')
            return render(request, 'branches/branch23/beds/view_all_beds.html', context)
    return render(request, 'index.html')











def multiple_single_pg1_bed_create_regi23(request):
    if 'username' in request.session:
        if request.method == 'POST':

            a = [

                '1',
                '1',
                '2',
                '2',
                '2',
                '2',
                '3',
                '3',
                '3',
                '4',
                '4',
                '5',
                '5',
                '5',
                '5',
                '6',
                '6',
                '6',
                '6',
                '7',
                '7',
                '7',
                '7',
                '8',
                '8',
                '8',
                '8',
                '9',
                '9',
                '9',
                '10',
                '10',
                '10',
                '10',
                '11',
                '11',
                '11',
                '11',
                '12',
                '12',
                '12',
                '12',
                '13',
                '13',
                '13',
                '13',
                '14',
                '14',
                '14',
                '14',
                '15',
                '15',
                '16',
                '16',
                '16',
                '16',
                '17',
                '17',
                '17',
                '17',
                '18',
                '18',
                '18',
                '18',
                '19',
                '19',
                '19',
                '19',
                '20',
                '20',
                '20',
                '20',
                '21',
                '21',
                '22',
                '22',
                '22',
                '22',

            ]

            b = [

                '1',
                '1',
                '2',
                '2',
                '2',
                '2',
                '3',
                '3',
                '3',
                '4',
                '4',
                '5',
                '5',
                '5',
                '5',
                '6',
                '6',
                '6',
                '6',
                '7',
                '7',
                '7',
                '7',
                '8',
                '8',
                '8',
                '8',
                '9',
                '9',
                '9',
                '10',
                '10',
                '10',
                '10',
                '11',
                '11',
                '11',
                '11',
                '12',
                '12',
                '12',
                '12',
                '13',
                '13',
                '13',
                '13',
                '14',
                '14',
                '14',
                '14',
                '15',
                '15',
                '16',
                '16',
                '16',
                '16',
                '17',
                '17',
                '17',
                '17',
                '18',
                '18',
                '18',
                '18',
                '19',
                '19',
                '19',
                '19',
                '20',
                '20',
                '20',
                '20',
                '21',
                '21',
                '22',
                '22',
                '22',
                '22',

            ]

            c = [

                '2',
                '2',
                '3',
                '3',
                '3',
                '4',
                '3',
                '3',
                '3',
                '2',
                '2',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '3',
                '3',
                '3',
                '4',
                '4',
                '4',
                '5',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '3',
                '3',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '3',
                '3',
                '4',
                '4',
                '4',
                '4',

            ]

            d = [

                '1',
                '2',
                '3',
                '5',
                '6',
                '4',
                '5',
                '6',
                '3',
                '1',
                '2',
                '1',
                '2',
                '4',
                '3',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '1',
                '3',
                '4',
                '5',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '8',
                '1',
                '2',
                '1',
                '2',
                '3',
                '4',

            ]

            print(len(a))
            print(len(b))
            print(len(c))
            print(len(d))

            for i in range(len(a)):

                #chk_bed_no = request.POST.get('bedno')
                chk_bed_no = d[i]
                print('chk_bed_no', chk_bed_no)
                #chk_room_no = request.POST.get('roomno')
                chk_room_no = a[i]
                print('chk_room_no', chk_room_no)

                bd_code = chk_bed_no + chk_room_no
                int_bd_code = int(bd_code)
                chk_bd_code = pg1_new_beds.objects.all().filter(bed_code=int_bd_code).exists()

                if chk_bd_code == True:

                    us = request.session['username']
                    bgs = background_color.objects.all().filter(username=us)
                    bg = background_color.objects.all().filter(username=us).exists()
                    a = []
                    if bg == True:
                        a.append(us)
                    else:
                        a.append('f')

                    context = {
                        'bg': bgs,
                        'us': us,
                        'th_us': a[0],
                        'name': us,

                        'brname': 'BRANCH THREE Room Creation Form',
                        'br': pg1_new_beds.objects.all().order_by('roon_no'),
                        'brname': 'BRANCH 23'
                    }
                    messages.info(request, 'BRANCH23 bed no already exists')
                    return render(request, 'branches/branch23/beds/view_all_beds.html', context)
                else:
                    room_no = a[i]
                    room_name = b[i]
                    bed_no = d[i]
                    room_type = c[i]

                    ic = pg1_new_beds()
                    ic.roon_no = room_no
                    ic.room_name = room_name

                    ic.bed_no = bed_no

                    ic.created_by = request.session['username']
                    ic.bed_code = int_bd_code
                    ic.share_type = room_type

                    ic.guest_code = 0
                    ic.jan_rent = 0
                    ic.jan_advance = 0
                    ic.jan_due_amt = 0
                    ic.jan_rent_flag = 33

                    ic.feb_rent = 0
                    ic.feb_advance = 0
                    ic.feb_due_amt = 0
                    ic.feb_rent_flag = 33

                    ic.march_rent = 0
                    ic.march_advance = 0
                    ic.march_due_amt = 0
                    ic.march_rent_flag = 33

                    ic.april_rent = 0
                    ic.april_advance = 0
                    ic.april_due_amt = 0
                    ic.april_rent_flag = 33

                    ic.may_rent = 0
                    ic.may_advance = 0
                    ic.may_due_amt = 0
                    ic.may_rent_flag = 33

                    ic.june_rent = 0
                    ic.june_advance = 0
                    ic.june_due_amt = 0
                    ic.june_rent_flag = 33

                    ic.july_rent = 0
                    ic.july_advance = 0
                    ic.july_due_amt = 0
                    ic.july_rent_flag = 33

                    ic.auguest_rent = 0
                    ic.auguest_advance = 0
                    ic.auguest_due_amt = 0
                    ic.auguest_rent_flag = 33

                    ic.sept_rent = 0
                    ic.sept_advance = 0
                    ic.sept_due_amt = 0
                    ic.sept_rent_flag = 33

                    ic.october_rent = 0
                    ic.october_advance = 0
                    ic.october_due_amt = 0
                    ic.october_rent_flag = 33

                    ic.nov_rent = 0
                    ic.nov_advance = 0
                    ic.nov_due_amt = 0
                    ic.nov_rent_flag = 33

                    ic.dec_rent = 0
                    ic.dec_advance = 0
                    ic.dec_due_amt = 0
                    ic.dec_rent_flag = 33

                    ic.flag = 1

                    ic.save()

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
            a = []
            if bg == True:
                a.append(us)
            else:
                a.append('f')

            context = {
                'bg': bgs,
                'us': us,
                'th_us': a[0],
                'name': us,

                'brname': 'BRANCH 23 Room Creation Form',
                'br': pg1_new_beds.objects.all().order_by('roon_no'),
                'brname': 'BRANCH 23'
            }
            messages.info(request, 'BRANCH23 room created sucessfully')
            return render(request, 'branches/branch23/beds/view_all_beds.html', context)
    return render(request, 'index.html')
















def pg1_view_all_beds_ob_ch23(request):
    if 'username' in request.session:

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,

            'br': pg1_new_beds.objects.all().order_by('roon_no')
        }
        return render(request,'branches/branch23/beds/view_all_beds.html',context)
    return render(request,'index.html')

def delete_bed_ob_ch23(request,id):
    if 'username' in request.session:
        dr = pg1_new_beds.objects.get(id=id)
        dr.delete()

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,

            'br': pg1_new_beds.objects.all().order_by('roon_no')
        }
        return render(request, 'branches/branch23/beds/view_all_beds.html', context)
    return render(request, 'index.html')

def update_bed_basic_details_ob_ch23(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            room_type = request.POST.get('roomtype')
            ic = pg1_new_beds.objects.get(id=id)
            ic.created_by = request.session['username']
            ic.share_type = room_type
            ic.save()

            nuph=pg1_new_beds.objects.all().filter(id=id)
            np=[]
            for i in nuph:
                np.append(i.self_mob)

            nc=pg1_new_guest.objects.get(self_mob=np[0])
            nc.created_by = request.session['username']
            nc.share_type = room_type
            nc.save()

            return pg1_view_all_beds_ob_ch23(request)

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,

            'br': pg1_new_beds.objects.all().order_by('roon_no'),
            'sd': pg1_new_beds.objects.get(id=id),
            'roomno': room_pg1.objects.all().values('share_type').distinct(),
        }
        messages.info(request, ' Room Created Sucessfully')
        return render(request, 'branches/branch23/beds/update_bed.html', context)
    return render(request,'index.html')


#bed creation end here

