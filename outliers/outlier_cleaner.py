#!/usr/bin/python3


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error)
    """

    cleaned_data = []

    ### your code goes here
    import math

    error_list = []
    for index in range(len(predictions)):
        error_list.extend(abs(predictions[index] - net_worths[index]))

    error_list.sort()
    number_keep = int(math.floor(len(error_list) * 0.9))
    threshold = error_list[number_keep - 1]


    print("threshold: ", threshold)

    # topErrors = error_list[number_keep:]
    # print("top_count: ", topErrors)

    for index in range(len(predictions)):
        error = abs(predictions[index] - net_worths[index])
        if( error <= threshold):
            cleaned_data.append([ages[index], net_worths[index], error])
        else:
            pass


    return cleaned_data
