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
    # Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the
    # count() method for aggregation. Use the head() method on this returned DataFrame.
    byMonth = df.groupby('Month').count()
    print(byMonth)
    # Now create a simple plot off of the dataframe indicating the count of calls per month.
    byMonth['twp'].plot()
    plt.show()
    # Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month.
    # Keep in mind you may need to reset the index to a column.
    sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())
    plt.show()
    # Create a new column called 'Date' that contains the date from the timeStamp column.
    # You'll need to use apply along with the .date() method.
    df['Date'] = df['timeStamp'].apply(lambda data: data.date())
    print(df['Date'])
    # Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.
    df.groupby('Date').count()['twp'].plot()
    plt.tight_layout()
    plt.show()
    # Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call
    df[df['Reason'] == 'Traffic'].groupby('Date').count()['twp'].plot()
    plt.tight_layout()
    plt.title('Traffic')
    plt.show()
    df[df['Reason'] == 'EMS'].groupby('Date').count()['twp'].plot()
    plt.tight_layout()
    plt.title('EMS')
    plt.show()
    df[df['Reason'] == 'Fire'].groupby('Date').count()['twp'].plot()
    plt.tight_layout()
    plt.title('Fire')
    plt.show()
    # Now let's move on to creating heatmaps with seaborn and our data. We'll first need to restructure the dataframe
    # so that the columns become the Hours and the Index becomes the Day of the Week. There are lots of ways to do
    # this, but I would recommend trying to combine groupby with an unstack method. Reference the solutions if you
    # get stuck on this!



if __name__ == '__main__':
    calls_911()
