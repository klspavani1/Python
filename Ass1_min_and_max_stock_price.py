#Python program to find min and max stock prices

stock_prices={'Microsoft':215,
                'Facebook':250,
                'apple'   :440,
                'google'  :1470,
                'IBM'     :125,
                'Accenture':228,
                'Adobe'    :450,
                'Intel'    :50,
                'Oracle'   :50
}

l=[]#list containing company name with max and min prices
v=max(stock_prices.values())#maximum stock_price value
k=min(stock_prices.values())#minimum stock_price value
print("Maximum price:-",v)
print("Minimum price:-",k)
for key,value in stock_prices.items():
    if(value==v or value==k):
        l.append([key,value])
print("Max and Min prices along with companies", l)