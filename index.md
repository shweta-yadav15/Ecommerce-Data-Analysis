## Background

E Commerce industry is forecasted to double in size within the next two years and grow from 3.53 trillion US dollars in retail ecommerce sales in 2019, up to 6.54 trillion US dollars in 2022. The key drivers of success over the next decade will be centered on building a deep understanding of and connection to the empowered consumer, and the only way to understand consumer behavior is to measure and analyze. 

## Motivation

This project deals with many real-world challenges faced by e-commerce websites that includes predicting customer lifetime value using RFM score and k-means clustering, customer segmentation to find out best valued customers. Also, predicting review score they customers will give to their order experience depending on their location, order cost and other factors. I have also done a detailed analysis of how geolocation can affect user's experience and their purchase and much more.

## Dataset

Brazilian ecommerce public dataset of orders made at Olist Store. The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. Also included is a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates.

This dataset have nine tables which are connected with few common attributes. [Dataset Link](https://www.kaggle.com/olistbr/brazilian-ecommerce)

## Project Overview
The project is divided into two parts:
1. Analysis and Visualizations- Detailed anaysis, understanding metrics and graph plotting
2. Predictions- Customer lifetime value prediction, predicting customer satisfaction and segmentation

# Part 1: Analysis
Few instances of the analysis performed are as follows:

![Overall_Study](https://user-images.githubusercontent.com/33171500/93948439-b14fa880-fcfb-11ea-84af-6e86ebf28120.png)

* There is an upward trend in orders purchased between January 2017 and July 2018.

![Overall_Study](https://user-images.githubusercontent.com/33171500/93949055-34253300-fcfd-11ea-9a26-ecac726a80e3.png)

* Unfortunately, who lives in the north and northeast of Brazil has to bear with higher freight costs and has to wait longer to receive their purchase.

![Overall_Study](https://user-images.githubusercontent.com/33171500/93948934-eb6d7a00-fcfc-11ea-8a29-a4f052927370.png)

* As the consequence of late delivery customers in north side are likely to give lower reviews.
![Overall_Study](https://user-images.githubusercontent.com/33171500/93948895-d4c72300-fcfc-11ea-9cf5-c30e4c7bc148.png)

* Most of the revenue came from the Southeast and South regions of Brazil. Also, large cities and capitals, where population is bigger, have larger participation on revenue.
![Overall_Study](https://user-images.githubusercontent.com/33171500/93948937-edcfd400-fcfc-11ea-8be8-15ae5e3521cd.png)

* Monthly retention rate shows if customers continue to buy products from the website. There is a upward linear trend but with few major exceptions.
![Overall_Study](https://user-images.githubusercontent.com/33171500/93948977-0809b200-fcfd-11ea-9fc3-f4d1d4260d97.png)

* Monday blues are showing effects even here. Customers seem to most likely buy on Monday then any other day of the week.
![Overall_Study](https://user-images.githubusercontent.com/33171500/93948981-093adf00-fcfd-11ea-8c33-4bfd19192380.png)

* Afternoon boredom is making customers buy items mostly in afternoons.
![Overall_Study](https://user-images.githubusercontent.com/33171500/93949016-1eb00900-fcfd-11ea-859e-40f5cac9504d.png)

* Company seems to be doing well in terms of delivery time since most of the orders are getting delivered way before they are expected.
![Overall_Study](https://user-images.githubusercontent.com/33171500/93949045-31c2d900-fcfd-11ea-85a9-14a4ee60614b.png)

*
![Overall_Study](https://user-images.githubusercontent.com/33171500/93949050-32f40600-fcfd-11ea-8a44-2dbbab31dec0.png)


























```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

