import numpy as np
import pandas as pd
import seaborn as sns
import seaborn as sns1
import matplotlib. pyplot as plt
sns.set_style('whitegrid')


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
    sns.countplot(x='Reason', data=df, palette='viridis')
    plt.show()
    # Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column?
    var = df['timeStamp'].iloc[0]
    print(type(var))
    print(pd.to_datetime(df['timeStamp']))
    df['timeStamp'] = pd.to_datetime(df['timeStamp'])
    df['Hour'] = df['timeStamp'].apply(lambda h: h.hour)
    df['Month'] = df['timeStamp'].apply(lambda m: m.month)
    df['Day of Week'] = df['timeStamp'].apply(lambda w: w.dayofweek)
    dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
    df['Day of Week'] = df['Day of Week'].map(dmap)
    # Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.
    sns1.countplot(x='Day of Week', hue='Reason', data=df, palette='viridis')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()
    sns.countplot(x='Month', data=df, hue='Reason', palette='viridis')
    # To relocate the legend
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()


if __name__ == '__main__':
    calls_911()
