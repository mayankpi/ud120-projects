#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


####################################################################################
# How many poi have their total payments 'NaN'?

count1 = 0
count = 0
for each in enron_data:
	if enron_data[each]['poi'] == True:
		if enron_data[each]['total_payments'] == 'NaN':
			count += 1
		count1 += 1
count += 10
count1 += 10
print count1
print count

per = (count * 100)/count1
print per
###################################################################################

####################################################################################
# count = 0
# count1 = 0
# for each in enron_data:
# 	if enron_data[each]['total_payments'] == 'NaN':
# 		count1 += 1
# 	count += 1
# print count1+10
# print count+10
# per = ((count1+10) * 100)/(count + 10)
# print per

####################################################################################

################################################################################
#How many members have known salary and how many have known email address?



#TEST CODE
# for each in enron_data:
# 	print enron_data[each]
#print enron_data['LAY KENNETH L']

# count1 = 0
# count2 = 0
# for each in enron_data:
# 	if enron_data[each]['salary'] != 'NaN':
# 		count1 += 1
# 	if enron_data[each]['email_address'] != 'NaN':
# 		count2 += 1
		

# print count1
# print count2



################################################################################

#################################################################################
#Of Lay, Skilling and Andrew who took the most amount of money? How much money was it?

# print enron_data['SKILLING JEFFREY K']['total_payments']
# print enron_data['LAY KENNETH L']['total_payments']
# print enron_data['FASTOW ANDREW S']['total_payments']



#################################################################################







##################################################################################
# Hoe many values of stocks are exercised by the person jefferey k skilling


#print enron_data['SKILLING JEFFREY K']['exercised_stock_options']


####################################################################################



################################################################################
#How many email messages do we have from Wesley Colwell to persons of interest?


# [s for s in enron_data.keys() if "COLWELL" in s]
# enron_data['COLWELL WESLEY']
# print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
#################################################################################

# print len(enron_data["COLWELL WESLEY"]["email"])


# print enron_data["PRENTICE JAMES"]["total_stock_value"]   //print the total value of the stock of the person james prentice

################################################################
#Count the number of "poi"(Person of interest) in the enron data

# count = 0
# for each in enron_data:
# 	if enron_data[each]["poi"] == 1:
# 		count += 1

# print count
###################################################################


#print len(enron_data[enron_data.keys()[0]])               //Print number of features of each user
#print len(enron_data)               //print size of enron data