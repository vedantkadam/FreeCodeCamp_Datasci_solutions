import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",
                 parse_dates=['date'],
                 index_col='date')

# Clean data
# Clean data
df=df.drop(df[(df['value']<df['value'].quantile(0.025)) | (df['value']>df['value'].quantile(0.975))].index)
print(df)

def draw_line_plot():
  fig, ax = plt.subplots(figsize=(10, 5))
  plt.plot(df['value'],color='red',linewidth=0.8)
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
    df_bar = df.copy()
    df_bar['Year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['Month'] = pd.DatetimeIndex(df_bar.index).month
    
    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean()
    df_bar = df_bar.unstack()
    month_names=['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                 'August', 'September', 'October', 'November', 'December']
    # Draw bar plot
    fig = df_bar.plot(kind= 'bar', figsize = (15,10)).figure
    
    plt.title('')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    lg = plt.legend(title= 'Months', fontsize = 15, labels = month_names)
    title = lg.get_title()
    title.set_fontsize(15)
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    fig, ax = plt.subplots(figsize=(10, 5))
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    plt2=sns.boxplot(x='Month',y='value',data=df_box)
    plt2.set_title("Month-wise Box Plot (Trend)")
    plt2.set_xlabel('Month')
    plt2.set_ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
