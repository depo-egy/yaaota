# Yaaota Task

## Disclaimer:
In this project , I did the required task as given by the cto of Yaaota , which includes:
<ol>
<li>Scraping the urls and titles from https://2b.com.eg/ </li>
<li>Saving this data to sqlite database </li>
<li>Build NLP based machine learning model to detect the category of a certain item</li>
<li>Api for such request </li>
</ol>

Note: Due to heavy workload , I worked on the task for 3 days instead of 5 days (Friday, Saturday, Sunday)</br>
      I did not use any backend

## Technology used:
<ol>
<li>Scraping: I used Scrapy for two reason:
    <ol>
     <li>
         To emphasize on the fact that I can learn any new technology , this is the first time to used scrapy , before I used beautifulsoup and selenium.
     </li>
     <li>
        To get benefit from features of scrapy: the database pipeline, and scrapy shell.
     </li>
    </ol>
</li>
<li>ML model: used sklearn , pandas , ntlk , joblib for serializing , jupyter notebook for developing.</li>
<li>Api: used Flask </li>
</ol>

Finally , I used Docker for production-level deployment. I built dockerfile and docker-compose for such jobs.

## Model:
       Model selection: used cross validation to select a model from 7 models.</br>
       Imbalanced data: used SMOTE. </br>
       Model Evaluation: Used F1 score. </br>
       Data Cleaning: Actually it was almost clean without missing data since we used scraping to gather data. </br>
       Preprocessing: used NTLK for nlp preprocessing.</br>

