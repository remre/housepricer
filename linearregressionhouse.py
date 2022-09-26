import pandas as pd 
from typing import Callable

from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, BayesianRidge
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error , mean_squared_log_error
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingGridSearchCV
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.ensemble import StackingRegressor
from sklearn import tree
from sklearn.tree          import DecisionTreeRegressor
from sklearn.ensemble      import RandomForestRegressor
from sklearn.ensemble      import ExtraTreesRegressor
from sklearn.ensemble      import AdaBoostRegressor
from sklearn.ensemble      import GradientBoostingRegressor
from sklearn import pipeline      # Pipeline
from sklearn import impute
import time
from sklearn import metrics   
from sklearn import compose

# call the dataframe
df =pd.read_csv('C:/Users/emreb/Documents/projects/houserentpre/dts/House_Rent_Dataset.csv')

# Seperate day month and year

df['Posted On'] = pd.to_datetime(df['Posted On'])
df['month'] = df['Posted On'].dt.month
df['year'] = df['Posted On'].dt.year
df2=df.copy()

# Seperate floor level and total floor and drop Floor column

df2 = df2.join(df['Floor'].str.split(' out of ', 1, expand=True).rename(columns={0:'floor level', 1:'total floor'}))
df2['floor level'] = df2.apply(lambda x: 0 if x['floor level'] =='Ground' \
                               else ( -2 if x['floor level'] =='Lower Basement' else -1 if x['floor level'] =='Upper Basement' else (x['floor level']) ) , axis=1)
# print("Status: Changed 'Ground'=0, 'Lower Basement'=-1, Rest = total floor")

df2.drop('Floor',axis=1,inplace=True)

def convertto_int(df,columns):
    for col in columns:
        df[col] = df[col].astype('int64')
        
    # return df
    
tonum_cols = ['floor level'], ['total floor']
df2.dropna(inplace=True)
convertto_int(df2,tonum_cols)
# df2['City'].unique()
# print(df['City'].unique())

df2= df2[~df2['Point of Contact'].str.contains("Contact Builder")]
df2 = df2[~df2['Area Type'].str.contains("Built Area")]
df2 = df2[df2.Rent < 3400000]

orcat_vars  = [ 'total floor', 'Area Type', 'Area Locality', 'Furnishing Status', 'Tenant Preferred'] 
nomcat_vars  = ['City', 'Point of Contact']
num_vars = ['BHK','Size','floor level','total floor','Bathroom','month','year']
cate_vars  = ['Furnishing Status', 'Tenant Preferred','Point of Contact','City','Area Type']
coltodrop = ['Area Locality', 'Posted On']

def one_hot_encode(df, column):
    # Get one hot encoding of columns B
    one_hot = pd.get_dummies(df[column])
    # Drop column as it is now encoded
    df = df.drop(column,axis = 1)
    # print(f"one hot encoded {column}")
    # Join the encoded df
    df = df.join(one_hot)
    return df
def drop_unnecs(df,columns):
    for col in columns:

        df.drop(col,axis=1,inplace=True)
    return df
def test_predict(model,X_train,X_test,y_train,y_test, parameters = None):
    model.fit(X_train, y_train)
    prediction_test = model.predict(X_test)
    model_text_list=[]; metric_list=[]; score_list=[] ; param_list=[]
    
    # create list of metric to be examined
    metric_functions = [r2_score, r2_score, mean_squared_error,mean_squared_error,mean_absolute_error]
    metric_functions_text = ['R_Squared', 'Adj_R_Squared', 'MSE','RMSE','MAE']
    
    # for loop of each of the 5 metrics
    for metric_function, metric_function_text in zip(metric_functions, metric_functions_text):
        if metric_function_text == 'Adj_R_Squared':
            Adj_r2 = 1 - (1-r2_score(y_test, prediction_test)) * (len(y)-1)/(len(y)-X.shape[1]-1)
            model_text_list.append(type(model).__name__); metric_list.append(metric_function_text); score_list.append(Adj_r2); param_list.append(parameters)
        elif metric_function_text == 'RMSE':
            rmse = mean_squared_error(y_test, prediction_test, squared=False)
            model_text_list.append(type(model).__name__); metric_list.append(metric_function_text); score_list.append(rmse); param_list.append(parameters)
        else:
            model_text_list.append(type(model).__name__); metric_list.append(metric_function_text); score_list.append(metric_function(y_test, prediction_test)); param_list.append(parameters) 
    
    d = {'model':model_text_list, 'parameters': param_list ,'metric': metric_list, 'test predict score': score_list}
    df = pd.DataFrame(data=d)
    return df


df3 = df2.copy()
drop_unnecs(df3,coltodrop)
for nom in cate_vars:

    df3 = one_hot_encode(df3,nom)





# numerical_features = df3.dtypes[df3.dtypes != "object"].index

# scaler = StandardScaler()
# df3[numerical_features] = scaler.fit_transform(df3[numerical_features])

X = df3.drop('Rent',axis=1)
y =df3[['Rent']].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
LinearRegression_test = test_predict(model, X_train,X_test,y_train,y_test)
print(LinearRegression_test)




# results_ord = results.sort_values(by=['MSE'], ascending=False, ignore_index=True)
# results_ord.index += 1 
# results_ord.style.bar(subset=['MSE', 'r2_score'], vmin=0, vmax=100, color='#5fba7d')
# lasomodel =  Lasso(alpha=1.0,max_iter=1000)
# Laso_test = test_predict(lasomodel, X_train,X_test,y_train,y_test)
# print(Laso_test)


# df2.loc[0,['Num','NAME']] = [100,'Python']