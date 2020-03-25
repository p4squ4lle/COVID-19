#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import csv
import datetime as dt


wd = ('/home/pasinger/Wolke/coding/COVID-19/csse_covid_19_data/'
      'csse_covid_19_time_series/')
conf_filen = 'time_series_covid19_confirmed_global.csv'
death_filen = 'time_series_covid19_deaths_global.csv'

country = 'global'

with open(wd + conf_filen, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    
    first_row = next(csv_reader)
    dates = first_row[4:]
    x = [dt.datetime.strptime(d,'%m/%d/%y').date() for d in dates]
    
    if country == 'global':
        conf = [0] * len(dates)
        for row in csv_reader:
            for i in range(len(dates)):
                conf[i] += int(row[4+i])
    
    else:   
        for row in csv_reader:
            if row[1] == country:
                conf = [int(i) for i in row[4:]]
                break
            else:
                continue
            
with open(wd + death_filen, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    
    if country == 'global':
        death = [0] * len(dates)
        for row in csv_reader:
            for i in range(len(dates)):
                death[i] += int(row[4+i])
    
    else:
        for row in csv_reader:
            if row[1] == country:
                death = [int(i) for i in row[4:]]
                break
            else:
                continue
            
#%%
plt.close('all')            
plt.figure('cases')
plt.plot(x, conf, label='confirmed (latest =' + str(conf[-1]) + ')')
plt.plot(x, death, label='deaths (latest =' + str(death[-1]) + ')')
#plt.yscale('log')
plt.gcf().autofmt_xdate()
plt.legend()
plt.show()

#%%

plt.figure('rel deaths')
plt.plot(x[9:], [death[i+9]/conf[i+9] for i in range(len(conf)-9)])
plt.gcf().autofmt_xdate()
plt.show()

#%%

plt.figure('abs. zunahme pro tag')
plt.plot(x[1:], [conf[i+1]-conf[i] for i in range(len(conf)-1)])
plt.gcf().autofmt_xdate()
plt.show()

#%%
plt.figure('rel. zunahme pro tag')
plt.plot(x[10:], [(conf[i+10]-conf[i+9])/conf[i+10] 
                  for i in range(len(conf)-10)])
plt.gcf().autofmt_xdate()
plt.show()