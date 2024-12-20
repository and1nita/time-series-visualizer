import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
df.index = pd.to_datetime(df.index)

def draw_line_plot():
    # Draw line plot
    plt.rcParams.update({'font.size': 8})
    fig, ax = plt.subplots(figsize=(12,3.8), dpi=200)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.plot(df, color='tab:red', linewidth=1)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Month'] = df_bar.index.month_name()
    df_bar['Year'] = df_bar.index.year
    df_bar = df_bar.groupby(by=['Year','Month'], as_index=False).mean()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(5.4,4.8), dpi=200)
    hue_order = map(lambda x: pd.to_datetime(x, format='%m').month_name(), range(1,13))
    ax = sns.barplot(data=df_bar, x='Year', y='value', hue='Month', hue_order=hue_order, palette=sns.color_palette(), saturation=2, width=0.5)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
