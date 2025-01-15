from django.shortcuts import render
from django.contrib import messages
from myapp.models import *

import branch1app
import branch2app
import branch3app
import branch4app
import branch5app
import branch6app
import branch7app

import branch21app
import branch22app
import branch23app
import branch24app

import branch31app
import branch32app
import branch33app
import branch34app

import branch41app
import branch42app

import branch51app
import branch52app


def total_guest():
    tg=[]
    total_guest_br1 = branch1app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br1))
    total_guest_br2= branch2app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br5))
    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br7))

    total_guest_br21 = branch21app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br21))
    total_guest_br22 = branch22app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br22))
    total_guest_br23 = branch23app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br23))
    total_guest_br24 = branch24app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br24))

    total_guest_br31 = branch31app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br31))
    total_guest_br32 = branch32app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br32))
    total_guest_br33 = branch33app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br33))
    total_guest_br34 = branch34app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br34))

    total_guest_br41 = branch41app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br41))
    total_guest_br42 = branch42app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br42))

    total_guest_br51 = branch51app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br51))
    total_guest_br52 = branch52app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br52))

    return sum(tg)

def guest_details(request):
    context={
        'tot_guest' : total_guest(),
    }
    return render(request,'admindashboard/guest_details/guest_details.html',context)


def branchwise_guest_details(request):
    comfort=[]
    total_guest_br1 = branch1app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br1))
    total_guest_br2= branch2app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br5))
    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br7))

    prestige=[]
    total_guest_br21 = branch21app.models.pg1_new_beds.objects.all().filter(flag=2)
    prestige.append(len(total_guest_br21))
    total_guest_br22 = branch22app.models.pg1_new_beds.objects.all().filter(flag=2)
    prestige.append(len(total_guest_br22))
    total_guest_br23 = branch23app.models.pg1_new_beds.objects.all().filter(flag=2)
    prestige.append(len(total_guest_br23))
    total_guest_br24 = branch24app.models.pg1_new_beds.objects.all().filter(flag=2)
    prestige.append(len(total_guest_br24))

    perfect=[]
    total_guest_br31 = branch31app.models.pg1_new_beds.objects.all().filter(flag=2)
    perfect.append(len(total_guest_br31))
    total_guest_br32 = branch32app.models.pg1_new_beds.objects.all().filter(flag=2)
    perfect.append(len(total_guest_br32))
    total_guest_br33 = branch33app.models.pg1_new_beds.objects.all().filter(flag=2)
    perfect.append(len(total_guest_br33))
    total_guest_br34 = branch34app.models.pg1_new_beds.objects.all().filter(flag=2)
    perfect.append(len(total_guest_br34))

    happy_homes=[]
    total_guest_br41 = branch41app.models.pg1_new_beds.objects.all().filter(flag=2)
    happy_homes.append(len(total_guest_br41))
    total_guest_br42 = branch42app.models.pg1_new_beds.objects.all().filter(flag=2)
    happy_homes.append(len(total_guest_br42))

    comfort_ladies=[]
    total_guest_br51 = branch51app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort_ladies.append(len(total_guest_br51))
    total_guest_br52 = branch52app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort_ladies.append(len(total_guest_br52))

    context={
        'comfort' : comfort,
        'prestige' : prestige,
        'perfect' : perfect,
        'happy_homes' : happy_homes,
        'comfort_ladies' : comfort_ladies,

    }
    return render(request,'admindashboard/guest_details/branchwise_guest_details.html', context)