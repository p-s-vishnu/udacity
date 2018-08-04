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

# total data points
print 'No. of training set :', len(enron_data)

# number of features
feature = [value for value in enron_data.values()]
print 'Number of features :', len(feature[0])

# total POI (person of interest)
poi_in_dataset = 0
# for data in enron_data:
# print data
#    if enron_data[data]['poi']:
#       poi_in_dataset = poi_in_dataset + 1
poi_in_dataset = sum([1 for data in enron_data if enron_data[data]['poi']])
print 'POIs\' in Enron data set :', poi_in_dataset

# actual number of POI
poi_name_record = open("../final_project/poi_names.txt").read().split("\n")
actual_poi = sum([1 for record in poi_name_record if "y" in record or "n" in record])
print 'POIs\' found manually :', actual_poi

# stock value of James Prentice
# print enron_data["PRENTICE JAMES"]
print 'Total stock value :', enron_data["PRENTICE JAMES"]['total_stock_value']

# How many email messages do we have from Wesley Colwell to persons of interest?
print 'Emails from Wesley Colwell to poi :', enron_data['COLWELL WESLEY']['from_this_person_to_poi']

# Value of stock options exercised by Jeffrey K Skilling?
print 'Exercised stock options ', enron_data['SKILLING JEFFREY K']['exercised_stock_options']

# Of these three individuals (Lay, Skilling and Fastow), who took home the most money?
print '\nMoney by LAY:', enron_data['LAY KENNETH L']['total_payments']
print 'Money by SKILLING:', enron_data['SKILLING JEFFREY K']['total_payments']
print 'Money by FASTOW:', enron_data['FASTOW ANDREW S']['total_payments']

# How many folks in this dataset have a quantified salary? What about a known email address?
no_salary_detail = 0
no_email_address = 0

for people in enron_data:
    if enron_data[people]['salary'] == 'NaN':
        no_salary_detail += 1
    if enron_data[people]['email_address'] == 'NaN':
        no_email_address += 1
print len(enron_data) - no_salary_detail, 'have a quantified salary'
print len(enron_data) - no_email_address, 'have a known email address.'

no_total_payment = sum([1 for key in enron_data if enron_data[key]['total_payments'] == 'NaN'])
print '\npeople having no total payment detail :', no_total_payment

# What percentage of people
print float(no_total_payment) / len(enron_data) * 100, '% of people'

no_total_payment_poi = sum(
    [1 for key in enron_data if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi']])
print '\n', float(
    no_total_payment_poi) / poi_in_dataset * 100, '% of POI, hence the classifer might always consider people with no total payment as non-POI'
