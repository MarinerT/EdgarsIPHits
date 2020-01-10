#!/usr/bin/env python

import pandas as pd
import ipaddress
import numpy as np
import pandasql as ps

def pipeline(filename):
    df = pd.read_csv(filename,names = ['ip','date','time','zone','cik','accession','extention','code','size','idx','norefer','noagent','find','crawler','browser'])
    df['ip']= to_ipaddress(df['ip'])
    df['date'] = pd.to_datetime(df['date'])
    df['date'] = [date.date() for date in df['date']]
    return df[['ip', 'date','cik','accession']]

def to_ipaddress(arr): 
    arr = [np.char.replace(ip, ip[-3:],'000') for ip in arr]
    return [int(ipaddress.IPv4Address(x)) for x in arr]

def setupiptable(filename):
    df = pd.read_csv(filename)
    df.iloc[:,0] = df.iloc[:,0].apply(lambda x: int(ipaddress.IPv4Address(x)))
    df.iloc[:,1] = df.iloc[:,1].apply(lambda x: int(ipaddress.IPv4Address(x)))
    df.columns = ["from_ip","to_ip","code","country"]
    return df.drop(columns=['code'],axis=1)

df03 = pipeline('~/Documents/Data/output03.csv')
#df10 = pipeline('~/Documents/Data/output10.csv')
#df17 = pipeline('~/Documents/Data/output17.csv')
dfgeo = setupiptable('~/Downloads/IP2LOCATION-LITE-DB1.CSV')

sql1code = '''
    SELECT * 
    FROM df03, dfgeo
    WHERE ip BETWEEN from_ip AND to_ip
'''
newdf03 = ps.sqldf(sql1code, locals()).drop(columns=['from_ip','to_ip'])


sql2code = '''
    SELECT * 
    FROM df10, dfgeo
    WHERE ip BETWEEN from_ip AND to_ip
'''
#newdf10 = ps.sqldf(sql2code, locals()).drop(columns=['from_ip','to_ip'])

sql3code = '''
    SELECT * 
    FROM df17, dfgeo
    WHERE ip BETWEEN from_ip AND to_ip
'''
#newdf17 = ps.sqldf(sql3code, locals()).drop(columns=['from_ip','to_ip'])

newdf03.to_csv(r'~/Documents/Data/newdf17_saved.csv')
#newdf10.to_csvr(r'~/Documents/Data/newdf10_saved.csv')
#newdf17.to_csvr(r'~/Documents/Data/newdf17_saved.csv')



