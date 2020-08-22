# Sales_Prediction

## Motivationg
This project deals with many real-world challenges faced by e-commerce websites that includes predictin customer lifetime value using RFM score and k-means clustering, customer segmentation to find out best valued customers. Also, predicting review score they customers will give to their order experience depending on their location, order cost and other factors. I have also done a detailed analysis of how geolocation can affect user's experience and their purchase and much more.

---

## Dataset
Brazilian ecommerce public dataset of orders made at Olist Store. The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. Also included is a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates.

This dataset have nine tables which are connected with few common attributes.
https://www.kaggle.com/olistbr/brazilian-ecommerce

---

## Files Description
This is the file-folder structure of the project.

```
.
├── preprocessing_analysis     
│   ├── geolocation_analysis.ipynb                        #Detailed analysis related to geolocation of a customer
│   └── overall_data_analysis.ipynb                       #Data analysis from all the files to better understand data
|   └── understanding_metrics.ipynb                       #Metrics like new customer vs old customers
|
├── predictions                   
│   ├── customer_lifetime_value_prediction.ipynb          #Predicting which customer is most important to act accordingly  
│   └──predicting_customer_satisfaction                   #Customer review score prediction
|
├── customer_segmentation.ipynb                           #Dividing customers as active, non active using RFM matrix
│           
└── README.md
```
---

