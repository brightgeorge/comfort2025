from django.shortcuts import render
from django.contrib import messages

from myapp.models import *


import datetime

# Create your views here.

def index(request):
    context={

    }
    return render(request,'index.html',context)

def login_request(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if login.objects.filter(username=username,password=password).exists():
            loginobj=login.objects.get(username=username,password=password)
            request.session['userid']=loginobj.id
            role=loginobj.role

            if role=='Admin':
                ul=[]
                teul=login.objects.all().filter(user_flage=1)
                ltuel=len(teul)

                tdul = login.objects.all().filter(user_flage=0)
                ltudl = len(tdul)

                ul.append(ltuel)
                ul.append(ltudl)


                request.session['username'] = username
                us = request.session['username']

                context={
                   'user':loginobj,
                    'name': us,
                    'yy':ul,
                    'active_user':ltuel,
                    'total_disableusers':ltudl,
                }
                return render(request,'admindashboard/adminindex.html',context)

            if role=='User':
                request.session['username'] = username
                us = request.session['username']
                import myapp
                #bgs = myapp.models.background_color.objects.all().filter(username=us)
                #bg = myapp.models.background_color.objects.all().filter(username=us).exists()
                #a = []
                #if bg == True:
                    #a.append(us)
                #else:
                    #a.append('f')

                context = {
                    #'bg': bgs,
                    #'us': us,
                    #'th_us': a[0],
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'user/userindex.html', context)

            if role == 'Branch1':
                request.session['username'] = username
                us = request.session['username']
                import branch1app
                bgs = branch1app.models.background_color.objects.all().filter(username=us)
                bg = branch1app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name': us
                }
                return render(request, 'branches/branch1/branch1index.html', context)


            if role == 'Branch2':
                request.session['username'] = username
                us = request.session['username']
                import branch2app
                bgs = branch2app.models.background_color.objects.all().filter(username=us)
                bg = branch2app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name': us
                }
                return render(request, 'branches/branch2/branch1index.html', context)


            if role == 'Branch3':
                request.session['username'] = username
                us = request.session['username']
                import branch3app
                bgs = branch3app.models.background_color.objects.all().filter(username=us)
                bg = branch3app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name': us
                }
                return render(request, 'branches/branch3/branch1index.html', context)


            if role == 'Branch4':
                request.session['username'] = username
                us = request.session['username']
                import branch4app
                bgs = branch4app.models.background_color.objects.all().filter(username=us)
                bg = branch4app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name': us
                }
                return render(request, 'branches/branch4/branch1index.html', context)


            if role == 'Branch5':
                request.session['username'] = username
                us = request.session['username']
                import branch5app
                bgs = branch5app.models.background_color.objects.all().filter(username=us)
                bg = branch5app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name': us
                }
                return render(request, 'branches/branch5/branch1index.html', context)


            if role == 'Branch6':
                request.session['username'] = username
                us = request.session['username']
                import branch6app
                bgs = branch6app.models.background_color.objects.all().filter(username=us)
                bg = branch6app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name': us
                }
                return render(request, 'branches/branch6/branch1index.html', context)

            if role == 'Branch7':
                request.session['username'] = username
                us = request.session['username']
                import branch7app
                bgs = branch7app.models.background_color.objects.all().filter(username=us)
                bg = branch7app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name': us
                }
                return render(request, 'branches/branch7/branch1index.html', context)

            if role == 'Branch21':
                request.session['username'] = username
                us = request.session['username']
                import branch21app
                bgs = branch21app.models.background_color.objects.all().filter(username=us)
                bg = branch21app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name': us
                }
                return render(request, 'branches/branch21/branch1index.html', context)

            if role == 'Branch22':
                request.session['username'] = username
                us = request.session['username']
                import branch22app
                bgs = branch22app.models.background_color.objects.all().filter(username=us)
                bg = branch22app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name': us
                }
                return render(request, 'branches/branch22/branch1index.html', context)

            if role == 'Branch23':
                request.session['username'] = username
                us = request.session['username']
                import branch23app
                bgs = branch23app.models.background_color.objects.all().filter(username=us)
                bg = branch23app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name': us
                }
                return render(request, 'branches/branch23/branch1index.html', context)

            if role == 'Branch24':
                request.session['username'] = username
                us = request.session['username']
                import branch24app
                bgs = branch24app.models.background_color.objects.all().filter(username=us)
                bg = branch24app.models.background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'user': loginobj,
                    'name': us
                }
                return render(request, 'branches/branch24/branch1index.html', context)













            else:
                return render(request,'index.html',context={'user':loginobj})
        else:
            return render(request,'index.html',context={'msg':'User Name or Password Incorrect'})
    else:
        return render(request,'index.html')


def admin_dashboard(request):
    ul = []
    teul = login.objects.all().filter(user_flage=1)
    ltuel = len(teul)

    tdul = login.objects.all().filter(user_flage=0)
    ltudl = len(tdul)

    ul.append(ltuel)
    ul.append(ltudl)

    us = request.session['username']

    context = {
        'name': us,
        'yy': ul,
        'active_user': ltuel,
        'total_disableusers': ltudl,


    }
    return render (request,'admindashboard/adminindex.html',context)


def user_dashboard_old(request):
    us = request.session['username']


    context = {
        'name': us,
        'sp': manual_datas.objects.all().filter(flag=2,head='speed'),
        'len': manual_datas.objects.all().filter(flag=2, head_order="1"),
        'we': manual_datas.objects.all().filter(flag=2, head_order="2"),

        'fsp' : mcalc.speed(),
        'plc_re' : mcalc.refresh_plc_regi(),


    }
    return render (request,'user/userindex.html',context)

#************USER SECTION STARTED HERE ***************

def view_all_users(request):
    if 'username' in request.session:
        vu=login.objects.filter(user_flage=1)
        context={
            'users':vu
        }
        return render(request,'admindashboard/users/view_all_users.html',context)
    return render(request,'index.html')

def create_user(request):
    if 'username' in request.session:
        return render(request,'admindashboard/users/user_creation.html')
    return render(request, 'index.html')

def user_regi(request):
    itname = request.POST.get('username')
    chkitemname = login.objects.filter(username=itname).exists()
    print('this is m y test uname',chkitemname)
    empcod= request.POST.get('code')
    chkemcod= login.objects.filter(emp_id=empcod).exists()
    print('this is m y test user code', chkemcod)
    if chkitemname == True or chkemcod == True:
        if chkitemname == True and chkemcod == True:
            messages.info(request, 'User name and Employee Code both are already exists!. please try another one')
        if chkitemname == False and chkemcod == True:
            messages.info(request, 'Employee Code already exists!. please try another one')
        if chkitemname == True and chkemcod == False:
            messages.info(request, 'User name already exists!. please try another one')
        return render(request, 'admindashboard/users/user_creation.html', )
    else:
        if request.method == 'POST':
            ucode=request.POST.get('code')
            empname = request.POST.get('name')
            uname = request.POST.get('username')
            upass = request.POST.get('password')
            urole = request.POST.get('role')
            #empbranch = request.POST.get('branch')

            udes = request.POST.get('description')
            fl = request.POST.get('eanable_disable')
            chk = 11
            if fl == None:
                chk = 0
            else:
                chk = 1
            uc=login()
            uc.emp_id = ucode
            uc.emp_name = empname
            uc.username = uname
            uc.password = upass
            uc.role = urole
            #uc.emp_branch=empbranch

            uc.emp_description=udes
            uc.user_flage = chk
            uc.save()

    messages.info(request,'user created sucessfully')
    context = {
        'users': login.objects.filter(user_flage=1),
    }
    return render(request,'admindashboard/users/view_all_users.html',context)

def delete_user(request,id):
    if 'username' in request.session:
        de=login.objects.get(id=id)
        de.delete()
        messages.info(request, 'user deleted sucessfully')
        vu = login.objects.all()
        context = {
            'users': login.objects.filter(user_flage=1),
            'users': vu
        }
        return render(request, 'admindashboard/users/view_all_users.html', context)
    return render(request, 'index.html')

def user_update(request,id):
    if request.method == 'POST':
        ucode = request.POST.get('code')
        empname = request.POST.get('name')
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        urole = request.POST.get('role')

        udes = request.POST.get('description')
        fl = request.POST.get('eanable_disable')
        chk = 11
        if fl == None:
            chk = 0
        else:
            chk = 1
        uc = login.objects.get(id=id)
        uc.emp_id = ucode
        uc.emp_name = empname
        uc.username = uname
        uc.password = upass
        uc.role = urole

        uc.emp_description = udes
        uc.user_flage = chk
        uc.save()
        messages.info(request, 'user updated sucessfully')
        return view_all_users(request)

    context = {
        'users': login.objects.filter(user_flage=1),
        'sd': login.objects.get(id=id),
    }
    return render(request,'admindashboard/users/update_user.html',context)

#************USER SECTION END HERE ***************



#logout
def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return render(request,'index.html')