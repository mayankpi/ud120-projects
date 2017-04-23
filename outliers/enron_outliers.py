#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop( "TOTAL", 0 )
data = featureFormat(data_dict, features)


# max = 0
# for each in data_dict:
# 	# print each
# 	if (data_dict[each]['salary'] != 'Nan' and data_dict[each]['salary'] > max):
# 		max = data_dict[each]['salary']
# 		temp = each

# print data_dict['TOTAL']['salary']
# print temp


### your code below
for each in data_dict:
	if data_dict[each]['salary'] > 10**6 and data_dict[each]['bonus'] > 5*(10**6) and data_dict[each]['salary'] != 'NaN' :
		print each
		print data_dict[each]['salary']



for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()