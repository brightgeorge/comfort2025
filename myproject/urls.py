"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import myapp.userurls
import branch1app.b1userurls
import branch2app.b2userurls
import branch3app.b3userurls
import branch4app.b4userurls
import branch5app.b5userurls
import branch6app.b6userurls
import branch7app.b7userurls
import branch8app.b8userurls
import branch9app.b9userurls
import branch10app.b10userurls

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include(myapp.userurls)),
    path('br1/',include(branch1app.b1userurls)),
    path('br2/', include(branch2app.b2userurls)),
    path('br3/', include(branch3app.b3userurls)),
    path('br4/', include(branch4app.b4userurls)),
    path('br5/', include(branch5app.b5userurls)),
    path('br6/', include(branch6app.b6userurls)),
    path('br7/', include(branch7app.b7userurls)),
    path('br8/', include(branch8app.b8userurls)),
    path('br9/', include(branch9app.b9userurls)),
    path('br10/', include(branch10app.b10userurls)),

]
