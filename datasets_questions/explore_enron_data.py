#!/usr/bin/python3

"""
    starter code for exploring the Enron dataset (emails + finances)
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))


# counter of people
people = 0
poiCount = 0
salaryCounter = 0
emailCounter = 0
total_payment_nan = 0
poi_total_payment_nan = 0

for person in enron_data:
    people += 1
    if enron_data[person]['poi'] == 1:
        poiCount += 1
        if enron_data[person]['total_payments'] == "NaN":
            poi_total_payment_nan += 1

    if enron_data[person]['salary'] != "NaN":
        salaryCounter += 1
    if enron_data[person]['email_address'] != "NaN":
        emailCounter += 1
    if enron_data[person]['total_payments'] == "NaN":
        total_payment_nan += 1


print ("People: ", people)
print ("poi count: ", poiCount)
print ("email counter: ", emailCounter)
print ("salary counter: ", salaryCounter)
print ("total payment NaN: ", total_payment_nan, " ,Ratio: ", total_payment_nan / people)
print ("total payment NaN in POI: ", poi_total_payment_nan, " ,Ratio: ", poi_total_payment_nan / poiCount)



poiFile = open("../final_project/poi_names.txt")
poiCount2 = 0
lines = poiFile.readlines()
for line in lines:
    if line[0] == '(':
        poiCount2 += 1

print ("poi count2: ", poiCount2)

James_stockvalue = enron_data["PRENTICE JAMES"]["total_stock_value"]
print ("James Stock Value: ", James_stockvalue)

Wesley_emailToPOI = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print ("Wesley's to POI: ", Wesley_emailToPOI)

jeffrey_stock_option = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print ("Jeffrey's stock option: ", jeffrey_stock_option)

fraudvalue = enron_data["SKILLING JEFFREY K"]["total_payments"]
print ("total_payment: ", fraudvalue)
