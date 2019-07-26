# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler as mini
from sklearn.model_selection import train_test_split
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler as mini
from sklearn.model_selection import train_test_split
data = pd.read_csv('data/BTC-USD.csv')
df0,df1 = data.shape[0], data.shape[1]
print('Bitcoin Data Has {} Transactions with {} features'.format(df0,df1))
data= data.drop(['Date'], axis =1)
data = data.drop('Adj Close',axis=1)
#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.
X= data.drop(['High'],axis=1)
y= data['High']
mini = mini()
X = mini.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.64)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X_train, y_train)

# Saving model to disk
pickle.dump(regressor, open('models/bit_model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('models/bit_model.pkl','rb'))
future_x = X
X = X[3290:3297]
# future_x = X[-1]
# x = X[:-1]
bata = pd.read_csv('data/BTC-USD.csv')
date = bata['Date']
date = date[3296:3297]
print(date)
bata = pd.read_csv('data/BTC-USD.csv')
date = bata['Date']
print('PREDICTED HIGH')
y = model.predict(future_x)
print(y[3296:3297])




eth_data = pd.read_csv('data/ETH-USD.csv')
df0,df1 = eth_data.shape[0], eth_data.shape[1]
print('{} dates'.format(df0))
eth_data= eth_data.drop(['Date'], axis =1)
eth_data = eth_data.drop('Adj Close',axis=1)
eth_X= eth_data.drop(['High'],axis=1)
eth_y= eth_data['High']
eth_X = mini.fit_transform(eth_X)
eth_X_train,eth_X_test,eth_y_train,eth_y_test = train_test_split(eth_X,eth_y,test_size=.64)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(eth_X_train, eth_y_train)

# Saving model to disk
pickle.dump(regressor, open('models/eth_model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('models/eth_model.pkl','rb'))
eth_future_x = eth_X
eth_X = eth_X[1443:1450]
    # future_x = X[-1]
    # x = X[:-1]
eth_bata = pd.read_csv('data/ETH-USD.csv')
eth_date = eth_bata['Date']
eth_date = eth_date[1443:1450]
print(eth_date)
eth_bata = pd.read_csv('data/ETH-USD.csv')
eth_date = eth_bata['Date']
print('PREDICTED HIGH')
eth_y = model.predict(eth_future_x)
print(eth_y[1443:1450])

eth_output =eth_y[1449:1450]


AAPL_data = pd.read_csv('data/AAPL.csv')
df0,df1 = AAPL_data.shape[0], AAPL_data.shape[1]
print('{} dates'.format(df0))
AAPL_data = AAPL_data.fillna(28.630752329973355)
AAPL_data= AAPL_data.drop(['Date'], axis =1)
AAPL_data = AAPL_data.drop('Adj Close',axis=1)
AAPL_X= AAPL_data.drop(['High'],axis=1)
AAPL_y= AAPL_data['High']
AAPL_X = mini.fit_transform(AAPL_X)
AAPL_X_train,AAPL_X_test,AAPL_y_train,AAPL_y_test = train_test_split(AAPL_X,AAPL_y,test_size=.64)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(AAPL_X_train, AAPL_y_train)

# Saving model to disk
pickle.dump(regressor, open('models/AAPL_model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('models/AAPL_model.pkl','rb'))
AAPL_future_x = AAPL_X
AAPL_X = AAPL_X[9730:9737]
    # future_x = X[-1]
    # x = X[:-1]
AAPL_bata = pd.read_csv('data/AAPL.csv')
AAPL_date = AAPL_bata['Date']
AAPL_date = AAPL_date[9736:9737]
print(AAPL_date)
AAPL_bata = pd.read_csv('data/AAPL.csv')
AAPL_date = AAPL_bata['Date']
print('PREDICTED HIGH')
AAPL_y = model.predict(AAPL_future_x)
print(AAPL_y[9736:9737])

AAPL_output =AAPL_y[9736:9737]


MSFT_data = pd.read_csv('data/MSFT.csv')
df0,df1 = MSFT_data.shape[0], MSFT_data.shape[1]
print('{} dates'.format(df0))
MSFT_data= MSFT_data.drop(['Date'], axis =1)
MSFT_data = MSFT_data.drop('Adj Close',axis=1)
MSFT_X= MSFT_data.drop(['High'],axis=1)
MSFT_y= MSFT_data['High']
MSFT_y.mean()
MSFT_X = mini.fit_transform(MSFT_X)
MSFT_X_train,MSFT_X_test,MSFT_y_train,MSFT_y_test = train_test_split(MSFT_X,MSFT_y,test_size=.64)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(MSFT_X_train, MSFT_y_train)

# Saving model to disk
pickle.dump(regressor, open('models/MSFT_model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('models/MSFT_model.pkl','rb'))
MSFT_future_x = MSFT_X
MSFT_X = MSFT_X[8404:8411]
    # future_x = X[-1]
    # x = X[:-1]
MSFT_bata = pd.read_csv('data/MSFT.csv')
MSFT_date = MSFT_bata['Date']
MSFT_date = MSFT_date[8410:8411]
print(MSFT_date)
MSFT_bata = pd.read_csv('data/MSFT.csv')
MSFT_date = MSFT_bata['Date']
print('PREDICTED HIGH')
MSFT_y = model.predict(MSFT_future_x)
print(MSFT_y[8410:8411])


MSFT_output =MSFT_y[8410:8411]


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler as mini
from sklearn.model_selection import train_test_split
dow_data = pd.read_csv('data/DJI.csv')
dow_df0,dow_df1 = dow_data.shape[0], dow_data.shape[1]
print(dow_df0)
dow_data= dow_data.drop(['Date'], axis =1)
dow_data = dow_data.drop('Adj Close',axis=1)
#Splitting Training and Test Set
#Since we have a very small dow_dataset, we will train our model with all availabe dow_data.
dow_X= dow_data.drop(['High'],axis=1)
dow_y= dow_data['High']
print(y[8686:8694])
mini = mini()
dow_X = mini.fit_transform(dow_X)

dow_X_train,dow_X_test,dow_y_train,dow_y_test = train_test_split(dow_X,dow_y,test_size=.64)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig dow_data
regressor.fit(dow_X_train, dow_y_train)

# Saving model to disk
pickle.dump(regressor, open('models/dow_model.pkl','wb'))

# Loading model to compare the results
dow_model = pickle.load(open('models/dow_model.pkl','rb'))
dow_future_x = dow_X
dow_X = dow_X[8692:8693]
# future_x = X[-1]
# x = X[:-1]
dow_bata = pd.read_csv('data/DJI.csv')
dow_date = dow_bata['Date']
dow_date = dow_date[8692:8693]
print(date)
dow_bata = pd.read_csv('data/DJI.csv')
dow_date = dow_bata['Date']
print('PREDICTED High')
dow_y = dow_model.predict(dow_future_x)
print(dow_y[8692:8693])
