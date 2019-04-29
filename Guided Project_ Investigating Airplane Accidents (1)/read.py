############ STEP 1 #######################################
f = open("AviationData.txt", "r")
data_list = f.read(5)

aviation_data=f.readlines()

#print(aviation_data[0])

aviation_list = []

for line in aviation_data :
    aviation_list.append(line.split(" | "))
    
    
#print(aviation_list[1])

lax_code = []

for line in aviation_list:
    if 'LAX94LA336' in line:
        lax_code.append(line)
        
        
        
#print(lax_code)
#Conclusion : The for loop would be very expensive in time

############ STEP 2 #######################################


# Sort the list
#Use the bisect module to perform binary search (O(logn) time search)
import bisect 
sorted_aviation_list = sorted(aviation_list, key = lambda row: row[2])
sorted_accident_numbers = [row[2] for row in sorted_aviation_list]
lax_index = bisect.bisect_left(sorted_accident_numbers, "LAX94LA336")
#print(sorted_aviation_list[lax_index])


############ STEP 3 #######################################

aviation_dict_list = []
header = aviation_data[0].split(" | ")
for row in aviation_data[1:]:
    splited_dict_row= dict(zip(header, row.split(" | ")))
    aviation_dict_list.append(splited_dict_row)

lax_dict =[]

for row_dict in aviation_dict_list:
    if 'LAX94LA336' in row_dict.values():
        lax_dict.append(row_dict)
        
#print(lax_dict)


##Conclusion: It is way easier to work with dictionnaries

############ STEP 4 #######################################

# we're looking to filter our data by the column or the key "Investigation Type" == "Accident" grouped by state (parse "Location")
import numpy as np 
states_list = []
location = aviation_dict_list[0].get("Location").split(', ')


for x in range(0,len(aviation_dict_list)): 
    loc = aviation_dict_list[x]['Location'][-2:]
    states_list.append(loc)
    
    
#print(set(states_list))
states  = set(states_list)

import collections

states_dict = {}
for x in range(0,len(aviation_dict_list)):
    loc = aviation_dict_list[x]['Location'][-2:]
    Inv_Type = aviation_dict_list[x]['Investigation Type']
    if Inv_Type == "Accident" :
        states_dict[loc] = states_dict.get(loc, 0) + 1
max_acc = max(states_dict.values())  
#print(max_acc)

#print(list(states_dict.values()).index(max_acc))
#it separates the dictionary's values in a list, finds the position of the value you have
ind = list(states_dict.values()).index(max_acc)
#and gets the key at that position.
max_acc_state = list(states_dict.keys())[ind]
#print(max_acc_state)

##Conclusion: The state of the most aviation accidents is CA: California with 7879 accidents

############ STEP 5 #######################################

###Fatalities and serious injuries by mounth and year

import datetime

monthly_injuries = {}

month_dict_name = {'':'Not provided','01' : "January",
       '02' : "February",
       '03' : "March",
       '04' : "April",
       '05' : "May",
       '06' : "June",
       '07' : "July",
       '08' : "August",
       '09' : "September",
       '10' : "October",
       '11' : "November",
       '12' : "December"}
for x in range(0,len(aviation_dict_list)):
    ev_mth = aviation_dict_list[x]['Event Date'][:2]
    mth = month_dict_name[ev_mth]
    if aviation_dict_list[x]['Total Fatal Injuries'] == '' :
        aviation_dict_list[x]['Total Fatal Injuries']  = 0
    if aviation_dict_list[x]['Total Serious Injuries'] == '':
        aviation_dict_list[x]['Total Serious Injuries']  = 0
    Fat_Ser_Inj_Nbr= int(aviation_dict_list[x]['Total Fatal Injuries']) + int(aviation_dict_list[x]['Total Serious Injuries'] )
    monthly_injuries[mth] = monthly_injuries.get(mth, 0) + Fat_Ser_Inj_Nbr

print(monthly_injuries)

print(sorted(monthly_injuries.items(), key=lambda x: x[1]))
##Conclusion: There is more injuries in summer. We can also suppose that there is more people travelling in summer and in december by the holidays.  










    
        
    

