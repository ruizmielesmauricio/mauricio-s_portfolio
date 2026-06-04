
# Mauricio Ruiz | Portfolio
#### _Data Analyst and Journalist | Currently working at TikTok | Based in Dublin - Ireland_
#### Blog: [Life In Data](https://ruizmielesmauricio.github.io)

# Projects:
* TOC
{:toc}

## NASDAQ-100 ML Stock Price Predictions
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
actual returns in the index.<br>
**[Final Report](https://github.com/ruizmielesmauricio/nasdaq100-macroeconomic-ml/blob/main/results/figures/Mauricio_Ruiz_Report.pdf)** <br>
<table align="center">
  <tr>
    <th>Clasiffication Model Accuracy</th>
    <th>Regression Model Predictions</th>
  </tr>
  <tr>
    <td align="center">
     <img src="https://raw.githubusercontent.com/ruizmielesmauricio/nasdaq100-macroeconomic-ml/refs/heads/main/results/figures/clf_confusion_matrix.png" width="250">
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/ruizmielesmauricio/nasdaq100-macroeconomic-ml/refs/heads/main/results/figures/reg_actual_vs_pred_over_time.png" width="250">
    </td>
  </tr>
</table>

---
## Kepler Exoplanet Classification
[Machine Learning for Exoplanet Detection Using KOI Cumulative and Stellar Properties DR25 Datasets](https://github.com/ruizmielesmauricio/exoplanets-ml)
#### Summary:
The main aim of this project is to use five different machine learning algorithms to classify accurately if the celestial objects captured by the Kepler satellite are actual exoplanets. In order to do this, two different datasets have been used to train the models: Kepler Objects of Interest (KOI) cumulative data and Kepler stellar properties stored in Keplers Input Catalog - KIC (DR25). The five algorithms selected for this research are: Random Forest, Extreme Gradient Boosting (XGBoost) , Support Vector Machine, K-Nearest Neighbors (KNN), and Multi-Layer Perceptron (MLP). The accuracy of these models was assessed with different metrics after performing exploratory data analysis, feature engineering and tuning the algorithms’ parameters adequately. 
The tree-based models achieved the most accurate results overall, showing a more balanced performance (despite using only for these models imbalanced data) and predicting more accurately confirmed exoplanets as well as false positives.
SVM performed well overall but struggled in classifying possible candidates (class 1) and struggling to make accurate decisions in the mid-range of confidence levels as seen in the confidence plot.
KNN showed moderate accuracy performance but due to the high multidimensionality did not perform as well as other models. This model also predicted a high number of cases incorrectly with high confidence reducing reliability in its results. 
MLP achieved good accuracy, however, showed high confidence which leads to considering that needs to be calibrated in deeper level. This model also predicted incorrectly with high confidence which makes its results less reliable. 
Tree based models performed much better than the other models demonstrating their robustness and ability to perform with the current data. However, all the models seemed to have a higher accuracy in class 0 (FP) due to higher sample of that specific class. 
<br>**[Report](https://github.com/ruizmielesmauricio/exoplanets-ml/blob/98d4584e6c782548ec9b7445bdde6491b69e82c6/Results/Mauricio_Ruiz_Report.pdf.pdf)** <br>

<table align="center">
  <tr>
    <th>KNN</th>
    <th>MLP</th>
    <th>Random Forest</th>
    <th>SVM</th>
    <th>XGBoost</th>
  </tr>
  <tr>
    <td align="center">
     <img src="https://github.com/ruizmielesmauricio/exoplanets-ml/raw/main/Results/cm_knn.png" width="250">
    </td>
    <td align="center">
      <img src="https://github.com/ruizmielesmauricio/exoplanets-ml/raw/main/Results/cm_mlp.png" width="250">
    </td>
    <td align="center">
      <img src="https://github.com/ruizmielesmauricio/exoplanets-ml/raw/main/Results/cm_random_forest.png" width="250">
    </td>
    <td align="center">
      <img src="https://github.com/ruizmielesmauricio/exoplanets-ml/raw/main/Results/cm_svm.png" width="250">
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/ruizmielesmauricio/exoplanets-ml/refs/heads/main/Results/cm_xgboost.png" width="250">
    </td>
  </tr>
</table>


---
## Big Four Thrash Metal Dashboard
[The Big Four of Thrash Metal in Data](https://github.com/ruizmielesmauricio/BigFour)
#### Summary:
This project presents an interactive data analytics dashboard exploring the musical and audience characteristics of the “Big Four” of thrash metal: Metallica, Megadeth, Slayer, and Anthrax. The analysis combines data from multiple sources, including MusicBrainz, Last.fm, and GetSongBPM, to build a unified dataset covering discographies, track popularity, and musical features such as tempo (BPM).
A structured data pipeline was implemented to extract, clean, and merge the data, followed by feature engineering to generate album-level metrics such as total streams, listener counts, and average BPM. Exploratory data analysis was conducted to identify trends in popularity and musical style, including top tracks, dominant albums, and differences in tempo across bands.
The final output is a fully interactive dashboard built with Streamlit and Plotly, allowing users to explore key insights, compare albums, and analyze band performance dynamically. Visualizations include popularity comparisons, tempo distributions, and relative dominance metrics using ratio matrices.
The analysis highlights clear contrasts between the bands, with Metallica leading in overall popularity, while Slayer stands out for higher tempo characteristics. This project demonstrates practical skills in data engineering, API integration, feature engineering, and data visualization, delivering both analytical insights and a user-friendly interface for exploration.
<br>**[Dashboard](https://ruizmielesmauricio.github.io/BigFour/)**
<br>**[Report](https://github.com/ruizmielesmauricio/BigFour/blob/main/Report.md)** <br>

<div style="text-align:center;">
  <h3 style="color:#e53935;">Preview</h3>
  <img src="https://raw.githubusercontent.com/ruizmielesmauricio/BigFour/refs/heads/main/Images/section_1.png" width="650">
</div>

---
## Death Discography Overview
[Death Albums Overview](https://github.com/ruizmielesmauricio/death_discography)  
[Report](https://github.com/ruizmielesmauricio/death_discography/blob/main/README.md)

**[Dashboard](https://deathdiscography-h9p46woir6f86utjcw2ikh.streamlit.app)**

#### Summary: 
Built an interactive music analytics dashboard focused on the complete studio discography of the band Death using Python and Streamlit. The project involved collecting, cleaning, and integrating data from multiple APIs and sources, including Spotify, Last.fm, MusicBrainz, and AcousticBrainz.
The workflow included retrieving official studio albums, filtering tracklists to retain only original releases, enriching the dataset with release dates, album artwork, listener statistics, playcounts, durations, and BPM information, and handling API inconsistencies and remastered-release metadata issues through custom data-cleaning logic.
The final dataset was transformed into an interactive Streamlit dashboard featuring:
- Album exploration and timeline analysis
- BPM and duration analytics
- Listener and playcount insights
- Track-level filtering and ranking
- Album-vs-album comparison tools
- Dynamic visualizations using Plotly  


The project demonstrates skills in:  
1. API integration  
2. Data wrangling and cleaning  
3. Exploratory data analysis  
4. Interactive dashboard development  
5. Python data tooling (Pandas, Requests, Plotly, Streamlit)  
6. GitHub version control and deployment through Streamlit Cloud

<div style="text-align:center;">
  <h3 style="color:#e53935;">Preview</h3>
  <img src="https://raw.githubusercontent.com/ruizmielesmauricio/death_discography/refs/heads/main/death_album_artworks/death.png" width="650">
</div>


---
## Ask My AI Portfolio Assistant

<section style="margin-top: 40px; width: 100%;">

  <p>
    Ask questions about my experience, projects, skills, education, and data analytics work.
  </p>

  <iframe
    src="https://mauricio-ai-cv-assistant.streamlit.app/?embed=true"
    style="width: 100%; min-height: 900px; border: 1px solid #ddd; border-radius: 12px; background: white;"
    frameborder="0"
    scrolling="yes">
  </iframe>
</section>

<a
  href="https://mauricio-ai-cv-assistant.streamlit.app"
  target="_blank"
  style="display: inline-block; padding: 12px 18px; border-radius: 8px; border: 1px solid #ddd; text-decoration: none;">
  Open AI Portfolio Assistant
</a>
