import pandas as pd
import mtplotlib.pyplot as plt
df=pd.read_csv('fcc-forum-pageviews.csv',
               index_col=0,
               parce_dates=True)
bottom_threshold=df['value'].quantile(0.025)
top_threshold=df['value'].quantile(0.975)
df_clean=df[(df['value']>=bottom_threshold)&(df['value']<=top_threshold)
]
def draw_line_plot():
    fig, ax =plt.subplots(figsize=(12,6))
    ax.plot(df_clean.index,
            df_clean['value'],color='red',linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('date')
    ax.set_ylabel('Page Views')
    return fig
def draw_bar_plot():
    df_bar = df_clean.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    fig = df_bar.plot(kind='bar', figsize=(10, 8)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    
    plt.close()
    return fig
def draw_box_plot():
    df_box = df_clean.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    
    sns.boxplot(x='month', y='value', data=df_box, order=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ], ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    
    plt.close()
    return fig
    
    
                        
    
