from django.shortcuts import render
from django.contrib import messages


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


######TOTAL COLLECTION START HERE

def total_collection_details(request):
    comfort1_total_collection = branch1app.admin_dashboard_calculations_br1.grand_total_collection()
    comfort2_total_collection = branch2app.admin_dashboard_calculations_br2.grand_total_collection()
    comfort3_total_collection = branch3app.admin_dashboard_calculations_br3.grand_total_collection()
    comfort4_total_collection = branch4app.admin_dashboard_calculations_br4.grand_total_collection()
    comfort5_total_collection = branch5app.admin_dashboard_calculations_br5.grand_total_collection()
    comfort6_total_collection = branch6app.admin_dashboard_calculations_br6.grand_total_collection()
    comfort7_total_collection = branch7app.admin_dashboard_calculations_br7.grand_total_collection()

    prestige1_total_collection = branch21app.admin_dashboard_calculations_br21.grand_total_collection()
    prestige2_total_collection = branch22app.admin_dashboard_calculations_br22.grand_total_collection()
    prestige3_total_collection = branch23app.admin_dashboard_calculations_br23.grand_total_collection()
    prestige4_total_collection = branch24app.admin_dashboard_calculations_br24.grand_total_collection()

    perfect1_total_collection = branch31app.admin_dashboard_calculations_br31.grand_total_collection()
    perfect2_total_collection = branch32app.admin_dashboard_calculations_br32.grand_total_collection()
    perfect3_total_collection = branch33app.admin_dashboard_calculations_br33.grand_total_collection()
    perfect4_total_collection = branch34app.admin_dashboard_calculations_br34.grand_total_collection()

    happy_homes1_total_collection = branch41app.admin_dashboard_calculations_br41.grand_total_collection()
    happy_homes2_total_collection = branch42app.admin_dashboard_calculations_br42.grand_total_collection()

    comfort_ladies1_total_collection = branch51app.admin_dashboard_calculations_br51.grand_total_collection()
    comfort_ladies2_total_collection = branch52app.admin_dashboard_calculations_br52.grand_total_collection()

    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    comfort_total_collection = []
    comfort_total_collection.append(comfort1_total_collection[cm])
    comfort_total_collection.append(comfort2_total_collection[cm])
    comfort_total_collection.append(comfort3_total_collection[cm])
    comfort_total_collection.append(comfort4_total_collection[cm])
    comfort_total_collection.append(comfort5_total_collection[cm])
    comfort_total_collection.append(comfort6_total_collection[cm])
    comfort_total_collection.append(comfort7_total_collection[cm])

    prestige_total_collection = []
    prestige_total_collection.append(prestige1_total_collection[cm])
    prestige_total_collection.append(prestige2_total_collection[cm])
    prestige_total_collection.append(prestige3_total_collection[cm])
    prestige_total_collection.append(prestige4_total_collection[cm])

    perfect_total_collection = []
    perfect_total_collection.append(perfect1_total_collection[cm])
    perfect_total_collection.append(perfect2_total_collection[cm])
    perfect_total_collection.append(perfect3_total_collection[cm])
    perfect_total_collection.append(perfect4_total_collection[cm])

    happy_homes_total_collection = []
    happy_homes_total_collection.append(happy_homes1_total_collection[cm])
    happy_homes_total_collection.append(happy_homes2_total_collection[cm])

    comfort_ladies_total_collection = []
    comfort_ladies_total_collection.append(comfort_ladies1_total_collection[cm])
    comfort_ladies_total_collection.append(comfort_ladies2_total_collection[cm])

    comfort_total_collections = sum(comfort_total_collection)
    prestige_total_collections = sum(prestige_total_collection)
    perfect_total_collections = sum(perfect_total_collection)
    happy_homes_total_collections = sum(happy_homes_total_collection)
    comfort_ladies_total_collections = sum(comfort_ladies_total_collection)

    total_collection = comfort_total_collections + prestige_total_collections + perfect_total_collections + happy_homes_total_collections + comfort_ladies_total_collections
    print('this is total branch total_collection sum',total_collection)
    context = {
        'total_collection' : total_collection,
        'comfort_total_collection': comfort_total_collections,
        'prestige_total_collection': prestige_total_collections,
        'perfect_total_collection': perfect_total_collections,
        'happy_homes_total_collection': happy_homes_total_collections,
        'comfort_ladies_total_collection': comfort_ladies_total_collections,

    }
    return render(request,'admindashboard/total_collection_calculations/total_collection_calculations_details.html',context)
'''
def total_advance():
    a1 = admin_dashboard_calculations_br1.total_collection_advance()
    a2 = branch2app.admin_dashboard_calculations_br2.total_collection_advance()
    a3 = branch3app.admin_dashboard_calculations_br3.total_collection_advance()
    a4 = branch4app.admin_dashboard_calculations_br4.total_collection_advance()
    a5 = branch5app.admin_dashboard_calculations_br5.total_collection_advance()
    a6 = branch6app.admin_dashboard_calculations_br6.total_collection_advance()
    a7 = branch7app.admin_dashboard_calculations_br7.total_collection_advance()
    a8 = branch8app.admin_dashboard_calculations_br8.total_collection_advance()
    a9 = branch9app.admin_dashboard_calculations_br9.total_collection_advance()

    a10 = branch10app.admin_dashboard_calculations_br10.total_collection_advance()
    a11 = branch11app.admin_dashboard_calculations_br11.total_collection_advance()
    a12 = branch12app.admin_dashboard_calculations_br12.total_collection_advance()
    a13 = branch13app.admin_dashboard_calculations_br13.total_collection_advance()
    a14 = branch14app.admin_dashboard_calculations_br14.total_collection_advance()

    a15 = branch15app.admin_dashboard_calculations_br15.total_collection_advance()
    a16 = branch16app.admin_dashboard_calculations_br16.total_collection_advance()

    l = []
    l.append(a1)
    l.append(a2)
    l.append(a3)
    l.append(a4)
    l.append(a5)
    l.append(a6)
    l.append(a7)
    l.append(a8)
    l.append(a9)

    l.append(a10)
    l.append(a11)
    l.append(a12)
    l.append(a13)
    l.append(a14)

    l.append(a15)
    l.append(a16)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

def total_discount():
    a1 = admin_dashboard_calculations_br1.total_discount()
    a2 = branch2app.admin_dashboard_calculations_br2.total_discount()
    a3 = branch3app.admin_dashboard_calculations_br3.total_discount()
    a4 = branch4app.admin_dashboard_calculations_br4.total_discount()
    a5 = branch5app.admin_dashboard_calculations_br5.total_discount()
    a6 = branch6app.admin_dashboard_calculations_br6.total_discount()
    a7 = branch7app.admin_dashboard_calculations_br7.total_discount()
    a8 = branch8app.admin_dashboard_calculations_br8.total_discount()
    a9 = branch9app.admin_dashboard_calculations_br9.total_discount()

    a10 = branch10app.admin_dashboard_calculations_br10.total_discount()
    a11 = branch11app.admin_dashboard_calculations_br11.total_discount()
    a12 = branch12app.admin_dashboard_calculations_br12.total_discount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_discount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_discount()

    a15 = branch15app.admin_dashboard_calculations_br15.total_discount()
    a16 = branch16app.admin_dashboard_calculations_br16.total_discount()

    l = []
    l.append(a1)
    l.append(a2)
    l.append(a3)
    l.append(a4)
    l.append(a5)
    l.append(a6)
    l.append(a7)
    l.append(a8)
    l.append(a9)

    l.append(a10)
    l.append(a11)
    l.append(a12)
    l.append(a13)
    l.append(a14)

    l.append(a15)
    l.append(a16)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

def all_total_collatable_amount():
    a1 = admin_dashboard_calculations_br1.total_colatable_amount()
    a2 = branch2app.admin_dashboard_calculations_br2.total_colatable_amount()
    a3 = branch3app.admin_dashboard_calculations_br3.total_colatable_amount()
    a4 = branch4app.admin_dashboard_calculations_br4.total_colatable_amount()
    a5 = branch5app.admin_dashboard_calculations_br5.total_colatable_amount()
    a6 = branch6app.admin_dashboard_calculations_br6.total_colatable_amount()
    a7 = branch7app.admin_dashboard_calculations_br7.total_colatable_amount()
    a8 = branch8app.admin_dashboard_calculations_br8.total_colatable_amount()
    a9 = branch9app.admin_dashboard_calculations_br9.total_colatable_amount()

    a10 = branch10app.admin_dashboard_calculations_br10.total_colatable_amount()
    a11 = branch11app.admin_dashboard_calculations_br11.total_colatable_amount()
    a12 = branch12app.admin_dashboard_calculations_br12.total_colatable_amount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_colatable_amount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_colatable_amount()

    a15 = branch15app.admin_dashboard_calculations_br15.total_colatable_amount()
    a16 = branch16app.admin_dashboard_calculations_br16.total_colatable_amount()

    l = []
    l.append(a1)
    l.append(a2)
    l.append(a3)
    l.append(a4)
    l.append(a5)
    l.append(a6)
    l.append(a7)
    l.append(a8)
    l.append(a9)

    l.append(a10)
    l.append(a11)
    l.append(a12)
    l.append(a13)
    l.append(a14)

    l.append(a15)
    l.append(a16)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

def all_total_collected_amount():
    a1 = admin_dashboard_calculations_br1.total_collected_amount()
    a2 = branch2app.admin_dashboard_calculations_br2.total_collected_amount()
    a3 = branch3app.admin_dashboard_calculations_br3.total_collected_amount()
    a4 = branch4app.admin_dashboard_calculations_br4.total_collected_amount()
    a5 = branch5app.admin_dashboard_calculations_br5.total_collected_amount()
    a6 = branch6app.admin_dashboard_calculations_br6.total_collected_amount()
    a7 = branch7app.admin_dashboard_calculations_br7.total_collected_amount()
    a8 = branch8app.admin_dashboard_calculations_br8.total_collected_amount()
    a9 = branch9app.admin_dashboard_calculations_br9.total_collected_amount()

    a10 = branch10app.admin_dashboard_calculations_br10.total_collected_amount()
    a11 = branch11app.admin_dashboard_calculations_br11.total_collected_amount()
    a12 = branch12app.admin_dashboard_calculations_br12.total_collected_amount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_collected_amount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_collected_amount()

    a15 = branch15app.admin_dashboard_calculations_br15.total_collected_amount()
    a16 = branch16app.admin_dashboard_calculations_br16.total_collected_amount()

    l = []
    l.append(a1)
    l.append(a2)
    l.append(a3)
    l.append(a4)
    l.append(a5)
    l.append(a6)
    l.append(a7)
    l.append(a8)
    l.append(a9)

    l.append(a10)
    l.append(a11)
    l.append(a12)
    l.append(a13)
    l.append(a14)

    l.append(a15)
    l.append(a16)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

def all_total_due():
    a1 = admin_dashboard_calculations_br1.total_due()
    a2 = branch2app.admin_dashboard_calculations_br2.total_due()
    a3 = branch3app.admin_dashboard_calculations_br3.total_due()
    a4 = branch4app.admin_dashboard_calculations_br4.total_due()
    a5 = branch5app.admin_dashboard_calculations_br5.total_due()
    a6 = branch6app.admin_dashboard_calculations_br6.total_due()
    a7 = branch7app.admin_dashboard_calculations_br7.total_due()
    a8 = branch8app.admin_dashboard_calculations_br8.total_due()
    a9 = branch9app.admin_dashboard_calculations_br9.total_due()

    a10 = branch10app.admin_dashboard_calculations_br10.total_due()
    a11 = branch11app.admin_dashboard_calculations_br11.total_due()
    a12 = branch12app.admin_dashboard_calculations_br12.total_due()
    a13 = branch13app.admin_dashboard_calculations_br13.total_due()
    a14 = branch14app.admin_dashboard_calculations_br14.total_due()

    a15 = branch15app.admin_dashboard_calculations_br15.total_due()
    a16 = branch16app.admin_dashboard_calculations_br16.total_due()

    l = []
    l.append(a1)
    l.append(a2)
    l.append(a3)
    l.append(a4)
    l.append(a5)
    l.append(a6)
    l.append(a7)
    l.append(a8)
    l.append(a9)

    l.append(a10)
    l.append(a11)
    l.append(a12)
    l.append(a13)
    l.append(a14)

    l.append(a15)
    l.append(a16)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

#*************************************
#####LIST OF TOTAL COLLECTION
#*************************************

def branchwise_total_collection(request):
    a1 = admin_dashboard_calculations_br1.grand_total_collection()
    a2 = branch2app.admin_dashboard_calculations_br2.grand_total_collection()
    a3 = branch3app.admin_dashboard_calculations_br3.grand_total_collection()
    a4 = branch4app.admin_dashboard_calculations_br4.grand_total_collection()
    a5 = branch5app.admin_dashboard_calculations_br5.grand_total_collection()
    a6 = branch6app.admin_dashboard_calculations_br6.grand_total_collection()
    a7 = branch7app.admin_dashboard_calculations_br7.grand_total_collection()
    a8 = branch8app.admin_dashboard_calculations_br8.grand_total_collection()
    a9 = branch9app.admin_dashboard_calculations_br9.grand_total_collection()

    a10 = branch10app.admin_dashboard_calculations_br10.grand_total_collection()
    a11 = branch11app.admin_dashboard_calculations_br11.grand_total_collection()
    a12 = branch12app.admin_dashboard_calculations_br12.grand_total_collection()
    a13 = branch13app.admin_dashboard_calculations_br13.grand_total_collection()
    a14 = branch14app.admin_dashboard_calculations_br14.grand_total_collection()

    a15 = branch15app.admin_dashboard_calculations_br15.grand_total_collection()
    a16 = branch16app.admin_dashboard_calculations_br16.grand_total_collection()

    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    list_total_gtc = []
    list_total_gtc.append(a1[cm])
    list_total_gtc.append(a2[cm])
    list_total_gtc.append(a3[cm])
    list_total_gtc.append(a4[cm])
    list_total_gtc.append(a5[cm])
    list_total_gtc.append(a6[cm])
    list_total_gtc.append(a7[cm])
    list_total_gtc.append(a8[cm])
    list_total_gtc.append(a9[cm])

    list_total_gtc.append(a10[cm])
    list_total_gtc.append(a11[cm])
    list_total_gtc.append(a12[cm])
    list_total_gtc.append(a13[cm])
    list_total_gtc.append(a14[cm])

    list_total_gtc.append(a15[cm])
    list_total_gtc.append(a16[cm])

#******list_total_advance

    a1 = admin_dashboard_calculations_br1.total_collection_advance()
    a2 = branch2app.admin_dashboard_calculations_br2.total_collection_advance()
    a3 = branch3app.admin_dashboard_calculations_br3.total_collection_advance()
    a4 = branch4app.admin_dashboard_calculations_br4.total_collection_advance()
    a5 = branch5app.admin_dashboard_calculations_br5.total_collection_advance()
    a6 = branch6app.admin_dashboard_calculations_br6.total_collection_advance()
    a7 = branch7app.admin_dashboard_calculations_br7.total_collection_advance()
    a8 = branch8app.admin_dashboard_calculations_br8.total_collection_advance()
    a9 = branch9app.admin_dashboard_calculations_br9.total_collection_advance()

    a10 = branch10app.admin_dashboard_calculations_br10.total_collection_advance()
    a11 = branch11app.admin_dashboard_calculations_br11.total_collection_advance()
    a12 = branch12app.admin_dashboard_calculations_br12.total_collection_advance()
    a13 = branch13app.admin_dashboard_calculations_br13.total_collection_advance()
    a14 = branch14app.admin_dashboard_calculations_br14.total_collection_advance()

    a15 = branch15app.admin_dashboard_calculations_br15.total_collection_advance()
    a16 = branch16app.admin_dashboard_calculations_br16.total_collection_advance()

    list_total_advance = []
    list_total_advance.append(a1)
    list_total_advance.append(a2)
    list_total_advance.append(a3)
    list_total_advance.append(a4)
    list_total_advance.append(a5)
    list_total_advance.append(a6)
    list_total_advance.append(a7)
    list_total_advance.append(a8)
    list_total_advance.append(a9)

    list_total_advance.append(a10)
    list_total_advance.append(a11)
    list_total_advance.append(a12)
    list_total_advance.append(a13)
    list_total_advance.append(a14)

    list_total_advance.append(a15)
    list_total_advance.append(a16)

#***********list_total_discount

    a1 = admin_dashboard_calculations_br1.total_discount()
    a2 = branch2app.admin_dashboard_calculations_br2.total_discount()
    a3 = branch3app.admin_dashboard_calculations_br3.total_discount()
    a4 = branch4app.admin_dashboard_calculations_br4.total_discount()
    a5 = branch5app.admin_dashboard_calculations_br5.total_discount()
    a6 = branch6app.admin_dashboard_calculations_br6.total_discount()
    a7 = branch7app.admin_dashboard_calculations_br7.total_discount()
    a8 = branch8app.admin_dashboard_calculations_br8.total_discount()
    a9 = branch9app.admin_dashboard_calculations_br9.total_discount()

    a10 = branch10app.admin_dashboard_calculations_br10.total_discount()
    a11 = branch11app.admin_dashboard_calculations_br11.total_discount()
    a12 = branch12app.admin_dashboard_calculations_br12.total_discount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_discount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_discount()

    a15 = branch15app.admin_dashboard_calculations_br15.total_discount()
    a16 = branch16app.admin_dashboard_calculations_br16.total_discount()

    total_discount = []
    total_discount.append(a1)
    total_discount.append(a2)
    total_discount.append(a3)
    total_discount.append(a4)
    total_discount.append(a5)
    total_discount.append(a6)
    total_discount.append(a7)
    total_discount.append(a8)
    total_discount.append(a9)

    total_discount.append(a10)
    total_discount.append(a11)
    total_discount.append(a12)
    total_discount.append(a13)
    total_discount.append(a14)

    total_discount.append(a15)
    total_discount.append(a16)


#******list_all_total_collatable_amount

    a1 = admin_dashboard_calculations_br1.total_colatable_amount()
    a2 = branch2app.admin_dashboard_calculations_br2.total_colatable_amount()
    a3 = branch3app.admin_dashboard_calculations_br3.total_colatable_amount()
    a4 = branch4app.admin_dashboard_calculations_br4.total_colatable_amount()
    a5 = branch5app.admin_dashboard_calculations_br5.total_colatable_amount()
    a6 = branch6app.admin_dashboard_calculations_br6.total_colatable_amount()
    a7 = branch7app.admin_dashboard_calculations_br7.total_colatable_amount()
    a8 = branch8app.admin_dashboard_calculations_br8.total_colatable_amount()
    a9 = branch9app.admin_dashboard_calculations_br9.total_colatable_amount()

    a10 = branch10app.admin_dashboard_calculations_br10.total_colatable_amount()
    a11 = branch11app.admin_dashboard_calculations_br11.total_colatable_amount()
    a12 = branch12app.admin_dashboard_calculations_br12.total_colatable_amount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_colatable_amount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_colatable_amount()

    a15 = branch15app.admin_dashboard_calculations_br15.total_colatable_amount()
    a16 = branch16app.admin_dashboard_calculations_br16.total_colatable_amount()

    total_colatable_amount = []
    total_colatable_amount.append(a1)
    total_colatable_amount.append(a2)
    total_colatable_amount.append(a3)
    total_colatable_amount.append(a4)
    total_colatable_amount.append(a5)
    total_colatable_amount.append(a6)
    total_colatable_amount.append(a7)
    total_colatable_amount.append(a8)
    total_colatable_amount.append(a9)

    total_colatable_amount.append(a10)
    total_colatable_amount.append(a11)
    total_colatable_amount.append(a12)
    total_colatable_amount.append(a13)
    total_colatable_amount.append(a14)

    total_colatable_amount.append(a15)
    total_colatable_amount.append(a16)

#*******list_all_total_collected_amount

    a1 = admin_dashboard_calculations_br1.total_collected_amount()
    a2 = branch2app.admin_dashboard_calculations_br2.total_collected_amount()
    a3 = branch3app.admin_dashboard_calculations_br3.total_collected_amount()
    a4 = branch4app.admin_dashboard_calculations_br4.total_collected_amount()
    a5 = branch5app.admin_dashboard_calculations_br5.total_collected_amount()
    a6 = branch6app.admin_dashboard_calculations_br6.total_collected_amount()
    a7 = branch7app.admin_dashboard_calculations_br7.total_collected_amount()
    a8 = branch8app.admin_dashboard_calculations_br8.total_collected_amount()
    a9 = branch9app.admin_dashboard_calculations_br9.total_collected_amount()

    a10 = branch10app.admin_dashboard_calculations_br10.total_collected_amount()
    a11 = branch11app.admin_dashboard_calculations_br11.total_collected_amount()
    a12 = branch12app.admin_dashboard_calculations_br12.total_collected_amount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_collected_amount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_collected_amount()

    a15 = branch15app.admin_dashboard_calculations_br15.total_collected_amount()
    a16 = branch16app.admin_dashboard_calculations_br16.total_collected_amount()

    total_collected_amount = []
    total_collected_amount.append(a1)
    total_collected_amount.append(a2)
    total_collected_amount.append(a3)
    total_collected_amount.append(a4)
    total_collected_amount.append(a5)
    total_collected_amount.append(a6)
    total_collected_amount.append(a7)
    total_collected_amount.append(a8)
    total_collected_amount.append(a9)

    total_collected_amount.append(a10)
    total_collected_amount.append(a11)
    total_collected_amount.append(a12)
    total_collected_amount.append(a13)
    total_collected_amount.append(a14)

    total_collected_amount.append(a15)
    total_collected_amount.append(a16)


#*****list_all_total_due

    a1 = admin_dashboard_calculations_br1.total_due()
    a2 = branch2app.admin_dashboard_calculations_br2.total_due()
    a3 = branch3app.admin_dashboard_calculations_br3.total_due()
    a4 = branch4app.admin_dashboard_calculations_br4.total_due()
    a5 = branch5app.admin_dashboard_calculations_br5.total_due()
    a6 = branch6app.admin_dashboard_calculations_br6.total_due()
    a7 = branch7app.admin_dashboard_calculations_br7.total_due()
    a8 = branch8app.admin_dashboard_calculations_br8.total_due()
    a9 = branch9app.admin_dashboard_calculations_br9.total_due()

    a10 = branch10app.admin_dashboard_calculations_br10.total_due()
    a11 = branch11app.admin_dashboard_calculations_br11.total_due()
    a12 = branch12app.admin_dashboard_calculations_br12.total_due()
    a13 = branch13app.admin_dashboard_calculations_br13.total_due()
    a14 = branch14app.admin_dashboard_calculations_br14.total_due()

    a15 = branch15app.admin_dashboard_calculations_br15.total_due()
    a16 = branch16app.admin_dashboard_calculations_br16.total_due()

    total_due = []
    total_due.append(a1)
    total_due.append(a2)
    total_due.append(a3)
    total_due.append(a4)
    total_due.append(a5)
    total_due.append(a6)
    total_due.append(a7)
    total_due.append(a8)
    total_due.append(a9)

    total_due.append(a10)
    total_due.append(a11)
    total_due.append(a12)
    total_due.append(a13)
    total_due.append(a14)

    total_due.append(a15)
    total_due.append(a16)


    context={
        'grand_total_collection':list_total_gtc,
        'total_collection_advance': list_total_advance,
        'total_discount': total_discount,

        'total_colatable_amount': total_colatable_amount,
        'total_collected_amount': total_collected_amount,
        'total_due': total_due
    }
    return render(request,'admindashboard/admin_dashboard_reports/branchwise_total_collection.html', context)


'''


######TOTAL COLLECTION END HERE

