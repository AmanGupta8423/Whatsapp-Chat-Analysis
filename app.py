import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

st.sidebar.title("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    
    df = preprocessor.preprocess(data)
    

    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'All')
    selected_user = st.sidebar.selectbox('Show Analysis With Respect To',user_list)
    st.title('Messages')
    if selected_user == 'All':
        st.dataframe(df)
    else:
        st.dataframe(df[df['user'] == selected_user])

    if st.sidebar.button('Analyse'):
        col1,col2 = st.columns(2)
        with col1:
            st.title('Participation')
            timeline = helper.monthly_participation(selected_user,df)
            fig,ax = plt.subplots(figsize=(12,6))
            ax.bar(timeline['time'],timeline['message'],color='purple')
            ax.set_xticklabels(timeline['time'],rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.title('Daily Participation')
            daily_timeline = helper.daily_participation(selected_user,df)
            fig,ax = plt.subplots(figsize=(12,6))
            ax.plot(daily_timeline['only_date'],daily_timeline['message'],color='brown')
            ax.set_xticklabels(daily_timeline['only_date'],rotation='vertical')
            st.pyplot(fig)
        # col1,col2 = st.columns(2)
        # with col1:
        st.title('Weekly Participation') 
        weekly_timeline = helper.weekly_participation(selected_user,df)
        fig,ax = plt.subplots(figsize=(12,6))
        ax.bar(weekly_timeline.index,weekly_timeline.values)
        ax.set_xticklabels(weekly_timeline.index,rotation='vertical')
        st.pyplot(fig)
        # with col2:
        #      st.title('Monthly Participation') 
        #      monthly_timeline = helper.monthly_participation(selected_user,df)
        #      fig,ax = plt.subplots(figsize=(12,6))
        #      ax.plot(monthly_timeline.index,monthly_timeline.values,color='green')
        #      ax.set_xticklabels(monthly_timeline.index,rotation='vertical')
        #      st.pyplot(fig)

        st.title('Activity Heat Map')
        activity_heat_map = helper.hourly_participation(selected_user,df)
        fig,ax = plt.subplots(figsize=(12,6))
        ax=sns.heatmap(activity_heat_map, annot=True, fmt='.0f',annot_kws={"size": 8}, cmap="YlGnBu")
        ax.set_xlabel('Timeline')
        ax.set_ylabel('Day')
        st.pyplot(fig)

        st.title('Top Statistics')
        num_messages, total_words, num_media, num_links = helper.fetch_stats(selected_user,df)
        col1,col2,col3,col4 = st.columns(4)

        with col1:
            st.header('Total Messages')
            st.title(num_messages)

        with col2:
            st.header('Total Words')
            st.title(total_words)

        with col3:
            st.header('Media Shared')
            st.title(num_media)

        with col4:
            st.header('Links Shared')
            st.title(num_links)

        if selected_user == 'All':
            st.title('Most active members')
            x,d = helper.fetch_most_busy_users(df)
            fig,ax = plt.subplots(figsize=(12,6))
            
            col1,col2 = st.columns(2)
            with col1:
                ax.bar(x.index,x.values,color='orange')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(d)

        st.title('Word Cloud')
        df_wc = helper.create_word_cloud(selected_user,df)
        fig,ax = plt.subplots(figsize=(12,6))
        ax.imshow(df_wc)
        st.pyplot(fig)

        st.title('Most Common Words')
        common_words = helper.most_common_words(selected_user,df)
        df_common = pd.DataFrame(common_words,columns=['word','count'])
        # st.dataframe(df_common)
        fig,ax = plt.subplots(figsize=(12,6))
        ax.barh(df_common['word'],df_common['count'],color='green')
        st.pyplot(fig)

        st.title('Emoji Tracker')
        emoji_df = helper.emoji_track(selected_user,df)
        st.dataframe(emoji_df) 

        