import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
)


st.markdown("""
<style>
    .main { background-color: #0d1117; }
    h1, h2, h3, h4, h5, h6 { color: #e6e6e6 !important; }
    p, div, span { color: #d0d7de !important; }
    .metric { background-color: #161b22 !important; padding: 12px; border-radius: 12px; }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    return pd.read_csv("/Users/hibrizi/Project/hotel-segmentation-dashboard/data/user_features_with_clusters.csv")

df = load_data()


cluster_names = {
    0: "Cancellation-Prone",
    1: "Regular Users",
    2: "Active Planners",
    3: "Loyal High-Spenders"
}

df["cluster_name"] = df["cluster"].map(cluster_names)

numeric_cols = [
    "total_bookings", "cancel_rate", "mean_adr", "avg_stay_nights",
    "special_requests_mean", "booking_changes_mean", "used_promo_rate",
    "recency_days", "loyalty_index", "engagement_score"
]


st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Menu:",
    ["Home", "Cluster Overview", "Behavioral Heatmap", "Cluster Explorer"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("Developed by **Falah R. Hibrizi** 🔥")


if page == "Home":
    st.title("📊 Customer Segmentation Dashboard")
    st.markdown("Explore behavioral patterns and key characteristics across customer segments.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Users", f"{len(df):,}")
    col2.metric("Avg Bookings", f"{df.total_bookings.mean():.2f}")
    col3.metric("Avg ADR", f"{df.mean_adr.mean():.2f}")
    col4.metric("Avg Engagement", f"{df.engagement_score.mean():.2f}")


    st.markdown("### 👥 Cluster Size Distribution")
    cluster_counts = df["cluster_name"].value_counts()

    fig = px.bar(
        cluster_counts,
        text=cluster_counts.values,
        color=cluster_counts.values,
        color_continuous_scale="Blues",
        title="Number of Customers per Cluster"
    )
    st.plotly_chart(fig, use_container_width=True)


elif page == "Cluster Overview":
    st.title("👥 Cluster Overview")

    fig = px.pie(
        df,
        names="cluster_name",
        title="Cluster Distribution (%)",
        hole=0.45,
        color="cluster_name",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📌 Segment Summaries")
    st.write("""
    - **Cancellation-Prone** → High cancellations, low engagement  
    - **Regular Users** → Stable behavior, moderate spenders  
    - **Active Planners** → High engagement, many booking changes  
    - **Loyal High-Spenders** → High revenue, frequent bookings  
    """)


elif page == "Behavioral Heatmap":
    st.title("🔥 Behavioral Feature Heatmap")

    cluster_profile = df.groupby("cluster_name")[numeric_cols].mean().reset_index()

    fig = px.imshow(
        cluster_profile[numeric_cols],
        x=numeric_cols,
        y=cluster_profile["cluster_name"],
        color_continuous_scale="Teal",
        title="Average Feature Values by Cluster"
    )
    st.plotly_chart(fig, use_container_width=True)


elif page == "Cluster Explorer":
    st.title("🔍 Cluster Explorer")

    selected = st.selectbox("Select Cluster:", df["cluster_name"].unique())
    filtered = df[df["cluster_name"] == selected]

    st.markdown(f"### 📌 Segment: **{selected}**")
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Bookings", f"{filtered.total_bookings.mean():.2f}")
    col2.metric("Avg ADR", f"{filtered.mean_adr.mean():.2f}")
    col3.metric("Avg Engagement", f"{filtered.engagement_score.mean():.2f}")

    feature = st.selectbox("Feature Distribution:", numeric_cols)
    fig = px.histogram(
        filtered,
        x=feature,
        nbins=25,
        color="cluster_name",
        title=f"{feature} Distribution for {selected}"
    )
    st.plotly_chart(fig, use_container_width=True)
