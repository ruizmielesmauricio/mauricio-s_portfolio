
# Mauricio Ruiz | Portfolio
#### _Data Analyst and Journalist | Currently working at TikTok | Based in Dublin - Ireland_
#### Blog: [Life In Data](https://lifeindata.hashnode.dev)

## Projects:
----
### NASDAQ-100 ML Stock Price Predictions
[Analysis of macroeconomic metrics and prices of top twenty markets in NASDAQ 100 to predict behavior and returns using machine learning](https://github.com/ruizmielesmauricio/nasdaq100-macroeconomic-ml)

#### Summary:
The main purpose of this project is to use supervised machine learning algorithms combining with historical financial data from the top 20 markets in NASDAQ-100 along with
macroeconomic indicators to predict NASDAQ 100’s returns or losses as well as the direction it will move (bullish or bearish). The data was gathered from October 1st, 2015,
until November 29th,2024, and includes stock prices, volume and some other relevant features from the top 20 constituent stocks in NASDAQ 100 as well as data related to 
macroeconomic indicators such as Federal Funds Rate, CPI, M2 Money Supply, and Treasury Yields. By understanding how these factors interact and affect NASDAQ’s index 
returns it is possible to make better informed decisions when investing in the market.
The algorithm used is Extreme Gradient Boost (XGBoost) for the two models, which is known to perform accurately in time series for continuous variables as well as
categorical. Two models were trained, one for the market movement direction (bullish, bearish,or stable) and one for returns. The training is based on splitting
the data as follows: 80% training and 20% testing chronologically.
The accuracy for each model was measured using different metrics. The classification model resulted with an accuracy of 74% and a F1-Score of 0.78 predicting bullish 
movements. For the regression model, the metrics used were R2 with a score of 0.4609 and Root Mean Squared Error (RMSE) of 0.0081 which reflects predictions close to the
actual returns in the index.

### Kepler Exoplanet Classification
Add link to repo and description, findings, accuracy charts
