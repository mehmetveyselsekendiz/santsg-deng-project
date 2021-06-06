import pandas as pd

df = pd.read_csv('forbes_billionaires.csv')


def list_to_dict(attributes, list):
    dict = {}
    i = 0
    for attribute in attributes:
        dict[attribute] = list[i]
        i += 1
    return dict


# print(list_to_dict(df.columns, df.values[0]))

forbes_billionaires_list = list(map(lambda x : list_to_dict(df.columns, x), df.values))
# print(forbes_billionaires_list)

# read csv file with pandas
# https://realpython.com/python-csv/