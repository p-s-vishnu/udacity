#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
features = ["salary", "bonus"]
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)

temp = sorted(data, key=lambda dat: dat[0], reverse=True)
max_sal = temp[0][0]
max_sal2 = temp[1][0]
for key, value in data_dict.items():
    sal = value['salary']
    # print sal
    if sal == max_sal:
        print '\nMax Salary ={} is for the KEY ={}'.format(sal, key)
    if sal == max_sal2:
        print '2nd most salary={} is for KEY ={}'.format(sal, key)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
