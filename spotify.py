import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Spotify Songs")

# Lê o CSV
@st.cache_data
def load_date():
    df = pd.read_csv("01 Spotify.csv")
    return df

df = load_date()
st.session_state["df_Spotify"] = df

df.set_index("Track",inplace=True)
artists = df["Artist"].value_counts().index
artist =st.sidebar.selectbox("Artista",artists)
df_filtered = df[df["Artist"] == artist]

albums = df_filtered["Album"].value_counts().index
album = st.selectbox("Album",albums)
df_filtered2 = df[df["Album"] == album]

col1,col2 = st.columns([0.7,0.3])
col1.bar_chart(df_filtered2["Stream"])
col2.line_chart(df_filtered2["Danceability"])

st.write(artist)


