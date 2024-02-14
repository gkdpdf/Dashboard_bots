import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")

from pymongo.mongo_client import MongoClient



#replace username and pwd from mongodb atlas
uri = "mongodb+srv://readb:readb@cluster0.ay8hame.mongodb.net/?retryWrites=true&w=majority"


# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


mydb_dashboard = client["Dashboard"]

records =mydb_dashboard['records']   

a=records.find()
b=pd.DataFrame(a)
b=b.drop("_id",axis=1)
print(b)





import plotly.express as px

col1, col2 = st.columns([5, 5])
with col1:

    
    # Create a line chart using Seaborn
    st.write("### Total Profit")
    sns.set_style("whitegrid")
    sns.lineplot(x='Date String', y='Cumulative Profit', data=b)
    st.pyplot()

with col2:
    # Create a line chart using Seaborn
    st.write("### ROI %")
    sns.set_style("whitegrid")
    sns.lineplot(x='Date String', y='ROI % till date', data=b)
    st.pyplot()
    
   

st.dataframe(b,width=2000)
