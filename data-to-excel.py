#!/usr/bin/python
import numpy as np
import pandas as pd
import boto3
import xlsxwriter
filename=raw_input("Please enter file name:")
if filename:
   data=[]
   ec2=boto3.resource('ec2')
   for i in ec2.instances.all():
       data.append([i.id,i.state['Name'],i.private_ip_address])
   df=pd.DataFrame(data,columns=['id','state','ip'])
   writer=pd.ExcelWriter(filename+'.xlsx',engine='xlsxwriter')
   df.to_excel(writer, sheet_name='prod')
   writer.save()
else:
  print "enter genuine file name"
