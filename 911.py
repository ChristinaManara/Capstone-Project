import numpy as np
import pandas as pd
import seaborn as sb


def calls_911():
    df = pd.read_csv('911.csv')
    df.info()
    print(df.info())
    print(df.head(3))
    # What are the top 5 zipcodes for 911 calls?
    print(df['zip'].value_counts().head(5))
    # What are the top 5 townships (twp) for 911 calls?
    print(df['twp'].value_counts().head(5))
    # Take a look at the 'title' column, how many unique title codes are there?
    print(df['title'].nunique())
    # In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire,
    # and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains
    # this string value
    df['Reason'] = df['title'].apply(lambda x: x.split(':')[0])
    print(df['Reason'])
    # What is the most common Reason for a 911 call based off of this new column?
    print(df['Reason'].value_counts())
    # Now use seaborn to create a count plot of 911 calls by Reason.



if __name__ == '__main__':
    calls_911()
