import streamlit as st
from PIL import Image
import pandas as pd
import joblib


st.title("College Football Project")
st.write("Here are some College football Stats")

df = pd.read_csv('cfb_off.csv')
st.dataframe(df)
st.write("Here is the Top 25 Offenses compared to the Bottom 25 Offenses")
image = Image.open("offensive_stats_comparison.png")

# Display the image with a caption
st.image(image, caption="Sample Image", width=400)


libertyvssouthernmiss = Image.open("liberty_vs_southern_miss.png")
st.write("This is what the top offense in the country(Liberty) on average does compared to the worst offense on average(Southern Miss)")
# Display the image with a caption
st.image(libertyvssouthernmiss, caption="Sample Image", width=400)

st.write("The next image is what the average offensive and defensive ranks are for the best team in country and 2022 National Championship Winner, the Georgia Bulldogs")


georgia = Image.open('georgia_performance_plot.png')

# Display the image with a caption
st.image(georgia, caption="Sample Image", width=400)

st.write('Nebraska is one of the more unique teams in football. You can see they consistantly are average in every stat but only win around 33% of their games')
neb = Image.open('nebraska_vs_iowa_comparison.png')

# Display the image with a caption
st.image(neb, caption="Sample Image", width=400)

Off_TDs = st.slider("Select the number of offensive touchdowns scored", min_value=1, max_value=100)
Off_Rank = st.slider("Select the Off rank of the team", min_value=1, max_value=133)
Def_Rank = st.slider("Select the Deff rank of the team", min_value=1, max_value=133)
Touchdowns = st.slider("Select how many TDs the team scored in total", min_value=1, max_value=300)
Yards_Play_Allowed = st.slider("Select the yards a team gave up per game on defense", min_value=1, max_value=700)
st.dataframe(df)
cfb_df = pd.DataFrame({
    "Off TDs": [Off_TDs],
    "Off Rank": [Off_Rank],
    "Def Rank": [Def_Rank],
    "Touchdowns": [Touchdowns],
    "Yards/Play Allowed": [Yards_Play_Allowed],
    
})
chosen = st.selectbox('Choose your model', ['Linear Regression'])


if chosen == 'Linear Regression':
    data = joblib.load('TEAMRANK.joblib')

model = data["model"]
Win_PCT_prediction = model.predict(cfb_df)

st.write("Predicted WIN%:", Win_PCT_prediction)