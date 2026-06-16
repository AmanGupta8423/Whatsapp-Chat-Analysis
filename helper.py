from urlextract import URLExtract
extract = URLExtract()
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji 
import seaborn as sns

import matplotlib.pyplot as plt 
def fetch_stats(selected_user,df):

    if selected_user != 'All':
        df = df[df['user'] == selected_user]
         
    num_msg = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())
    num_media = df[df['message'] == '<Media omitted>\n'].shape[0]
    
    links=[]
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_msg, len(words), num_media, len(links)


def fetch_most_busy_users(df):
    x = df['user'].value_counts().head()
    d = round((df['user'].value_counts()/df.shape[0])*100, 2).reset_index().rename(columns={'index':'x','user':'name','count':'percent_msg'})
    return x ,d


def create_word_cloud(selected_user,df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user]

    f = open('stop_hinglish.txt','r')
    stopwords = f.read()

    temp = df[(df['message'] != '<Media omitted>\n') & (df['message'] != 'group_notification')]
    def remove_stopwords(message):
        y = []
        for word in message.split():
            if word.lower() not in stopwords:
                y.append(word)
        return " ".join(y)
    temp['message'] = temp['message'].apply(remove_stopwords)
    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc


def most_common_words(selected_user,df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user]
    
    f = open('stop_hinglish.txt','r')
    stopwords = f.read()

    temp = df[(df['message'] != '<Media omitted>\n') & (df['message'] != 'group_notification')]
    words =[]
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stopwords:
                words.append(word)
    return Counter(words).most_common(20)

def emoji_track(selected_user,df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user]
    
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))),columns=['emoji','count'])
    return emoji_df

def monthly_participation(selected_user,df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user]
    
    
    timeline =  df.groupby(['year','month_num','month']).count()['message'].reset_index()
    timeline['time'] = timeline['month'] + '-' + timeline['year'].astype(str)
    return timeline

def daily_participation(selected_user,df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user]
    

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline

def weekly_participation(selected_user,df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user]
    
    return df['day_name'].value_counts()

# def monthly_participation(selected_user,df):
#     if selected_user != 'All':
#         df = df[df['user'] == selected_user] 
    
#     return df['month'].value_counts()

def hourly_participation(selected_user,df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user]
    activity_heat_map = df.pivot_table(index ='day_name',columns='period',values='message',aggfunc='count').fillna(0)
    return activity_heat_map

def filter_link(selected_user, df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user]

    data = []

    for user, message in zip(df['user'], df['message']):
        for url in extract.find_urls(message):
            data.append([user, url])

    return pd.DataFrame(data, columns=['User', 'Link'])