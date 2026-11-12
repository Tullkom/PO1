import pandas as pd

def swap_rows(df, row1, row2):
    row1_copy = df.iloc[row1].copy()
    row2_copy = df.loc[row2].copy()
    df.loc[df.index[row1]] = row2_copy
    df.loc[row2] = row1_copy
    return df 

# 1
df_1 = pd.DataFrame({
  'Name': ['Strom, Mrs. Wilhelm (Elna Matilda Persson)',
           'Navratil, Mr. Michel ("Louis MHoffman")',
           'Minahan, Miss. Daisy E'],
  'Age': [29, 36.5, 33],
  'Sex': ['female', 'male', 'female']
})
print(df_1)

# 2
df_2 = pd.read_csv('titanic_csv.csv', sep=';')
print(df_2)

# 3
url = 'https://gist.githubusercontent.com/zaryanezrya/8b4ef51c707cb16d5e88a44dc00a1bb2/raw/41230f49c6268e072dbf102672f670be256922ab/gistfile1.txt'
df_3 = pd.read_csv(url, sep=',')
print(df_3)

# 4
df_3.columns = df_2.columns
df = pd.concat((df_2, df_3)).drop_duplicates()
print(df)

# 5
df = df.set_index('PassengerId').sort_index()
print(df)

# 6
print(df.info())
print(df.describe())

# 7
df = swap_rows(df, 0, 2)
print(df)

# 8
mapping = {'male': 'm', 'female': 'f'}
df['Sex'] = df['Sex'].map(mapping)
print(df)

# 9
tickets = df.groupby('Ticket')['Name'].count()
large_tickets = tickets[tickets >= 6]
print(df[df['Ticket'].isin(large_tickets.index)])

# 10
cabin = df[df['Name'] == df_1['Name'][0]]['Cabin'].tolist()[0]
print(df[df['Cabin'] == cabin])

# 11
df['BirthYear'] = 1912 - df['Age']
print(df)

# 12
df['Companion'] = df.groupby('Cabin')['Name'].transform('count') - 1
print(df)

# 13
df = swap_rows(df, 0, 1)
print(df)

# 14
df.to_csv('titanic.csv')

# 15
print(df.sort_values('Fare', ascending=False)[:10])

# 16
print(pd.crosstab(df['Sex'], df['Survived']))

# 17
print(pd.crosstab(df['Pclass'], df['Survived']))