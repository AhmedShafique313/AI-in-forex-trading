from loading_csv import data

data.isnull().any()

col_to_remove = 'Gmt time'
dataset= data.drop(columns=[col_to_remove])
print(dataset.head()) 

print(dataset.corr())