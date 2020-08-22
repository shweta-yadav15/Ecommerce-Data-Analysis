# Sales_Prediction

## Motivation
This project deals with many real- world challenges faced by e commerce websites including predicting customer lifetime value using RFM score and k-means clustering, customer segmentation to finf out best ones. As well as predicting review score they will give to their order experience depening on their location, order cost and other factors. I have also done a detailed analysis of how geolocation can affect user's experience and their purchase and much more.

---

## Dataset
Brazilian ecommerce public dataset of orders made at Olist Store. The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. Also included is a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates.

This dataset have nine tables which are connected with few similar attributes. 

---

## Files Description
This is the file-folder structure of the project.

```
.
├── app     
│   ├── run.py                           #Flask file that runs app
│   └── templates   
│       ├── go.html                      #Classification result page of web app
│       └── master.html                  #Main page of web app    
├── data                   
│   ├── disaster_categories.csv          #Dataset including all the categories  
│   ├── disaster_messages.csv            #Dataset including all the messages
│   └── process_data.py                  #Data cleaning
├── models
│   └── train_classifier.py              #Training ML model           
└── README.md
```
---

