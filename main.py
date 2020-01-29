import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation,Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import Callback,EarlyStopping
import random
import sys

inFile = sys.argv[2]


input=[]
with open(inFile, 'r') as filehandle:
	for line in filehandle:
		line = line[:-1]
		input.append(line)
def fizzbuzz1(i): #software 1
  a=i%3;
  b=i%5;
  if((a+b)==0):
    return("fizzbuzz")
  elif(a==0):
    return("fizz")
  elif(b==0):
    return("buzz")
  else: 
    return(str(i))
def fizzbuzz2(i): #software 2
  a=i%3;
  b=i%5;
  if((a+b)==0):
    return [0,0,0,1]
  elif(a==0):
    return [0,1,0,0]
  elif(b==0):
    return [0,0,1,0]
  else: 
    return [1,0,0,0]


def dec2bin10(i):#Decimal 2 Binary Conversion
  binrep=np.zeros(10)
  j=9;
  while(i!=0):
    binrep[j]=i%2;
    i=int(i/2);
    j=j-1;
  return binrep

def fizz_buzz_pred(i, pred): # return predicted result
    return [str(i), "fizz", "buzz", "fizzbuzz"][pred.argmax()]

input = np.array(list(map(int, input))) #converting string list to integer list
m=len(input);
f1=open('Software1.txt','w');
f2=open('Software2.txt','w');
model = tf.keras.models.load_model('./model/my_model2.h5')
errors=0;
correct=0;
for i in range(m):
    f1.write(fizzbuzz1(input[i])); # Writng Output using Software 1(if-else)
    f1.write('\n');
    x = dec2bin10(input[i])
    y = model.predict(np.array(x).reshape(-1,10))
    f2.write(fizz_buzz_pred(input[i],y)); # Writng Output using Software 2 (neural network)
    f2.write('\n');
    
    
f1.close()
f2.close()
