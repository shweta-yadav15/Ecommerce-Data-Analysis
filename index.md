# Motivation

This project deals with many real-world challenges faced by e-commerce websites that includes predicting customer lifetime value using RFM score and k-means clustering, customer segmentation to find out best valued customers. Also, predicting review score that customers will give to their order experience depending on their location, order cost and other factors. I have also done a detailed analysis of how geolocation can affect user's experience and their purchase and much more.

# Dataset

Brazilian ecommerce public dataset of orders made at Olist Store. The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. Also included is a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates.

This [dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce) have nine tables which are connected by common attributes.

# Project Overview
The project is divided into two parts:
1. Analysis and Visualizations- Comprehensive anaysis, understanding metrics and graph plotting
2. Predictions- Customer lifetime value prediction, predicting customer satisfaction and segmentation

# Part 1: Analysis and Visualizations
Few instances of the analysis performed are as follows:

![Overall_Study](https://user-images.githubusercontent.com/33171500/93948439-b14fa880-fcfb-11ea-84af-6e86ebf28120.png)
 
![Overall_Study](https://user-images.githubusercontent.com/33171500/93949050-32f40600-fcfd-11ea-8a44-2dbbab31dec0.png)


* There is an upward trend in orders purchased between January 2017 and July 2018.

![Overall_Study](https://user-images.githubusercontent.com/33171500/94201775-b470a300-fe79-11ea-9a28-f1ce486a3e37.png)

* Unfortunately, customers who live in the north and northeast of Brazil have to bear with higher freight costs and has to wait longer to receive their purchase.

![Overall_Study](https://user-images.githubusercontent.com/33171500/94201805-bcc8de00-fe79-11ea-8ce8-b1f2765baa78.png)

* The consequence of late delivery is that the customers in north side are likely to give lower reviews.

![Overall_Study](https://user-images.githubusercontent.com/33171500/94201827-c4888280-fe79-11ea-9f82-d89287ebe4ae.png)

* Most of the revenue is coming from the Southeast and South regions of Brazil. Also, large cities and capitals, where population is bigger, have larger participation on revenue.

![Overall_Study](https://user-images.githubusercontent.com/33171500/94201844-ca7e6380-fe79-11ea-9c92-f567882fd6c9.png)

* Monthly retention rate shows whether customers continue to buy products from the website or not. There is an upward linear trend here but with few major exceptions.

![Overall_Study](https://user-images.githubusercontent.com/33171500/93948977-0809b200-fcfd-11ea-9fc3-f4d1d4260d97.png)

* Monday blues is showing effect on purchases. Customers seem to most likely buy on Monday then any other day of the week.

![Overall_Study](https://user-images.githubusercontent.com/33171500/93948981-093adf00-fcfd-11ea-8c33-4bfd19192380.png)

* Afternoon boredom is making customers buy more items then any other time of the day.

![Overall_Study](https://user-images.githubusercontent.com/33171500/94202035-20eba200-fe7a-11ea-8aeb-63dca33cc5c0.png)

* Company seems to be doing well in terms of delivery time since most of the orders are getting delivered way before they are expected.

![Overall_Study](https://user-images.githubusercontent.com/33171500/93949045-31c2d900-fcfd-11ea-85a9-14a4ee60614b.png)


# Part 2: Predictions

## 2.1 Predicting Customer Satisfaction: what score will a customer give for the order

The model helps to find a way to estimate that i.e. based on data about the product and order what will be the customer review score.

**The main hypothesis is that the product and how the order was fulfilled might influence the customer review score. Keeping in mind that each feature created is a new hypothesis to test.**

**Designing an Experiment:<br>
To answer the question data is collected from each order.From placing the order up to the delivery phase. With that, the model implemented estimates what will be the score given by the customer at the review phase.**

  Purchase   -->   Transport   -->   Delivery   -->   Review<br>
      [ Extract Features ]             [ Make Prediction ]

### 2.1.1 Cleaning and Feature Engineering
![data](https://user-images.githubusercontent.com/33171500/94206088-dbcb6e00-fe81-11ea-91a5-340233891e74.png)

The data was a mix of categorical, numerical as well as null values in 9 columns. In order to guarantee that the same transformation is applied to new/unseen data, I created custom transformers using scikit-learn BaseEstimator. Also, seven new features were engineered for better results: Working Days Estimated Delivery Time, Actual Delivery Time, Delivery Time, Is Late, Average Product Value, Total Order Value, Order Freight Ratio and Purchase Day of Week.

### 2.1.2 Model Building
- I created two separate pipelines for categorical and numerical data. 
- In categorical pipeline, to deal with missing values I used imputation of most frequent values and then applied one hot encoding. 
- In numerical pipeline, I used median imputation for null values and then standard scaling.
- Since the data was highly imbalanced, I used Stratified Shuffle Split that preserves the percentage of samples for each class. 
- Among k-Neighbors, Decision Tree, Random Forest, AdaBoost and Gradient BoostingClassifier, Random Forest classifier gave the best accuracy of 62%. I am planning to do the hyperaprameter tuning in future to improve the score.

## 2.2 Customer Segmentation
All customers using the website are not equally important, they have different needs and their own different profile. Our actions should adapt depending on that. There are different segmentations depending on what we are trying to achieve. To increase retention rate, we can do a segmentation based on churn probability and take actions. I am using RFM here. <br>
**RFM stands for Recency - Frequency - Monetary Value.**

There are three segments of customers in this case:
1. **Low Value**: Customers who are less active than others, not very frequent buyer/visitor and generates very low - zero - maybe negative revenue.
2. **Mid Value**: In the middle of everything. Often using the platform (but not as much as High Values), fairly frequent and generates moderate revenue.
3. **High Value**: The group we don’t want to lose. High Revenue, Frequency and low Inactivity.<br>

I calculated the Recency, Frequency and Monetary Value (called Revenue from now on) and apply unsupervised machine learning to identify different groups (clusters) for each.

### 2.2.1 Recency - To calculate recency, I used most recent purchase date of each customer and see how many days they are inactive for. After having no. of inactive days for each customer applied K-means clustering to assign customers a recency score.
The plot shows how is the distribution of recency across the customers with customer id on x-axis and recency on y-axis.

![pic](https://user-images.githubusercontent.com/33171500/94212238-dcb7cc00-fe90-11ea-91e2-a34f2d1832b9.png)

### 2.2.2 Frequency - To create frequency clusters, used total number of orders for each customer.
The x-axis on the plot shows number of times a customer bought a product and y-axis is frequeny. The plot is right skewed with most of the customers buying products less then 5 times or more specifically just one time.

![pic](https://user-images.githubusercontent.com/33171500/94212240-de818f80-fe90-11ea-9613-ef307c76f978.png)
### 2.2.3 Revenue - 
The plot has number of products on x-axis and revenue in Brazilian Reais (BRL) on y-axis. This plot is also right skewed with most of the products having very high monetary value.
![pic](https://user-images.githubusercontent.com/33171500/94212249-e2adad00-fe90-11ea-811b-5e589ae3f983.png)

### 2.2.4 Overall Score -

![pic](https://user-images.githubusercontent.com/33171500/94212296-040e9900-fe91-11ea-969c-efd3878ca7fa.png)

The scoring above clearly shows us that customers with score 8 is our best customers whereas 0 is the worst.<br>
To keep things simple the scores are renamed:<br>
0 to 2: Low Value<br>
3 to 4: Mid Value<br>
5+: High Value<br>

![pic](https://user-images.githubusercontent.com/33171500/94212304-07098980-fe91-11ea-85ca-5a16c9c4fadc.png)
![pic](https://user-images.githubusercontent.com/33171500/94212308-0a047a00-fe91-11ea-8d9d-3a41111c627b.png)
You can see how the segments are clearly differentiated from each other in terms of RFM.<br>

**We can start taking actions with this segmentation. The main strategies are quite clear:<br>
High Value: Improve Retention<br>
Mid Value: Improve Retention + Increase Frequency<br>
Low Value: Increase Frequency**

## 2.3 Customer Lifetime Value Prediction
We invest in customers (acquisition costs, offline ads, promotions, discounts & etc.) to generate revenue and be profitable. Naturally, these actions make some customers super valuable in terms of lifetime value but there are always some customers who pull down the profitability. We need to identify these behavior patterns, segment customers and act accordingly.

To calculate Lifetime Value first we need to select a time window. It can be anything like 3, 6, 12, 24 months. By the equation below, we can have Lifetime Value for each customer in that specific time window: <br>
**Lifetime Value: Total Gross Revenue - Total Cost**

This equation now gives us the historical lifetime value. If we see some customers having very high negative lifetime value historically, it could be too late to take an action. At this point, we need to predict the future with machine learning. We are going to build a simple machine learning model that predicts our customers lifetime value.

RFM scores for each customer ID are used as feature set. I took 3 months of data, calculate RFM and use it for predicting next 6 months. There is no cost specified in the dataset that’s why Revenue becomes our LTV directly. After RFM scoring, the feature set looks like this-

![pic](https://user-images.githubusercontent.com/33171500/94217371-17286580-fe9f-11ea-9485-3867160242c2.png)

Positive correlation is quite visible here. High RFM score means high LTV.

![pic](https://user-images.githubusercontent.com/33171500/94217375-17c0fc00-fe9f-11ea-88a0-5e24e6fd1105.png)

![pic](https://user-images.githubusercontent.com/33171500/94217377-17c0fc00-fe9f-11ea-99c0-75c1193f1e76.png)

I performed feature engineering, converted categorical columns to numerical columns, checked the correlation of features against our label, LTV clusters and split feature set and label (LTV) as X and y.

Then used XGBoost to do the classification. Since there are3 groups, it is a multi classification model.

![pic](https://user-images.githubusercontent.com/33171500/94217378-17c0fc00-fe9f-11ea-9e7e-36dc7800ae69.png)

I am getting 99% accuracy score on both train and test set which is odd. I need to investigate this. The future course of action is:
- Adding more features and improve feature engineering
- Try different models other than XGBoost
- Apply hyper parameter tuning to current model
- Add more data to the model if possible
