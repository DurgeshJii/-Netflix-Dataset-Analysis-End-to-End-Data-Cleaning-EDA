# -----------------------------------------
# PROJECT DAY 12  -  NETFLIX DATASET ANALYSIS
# -----------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv("netflix dataset.csv")
print(data)

# -------------------------------
# Basic Information
# -------------------------------

# 1. Head
print(data.head())

# 2. Tail
print(data.tail())

# 3. Shape
print(data.shape)

# 4. Size
print(data.size)

# 5. Columns
print(data.columns)

# 6. Data types
print(data.dtypes)

# 7. Missing info
print(data.info())

# -------------------------------
# TASK 1: REMOVE DUPLICATES
# -------------------------------

print(data[data.duplicated()])
data.drop_duplicates(inplace=True)
print(data.shape)

# -------------------------------
# TASK 2: NULL VALUES (HEATMAP)
# -------------------------------

print(data.isnull().sum())
sns.heatmap(data.isnull())
plt.show()

# -------------------------------
# Q1: Show Id and Director for "House of Cards"
# -------------------------------

print(data[data['Title'].isin(['House of Cards'])])
print(data[data['Title'].str.contains('House of Cards')])

# -------------------------------
# Q2: Year with Highest Releases
# -------------------------------

data['Date_N'] = pd.to_datetime(
    data['Release_Date'].astype(str).str.strip(),
    errors='coerce'
)

print(data['Date_N'].dt.year.value_counts())
data['Date_N'].dt.year.value_counts().plot(kind='bar')
plt.show()

# -------------------------------
# Q3: Count Movies vs TV Shows
# -------------------------------

print(data.groupby('Category').Category.count())
sns.countplot(data['Category'])
plt.show()

# -------------------------------
# Q4: Movies Released in Year 2000
# -------------------------------

data['Year'] = data['Date_N'].dt.year
print(data[(data['Category'] == 'Movie') & (data['Year'] == 2000)])

# -------------------------------
# Q5: TV Shows released only in India
# -------------------------------

print(data[(data['Category'] == 'TV Show') & (data['Country'] == 'India')]['Title'])

# -------------------------------
# Q6: Top 10 Directors with Most Content
# -------------------------------

print(data['Director'].value_counts().head(10))

# -------------------------------
# Q7: Movies with Comedies OR United Kingdom Content
# -------------------------------

print(data[(data['Category'] == 'Movie') & (data['Type'] == 'Comedies')])
print(data[(data['Category'] == 'Movie') & (data['Type'] == 'Comedies') |
           (data['Country'] == 'United Kingdom')])

# -------------------------------
# Q8: All Movies/Shows where Tom Cruise was cast
# -------------------------------

data_new = data.dropna()  # Remove rows where Cast is NaN
print(data_new[data_new['Cast'].str.contains('Tom Cruise')])

# -------------------------------
# Q9: Ratings Defined by Netflix
# -------------------------------

print(data['Rating'].nunique())
print(data['Rating'].unique())

# 9.1 Movies with 'TV-14' rating in Canada
print(data[(data['Category'] == 'Movie') &
           (data['Rating'] == 'TV-14') &
           (data['Country'] == 'Canada')])

# 9.2 TV Shows with 'R' rating after 2018
print(data[(data['Category'] == 'TV Show') &
           (data['Rating'] == 'R') &
           (data['Year'] > 2018)])

# -------------------------------
# Q10: Maximum Duration of Movie/Show
# -------------------------------

data[['Minutes', 'Unit']] = data['Duration'].str.split(' ', expand=True)
data['Minutes'] = pd.to_numeric(data['Minutes'], errors='coerce')

print("Max Duration:", data['Minutes'].max())
print("Min Duration:", data['Minutes'].min())
print("Average Duration:", data['Minutes'].mean())

# -------------------------------
# Q11: Country with Highest No. of TV Shows
# -------------------------------

data_tvshow = data[data['Category'] == 'TV Show']
print(data_tvshow.Country.value_counts().head(1))

# -------------------------------
# Q12: Sort Dataset by Year
# -------------------------------

print(data.sort_values(by='Year'))
print(data.sort_values(by='Year', ascending=False))

# -------------------------------
# Q13: Movie Dramas OR Kids TV
# -------------------------------

print(data[(data['Category'] == 'Movie') &
           (data['Type'] == 'Dramas')])

print(data[(data['Category'] == 'TV Show') &
           (data['Type'] == "Kids' TV")])

print(
    data[
        ((data['Category'] == 'Movie') & (data['Type'] == 'Dramas')) |
        ((data['Category'] == 'TV Show') & (data['Type'] == "Kids' TV"))
    ]
)
