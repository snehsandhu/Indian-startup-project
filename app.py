from operator import index

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Startup Analysis")
#styleeeeeeeeeeeeeee
st.markdown("""
<style>

    /* =========================
       GLOBAL
    ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at 0% 0%,
                rgba(139, 92, 246, 0.12),
                transparent 28%
            ),
            radial-gradient(
                circle at 100% 0%,
                rgba(6, 182, 212, 0.08),
                transparent 25%
            ),
            #080D1A;
    }

    .main .block-container {
        max-width: 1500px;
        padding: 2.5rem 3rem 4rem 3rem;
    }


    /* =========================
       SIDEBAR
    ========================= */

    [data-testid="stSidebar"] {
        background: #070B15;
        border-right: 1px solid #1E293B;
    }

    [data-testid="stSidebar"] h1 {
        color: #F8FAFC !important;
        font-size: 21px !important;
        font-weight: 800 !important;
    }

    [data-testid="stSidebar"] label {
        color: #CBD5E1 !important;
        font-weight: 600 !important;
    }


    /* =========================
       HEADINGS
    ========================= */

    h1 {
        color: #F8FAFC !important;
        font-size: 36px !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
    }

    h2 {
        color: #F1F5F9 !important;
        font-size: 25px !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #E2E8F0 !important;
        font-weight: 700 !important;
    }


    /* =========================
       SUBTITLE
    ========================= */

    .subtitle {
        color: #94A3B8;
        font-size: 15px;
        margin-top: -15px;
        margin-bottom: 30px;
    }


    /* =========================
       METRIC CARDS
    ========================= */

    [data-testid="stMetric"] {
        background:
            linear-gradient(
                145deg,
                #151C2F,
                #101827
            );

        border: 1px solid #263247;

        border-radius: 16px;

        padding: 20px;

        min-height: 120px;

        box-shadow:
            0 10px 30px rgba(0, 0, 0, 0.25);

        transition: all 0.2s ease;
    }

    [data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        border-color: #8B5CF6;

        box-shadow:
            0 15px 40px rgba(139, 92, 246, 0.15);
    }

    [data-testid="stMetricLabel"] {
        color: #94A3B8 !important;
        font-size: 13px !important;
        font-weight: 600 !important;
    }

    [data-testid="stMetricValue"] {
        color: #F8FAFC !important;
        font-size: 28px !important;
        font-weight: 800 !important;
    }


    /* =========================
       SELECT BOX
    ========================= */

    div[data-baseweb="select"] > div {
        background-color: #111827 !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }


    /* =========================
       BUTTON
    ========================= */

    .stButton > button {
        width: 100%;

        background:
            linear-gradient(
                90deg,
                #7C3AED,
                #4F46E5
            );

        color: white;

        border: none;

        border-radius: 10px;

        font-weight: 700;

        padding: 10px;

        transition: 0.2s;
    }

    .stButton > button:hover {
        background:
            linear-gradient(
                90deg,
                #8B5CF6,
                #6366F1
            );

        transform: translateY(-1px);
    }


    /* =========================
       DATAFRAME
    ========================= */

    [data-testid="stDataFrame"] {
        border: 1px solid #263247;
        border-radius: 14px;
        overflow: hidden;
    }


    /* =========================
       DIVIDER
    ========================= */

    hr {
        border-color: #1E293B !important;
    }

</style>
""", unsafe_allow_html=True)
#endddddd
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
        city_invest = df[df['investors'].str.contains(investor)].groupby('city')['amount in usd'].sum().sort_values(
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
        round_ = df[df['investors'].str.contains(investor)].groupby('round')['amount in usd'].sum().sort_values(
            ascending=False).head(3)
        st.subheader("Round")
        fig2, ax2 = plt.subplots()
        ax2.pie(round_, labels=round_.index, autopct='%0.01f%%')
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
def load_startup_details(startup):
    st.title(startup)
    colu1, colu2, colu3 = st.columns(3)
    with colu1:
        Industry = df[df['startup'] == startup]['Vertical'].iloc[0]
        st.metric("Industry", Industry)
    with colu2:
        sub_industry = df[df['startup'] == startup]['subvertical'].iloc[0]
        st.metric("Sub_Industry",sub_industry)
    with colu3:
        Loc = df[df['startup'] == startup]['city'].iloc[0]
        st.metric("Location", Loc)
    tabl = df[df['startup'] == startup][
         ['date', 'round', 'amount in usd', 'investors']
    ].sort_values('date').reset_index(drop=True)
    st.dataframe(tabl)
    c1,c2,c3,c4 = st.columns(4)
    with c1:
        total_fundings = tabl['amount in usd'].sum()
        if total_fundings >= 1_000_000_000:
            avg_display = f"${total_fundings / 1_000_000_000:.2f}B"
        elif total_fundings >= 1_000_000:
            avg_display = f"${total_fundings / 1_000_000:.2f}M"
        else:
            avg_display= f"${total_fundings:,.0f}"

        st.metric("Total Fundings", avg_display)
    with c2:
        total_rounds = tabl['round'].nunique()
        st.metric("Fundings Rounds",total_rounds )
    with c3:
        max_fundings = tabl['amount in usd'].max()
        if max_fundings >= 1_000_000_000:
            max_display = f"${max_fundings / 1_000_000_000:.2f}B"
        elif max_fundings >= 1_000_000:
            max_display = f"${max_fundings / 1_000_000:.2f}M"
        else:
            max_display= f"${max_fundings:,.0f}"
        st.metric("Largest Funding", max_display)
    with c4:
        investor_list = (
            tabl['investors']
            .dropna()
            .str.split(',')
            .explode()
            .str.strip()
        )
        number_of_investors = len(investor_list)
        st.metric("Investors", number_of_investors)
    funding = tabl['amount in usd']
    st.subheader("Fundings")
    figu, axu = plt.subplots()
    axu.plot(tabl['date'], funding.values)
    axu.set_title("Funding Journey")
    axu.set_xlabel("Date")
    axu.set_ylabel("Investment")
    st.pyplot(figu)
    z1,z2=st.columns(2)
    with z1:
        funding_rounds = tabl.groupby('round')['amount in usd'].sum()
        st.subheader("Rounds")
        f,a = plt.subplots(figsize=(8, 4))
        a.bar(funding_rounds.index, funding_rounds.values)
        a.set_title("Investment by Funding Round")
        a.set_xlabel("Round")
        a.set_ylabel("Investment")
        st.pyplot(f)
    with z2:
        investor_lis = (tabl['investors'].dropna().str.split(',').explode().str.strip().unique())
        top_investors = investor_lis.value_counts().head(10)
        st.subheader("Top Investors")
        st.dataframe(
            top_investors.reset_index(
                name="Number of Investments"
            ),
        )
st.sidebar.title("Startup Funding Analysis")
option = st.sidebar.selectbox('select one',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    #btn0 = st.sidebar.button("Find Overall Analysis")
    #if btn0:
    load_overall_analysis()
elif option == 'Startup':
    selected_startup = st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    button = st.sidebar.button("Find startup Details")
    if button:
        load_startup_details(selected_startup)

elif option == 'Investor':
    selected_investor = st.sidebar.selectbox('Select investors',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button("Find Investor Details")
    if btn2:
        load_investor_details(selected_investor)

