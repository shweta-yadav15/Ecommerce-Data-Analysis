## Background

E Commerce industry is forecasted to double in size within the next two years and grow from 3.53 trillion US dollars in retail ecommerce sales in 2019, up to 6.54 trillion US dollars in 2022. The key drivers of success over the next decade will be centered on building a deep understanding of and connection to the empowered consumer, and the only way to understand consumer behavior is to measure and analyze. 

## Motivation

This project deals with many real-world challenges faced by e-commerce websites that includes predicting customer lifetime value using RFM score and k-means clustering, customer segmentation to find out best valued customers. Also, predicting review score that customers will give to their order experience depending on their location, order cost and other factors. I have also done a detailed analysis of how geolocation can affect user's experience and their purchase and much more.

## Dataset

Brazilian ecommerce public dataset of orders made at Olist Store. The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. Also included is a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates.

This [dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce) have nine tables which are connected by common attributes.

## Project Overview
The project is divided into two parts:
1. Analysis and Visualizations- Comprehensive anaysis, understanding metrics and graph plotting
2. Predictions- Customer lifetime value prediction, predicting customer satisfaction and segmentation

# Part 1: Analysis and Visualizations
Few instances of the analysis performed are as follows:

* ![Overall_Study](https://user-images.githubusercontent.com/33171500/93948439-b14fa880-fcfb-11ea-84af-6e86ebf28120.png)


* ![Overall_Study](https://user-images.githubusercontent.com/33171500/93949050-32f40600-fcfd-11ea-8a44-2dbbab31dec0.png)


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
Let's say your manager asks you: **"What is the probable score that we getting from customers?"**

The model helps to find a way to estimate that i.e. based on data about the product and order what will be the customer review score.

**The hypothesis
The main hypothesis is that the product and how the order was fulfilled might influence the customer review score. Keeping in mind that each feature created is a new hypothesis to test.**

**Designing an Experiment
To answer that question data is collected from each order from placing the order up to the delivery phase. With that, the model implemented estimates what will be the score given by the customer at the review phase.**

                                                  Purchase   -->   Transport   -->   Delivery   -->    Review
                                                    [ Extract Features ]                [ Make Prediction ]

### 2.1.1 Cleaning and Feature Engineering
[data](https://user-images.githubusercontent.com/33171500/94206088-dbcb6e00-fe81-11ea-91a5-340233891e74.png)

The data was a mix of categorical, numerical values as well as null values in 9 columns. In order to guarantee that the same transformation is applied to new/unseen data, I created custom transformers using scikit-learn BaseEstimator. Also, seven new features were engineered for better results: Working Days Estimated Delivery Time, Actual Delivery Time, Delivery Time, Is Late, Average Product Value, Total Order Value, Order Freight Ratio and Purchase Day of Week.

### 2.1.2 Model Building
- I created two separate pipelines for categorical and numerical data. 
- In categorical pipeline, to deal with missing values I used imputation of most frequent values and then applied one hot encoding. 
- In numerical pipeline, I used median imputation for null values and then standard scaling.
- Since the data was highly imbalanced, I used Stratified Shuffle Split that preserves the percentage of samples for each class. 
- Among k-Neighbors, Decision Tree, Random Forest, AdaBoost and Gradient BoostingClassifier, Random Forest classifier gave the best accuracy of 62%. I am planning to do the hyperaprameter tuning in future to improve the score.

## 2.2 Customer Segmentation
Customers who use the platform have different needs and they have their own different profile. Our actions should adapt depending on that. There are different segmentations according to what we are trying to achieve. To increase retention rate, we can do a segmentation based on churn probability and take actions. But there are very common and useful segmentation methods as well. I used RFM here. 
**RFM stands for Recency - Frequency - Monetary Value.**

There are three segments of customers:
1. Low Value: Customers who are less active than others, not very frequent buyer/visitor and generates very low - zero - maybe negative revenue.
2. Mid Value: In the middle of everything. Often using our platform (but not as much as our High Values), fairly frequent and generates moderate revenue.
3. High Value: The group we don’t want to lose. High Revenue, Frequency and low Inactivity.
As the methodology, we need to calculate Recency, Frequency and Monetary Value (Revenue from now on) and apply unsupervised machine learning to identify different groups (clusters) for each.

### 2.2.1 Recency - To calculate recency, I used most recent purchase date of each customer and see how many days they are inactive for. After having no. of inactive days for each customer, applied K-means clustering to assign customers a recency score.
[pic](https://user-images.githubusercontent.com/33171500/94212238-dcb7cc00-fe90-11ea-91e2-a34f2d1832b9.png)

### 2.2.2 Frequency - To create frequency clusters, found total number orders for each customer.
[pic](https://user-images.githubusercontent.com/33171500/94212240-de818f80-fe90-11ea-9613-ef307c76f978.png)
### 2.2.3 Revenue - 
[pic](https://user-images.githubusercontent.com/33171500/94212249-e2adad00-fe90-11ea-811b-5e589ae3f983.png)

[pic](https://user-images.githubusercontent.com/33171500/94212296-040e9900-fe91-11ea-969c-efd3878ca7fa.png)
[pic](https://user-images.githubusercontent.com/33171500/94212304-07098980-fe91-11ea-85ca-5a16c9c4fadc.png)
[pic](https://user-images.githubusercontent.com/33171500/94212308-0a047a00-fe91-11ea-8d9d-3a41111c627b.png)

## 2.3 Customer Lifetime Value Prediction
We invest in customers (acquisition costs, offline ads, promotions, discounts & etc.) to generate revenue and be profitable. Naturally, these actions make some customers super valuable in terms of lifetime value but there are always some customers who pull down the profitability. We need to identify these behavior patterns, segment customers and act accordingly.

To calculate Lifetime Value first we need to select a time window. It can be anything like 3, 6, 12, 24 months. By the equation below, we can have Lifetime Value for each customer in that specific time window: **Lifetime Value: Total Gross Revenue - Total Cost**

This equation now gives us the historical lifetime value. If we see some customers having very high negative lifetime value historically, it could be too late to take an action. At this point, we need to predict the future with machine learning. We are going to build a simple machine learning model that predicts our customers lifetime value.

In order to calculate the value:

- Define an appropriate time frame for Customer Lifetime Value calculation
- Identify the features we are going to use to predict future and create them
- Calculate lifetime value (LTV) for training the machine learning model
- Build and run the machine learning model
- Check if the model is useful





