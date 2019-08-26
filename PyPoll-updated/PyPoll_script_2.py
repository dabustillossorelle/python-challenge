#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import csv


# In[ ]:


PyPollpath = os.path.join("Resources","election_data.csv")


# In[ ]:


with open(PyPollpath, "r", newline="") as PyPollfile:
    PyPollreader = csv.reader(PyPollfile, delimiter=",")
#     for row in PyPollreader: 
#         print(','.join(row))


# In[ ]:


voter_id=[]
with open(PyPollpath, "r") as PyPollfile:
    PyPollreader = csv.reader(PyPollfile, delimiter=",")
    next(PyPollreader)  
    for row in PyPollreader:
        voter_id.append(row[0])


# In[ ]:


print(voter_id)


# In[ ]:


total_votes=len(voter_id)
print(total_votes)


# In[ ]:


candidate=[]
with open(PyPollpath, "r") as PyPollfile:
    PyPollreader = csv.reader(PyPollfile, delimiter=",")
    next(PyPollreader) 
    for row in PyPollreader:
       candidate.append(row[2])


# In[ ]:


print(candidate)


# In[ ]:


from collections import Counter
number_votes=Counter(candidate)


# In[ ]:


print(number_votes)


# In[ ]:


dict(number_votes)


# In[ ]:


votes_per_cand=dict(number_votes)


# In[ ]:


print(votes_per_cand)


# In[ ]:


Khan_tot=votes_per_cand["Khan"]
print(Khan_tot)


# In[ ]:


Khan_per=((Khan_tot/total_votes)*100)
print(Khan_per)


# In[ ]:


Correy_tot=votes_per_cand["Correy"]
print(Correy_tot)


# In[ ]:


Correy_per=((Correy_tot/total_votes)*100)
print(Correy_per)


# In[ ]:


Li_tot=votes_per_cand["Li"]
print(Li_tot)


# In[ ]:


Li_per=((Li_tot/total_votes)*100)
print(Li_per)


# In[ ]:


O_tot=votes_per_cand["O'Tooley"]
print(O_tot)


# In[ ]:


O_per=((O_tot/total_votes)*100)
print(O_per)


# In[ ]:


Title= "Election Results"
total_votes_str=str(total_votes)
Khan_tot_str=str(Khan_tot)
Correy_tot_str=str(Correy_tot)
Li_tot_str=str(Li_tot)
O_tot_str=str(O_tot)
Khan_per_str=str(Khan_per)
Correy_per_str=str(Correy_per)
Li_per_str=str(Li_per)
O_per_str=str(O_per)
format_line=("_____________________________________")
winner=("Winner:Khan")


# In[ ]:


print(Title)
print(format_line)
print(f"Total Votes" + " " + total_votes_str)
print(f"Khan:" + " " + Khan_per_str +"%"+ " "+ Khan_tot_str)
print(f"Correy:" + " " + Correy_per_str +"%"+ " "+ Correy_tot_str)
print(f"Li:" + " " + Li_per_str +"%"+ " "+ Li_tot_str)
print(f"O'Tooley:" + " " + O_per_str +"%"+ " "+ O_tot_str)
print(format_line)
print(winner)


# In[ ]:


Line1=(Title)
Line2=(format_line)
Line3=(f"Total Votes" + " " + total_votes_str)
Line4=(f"Khan:" + " " + Khan_per_str +"%"+ " "+ Khan_tot_str)
Line5=(f"Correy:" + " " + Correy_per_str +"%"+ " "+ Correy_tot_str)
Line6=(f"Li:" + " " + Li_per_str +"%"+ " "+ Li_tot_str)
Line7=(f"O'Tooley:" + " " + O_per_str +"%"+ " "+ O_tot_str)
Line8=(format_line)
Line9=(winner)


# In[ ]:


PyPollpath_text='PyPoll.txt'
PyPoll_filet=open(PyPollpath_text, 'w')
PyPoll_filet.write(Line1 + '\n')
PyPoll_filet.write(Line2 + '\n')
PyPoll_filet.write(Line3 + '\n')
PyPoll_filet.write(Line4 + '\n')
PyPoll_filet.write(Line5 + '\n')
PyPoll_filet.write(Line6 + '\n')
PyPoll_filet.write(Line7 + '\n')
PyPoll_filet.write(Line8 + '\n')
PyPoll_filet.write(Line9 + '\n')


# In[ ]:




