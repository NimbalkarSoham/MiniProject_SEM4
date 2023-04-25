from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from connection_db import conn


sql_query = '''select * from sangli_crop_price'''
dataset = pd.read_sql_query(sql_query, conn)

X = dataset['Year'].to_numpy()  # Input variables
# Output variable
y = dataset['WHEAT HARVEST PRICE (Rs per Quintal)'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

X_train = X_train.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)


regressor = LinearRegression()
regressor.fit(X_train, y_train)

price_2017 = regressor.predict([[2017]])
price_2018 = regressor.predict([[2018]])
price_2019 = regressor.predict([[2019]])
price_2020 = regressor.predict([[2020]])
price_2021 = regressor.predict([[2021]])
price_2022 = regressor.predict([[2022]])
price_2023 = regressor.predict([[2023]])
next_year_price = regressor.predict([[2024]])

y_pred = regressor.predict(X_test)
r2_score(y_test, y_pred)

prices = np.append(y, [price_2017, price_2018, price_2019, price_2020,
                   price_2021, price_2022, price_2023, next_year_price])
year = np.append(X, [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])

Sangli_price_df = pd.DataFrame({'Year': year,
                                'Rate': prices})
Sangli_price_df.set_index('Year', inplace=True)
