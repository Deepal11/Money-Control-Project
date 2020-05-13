from django.shortcuts import render
from .models import BSE_Top_Gainers, NSE_Top_Gainers
from .models import BSE_Top_Losers, NSE_Top_Losers
from .models import Only_Buyers_BSE, Only_Buyers_NSE
from .models import Only_Sellers_BSE, Only_Sellers_NSE
from .models import Week_High_BSE, Week_High_NSE
from .models import Week_Low_BSE, Week_Low_NSE
from .models import Price_Shockers_BSE, Price_Shockers_NSE
from .models import Volume_Shockers_BSE, Volume_Shockers_NSE

# Create your views here.

def home(request):
    obj1 = BSE_Top_Gainers.objects.all().order_by('-perc_gain')[:5]
    obj2 = NSE_Top_Gainers.objects.all().order_by('-perc_gain')[:5]
    obj3 = BSE_Top_Losers.objects.all().order_by('perc_loss')[:5]
    obj4 = NSE_Top_Losers.objects.all().order_by('perc_loss')[:5]
    obj5 = Only_Buyers_BSE.objects.all().order_by('-perc_chng')[:5]
    obj6 = Only_Buyers_NSE.objects.all().order_by('-perc_chng')[:5]
    obj7 = Only_Sellers_BSE.objects.all().order_by('perc_chng')[:5]
    obj8 = Only_Sellers_NSE.objects.all().order_by('perc_chng')[:5]
    obj9 = Week_High_BSE.objects.all().order_by('-perc_chng')[:5]
    obj10 = Week_High_NSE.objects.all().order_by('-perc_chng')[:5]
    obj11 = Week_Low_BSE.objects.all().order_by('perc_chng')[:5]
    obj12 = Week_Low_NSE.objects.all().order_by('perc_chng')[:5]
    obj13 = Price_Shockers_BSE.objects.all().order_by('-perc_chng')[:5]
    obj14 = Price_Shockers_NSE.objects.all().order_by('-perc_chng')[:5]
    obj15 = Volume_Shockers_BSE.objects.all().order_by('-perc_chng2')[:5]
    obj16 = Volume_Shockers_NSE.objects.all().order_by('-perc_chng2')[:5]
    d={'rec1':obj1,'rec2':obj2,'rec3':obj3,'rec4':obj4,'rec5':obj5,'rec6':obj6,'rec7':obj7,'rec8':obj8,
        'rec9':obj9,'rec10':obj10,'rec11':obj11,'rec12':obj12,'rec13':obj13,'rec14':obj14,'rec15':obj15,'rec16':obj16
    }
    return render(request,'home.html',context=d)

def viewmore1(request):
    obj1 = BSE_Top_Gainers.objects.all().order_by('-perc_gain')
    d = {'tb1': obj1} 
    return render(request,"ViewMore1.html",context=d)

def viewmore2(request):
    obj1 = NSE_Top_Gainers.objects.all().order_by('-perc_gain')
    d = {'tb1': obj1} 
    return render(request,"ViewMore2.html",context=d)

def viewmore3(request):
    obj1 = BSE_Top_Losers.objects.all().order_by('perc_loss')
    d = {'tb1': obj1} 
    return render(request,"ViewMore3.html",context=d)

def viewmore4(request):
    obj1 = NSE_Top_Losers.objects.all().order_by('perc_loss')
    d = {'tb1': obj1} 
    return render(request,"ViewMore4.html",context=d)

def viewmore5(request):
    obj1 = Only_Buyers_BSE.objects.all().order_by('-perc_chng')
    d = {'tb1': obj1} 
    return render(request,"ViewMore5.html",context=d)

def viewmore6(request):
    obj1 = Only_Buyers_NSE.objects.all().order_by('-perc_chng')
    d = {'tb1': obj1} 
    return render(request,"ViewMore6.html",context=d)

def viewmore7(request):
    obj1 = Only_Sellers_BSE.objects.all().order_by('perc_chng')
    d = {'tb1': obj1} 
    return render(request,"ViewMore7.html",context=d)

def viewmore8(request):
    obj1 = Only_Sellers_NSE.objects.all().order_by('perc_chng')
    d = {'tb1': obj1} 
    return render(request,"ViewMore8.html",context=d)

def viewmore9(request):
    obj1 = Week_High_BSE.objects.all().order_by('-perc_chng')
    d = {'tb1': obj1} 
    return render(request,"ViewMore9.html",context=d)

def viewmore10(request):
    obj1 = Week_High_NSE.objects.all().order_by('-perc_chng')
    d = {'tb1': obj1} 
    return render(request,"ViewMore10.html",context=d)

def viewmore11(request):
    obj1 = Week_Low_BSE.objects.all().order_by('perc_chng')
    d = {'tb1': obj1} 
    return render(request,"ViewMore11.html",context=d)

def viewmore12(request):
    obj1 = Week_Low_NSE.objects.all().order_by('perc_chng')
    d = {'tb1': obj1} 
    return render(request,"ViewMore12.html",context=d)

def viewmore13(request):
    obj1 = Price_Shockers_BSE.objects.all().order_by('-perc_chng')
    d = {'tb1': obj1} 
    return render(request,"ViewMore13.html",context=d)

def viewmore14(request):
    obj1 = Price_Shockers_NSE.objects.all().order_by('-perc_chng')
    d = {'tb1': obj1} 
    return render(request,"ViewMore14.html",context=d)

def viewmore15(request):
    obj1 = Volume_Shockers_BSE.objects.all().order_by('-perc_chng2')
    d = {'tb1': obj1} 
    return render(request,"ViewMore15.html",context=d)

def viewmore16(request):
    obj1 = Volume_Shockers_NSE.objects.all().order_by('-perc_chng2')
    d = {'tb1': obj1} 
    return render(request,"ViewMore16.html",context=d)