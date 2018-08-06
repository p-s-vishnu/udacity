#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    residual_errors = net_worths - predictions

    for age, net_worth, error in zip(ages, net_worths, residual_errors):
        cleaned_data.append([age, net_worth, error])
    cleaned_data.sort(key=lambda x: x[2], reverse=True)
    cleaned_data = cleaned_data[0:81]
    print 'No of cleaned elements ', len(cleaned_data)
    return cleaned_data
