from django.db import models

# Create your models here.
class BSE_Top_Gainers(models.Model):
    company_name = models.CharField(max_length=30)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    last_price = models.FloatField(default=0)
    prev_close = models.FloatField(default=0)
    change = models.FloatField(default=0)
    perc_gain = models.FloatField(default=0)

class NSE_Top_Gainers(models.Model):
    company_name = models.CharField(max_length=30)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    last_price = models.FloatField(default=0)
    prev_close = models.FloatField(default=0)
    change = models.FloatField(default=0)
    perc_gain = models.FloatField(default=0)

class BSE_Top_Losers(models.Model):
    company_name = models.CharField(max_length=30)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    last_price = models.FloatField(default=0)
    prev_close = models.FloatField(default=0)
    change = models.FloatField(default=0)
    perc_loss = models.FloatField(default=0)

class NSE_Top_Losers(models.Model):
    company_name = models.CharField(max_length=30)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    last_price = models.FloatField(default=0)
    prev_close = models.FloatField(default=0)
    change = models.FloatField(default=0)
    perc_loss = models.FloatField(default=0)

class Only_Buyers_BSE(models.Model):
    company_name = models.CharField(max_length=30)
    sector = models.CharField(max_length=50)
    bid_qty = models.IntegerField(default=0)
    last_price = models.FloatField(default=0)
    diff = models.FloatField(default=0)
    perc_chng = models.FloatField(default=0)

class Only_Buyers_NSE(models.Model):
    company_name = models.CharField(max_length=30)
    sector = models.CharField(max_length=50)
    bid_qty = models.IntegerField(default=0)
    last_price = models.FloatField(default=0)
    diff = models.FloatField(default=0)
    perc_chng = models.FloatField(default=0)

class Only_Sellers_BSE(models.Model):
    company_name = models.CharField(max_length=30)
    sector = models.CharField(max_length=50)
    offer_qty = models.IntegerField(default=0)
    last_price = models.FloatField(default=0)
    diff = models.FloatField(default=0)
    perc_chng = models.FloatField(default=0)

class Only_Sellers_NSE(models.Model):
    company_name = models.CharField(max_length=30)
    sector = models.CharField(max_length=50)
    offer_qty = models.IntegerField(default=0)
    last_price = models.FloatField(default=0)
    diff = models.FloatField(default=0)
    perc_chng = models.FloatField(default=0)

class Week_High_BSE(models.Model):
    company_name = models.CharField(max_length=30)
    group = models.CharField(max_length=2)
    todays_high = models.FloatField(default=0)
    todays_low = models.FloatField(default=0)
    last_price = models.FloatField(default=0)
    chng = models.FloatField(default=0)
    perc_chng = models.FloatField(default=0)

class Week_High_NSE(models.Model):
    company_name = models.CharField(max_length=30)
    todays_high = models.FloatField(default=0)
    todays_low = models.FloatField(default=0)
    last_price = models.FloatField(default=0)
    chng = models.FloatField(default=0)
    perc_chng = models.FloatField(default=0)

class Week_Low_BSE(models.Model):
    company_name = models.CharField(max_length=30)
    group = models.CharField(max_length=2)
    todays_high = models.FloatField(default=0)
    todays_low = models.FloatField(default=0)
    last_price = models.FloatField(default=0)
    chng = models.FloatField(default=0)
    perc_chng = models.FloatField(default=0)

class Week_Low_NSE(models.Model):
    company_name = models.CharField(max_length=30)
    todays_high = models.FloatField(default=0)
    todays_low = models.FloatField(default=0)
    last_price = models.FloatField(default=0)
    chng = models.FloatField(default=0)
    perc_chng = models.FloatField(default=0)

class Price_Shockers_BSE(models.Model):
    company_name = models.CharField(max_length=30)
    group = models.CharField(max_length=2)
    sector = models.CharField(max_length=50)
    current_price = models.FloatField(default=0)
    previous_price = models.FloatField(default=0)
    perc_chng = models.FloatField(default=0)

class Price_Shockers_NSE(models.Model):
    company_name = models.CharField(max_length=30)
    group = models.CharField(max_length=2)
    sector = models.CharField(max_length=50)
    current_price = models.FloatField(default=0)
    previous_price = models.FloatField(default=0)
    perc_chng = models.FloatField(default=0)

class Volume_Shockers_BSE(models.Model):
    company_name = models.CharField(max_length=30)
    group = models.CharField(max_length=2)
    sector = models.CharField(max_length=50)
    last_price = models.FloatField(default=0)
    perc_chng1 = models.FloatField(default=0)
    avg_volume = models.IntegerField(default=0)
    perc_chng2 = models.IntegerField(default=0)

class Volume_Shockers_NSE(models.Model):
    company_name = models.CharField(max_length=30)
    group = models.CharField(max_length=2)
    sector = models.CharField(max_length=50)
    last_price = models.FloatField(default=0)
    perc_chng1 = models.FloatField(default=0)
    avg_volume = models.IntegerField(default=0)
    perc_chng2 = models.IntegerField(default=0)