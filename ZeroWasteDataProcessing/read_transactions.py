import pandas as pd

# Get transactions from initial Junction dataset
transactions_file = "data/database/Junction_data.csv"
nrows = 200000
chunk_size = 10 ** 6
person1 = 6715
person2 = 6712
df_single_person1 = pd.DataFrame(columns=['AreaId', 'Receipt', 'TransactionDate', 'BeginHour', 'EAN', 'Quantity',
                                          'PersonAgeGrp', 'KCustomer', 'QualClass', 'EasyClass'])
df_single_person2 = pd.DataFrame(columns=['AreaId', 'Receipt', 'TransactionDate', 'BeginHour', 'EAN', 'Quantity',
                                          'PersonAgeGrp', 'KCustomer', 'QualClass', 'EasyClass'])

# Complete set for only two personalities
# i = 0
# for chunk in pd.read_csv(transactions_file, chunksize=chunk_size, sep=";"):
#     print(i)
#     person1_chunk = chunk.loc[chunk['KCustomer'] == person1]
#     person2_chunk = chunk.loc[chunk['KCustomer'] == person2]
#     df_single_person1 = df_single_person1.append(person1_chunk, ignore_index=True)
#     df_single_person2 = df_single_person2.append(person2_chunk, ignore_index=True)
#     i = i + 1
# df_single_person1.to_csv(path_or_buf='data/df_single_person1.csv', index=False, sep=';')
# df_single_person2.to_csv(path_or_buf='data/df_single_person2.csv', index=False, sep=';')


# Two person's data from first N transactions
transactions = pd.read_csv(transactions_file, nrows=nrows, sep=';')
person1_chunk = transactions.loc[transactions['KCustomer'] == person1]
person2_chunk = transactions.loc[transactions['KCustomer'] == person2]
df_single_person1 = df_single_person1.append(person1_chunk, ignore_index=True)
df_single_person2 = df_single_person2.append(person2_chunk, ignore_index=True)
print(df_single_person1)
df_single_person1.to_csv(path_or_buf='data/tables/df_single_person1_medium.csv', index=False, sep=';')
df_single_person2.to_csv(path_or_buf='data/tables/df_single_person2_medium.csv', index=False, sep=';')

# Get the first and the last rows from the initial Junction dataset
# transactions = pd.read_csv(transactions_file, nrows=nrows)
# print(transactions.iloc[0])
# count = len(open(transactions_file).readlines())
# df = pd.read_csv(transactions_file, skiprows=range(2, count-1), header=0)
# print(df)
