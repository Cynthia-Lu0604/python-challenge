#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#he greatest decrease in losses (date and amount) over the entire period


# In[2]:


#import dependencies
import os
import csv


# In[3]:


#define variables
monthcount = 0
netprofitloss = 0
value = 0
change = 0
dates =[]
profits =[]


# In[4]:


#define path
bankdata = os.path.join ("budget_data.csv")

#read and store csv as csvfile
with open(bankdata) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    
#skip header 
    bankdataheader=next(csvreader)

#print(bankdataheader)

    first_row = next(csvreader)
    monthcount += 1
    netprofitloss += int(first_row[1])
    value = int(first_row[1])
    
    for row in csvreader: 
        #track dates
        dates.append(row[0])
        #calculate change and appending to corresponding datapoint
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        monthcount += 1
        
        netprofitloss = netprofitloss + int(row[1])
        
#print via f-strng
#print(f"Total Months: {str(monthcount)}")
#print(f"Total: ${str(netprofitloss)}")


# In[5]:


#calculate average change 
avgchange = sum(profits)/len(profits)
#print via f-string
#print(f"Average Change:${str(round(avgchange,2))}")


# In[6]:


#find the stock with the greatest profit
greatest_increase = max(profits)
#index/locate datapoint
greatest_index = profits.index(greatest_increase)
#identify corresponding date
greatest_date = dates[greatest_index]
#print via f-string
#print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")


# In[7]:


#find the stock with lowest profit
greatest_decrease = min(profits)
#index/locate datapoint
worst_index = profits.index(greatest_decrease)
#identify correspondiong datapoint
worst_date = dates[worst_index]
#print via f-string
#print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")    


# In[8]:


print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {str(monthcount)}")
print(f"Total: ${str(netprofitloss)}")
print(f"Average Change:${str(round(avgchange,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")    
print("------------------------------------")





