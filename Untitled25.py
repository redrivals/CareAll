#!/usr/bin/env python
# coding: utf-8

# In[48]:


import random
import pandas as pd
def adult():
    global adult_name
    global num_adult
   
    num_adult = int(input("Please enter number of Adults:"))
    print("you entered adults",num_adult)
    global adult_info
    adult_info = {}
    adult_data = [' Review ', 'Rating ']
   
    for i in range(0,num_adult):
        adult_name = input("Name :")
        adult_info[adult_name] = {}
        for entry in adult_data:
            adult_info[adult_name][entry] = random.choice([1,2,3,4,5]) 
            
                

    
def young():
    global young_name
    global young_info
    num_young = int(input("Please enter number of young:"))
    print("you entered young",num_young)
    global young_info
    young_info = {}
    young_data = [' Review : ', 'Rating ']
    for i in range(0,num_young):
        young_name = input("Name :")
        young_info[young_name] = {}
        for entry in young_data:
            young_info[young_name][entry] = random.choice([1,2,3,4,5]) 
def adult_choice():
    global a_choice
    a_key=adult_info.keys()   
    a_choice=[]
    print("#########Adult Select########")
   
    for a in a_key:
        print(a)
    
        a_ch = [a,input()] 
        a_choice.append(a_ch) 

    print(a_choice) 
    
    ac=dict(a_choice)
    print("SELECTED CHOICE")
    print(ac)

def young_choice():
    global y_choice
    global n
    global d
    y_key=young_info.keys()   
    y_choice=[]
    print("#########Young Select########")
    n = int(input("Enter number of adults you want to select : ")) 
    if n>4:
        print("OUT OF RANGE!!ERROR!!!")
    else:
        for a in y_key:
            print(a)
            for i in range(0, n): 
                y_ch= [a,input()] 
                y_choice.append(y_ch) 

     
    yc=dict(y_choice)
    print("SELECTED CHOICE")
    print(yc)
    

def common():
    intersected_df = pd.merge(df2, a, how='inner')
    print(intersected_df)

    

    
    

print("###########CAREALL###############")
print("PLEASE ENTER THE DETAILS FIRST!")
print("ENTER THE DETAILS FOR ADULT")
adult()
print("THANKYOU!!")
print("NOW ENTER THE DETAILS FOR YOUNG")
young()
print("THANKYOU!!")
print("#################################")
print("List of adults available to take care of :")

df=pd.DataFrame(adult_info)
print(df)
print("List of youngs available :")
df1=pd.DataFrame(young_info)
print(df1)
young_choice()
adult_choice()
print("TABLE OF YOUNG CHOICE:")
df2=pd.DataFrame(y_choice)
df2.rename(columns={0:'Name of young'}, inplace=True)
print(df2)

print("TABLE OF ADULT CHOICE:")
df3=pd.DataFrame(a_choice)
df3.rename(columns={0:'Name of adult'}, inplace=True)
print(df3)





  


# In[55]:





# In[54]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


a


# In[ ]:





# In[ ]:





# In[ ]:




