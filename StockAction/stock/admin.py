from django.contrib import admin

# Register your models here.
from .models import BSE_Top_Gainers, NSE_Top_Gainers
from .models import BSE_Top_Losers, NSE_Top_Losers
from .models import Only_Buyers_BSE, Only_Buyers_NSE
from .models import Only_Sellers_BSE, Only_Sellers_NSE
from .models import Week_High_BSE, Week_High_NSE
from .models import Week_Low_BSE, Week_Low_NSE
from .models import Price_Shockers_BSE, Price_Shockers_NSE
from .models import Volume_Shockers_BSE, Volume_Shockers_NSE

admin.site.register(BSE_Top_Gainers)
admin.site.register(NSE_Top_Gainers)
admin.site.register(BSE_Top_Losers)
admin.site.register(NSE_Top_Losers)
admin.site.register(Only_Buyers_BSE)
admin.site.register(Only_Buyers_NSE)
admin.site.register(Only_Sellers_BSE)
admin.site.register(Only_Sellers_NSE)
admin.site.register(Week_High_BSE)
admin.site.register(Week_High_NSE)
admin.site.register(Week_Low_BSE)
admin.site.register(Week_Low_NSE)
admin.site.register(Price_Shockers_BSE)
admin.site.register(Price_Shockers_NSE)
admin.site.register(Volume_Shockers_BSE)
admin.site.register(Volume_Shockers_NSE)
