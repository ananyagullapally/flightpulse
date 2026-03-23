import streamlit as st
import duckdb

# Connect to DB
conn = duckdb.connect("data/flightpulse.duckdb")

# Airline routes
st.title("✈️ FlightPulse Dashboard")

st.markdown("---")

total_routes = conn.execute("SELECT COUNT(*) FROM raw.flights").fetchone()[0]
st.metric("Total Routes Processed", total_routes)

st.header("Top Airlines by Routes")
airlines = conn.execute("""
    SELECT * FROM mart_airline_routes
    LIMIT 10
""").fetchdf()

st.dataframe(airlines)
st.bar_chart(airlines.set_index("airline")["total_routes"])

# Airport activity
st.header("Top Airports")
airports = conn.execute("""
    SELECT * FROM mart_airport_activity
    LIMIT 10
""").fetchdf()

st.dataframe(airports)

# Route frequency
st.header("Most Frequent Routes")
routes = conn.execute("""
    SELECT * FROM mart_route_frequency
    LIMIT 10
""").fetchdf()

st.dataframe(routes)
