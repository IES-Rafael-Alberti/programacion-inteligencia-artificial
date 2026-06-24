

import threadpoolctl
from sklearn.preprocessing import StandardScaler
from pathlib import Path
import os
import numpy as np
import pandas as pd
print(pd.__version__)
print(np.__version__)

filename = 'Euromillones'

df = pd.read_csv('./'+filename+'.csv')
df = df.drop(['No.', 'Date', 'Jackpot','Wins'], axis=1)

df.columns = ['A', 'B', 'C', 'D', 'E', 'Bonus', 'Extra']
scaler = StandardScaler().fit(df.values)

from keras.models import Sequential
from keras.models import load_model
from keras.layers import LSTM, Dense, Dropout

import numpy as np

batch_size = 25


model = load_model('./input/'+filename+'.h5')
to_predict=df.loc[-5:]
scaled_to_predict=scaler.transform(to_predict)

scaled_predicted_output_1 = model.predict(np.array([scaled_to_predict]))
data = scaler.inverse_transform(scaled_predicted_output_1).astype(int)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'Bonus', 'Extra'])
df.to_csv(''+filename+'.csv', index=False)
print(df)