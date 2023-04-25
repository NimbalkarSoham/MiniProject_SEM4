from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
from connection_db import conn


sql_query = '''select * from sangli_weather where DATE NOT like '%2023' '''
df_data = pd.read_sql_query(sql_query, conn)

query_2022 = '''select * from sangli_weather where DATE like '%2022' '''
data_2022 = pd.read_sql_query(query_2022, conn)
data_2022.replace(-999, None, inplace=True)
data_2022 = data_2022.ffill()

df_data.replace(-999, None, inplace=True)

df_data = df_data.ffill()

df = df_data

# Extract the features and target variables
X = df.drop(['DATE', 'YEAR', 'DOY', 'GWETTOP', 'GWETPROF',
             'PRECTOTCORR', 'T2MDEW'], axis=1)
y_prec = df['PRECTOTCORR']

# Split the dataset into training and testing sets
X_train, X_test, y_prec_train, y_prec_test = train_test_split(
    X, y_prec, test_size=0.2, random_state=42)

# Train a random forest regression model for precipitation
rf_prec = RandomForestRegressor(n_estimators=100, random_state=42)
rf_prec.fit(X_train, y_prec_train)

# Evaluate the models on the test set
y_prec_pred = rf_prec.predict(X_test)

# Calculate the root mean squared error (RMSE) for the models
prec_rmse = mean_squared_error(y_prec_test, y_prec_pred, squared=False)

# Make predictions for the next 6 months of temperature and precipitation
# Create a DataFrame for next 6 months with lagged temperature and precipitation values
X_pred = pd.DataFrame({'T2M': data_2022['T2M'],
                       'T2M_MAX': data_2022['T2M_MAX'],
                       'T2M_MIN': data_2022['T2M_MIN'],
                       'QV2M': data_2022['QV2M'],
                       'PS': data_2022['PS'],})

X_pred['PS'] += 0.064
X_pred['QV2M'] -= 0.40
X_pred['T2M'] += 0.53
X_pred['T2M_MAX'] += 0.84
X_pred['T2M_MIN'] += 0.20

y_prec_pred_next_six_months = rf_prec.predict(X_pred)

X_pred['Precipitation'] = y_prec_pred_next_six_months

next_12_months = pd.date_range(start='2023-01-01', periods=365, freq='D')

X_pred['Date'] = next_12_months
X_pred.set_index('Date', inplace=True)

df_sangli = X_pred
