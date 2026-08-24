from operator import index

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Startup Analysis")
df = pd.read_csv("startup_cleaned_data.csv")
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['month']= df['date'].dt.month
df['year'] = df['date'].dt.year
def load_overall_analysis():
    st.title("Overall Analysis")
    colum1,colum2,colum3,colum4 = st.columns(4)
    #Total investment
    with colum1:
        total = df['amount in usd'].sum()

        if total >= 1_000_000_000:
            result = f"${total / 1_000_000_000:.2f}B"
        elif total >= 1_000_000:
            result = f"${total / 1_000_000:.2f}M"
        else:
            result = f"${total:,.0f}"
        st.metric("Total", result)
    # Max money invested in a startup
    # Maximum investment
    with colum2:
        max_investment = df.groupby('startup')['amount in usd'].max().sort_values(ascending = False).head(1).values[0]

        if max_investment >= 1_000_000_000:
            max_display = f"${max_investment / 1_000_000_000:.2f}B"
        elif max_investment >= 1_000_000:
            max_display = f"${max_investment / 1_000_000:.2f}M"
        else:
            max_display = f"${max_investment:,.0f}"

        st.metric("Max Investment", max_display)
    with colum3:
        avg_investment = round(df.groupby('startup')['amount in usd'].sum().mean())
        if avg_investment >= 1_000_000_000:
            avg_display = f"${avg_investment / 1_000_000_000:.2f}B"
        elif max_investment >= 1_000_000:
            avg_display = f"${avg_investment / 1_000_000:.2f}M"
        else:
            avg_display= f"${avg_investment:,.0f}"

        st.metric("Avg Investment", avg_display)
    with colum4:
        total_investement_made = df['startup'].nunique()
        st.metric("Funded Startups", total_investement_made)

    st.header("MOM Investments")
    Selected_option = st.selectbox('Select Type',['Total','Count'])
    if Selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount in usd'].sum().reset_index()
        temp_df['x-axis'] = temp_df['month'].astype('str') + "-" + temp_df["year"].astype('str')
    else:
        temp_df = df.groupby(['year', 'month'])['amount in usd'].count().reset_index()
        temp_df['x-axis'] = temp_df['month'].astype('str') + "-" + temp_df["year"].astype('str')
    figure, axis = plt.subplots()
    axis.plot(temp_df['x-axis'],temp_df['amount in usd'] )
    st.pyplot(figure)


def load_investor_details(investor):
    st.title(investor)
    #load top 5 Investments
    recent_5 = df[df['investors'].str.contains(investor)].head()[['date','startup','Vertical','round','amount in usd']]
    st.subheader("Most Recent Investments")
    st.dataframe(recent_5)
    b1, b2 = st.columns(2)
    col1,col2,col3 = st.columns(3)

    with col1:
        city_invest = df[df['investors'].str.contains(investor)].groupby('city ')['amount in usd'].sum().sort_values(
            ascending=False).head()
        st.subheader("City")
        fig3, ax3 = plt.subplots()
        ax3.pie(city_invest, labels=city_invest.index, autopct='%0.01f%%')
        st.pyplot(fig3)
    with col2:
        sectors = df[df['investors'].str.contains(investor)].groupby('Vertical')['amount in usd'].sum().sort_values(
            ascending=False).head()
        st.subheader("Sectors")
        fig1, ax1 = plt.subplots()
        ax1.pie(sectors, labels=sectors.index, autopct='%0.01f%%')
        st.pyplot(fig1)
    with col2:
        round = df[df['investors'].str.contains(investor)].groupby('round')['amount in usd'].sum().sort_values(
            ascending=False).head(3)
        st.subheader("Round")
        fig2, ax2 = plt.subplots()
        ax2.pie(round, labels=round.index, autopct='%0.01f%%')
        st.pyplot(fig2)

    with b1:
        # biggest investments
        big_5 = df[df['investors'].str.contains(investor)].groupby('startup')['amount in usd'].sum().sort_values(
            ascending=False).head()
        st.subheader("Biggest Investments")
        fig, ax = plt.subplots()
        ax.bar(big_5.index, big_5.values)
        st.pyplot(fig)
        col1, col2, col3 = st.columns(3)
    with b2:

        YoY = df[df['investors'].str.contains(investor)].groupby('year')['amount in usd'].sum()
        st.subheader("YoY Investments")
        fig4, ax4 = plt.subplots()
        ax4.plot(YoY.index, YoY.values)
        st.pyplot(fig4)
st.sidebar.title("Startup Funding Analysis")
option = st.sidebar.selectbox('select one',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    #btn0 = st.sidebar.button("Find Overall Analysis")
    #if btn0:
    load_overall_analysis()
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    st.sidebar.button("Find startup Details")
    st.title("Startup Analysis")
elif option == 'Investor':
    selected_investor = st.sidebar.selectbox('Select investors',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button("Find Investor Details")
    if btn2:
        load_investor_details(selected_investor)

