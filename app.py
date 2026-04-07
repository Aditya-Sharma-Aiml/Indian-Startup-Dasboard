import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(layout='wide', page_title='Startup Analysis Dashboard', initial_sidebar_state='expanded')

# Load and prepare data
@st.cache_data
def load_data():
    df = pd.read_csv('startup_cleaned.csv')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    return df

df = load_data()

# ======================== UTILITY FUNCTIONS ========================

def get_startup_investors(startup_name):
    """Get all investors for a startup"""
    startup_df = df[df['startup'].str.lower() == startup_name.lower()]
    return startup_df

def get_investor_startups(investor_name):
    """Get all startups funded by an investor"""
    investor_df = df[df['investors'].str.contains(investor_name, case=False, na=False)]
    return investor_df

def get_all_unique_investors():
    """Parse and get all unique investor names"""
    all_investors = set()
    for investors_str in df['investors'].dropna():
        investors = [inv.strip() for inv in investors_str.split(',')]
        all_investors.update(investors)
    return sorted(list(all_investors))

def get_similar_startups(vertical_name):
    """Get other startups in the same vertical"""
    return df[df['vertical'].str.lower() == vertical_name.lower()]

def get_similar_investors(investor_name, top_n=5):
    """Find investors with similar investment patterns"""
    inv_data = get_investor_startups(investor_name)
    if len(inv_data) == 0:
        return pd.DataFrame()
    
    target_verticals = inv_data['vertical'].str.lower().unique()
    similar = df[df['vertical'].str.lower().isin(target_verticals)].copy()
    similar = similar[similar['investors'].str.contains(investor_name, case=False, na=False) == False]
    
    investor_counts = similar['investors'].str.split(',').apply(lambda x: pd.Series(x)).stack().value_counts().head(top_n)
    return investor_counts

# ======================== OVERALL ANALYSIS ========================

def load_overall_analysis():
    st.title('&#128202; Overall Analysis')
    
    # Filter out rows with 0 or NaN amounts for meaningful analysis
    analysis_df = df[df['amount'] > 0].copy()
    
    # KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    total = round(analysis_df['amount'].sum())
    max_funding = analysis_df.groupby('startup')['amount'].sum().max()
    avg_funding = analysis_df.groupby('startup')['amount'].sum().mean()
    num_startups = analysis_df['startup'].nunique()
    
    with col1:
        st.metric('Total Invested', f'{total} Cr')
    with col2:
        st.metric('Max Startup Funding', f'{round(max_funding)} Cr')
    with col3:
        st.metric('Avg Funding/Startup', f'{round(avg_funding)} Cr')
    with col4:
        st.metric('Funded Startups', num_startups)
    
    st.divider()
    
    # Month-over-Month Analysis
    st.subheader('&#128260; Month-over-Month Trends')
    col_mom1, col_mom2 = st.columns(2)
    
    with col_mom1:
        mom_type = st.radio('Select Type', ['Total Funding (Cr)', 'Number of Deals'], horizontal=True)
    
    try:
        if mom_type == 'Total Funding (Cr)':
            mom_df = analysis_df.groupby(['year', 'month'])['amount'].sum().reset_index()
        else:
            mom_df = analysis_df.groupby(['year', 'month']).size().reset_index(name='amount')
        
        if len(mom_df) > 0 and (mom_df['amount'] > 0).any():
            mom_df['x_axis'] = mom_df['month'].astype(str) + '-' + mom_df['year'].astype(str)
            
            fig_mom, ax_mom = plt.subplots(figsize=(12, 4))
            ax_mom.plot(mom_df['x_axis'], mom_df['amount'], marker='o', linewidth=2, markersize=6, color='#1f77b4')
            ax_mom.set_xlabel('Month-Year')
            ax_mom.set_ylabel(mom_type)
            ax_mom.tick_params(axis='x', rotation=45)
            ax_mom.grid(alpha=0.3)
            fig_mom.tight_layout()
            st.pyplot(fig_mom)
        else:
            st.info('No month-over-month data available')
    except Exception as e:
        st.error(f'Error displaying MoM trends: {str(e)}')
    
    st.divider()
    
    # Sector Analysis
    st.subheader('&#127942; Top Sectors')
    col_sector1, col_sector2 = st.columns(2)
    
    with col_sector1:
        st.write("**Sector-wise Funding (Amount)**")
        try:
            sector_amount = analysis_df.groupby('vertical')['amount'].sum().sort_values(ascending=False).head(10)
            if len(sector_amount) > 0 and (sector_amount > 0).any():
                fig_sector, ax_sector = plt.subplots(figsize=(8, 5))
                ax_sector.barh(sector_amount.index, sector_amount.values, color='#2ca02c')
                ax_sector.set_xlabel('Total Funding (Cr)')
                fig_sector.tight_layout()
                st.pyplot(fig_sector)
            else:
                st.info('No sector data available')
        except Exception as e:
            st.error(f'Error displaying sector funding: {str(e)}')
    
    with col_sector2:
        st.write("**Sector Distribution (Count)**")
        try:
            sector_count = analysis_df['vertical'].value_counts().head(10)
            if len(sector_count) > 0:
                fig_sector_pie, ax_pie = plt.subplots(figsize=(8, 5))
                ax_pie.pie(sector_count.values, labels=sector_count.index, autopct='%1.1f%%', startangle=90)
                fig_sector_pie.tight_layout()
                st.pyplot(fig_sector_pie)
            else:
                st.info('No sector count data available')
        except Exception as e:
            st.error(f'Error displaying sector distribution: {str(e)}')
    
    st.divider()
    
    # City-wise Analysis
    st.subheader('&#127750; City-wise Funding')
    try:
        city_funding = analysis_df.groupby('city')['amount'].sum().sort_values(ascending=False).head(10)
        if len(city_funding) > 0 and (city_funding > 0).any():
            fig_city, ax_city = plt.subplots(figsize=(10, 5))
            ax_city.bar(city_funding.index, city_funding.values, color='#ff7f0e')
            ax_city.set_ylabel('Total Funding (Cr)')
            ax_city.set_xlabel('City')
            ax_city.tick_params(axis='x', rotation=45)
            fig_city.tight_layout()
            st.pyplot(fig_city)
        else:
            st.info('No city data available')
    except Exception as e:
        st.error(f'Error displaying city-wise funding: {str(e)}')
    
    st.divider()
    
    # Top Startups
    st.subheader('&#128640; Top 10 Startups by Funding')
    top_startups = analysis_df.groupby('startup')['amount'].sum().sort_values(ascending=False).head(10)
    st.dataframe(top_startups.reset_index().rename(columns={'startup': 'Startup', 'amount': 'Total Funding (Cr)'}), use_container_width=True)
    
    # Top Investors
    st.subheader('&#128188; Top 10 Investors by Number of Deals')
    all_investors = get_all_unique_investors()
    investor_counts = []
    for inv in all_investors:
        count = len(get_investor_startups(inv))
        if count > 0:
            investor_counts.append((inv, count))
    
    investor_df = pd.DataFrame(investor_counts, columns=['Investor', 'Number of Deals']).sort_values('Number of Deals', ascending=False).head(10)
    st.dataframe(investor_df, use_container_width=True)

# ======================== INVESTOR POV ========================

def load_investor_details(investor):
    st.title(f'&#128176; {investor.title()}')
    
    investor_data = get_investor_startups(investor)
    
    if len(investor_data) == 0:
        st.warning(f'No investments found for {investor}')
        return
    
    # Summary Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric('Total Investments', len(investor_data))
    with col2:
        st.metric('Total Amount Invested (Cr)', round(investor_data['amount'].sum(), 2))
    with col3:
        st.metric('Avg Investment Size (Cr)', round(investor_data['amount'].mean(), 2))
    with col4:
        st.metric('Unique Startups', investor_data['startup'].nunique())
    
    st.divider()
    
    # Recent Investments
    st.subheader('&#128197; Most Recent Investments')
    recent_df = investor_data[['date', 'startup', 'vertical', 'city', 'round', 'amount']].sort_values('date', ascending=False).head(10)
    st.dataframe(recent_df, use_container_width=True)
    
    st.divider()
    
    # Biggest Investments
    col_big1, col_big2 = st.columns(2)
    
    with col_big1:
        st.subheader('&#128142; Biggest Investments')
        try:
            big_investments = investor_data.groupby('startup')['amount'].sum().sort_values(ascending=False).head(10)
            if len(big_investments) > 0 and (big_investments > 0).any():
                fig_big, ax_big = plt.subplots(figsize=(8, 5))
                ax_big.barh(big_investments.index, big_investments.values, color='#d62728')
                ax_big.set_xlabel('Amount (Cr)')
                fig_big.tight_layout()
                st.pyplot(fig_big)
            else:
                st.info('No investment data available')
        except Exception as e:
            st.error(f'Error displaying biggest investments: {str(e)}')
    
    with col_big2:
        st.subheader('&#127919; Sectors Invested In')
        sector_series = investor_data.groupby('vertical')['amount'].sum().sort_values(ascending=False)
        
        # Validate sector data
        if len(sector_series) > 0 and (sector_series > 0).any():
            fig_sector, ax_sector = plt.subplots(figsize=(8, 5))
            try:
                ax_sector.pie(sector_series.values, labels=sector_series.index, autopct='%1.1f%%', startangle=90)
                fig_sector.tight_layout()
                st.pyplot(fig_sector)
            except Exception as e:
                st.warning(f'Unable to display sector chart: {str(e)}')
        else:
            st.info('No valid sector data available for pie chart')
    
    st.divider()
    
    # Year-over-Year Trends
    st.subheader('&#128200; Year-over-Year Investment Trends')
    try:
        yoy_data = investor_data.groupby('year')['amount'].sum().sort_index()
        if len(yoy_data) > 0 and (yoy_data > 0).any():
            fig_yoy, ax_yoy = plt.subplots(figsize=(10, 4))
            ax_yoy.plot(yoy_data.index, yoy_data.values, marker='o', linewidth=2, markersize=8, color='#9467bd')
            ax_yoy.set_xlabel('Year')
            ax_yoy.set_ylabel('Amount Invested (Cr)')
            ax_yoy.grid(alpha=0.3)
            fig_yoy.tight_layout()
            st.pyplot(fig_yoy)
        else:
            st.info('No year data available')
    except Exception as e:
        st.error(f'Error displaying YoY trends: {str(e)}')
    
    st.divider()
    
    # Investment by Round Type
    st.subheader('&#128311; Investment Distribution by Round Type')
    try:
        round_dist = investor_data.groupby('round')['amount'].sum().sort_values(ascending=False)
        if len(round_dist) > 0 and (round_dist > 0).any():
            fig_round, ax_round = plt.subplots(figsize=(10, 5))
            ax_round.bar(range(len(round_dist)), round_dist.values, color='#17becf')
            ax_round.set_xticks(range(len(round_dist)))
            ax_round.set_xticklabels(round_dist.index, rotation=45)
            ax_round.set_ylabel('Amount (Cr)')
            fig_round.tight_layout()
            st.pyplot(fig_round)
        else:
            st.info('No round type data available')
    except Exception as e:
        st.error(f'Error displaying round distribution: {str(e)}')

# ======================== STARTUP/COMPANY POV ========================

def load_startup_details(startup):
    startup_data = get_startup_investors(startup)
    
    if len(startup_data) == 0:
        st.warning(f'No data found for startup: {startup}')
        return
    
    st.title(f'&#128640; {startup.title()}')
    
    # Basic Info
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric('Funding Rounds', len(startup_data))
    with col2:
        st.metric('Total Funding (Cr)', round(startup_data['amount'].sum(), 2))
    with col3:
        st.metric('Latest Round', startup_data['round'].iloc[-1] if len(startup_data) > 0 else 'N/A')
    with col4:
        st.metric('Total Investors', len(set([inv.strip() for inv in ','.join(startup_data['investors'].dropna()).split(',')])))
    
    st.divider()
    
    # Company Details
    st.subheader('&#128203; Company Information')
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.write(f"**Industry:** {startup_data['vertical'].iloc[0].title() if len(startup_data) > 0 else 'N/A'}")
        st.write(f"**Sub-industry:** {startup_data['subvertical'].iloc[0].title() if len(startup_data) > 0 else 'N/A'}")
        st.write(f"**Headquarters:** {startup_data['city'].iloc[0].title() if len(startup_data) > 0 else 'N/A'}")
    
    with col_info2:
        latest_date = startup_data['date'].max()
        st.write(f"**Latest Funding Date:** {latest_date.strftime('%B %d, %Y') if pd.notna(latest_date) else 'N/A'}")
        first_date = startup_data['date'].min()
        st.write(f"**First Funding Date:** {first_date.strftime('%B %d, %Y') if pd.notna(first_date) else 'N/A'}")
    
    st.divider()
    
    # Funding Timeline
    st.subheader('&#128181; Funding Timeline')
    timeline_df = startup_data[['date', 'round', 'amount', 'investors']].sort_values('date')
    st.dataframe(timeline_df, use_container_width=True)
    
    st.divider()
    
    # Funding Growth Chart
    st.subheader('&#128202; Cumulative Funding Over Time')
    try:
        timeline_sorted = startup_data.sort_values('date').copy()
        if len(timeline_sorted) > 0 and (timeline_sorted['amount'] > 0).any():
            timeline_sorted['cumulative'] = timeline_sorted['amount'].cumsum()
            
            fig_timeline, ax_timeline = plt.subplots(figsize=(10, 4))
            ax_timeline.plot(timeline_sorted['date'], timeline_sorted['cumulative'], marker='o', linewidth=2, markersize=8, color='#2ca02c')
            ax_timeline.set_xlabel('Date')
            ax_timeline.set_ylabel('Cumulative Funding (Cr)')
            ax_timeline.grid(alpha=0.3)
            fig_timeline.tight_layout()
            st.pyplot(fig_timeline)
        else:
            st.info('No timeline data available')
    except Exception as e:
        st.error(f'Error displaying timeline: {str(e)}')
    
    st.divider()
    
    # All Investors
    st.subheader('&#128101; All Associated Investors')
    all_inv = set()
    for inv_str in startup_data['investors'].dropna():
        if pd.notna(inv_str) and str(inv_str).strip():
            investors = [i.strip() for i in str(inv_str).split(',')]
            all_inv.update(investors)
    
    if all_inv:
        st.write(', '.join(sorted(all_inv)))
    else:
        st.info('No investor information available')
    
    st.divider()
    
    # Similar Companies
    st.subheader('&#129309; Similar Companies in Same Vertical')
    vertical = startup_data['vertical'].iloc[0] if len(startup_data) > 0 else None
    
    if vertical:
        similar = get_similar_startups(vertical)
        similar = similar[similar['startup'] != startup.lower()]
        
        if len(similar) > 0:
            similar_summary = similar.groupby('startup').agg({
                'amount': 'sum',
                'vertical': 'first'
            }).sort_values('amount', ascending=False).head(10).rename(columns={'amount': 'Total Funding (Cr)', 'vertical': 'Vertical'})
            st.dataframe(similar_summary, use_container_width=True)
        else:
            st.info('No similar companies found')

# ======================== MAIN APP ========================

st.sidebar.title('&#127970; Startup Funding Analysis Dashboard')
st.sidebar.markdown('---')

page = st.sidebar.radio('Select View', ['Overall Analysis', 'Investor Analysis', 'Startup Analysis'], label_visibility='collapsed')

if page == 'Overall Analysis':
    load_overall_analysis()

elif page == 'Investor Analysis':
    st.sidebar.subheader('Select Investor')
    all_investors = get_all_unique_investors()
    
    if len(all_investors) == 0:
        st.warning('No investors available in the dataset')
    else:
        selected_investor = st.sidebar.selectbox('Investor', all_investors, key='investor_select')
        
        if st.sidebar.button('View Details', key='investor_btn'):
            load_investor_details(selected_investor)
        else:
            st.info('&#128072; Select an investor and click "View Details" to see their investment portfolio')

elif page == 'Startup Analysis':
    st.sidebar.subheader('Select Startup')
    all_startups = sorted([s for s in df[df['startup'].notna()]['startup'].unique().tolist() if pd.notna(s) and str(s).strip()])
    
    if len(all_startups) == 0:
        st.warning('No startups available in the dataset')
    else:
        selected_startup = st.sidebar.selectbox('Startup', all_startups, key='startup_select')
        
        if st.sidebar.button('View Details', key='startup_btn'):
            load_startup_details(selected_startup)
        else:
            st.info('&#128072; Select a startup and click "View Details" to see their funding details')

# ======================== FOOTER ========================
st.divider()
footer_html = """
<div style='text-align: center; margin-top: 40px; padding: 20px; border-top: 2px solid #e0e0e0;'>
    <p style='color: #666; font-size: 14px; margin: 10px 0;'>
        <strong>Startup Funding Analysis Dashboard</strong>
    </p>
    <p style='color: #999; font-size: 13px; margin: 5px 0;'>
        © 2026 All rights reserved. Data sourced from Indian Startup Funding datasets.
    </p>
    <p style='color: #666; font-size: 13px; margin: 15px 0;'>
        <strong>Made with  <p style = 'color:crimson'> &#10084; </p> by Aditya Sharma</strong>
    </p>
    <p style='color: #bbb; font-size: 12px; margin: 10px 0;'>
        Built with Streamlit | Powered by Python &#128013;
    </p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)