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