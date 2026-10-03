import streamlit as st
import joblib
import numpy as np
model = joblib.load('reg_model')
df = joblib.load('laptop_data')

st.title("Laptop price prediction App")
st.caption("Please provide the specification and click on Predict Price")
st.caption("This ML model is based on 1200 old laptops only, might not give the accurate predictions")

company = st.selectbox("Manufacturer of the laptop",df['Company'].unique(),index=4)
typename = st.radio("Type of laptop",df['TypeName'].unique(),index=1,horizontal=True)
cpu = st.selectbox("Processor of the laptop",df['Cpu'].unique())
ram = st.radio("Ram on laptop(in GB)",[4,8,12,16,24,32,64,128],index=1,horizontal=True)
gpu = st.selectbox("Graphic on the laptop",df['Gpu'].unique(),index=1)
os = st.selectbox("OS of the laptop",df['OpSys'].unique(),index=2)
weight = st.slider("Weight of the laptop",min_value=0.7,max_value=5.0,step=0.1,value=1.8)
touchscreen = st.radio("Touchscreen?",['Yes','No'],index=1,horizontal=True)
ips = st.radio("IPS Display",['Yes','No'],index=1,horizontal=True)
hdd = st.radio("HDD",[0,128,500,1000],index=0,horizontal=True)
ssd = st.radio("SDD",[0,128,500,1000],index=0,horizontal=True)
screensize = st.slider("Screensize(measured diagonally, in inches)",min_value=9.5,max_value=18.5,step=0.1,value=15.6)
screen_resolution = st.selectbox("Screen resolution",[
    "2560x1600","1440x900","1920x1080","2880x1800","1366x768","2304x1440","3200x1800",
    "1920x1200","2256x1504","3840x2160","2160x1440","2560x1440","1600x900","2736x1824",
    "2400x1600"],index=2)

if st.button("Predict Price"):
    X_res = int(screen_resolution.split('x')[0])
    Y_res = int(screen_resolution.split('x')[1])
    ppi = round(np.sqrt(X_res**2 + Y_res**2)/screensize) #calculate the screen resolution
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    query = np.array([[company,typename,cpu,ram,gpu,os,weight,touchscreen,ips,hdd,ssd,ppi]])
    op = model.predict(query)
    st.subheader(f"The estimated laptop price for given specification is {int(round(op[0],-2))}")

