#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import csv


# In[4]:


csvpath = os.path.join("Resources","budget_data.csv")


# In[12]:


with open(csvpath, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader: 
        print(','.join(row))


# In[13]:


month_yr=[]
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  
    for row in csvreader:
        month_yr.append(row[0])


# In[14]:


print(month_yr)


# In[15]:


from collections import Counter
month_yr = ['Jan-2010', 'Feb-2010', 'Mar-2010', 'Apr-2010', 'May-2010', 'Jun-2010', 'Jul-2010', 'Aug-2010', 'Sep-2010', 'Oct-2010', 'Nov-2010', 'Dec-2010', 'Jan-2011', 'Feb-2011', 'Mar-2011', 'Apr-2011', 'May-2011', 'Jun-2011', 'Jul-2011', 'Aug-2011', 'Sep-2011', 'Oct-2011', 'Nov-2011', 'Dec-2011', 'Jan-2012', 'Feb-2012', 'Mar-2012', 'Apr-2012', 'May-2012', 'Jun-2012', 'Jul-2012', 'Aug-2012', 'Sep-2012', 'Oct-2012', 'Nov-2012', 'Dec-2012', 'Jan-2013', 'Feb-2013', 'Mar-2013', 'Apr-2013', 'May-2013', 'Jun-2013', 'Jul-2013', 'Aug-2013', 'Sep-2013', 'Oct-2013', 'Nov-2013', 'Dec-2013', 'Jan-2014', 'Feb-2014', 'Mar-2014', 'Apr-2014', 'May-2014', 'Jun-2014', 'Jul-2014', 'Aug-2014', 'Sep-2014', 'Oct-2014', 'Nov-2014', 'Dec-2014', 'Jan-2015', 'Feb-2015', 'Mar-2015', 'Apr-2015', 'May-2015', 'Jun-2015', 'Jul-2015', 'Aug-2015', 'Sep-2015', 'Oct-2015', 'Nov-2015', 'Dec-2015', 'Jan-2016', 'Feb-2016', 'Mar-2016', 'Apr-2016', 'May-2016', 'Jun-2016', 'Jul-2016', 'Aug-2016', 'Sep-2016', 'Oct-2016', 'Nov-2016', 'Dec-2016', 'Jan-2017', 'Feb-2017']
Counter(month_yr)


# In[16]:


month_yr = ['Jan-2010', 'Feb-2010', 'Mar-2010', 'Apr-2010', 'May-2010', 'Jun-2010', 'Jul-2010', 'Aug-2010', 'Sep-2010', 'Oct-2010', 'Nov-2010', 'Dec-2010', 'Jan-2011', 'Feb-2011', 'Mar-2011', 'Apr-2011', 'May-2011', 'Jun-2011', 'Jul-2011', 'Aug-2011', 'Sep-2011', 'Oct-2011', 'Nov-2011', 'Dec-2011', 'Jan-2012', 'Feb-2012', 'Mar-2012', 'Apr-2012', 'May-2012', 'Jun-2012', 'Jul-2012', 'Aug-2012', 'Sep-2012', 'Oct-2012', 'Nov-2012', 'Dec-2012', 'Jan-2013', 'Feb-2013', 'Mar-2013', 'Apr-2013', 'May-2013', 'Jun-2013', 'Jul-2013', 'Aug-2013', 'Sep-2013', 'Oct-2013', 'Nov-2013', 'Dec-2013', 'Jan-2014', 'Feb-2014', 'Mar-2014', 'Apr-2014', 'May-2014', 'Jun-2014', 'Jul-2014', 'Aug-2014', 'Sep-2014', 'Oct-2014', 'Nov-2014', 'Dec-2014', 'Jan-2015', 'Feb-2015', 'Mar-2015', 'Apr-2015', 'May-2015', 'Jun-2015', 'Jul-2015', 'Aug-2015', 'Sep-2015', 'Oct-2015', 'Nov-2015', 'Dec-2015', 'Jan-2016', 'Feb-2016', 'Mar-2016', 'Apr-2016', 'May-2016', 'Jun-2016', 'Jul-2016', 'Aug-2016', 'Sep-2016', 'Oct-2016', 'Nov-2016', 'Dec-2016', 'Jan-2017', 'Feb-2017']
len(month_yr)


# In[18]:


profit_losses=[]
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) 
    for row in csvreader:
       profit_losses.append(row[1])


# In[19]:


print(profit_losses)


# In[29]:


profit_losses = ['867884', '984655', '322013', '-69417', '310503', '522857', '1033096', '604885', '-216386', '477532', '893810', '-80353', '779806', '-335203', '697845', '793163', '485070', '584122', '62729', '668179', '899906', '834719', '132003', '309978', '-755566', '1170593', '252788', '1151518', '817256', '570757', '506702', '-1022534', '475062', '779976', '144175', '542494', '359333', '321469', '67780', '471435', '565603', '872480', '789480', '999942', '-1196225', '268997', '-687986', '1150461', '682458', '617856', '824098', '581943', '132864', '448062', '689161', '800701', '1166643', '947333', '578668', '988505', '1139715', '1029471', '687533', '-524626', '158620', '87795', '423389', '840723', '568529', '332067', '989499', '778237', '650000', '-1100387', '-174946', '757143', '445709', '712961', '-1163797', '569899', '768450', '102685', '795914', '60988', '138230', '671099']
for i in range(len(profit_losses)):
    profit_losses[i]=int (profit_losses[i])


# In[30]:


sum(profit_losses)


# In[31]:


print(profit_losses)


# In[32]:


average_profit_losses= sum(profit_losses)/len(profit_losses)
print(average_profit_losses)


# In[33]:


import operator
profit_losses = [867884, 984655, 322013, -69417, 310503, 522857, 1033096, 604885, -216386, 477532, 893810, -80353, 779806, -335203, 697845, 793163, 485070, 584122, 62729, 668179, 899906, 834719, 132003, 309978, -755566, 1170593, 252788, 1151518, 817256, 570757, 506702, -1022534, 475062, 779976, 144175, 542494, 359333, 321469, 67780, 471435, 565603, 872480, 789480, 999942, -1196225, 268997, -687986, 1150461, 682458, 617856, 824098, 581943, 132864, 448062, 689161, 800701, 1166643, 947333, 578668, 988505, 1139715, 1029471, 687533, -524626, 158620, 87795, 423389, 840723, 568529, 332067, 989499, 778237, 650000, -1100387, -174946, 757143, 445709, 712961, -1163797, 569899, 768450, 102685, 795914, 60988, 138230, 671099]
change_profit = res = list(map(operator.sub, profit_lossess[1:], profit_lossess[:-1]))
print(change_profit)


# In[34]:


average_change_profits=sum(change_profit)/len(change_profit)
print(average_change_profits)


# In[64]:


max(change_profit)


# In[65]:


min(change_profit)


# In[35]:


month_yr = ['Jan-2010', 'Feb-2010', 'Mar-2010', 'Apr-2010', 'May-2010', 'Jun-2010', 'Jul-2010', 'Aug-2010', 'Sep-2010', 'Oct-2010', 'Nov-2010', 'Dec-2010', 'Jan-2011', 'Feb-2011', 'Mar-2011', 'Apr-2011', 'May-2011', 'Jun-2011', 'Jul-2011', 'Aug-2011', 'Sep-2011', 'Oct-2011', 'Nov-2011', 'Dec-2011', 'Jan-2012', 'Feb-2012', 'Mar-2012', 'Apr-2012', 'May-2012', 'Jun-2012', 'Jul-2012', 'Aug-2012', 'Sep-2012', 'Oct-2012', 'Nov-2012', 'Dec-2012', 'Jan-2013', 'Feb-2013', 'Mar-2013', 'Apr-2013', 'May-2013', 'Jun-2013', 'Jul-2013', 'Aug-2013', 'Sep-2013', 'Oct-2013', 'Nov-2013', 'Dec-2013', 'Jan-2014', 'Feb-2014', 'Mar-2014', 'Apr-2014', 'May-2014', 'Jun-2014', 'Jul-2014', 'Aug-2014', 'Sep-2014', 'Oct-2014', 'Nov-2014', 'Dec-2014', 'Jan-2015', 'Feb-2015', 'Mar-2015', 'Apr-2015', 'May-2015', 'Jun-2015', 'Jul-2015', 'Aug-2015', 'Sep-2015', 'Oct-2015', 'Nov-2015', 'Dec-2015', 'Jan-2016', 'Feb-2016', 'Mar-2016', 'Apr-2016', 'May-2016', 'Jun-2016', 'Jul-2016', 'Aug-2016', 'Sep-2016', 'Oct-2016', 'Nov-2016', 'Dec-2016', 'Jan-2017', 'Feb-2017']
profit_lossess = [867884, 984655, 322013, -69417, 310503, 522857, 1033096, 604885, -216386, 477532, 893810, -80353, 779806, -335203, 697845, 793163, 485070, 584122, 62729, 668179, 899906, 834719, 132003, 309978, -755566, 1170593, 252788, 1151518, 817256, 570757, 506702, -1022534, 475062, 779976, 144175, 542494, 359333, 321469, 67780, 471435, 565603, 872480, 789480, 999942, -1196225, 268997, -687986, 1150461, 682458, 617856, 824098, 581943, 132864, 448062, 689161, 800701, 1166643, 947333, 578668, 988505, 1139715, 1029471, 687533, -524626, 158620, 87795, 423389, 840723, 568529, 332067, 989499, 778237, 650000, -1100387, -174946, 757143, 445709, 712961, -1163797, 569899, 768450, 102685, 795914, 60988, 138230, 671099]
change_profit = [0,116771, -662642, -391430, 379920, 212354, 510239, -428211, -821271, 693918, 416278, -974163, 860159, -1115009, 1033048, 95318, -308093, 99052, -521393, 605450, 231727, -65187, -702716, 177975, -1065544, 1926159, -917805, 898730, -334262, -246499, -64055, -1529236, 1497596, 304914, -635801, 398319, -183161, -37864, -253689, 403655, 94168, 306877, -83000, 210462, -2196167, 1465222, -956983, 1838447, -468003, -64602, 206242, -242155, -449079, 315198, 241099, 111540, 365942, -219310, -368665, 409837, 151210, -110244, -341938, -1212159, 683246, -70825, 335594, 417334, -272194, -236462, 657432, -211262, -128237, -1750387, 925441, 932089, -311434, 267252, -1876758, 1733696, 198551, -665765, 693229, -734926, 77242, 532869]
[''.join(map(str, i)) for i in zip(month_yr, profit_lossess,change_profit)]


# In[43]:


month_yr = ['Jan-2010', 'Feb-2010', 'Mar-2010', 'Apr-2010', 'May-2010', 'Jun-2010', 'Jul-2010', 'Aug-2010', 'Sep-2010', 'Oct-2010', 'Nov-2010', 'Dec-2010', 'Jan-2011', 'Feb-2011', 'Mar-2011', 'Apr-2011', 'May-2011', 'Jun-2011', 'Jul-2011', 'Aug-2011', 'Sep-2011', 'Oct-2011', 'Nov-2011', 'Dec-2011', 'Jan-2012', 'Feb-2012', 'Mar-2012', 'Apr-2012', 'May-2012', 'Jun-2012', 'Jul-2012', 'Aug-2012', 'Sep-2012', 'Oct-2012', 'Nov-2012', 'Dec-2012', 'Jan-2013', 'Feb-2013', 'Mar-2013', 'Apr-2013', 'May-2013', 'Jun-2013', 'Jul-2013', 'Aug-2013', 'Sep-2013', 'Oct-2013', 'Nov-2013', 'Dec-2013', 'Jan-2014', 'Feb-2014', 'Mar-2014', 'Apr-2014', 'May-2014', 'Jun-2014', 'Jul-2014', 'Aug-2014', 'Sep-2014', 'Oct-2014', 'Nov-2014', 'Dec-2014', 'Jan-2015', 'Feb-2015', 'Mar-2015', 'Apr-2015', 'May-2015', 'Jun-2015', 'Jul-2015', 'Aug-2015', 'Sep-2015', 'Oct-2015', 'Nov-2015', 'Dec-2015', 'Jan-2016', 'Feb-2016', 'Mar-2016', 'Apr-2016', 'May-2016', 'Jun-2016', 'Jul-2016', 'Aug-2016', 'Sep-2016', 'Oct-2016', 'Nov-2016', 'Dec-2016', 'Jan-2017', 'Feb-2017']
length_month_yr= [len(month_yr)]


# In[75]:


lngth_mth_yr_str=str(length_month_yr)


# In[49]:


sum_profit_losses= [sum(profit_losses)]


# In[72]:


sum_prft_loss_str=str(sum_profit_losses)


# In[73]:


average_change_profits=[sum(change_profit)/len(change_profit)]
print(average_change_profits)


# In[74]:


avg_chng_prft_str=str(average_change_profits)


# In[60]:


mx_chng_prft=[max(change_profit)]
print(mx_chng_prft)


# In[70]:


mx_chng_prft_str=str(mx_chng_prft)


# In[64]:


lst_chng_prft=[min(change_profit)]
print(lst_chng_prft)


# In[69]:


lst_chng_prft_str=str(lst_chng_prft)


# In[146]:


Title= "Financial Analysis"
lngth_mth_yr_str=str(length_month_yr)
sum_prft_loss_str=str(sum_profit_losses)
avg_chng_prft_str=str(average_change_profits)
mx_chng_prft_str=str(mx_chng_prft)
lst_chng_prft_str=str(lst_chng_prft)
print(Title)
print(f"Total Months:" + " " + lngth_mth_yr_str)
print(f"Total:" + " " + "$"+ sum_prft_loss_str)
print(f"Average Change:" + " "+ "$"+ avg_chng_prft_str)
print(f"Greatest Increase in Profits:" + "Feb-2012" + " "+ "$"+ mx_chng_prft_str)
print(f"Greatest Decrease in Profits:"+ "Sept-2013" + " " + "$"+ lst_chng_prft_str)


# In[147]:


Total_Mnths=str("Total Months:" + " " + lngth_mth_yr_str)
Total=str("Total:" + " " + "$"+ sum_prft_loss_str)
Avg_chng=str("Average Change:" + " "+ "$"+ avg_chng_prft_str)
Grt_Inc=str("Greatest Increase in Profits:" + "Feb-2012" + " "+ "$"+ mx_chng_prft_str)
Grt_Dec=str("Greatest Decrease in Profits:"+ "Sept-2013" + " " + "$"+ lst_chng_prft_str)
Title=str(Title)
print(Total_Mnths)


# In[149]:


PyBankpath='PyBank.txt'
PyBank_file=open(PyBankpath, 'w')
PyBank_file.write(Title + '\n')
PyBank_file.write(Total_Mnths + '\n')
PyBank_file.write(Total + '\n')
PyBank_file.write(Avg_chng + '\n')
PyBank_file.write(Grt_Inc + '\n')
PyBank_file.write(Grt_Dec + '\n')


# In[ ]:




