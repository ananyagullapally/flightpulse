import streamlit as st
import duckdb

# Connect to DB
conn = duckdb.connect("data/flightpulse.duckdb")

st.title("✈️ FlightPulse Dashboard")

# Airline routes
st.header("Top Airlines by Routes")
airlines = conn.execute("""
    SELECT * FROM mart_airline_routes
    LIMIT 10
""").fetchdf()
st.dataframe(airlines)

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
