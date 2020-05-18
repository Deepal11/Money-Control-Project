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
    
def viewmore(request,id):
    obj1 = BSE_Top_Gainers.objects.all().order_by('-perc_gain')
    obj2 = NSE_Top_Gainers.objects.all().order_by('-perc_gain')
    obj3 = BSE_Top_Losers.objects.all().order_by('perc_loss')
    obj4 = NSE_Top_Losers.objects.all().order_by('perc_loss')
    obj5 = Only_Buyers_BSE.objects.all().order_by('-perc_chng')
    obj6 = Only_Buyers_NSE.objects.all().order_by('-perc_chng')
    obj7 = Only_Sellers_BSE.objects.all().order_by('perc_chng')
    obj8 = Only_Sellers_NSE.objects.all().order_by('perc_chng')
    obj9 = Week_High_BSE.objects.all().order_by('-perc_chng')
    obj10 = Week_High_NSE.objects.all().order_by('-perc_chng')
    obj11 = Week_Low_BSE.objects.all().order_by('perc_chng')
    obj12 = Week_Low_NSE.objects.all().order_by('perc_chng')
    obj13 = Price_Shockers_BSE.objects.all().order_by('-perc_chng')
    obj14 = Price_Shockers_NSE.objects.all().order_by('-perc_chng')
    obj15 = Volume_Shockers_BSE.objects.all().order_by('-perc_chng2')
    obj16 = Volume_Shockers_NSE.objects.all().order_by('-perc_chng2')
    if id==1:
        heading = 'BSE Top Gainers'
        header = ['Company Name','High','Low','Last Price','Prev Close','Change','% Gain']
        rows = []
        for i in obj1:
            rows.append([i.company_name,i.high,i.low,i.last_price,i.prev_close,i.change,i.perc_gain])
    elif id==2:
        heading = 'NSE Top Gainers'
        header = ['Company Name','High','Low','Last Price','Prev Close','Change','% Gain']
        rows = []
        for i in obj2:
            rows.append([i.company_name,i.high,i.low,i.last_price,i.prev_close,i.change,i.perc_gain])
    elif id==3:
        heading = 'BSE Top Losers'
        header = ['Company Name','High','Low','Last Price','Prev Close','Change','% Loss']
        rows = []
        for i in obj3:
            rows.append([i.company_name,i.high,i.low,i.last_price,i.prev_close,i.change,i.perc_loss])
    elif id==4:
        heading = 'NSE Top Losers'
        header = ['Company Name','High','Low','Last Price','Prev Close','Change','% Loss']
        rows = []
        for i in obj4:
            rows.append([i.company_name,i.high,i.low,i.last_price,i.prev_close,i.change,i.perc_loss])
    elif id==5:
        heading = 'Only Buyers - BSE'
        header = ['Company Name','Sector','Bid Qty','Last Price','Diff','% Chg']
        rows = []
        for i in obj5:
            rows.append([i.company_name,i.sector,i.bid_qty,i.last_price,i.diff,i.perc_chng])
    elif id==6:
        heading = 'Only Buyers - NSE'
        header = ['Company Name','Sector','Bid Qty','Last Price','Diff','% Chg']
        rows = []
        for i in obj6:
            rows.append([i.company_name,i.sector,i.bid_qty,i.last_price,i.diff,i.perc_chng])
    elif id==7:
        heading = 'Only Sellers - BSE'
        header = ['Company Name','Sector','Offer Qty','Last Price','Diff','% Chg']
        rows = []
        for i in obj7:
            rows.append([i.company_name,i.sector,i.offer_qty,i.last_price,i.diff,i.perc_chng])
    elif id==8:
        heading = 'Only Sellers - NSE'
        header = ['Company Name','Sector','Offer Qty','Last Price','Diff','% Chg']
        rows = []
        for i in obj8:
            rows.append([i.company_name,i.sector,i.offer_qty,i.last_price,i.diff,i.perc_chng])
    elif id==9:
        heading = '52 Week High - BSE'
        header = ['Company Name','Group',"Today's High","Today's Low",'Last Price','Chg','% Chg']
        rows = []
        for i in obj9:
            rows.append([i.company_name,i.group,i.todays_high,i.todays_low,i.last_price,i.chng,i.perc_chng])
    elif id==10:
        heading = '52 Week High - NSE'
        header = ['Company Name',"Today's High","Today's Low",'Last Price','Chg','% Chg']
        rows = []
        for i in obj10:
            rows.append([i.company_name,i.todays_high,i.todays_low,i.last_price,i.chng,i.perc_chng])
    elif id==11:
        heading = '52 Week Low - BSE'
        header = ['Company Name','Group',"Today's High","Today's Low",'Last Price','Chg','% Chg']
        rows = []
        for i in obj11:
            rows.append([i.company_name,i.group,i.todays_high,i.todays_low,i.last_price,i.chng,i.perc_chng])
    elif id==12:
        heading = '52 Week Low - NSE'
        header = ['Company Name',"Today's High","Today's Low",'Last Price','Chg','% Chg']
        rows = []
        for i in obj12:
            rows.append([i.company_name,i.todays_high,i.todays_low,i.last_price,i.chng,i.perc_chng])
    elif id==13:
        heading = 'Price Shockers - BSE'
        header = ['Company Name','Group','Sector','Current Price','Previous Price','% Chg']
        rows = []
        for i in obj13:
            rows.append([i.company_name,i.group,i.sector,i.current_price,i.previous_price,i.perc_chng])
    elif id==14:
        heading = 'Price Shockers - NSE'
        header = ['Company Name','Group','Sector','Current Price','Previous Price','% Chg']
        rows = []
        for i in obj14:
            rows.append([i.company_name,i.group,i.sector,i.current_price,i.previous_price,i.perc_chng])
    elif id==15:
        heading = 'Volume Shockers - BSE'
        header = ['Company Name','Group','Sector','Last Price','% Chg','Avg Volume','% Chg']
        rows = []
        for i in obj15:
            rows.append([i.company_name,i.group,i.sector,i.last_price,i.perc_chng1,i.avg_volume,i.perc_chng2])
    elif id==16:
        heading = 'Volume Shockers - NSE'
        header = ['Company Name','Group','Sector','Last Price','% Chg','Avg Volume','% Chg']
        rows = []
        for i in obj16:
            rows.append([i.company_name,i.group,i.sector,i.last_price,i.perc_chng1,i.avg_volume,i.perc_chng2])
    return render(request,"ViewMore.html",{'heading':heading,'header':header,'rows':rows})