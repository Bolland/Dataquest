
# coding: utf-8

# In[2]:

file = open ("births.csv",'r')
text = file.read()
print(text)


# In[3]:

text_splitted = text.split('\n')


print(text_splitted)


# In[10]:

dates_tokenized = []
for item in text_splitted:
    dates_tokenized.append(item.split(','))

print(len(dates_tokenized))


# In[ ]:




# In[42]:

dates_tokenized_wo_header = dates_tokenized[1:]
#print(len(dates_tokenized_wo_header))

print(dates_tokenized_wo_header)    


# In[48]:

days_counts = {}

for entry in dates_tokenized_wo_header:
    print("dayofweek: " + entry[3])
    print("briths: " + entry[4])
    if (entry[3] in days_counts):
        print('yes')
        days_counts[entry[3]] = days_counts[entry[3]] + int(entry[4])
    else:
        print('n') 
        days_counts[entry[3]] = int(entry[4])
print(days_counts)


# # Analysing birth dates
# 
# ## Methodology
# * Read file with births
# * Split content up and tokenized
# * Grouped sum of births by day_of_week (1-7) and saved to dictionary days_counts
# 
# ## Data set
# * year - Year
# * month - Month
# * date_of_month - Day number of the month
# * day_of_week - Day of week. Monday is 1, Sunday is 7
# * birhts - bumber of birhts

# In[ ]:



