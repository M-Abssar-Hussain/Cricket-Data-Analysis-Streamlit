import pandas as pd
import streamlit as st
# import matplotlib.pyplot as plt
import plotly.express as px
# import numpy as np
# import seaborn as sns


st.sidebar.title("Navigation Bar")
st.sidebar.markdown("Go To")
choice = st.sidebar.radio('Select a Graph',["Top 10 Match Winner","Top 10 Toss Winner","Toss/Match Win","Toss/Match Win percentage"])

cric_df = pd.read_csv('provided text new.csv')
if choice == "Top 10 Toss Winner":
     st.title('Top 10 Toss winning countries')
     top_10 = cric_df.sort_values(by='Toss_Winner', ascending=False).head(10)
     fig_match_toss_win = px.bar(top_10,
                                 x='unique countries',
                                 y='Toss_Winner',
                                 color="unique countries")
     st.plotly_chart(fig_match_toss_win)
elif choice == "Top 10 Match Winner":
     top_10_match_win = cric_df.sort_values(by='matchwin', ascending=False).head(10)
     fig_top_10_match_win = px.bar(top_10_match_win,
                                   x='unique countries',
                                   y='matchwin')
     st.plotly_chart(fig_top_10_match_win)
elif choice == "Toss/Match Win":
     st.title("Toss winner and also match winner")
     toss_win_match_win = cric_df.sort_values(by='toss_win_match_win', ascending=False).head(10)
     fig_toss_win_match_win = px.bar(toss_win_match_win,
                                   x='unique countries',
                                   y='toss_win_match_win')
     st.plotly_chart(fig_toss_win_match_win)
# elif choice == "Toss/Match Win percentage":
#      toss_win_match_win_prcnt =cric_df.sort_values(by='toss_match%', ascending=False).head(10)
#      fig_toss_win_match_win_prcnt = px.pie(toss_win_match_win_prcnt,
#                                    names='unique countries',
#                                    values='toss_match%',
#                                    color='unique countries',
#                                    hole=0)
#      st.plotly_chart(fig_toss_win_match_win_prcnt)
elif choice == "Toss/Match Win percentage":
    st.title("Toss/Match Win percentage")
    
    temp_df = cric_df.copy()
    
 
    temp_df['toss_match_numeric'] = temp_df['toss_match%'].str.replace('%', '').astype(float)
    
    toss_win_match_win_prcnt = temp_df.sort_values(by='toss_match_numeric', ascending=False).head(10)
    
   
    fig_toss_win_match_win_prcnt = px.pie(
        toss_win_match_win_prcnt,
        names='unique countries',
        values='toss_match_numeric',  
        color='unique countries',
        hole=0
    )
    
    
    fig_toss_win_match_win_prcnt.update_traces(
        hovertemplate='%{label}<br>Percentage: %{value}%<extra></extra>'
    )
    
    st.plotly_chart(fig_toss_win_match_win_prcnt)
else:
     st.write("nothing selected")





