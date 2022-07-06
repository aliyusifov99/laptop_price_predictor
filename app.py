import streamlit as st
import pickle
import numpy as np
import pandas as pd
import base64

data = pd.read_csv('clean_data.csv')
pipe = pickle.load(open('model.pkl', 'rb'))

#set background image
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('bg.png')

#title
st.title('Laptop Price Predictor')

#inputs from user
company = st.selectbox('Company', data['Company'].unique())
type = st.selectbox('Type', data['TypeName'].unique())
cpu = st.selectbox('CPU', data['cpu_brand'].unique())
gpu = st.selectbox('GPU', data['Gpu'].unique())
ram = st.selectbox('RAM', [2,4,6,8,12,16,24,32,64,128])
hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD(in GB)', [0, 128, 256, 512, 1024, 2048])
opsys = st.selectbox('OS', data['OpSys'].unique())
ips = st.selectbox('IPS', data['IPS'].unique())
touchscreen = st.selectbox('Touchscreen', data['Touchscreen'].unique())
fourK = st.selectbox('4K', data['4k'].unique())
resolution = st.selectbox('Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'] )
screen_size = st.number_input('Screen Size(inch)', min_value=11.0, max_value=19.0, value=11.0)
weight = st.number_input('Weight', min_value=1.0)

#prediction using model
if st.button('Predict Price'):
    #calculate ppi
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res**2)) ** 0.5 / screen_size
    query = np.array([company, type, ram, gpu, opsys,weight, ips, touchscreen, fourK, ppi, cpu,hdd, ssd ])
    query = query.reshape(1, 13)
    df = pd.DataFrame(data=query, index=np.arange(len(query)), columns=['Company', 'TypeName', 'Ram', 'Gpu', 'OpSys', 'Weight', 'IPS',
        'Touchscreen', '4k', 'PPI', 'cpu_brand', 'HDD', 'SSD'])
    price = int(np.exp(pipe.predict(df)))
    price_in_usd = int(price * 0.013)
    st.title(f'The predicted price is {price_in_usd} $')


