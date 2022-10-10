import tensorflow as tf
import numpy as np
def model(data):
  model=tf.keras.models.load_model('server_model.h5')
  predicted=np.argmax(model.predict(np.array(data).reshape(-1,5)))
  drug_class=np.array(['drug Y','drug A','drug B','drug C','drug X'])
  return drug_class[predicted]

def std_minmax(a,minimum,maximum):
  return (a-minimum)/(maximum-minimum)  

def get_input(age,sex,bp,cholesterol,saltlevel):
  age=std_minmax(age,15,74)
  saltlevel=std_minmax(saltlevel,6.269,38.247)
  return model([age,sex,bp,cholesterol,saltlevel])

