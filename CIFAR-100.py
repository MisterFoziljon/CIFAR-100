import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import cv2
st.set_page_config(page_title='CIFAR-100 klassifikatsiya',layout='wide')
model = tf.keras.models.load_model("model.h5")

title = "CIFAR-100 dataseti yordamida o'qitilgan modelni sinovdan o'tkazish"
header1 = "Model haqida ma'lumot"
header2 = "Faylni yuklang va predict qiling"

data_main = [["optimizer","Adam"],["loss funksiyasi","Categorical Cross Entropy"],
              ["epochs","10"],["train loss qiymati","1.0224"],
             ["train accuracy qiymati","0.7005"],
             ["evaluate loss qiymati","3.01020"],
             ["evaluate accuracy qiymati","0.3797"],
             ["parametrlar soni","8 283 908"]]

information = pd.DataFrame(data_main,columns=["Parametrlar","Qiymatlar"])

st.markdown("<h1 style='text-align: center;font-size: 30px;'>"+title+"</h1>", unsafe_allow_html=True)
col1,col2 = st.columns(2)
col1.markdown("<h1 style='text-align: center;font-size: 20px;'>"+header1+"</h1>", unsafe_allow_html=True)
col1.dataframe(information,use_container_width=True)

col2.markdown("<h1 style='text-align: center;font-size: 20px;'>"+header2+"</h1>", unsafe_allow_html=True)
image = col2.file_uploader("Faylni yuklang")

if image is not None:

    file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    
    c1,c2,c3 = col2.columns(3)
    c2.image(img, channels="BGR",use_column_width=True)
    
    if c2.button("Predict",use_container_width=True):
        # normalizatsiya
        img = np.array(img)
        img = cv2.resize(img,(32,32))
        img = img.astype('float32')/255
        img = img.reshape(1,32,32,3)

        classlar = ['apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 'bicycle', 'bottle',
                    'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'camel', 'can', 'castle', 'caterpillar', 'cattle',
                    'chair', 'chimpanzee', 'clock', 'cloud', 'cockroach', 'couch', 'crab', 'crocodile', 'cup',
                    'dinosaur', 'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster', 'house',
                    'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion', 'lizard', 'lobster', 'man',
                    'maple_tree', 'motorcycle', 'mountain', 'mouse', 'mushroom', 'oak_tree', 'orange', 'orchid',
                    'otter', 'palm_tree', 'pear', 'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy', 'porcupine',
                    'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket', 'rose', 'sea', 'seal', 'shark', 'shrew',
                    'skunk', 'skyscraper', 'snail', 'snake', 'spider', 'squirrel', 'streetcar', 'sunflower',
                    'sweet_pepper', 'table', 'tank', 'telephone', 'television', 'tiger', 'tractor', 'train', 'trout',
                    'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman', 'worm']

        one_hot = model.predict(img)
        index = np.argmax(one_hot)
        predict = classlar[index]
        probability=one_hot[0][index]
        
        result = {"Atributlar":["Class nomi","Ehtimollik"],"Qiymatlar":[predict,probability]}
        
        col1.dataframe(result,use_container_width=True)
