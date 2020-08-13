{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Predicting_customer_satisfaction.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMvt/ldb5SdteW+i3lHUjJF",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shwets1503/Sales_Prediction/blob/master/Predicting_customer_satisfaction.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nsCqAdpDxI3L",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 124
        },
        "outputId": "15485723-b82c-4be1-835b-02c197769f20"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Go to this URL in a browser: https://accounts.google.com/o/oauth2/auth?client_id=947318989803-6bn6qk8qdgf4n4g3pfee6491hc0brc4i.apps.googleusercontent.com&redirect_uri=urn%3aietf%3awg%3aoauth%3a2.0%3aoob&scope=email%20https%3a%2f%2fwww.googleapis.com%2fauth%2fdocs.test%20https%3a%2f%2fwww.googleapis.com%2fauth%2fdrive%20https%3a%2f%2fwww.googleapis.com%2fauth%2fdrive.photos.readonly%20https%3a%2f%2fwww.googleapis.com%2fauth%2fpeopleapi.readonly&response_type=code\n",
            "\n",
            "Enter your authorization code:\n",
            "··········\n",
            "Mounted at /content/drive\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MFu_dnoyV_Ho",
        "colab_type": "text"
      },
      "source": [
        "### Importing Libraries\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "udMYorNzxQvg",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 72
        },
        "outputId": "d46291e2-60fb-40b0-ed92-3bcefd0da325"
      },
      "source": [
        "import numpy as np \n",
        "import pandas as pd \n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "import datetime as dt"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/statsmodels/tools/_testing.py:19: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.\n",
            "  import pandas.util.testing as tm\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7LFSnFEJWvdc",
        "colab_type": "text"
      },
      "source": [
        "# Data Understanding"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EXkqIieEWFTu",
        "colab_type": "text"
      },
      "source": [
        "### Importing Datasets"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1dWEzoC5xuDu",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "orders_df = pd.read_csv('../content/drive/My Drive/sales_data2/olist_orders_dataset.csv', engine='python')\n",
        "order_items = pd.read_csv('../content/drive/My Drive/sales_data2/olist_order_items_dataset.csv', engine='python')\n",
        "order_reviews = pd.read_csv('../content/drive/My Drive/sales_data2/olist_order_reviews_dataset.csv', engine='python')\n",
        "products = pd.read_csv('../content/drive/My Drive/sales_data3/olist_products_dataset.csv', engine='python')\n",
        "product_category = pd.read_csv('../content/drive/My Drive/sales_data3/product_category_name_translation.csv', engine='python')\n",
        "customer = pd.read_csv('../content/drive/My Drive/sales_data/customers_dataset.csv', engine='python')\n",
        "payments = pd.read_csv('../content/drive/My Drive/sales_data2/olist_order_payments_dataset.csv', engine='python')"
      ],
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "C56K1VvQy-qM",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Merging categories data with english translations and dropping that column \n",
        "categories = pd.merge(products, product_category,how ='left', left_on ='product_category_name', right_index = True, suffixes=(None, '_eng')).drop('product_category_name', axis=1)"
      ],
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xAVwIVu1xuMI",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Merging required datasets\n",
        "orders = pd.merge(order_reviews, order_items, how='left', on='order_id')\n",
        "orders = pd.merge(orders, orders_df, how='left', on='order_id')\n",
        "orders = pd.merge(orders, customer, how='left', on='customer_id')\n",
        "orders = pd.merge(orders, categories, how='left', on='product_id')"
      ],
      "execution_count": 36,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "avQTXnl-BCeH",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 257
        },
        "outputId": "18d0d94f-ea65-4059-a253-9e00969149af"
      },
      "source": [
        "# Dataset after Merging\n",
        "orders.head()"
      ],
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>review_id</th>\n",
              "      <th>order_id</th>\n",
              "      <th>review_score</th>\n",
              "      <th>review_comment_title</th>\n",
              "      <th>review_comment_message</th>\n",
              "      <th>review_creation_date</th>\n",
              "      <th>review_answer_timestamp</th>\n",
              "      <th>order_item_id</th>\n",
              "      <th>product_id</th>\n",
              "      <th>seller_id</th>\n",
              "      <th>shipping_limit_date</th>\n",
              "      <th>price</th>\n",
              "      <th>freight_value</th>\n",
              "      <th>customer_id</th>\n",
              "      <th>order_status</th>\n",
              "      <th>order_purchase_timestamp</th>\n",
              "      <th>order_approved_at</th>\n",
              "      <th>order_delivered_carrier_date</th>\n",
              "      <th>order_delivered_customer_date</th>\n",
              "      <th>order_estimated_delivery_date</th>\n",
              "      <th>customer_unique_id</th>\n",
              "      <th>customer_zip_code_prefix</th>\n",
              "      <th>customer_city</th>\n",
              "      <th>customer_state</th>\n",
              "      <th>product_name_lenght</th>\n",
              "      <th>product_description_lenght</th>\n",
              "      <th>product_photos_qty</th>\n",
              "      <th>product_weight_g</th>\n",
              "      <th>product_length_cm</th>\n",
              "      <th>product_height_cm</th>\n",
              "      <th>product_width_cm</th>\n",
              "      <th>product_category_name_eng</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>7bc2406110b926393aa56f80a40eba40</td>\n",
              "      <td>73fc7af87114b39712e6da79b0a377eb</td>\n",
              "      <td>4</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2018-01-18 00:00:00</td>\n",
              "      <td>2018-01-18 21:46:59</td>\n",
              "      <td>1.0</td>\n",
              "      <td>fd25ab760bfbba13c198fa3b4f1a0cd3</td>\n",
              "      <td>6d803cb79cc31c41c4c789a75933b3c7</td>\n",
              "      <td>2018-01-18 15:47:59</td>\n",
              "      <td>185.00</td>\n",
              "      <td>13.63</td>\n",
              "      <td>41dcb106f807e993532d446263290104</td>\n",
              "      <td>delivered</td>\n",
              "      <td>2018-01-11 15:30:49</td>\n",
              "      <td>2018-01-11 15:47:59</td>\n",
              "      <td>2018-01-12 21:57:22</td>\n",
              "      <td>2018-01-17 18:42:41</td>\n",
              "      <td>2018-02-02 00:00:00</td>\n",
              "      <td>68a5590b9926689be4e10f4ae2db21a8</td>\n",
              "      <td>6030</td>\n",
              "      <td>osasco</td>\n",
              "      <td>SP</td>\n",
              "      <td>42.0</td>\n",
              "      <td>858.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1300.0</td>\n",
              "      <td>30.0</td>\n",
              "      <td>30.0</td>\n",
              "      <td>35.0</td>\n",
              "      <td>sports_leisure</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>7bc2406110b926393aa56f80a40eba40</td>\n",
              "      <td>73fc7af87114b39712e6da79b0a377eb</td>\n",
              "      <td>4</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2018-01-18 00:00:00</td>\n",
              "      <td>2018-01-18 21:46:59</td>\n",
              "      <td>2.0</td>\n",
              "      <td>fd25ab760bfbba13c198fa3b4f1a0cd3</td>\n",
              "      <td>6d803cb79cc31c41c4c789a75933b3c7</td>\n",
              "      <td>2018-01-18 15:47:59</td>\n",
              "      <td>185.00</td>\n",
              "      <td>13.63</td>\n",
              "      <td>41dcb106f807e993532d446263290104</td>\n",
              "      <td>delivered</td>\n",
              "      <td>2018-01-11 15:30:49</td>\n",
              "      <td>2018-01-11 15:47:59</td>\n",
              "      <td>2018-01-12 21:57:22</td>\n",
              "      <td>2018-01-17 18:42:41</td>\n",
              "      <td>2018-02-02 00:00:00</td>\n",
              "      <td>68a5590b9926689be4e10f4ae2db21a8</td>\n",
              "      <td>6030</td>\n",
              "      <td>osasco</td>\n",
              "      <td>SP</td>\n",
              "      <td>42.0</td>\n",
              "      <td>858.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1300.0</td>\n",
              "      <td>30.0</td>\n",
              "      <td>30.0</td>\n",
              "      <td>35.0</td>\n",
              "      <td>sports_leisure</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>80e641a11e56f04c1ad469d5645fdfde</td>\n",
              "      <td>a548910a1c6147796b98fdf73dbeba33</td>\n",
              "      <td>5</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2018-03-10 00:00:00</td>\n",
              "      <td>2018-03-11 03:05:13</td>\n",
              "      <td>1.0</td>\n",
              "      <td>be0dbdc3d67d55727a65d4cd696ca73c</td>\n",
              "      <td>8e6d7754bc7e0f22c96d255ebda59eba</td>\n",
              "      <td>2018-03-06 12:48:39</td>\n",
              "      <td>79.79</td>\n",
              "      <td>8.30</td>\n",
              "      <td>8a2e7ef9053dea531e4dc76bd6d853e6</td>\n",
              "      <td>delivered</td>\n",
              "      <td>2018-02-28 12:25:19</td>\n",
              "      <td>2018-02-28 12:48:39</td>\n",
              "      <td>2018-03-02 19:08:15</td>\n",
              "      <td>2018-03-09 23:17:20</td>\n",
              "      <td>2018-03-14 00:00:00</td>\n",
              "      <td>64190b91b656ab8f37eb89b93dc84584</td>\n",
              "      <td>13380</td>\n",
              "      <td>nova odessa</td>\n",
              "      <td>SP</td>\n",
              "      <td>47.0</td>\n",
              "      <td>493.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>245.0</td>\n",
              "      <td>19.0</td>\n",
              "      <td>14.0</td>\n",
              "      <td>14.0</td>\n",
              "      <td>computers_accessories</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>228ce5500dc1d8e020d8d1322874b6f0</td>\n",
              "      <td>f9e4b658b201a9f2ecdecbb34bed034b</td>\n",
              "      <td>5</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2018-02-17 00:00:00</td>\n",
              "      <td>2018-02-18 14:36:24</td>\n",
              "      <td>1.0</td>\n",
              "      <td>d1c427060a0f73f6b889a5c7c61f2ac4</td>\n",
              "      <td>a1043bafd471dff536d0c462352beb48</td>\n",
              "      <td>2018-02-08 10:31:15</td>\n",
              "      <td>149.00</td>\n",
              "      <td>45.12</td>\n",
              "      <td>e226dfed6544df5b7b87a48208690feb</td>\n",
              "      <td>delivered</td>\n",
              "      <td>2018-02-03 09:56:22</td>\n",
              "      <td>2018-02-03 10:33:41</td>\n",
              "      <td>2018-02-06 16:18:28</td>\n",
              "      <td>2018-02-16 17:28:48</td>\n",
              "      <td>2018-03-09 00:00:00</td>\n",
              "      <td>1d47144362c14e94ccdd213e8ec277d5</td>\n",
              "      <td>44571</td>\n",
              "      <td>santo antonio de jesus</td>\n",
              "      <td>BA</td>\n",
              "      <td>59.0</td>\n",
              "      <td>1893.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>6550.0</td>\n",
              "      <td>20.0</td>\n",
              "      <td>20.0</td>\n",
              "      <td>20.0</td>\n",
              "      <td>computers_accessories</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>e64fb393e7b32834bb789ff8bb30750e</td>\n",
              "      <td>658677c97b385a9be170737859d3511b</td>\n",
              "      <td>5</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Recebi bem antes do prazo estipulado.</td>\n",
              "      <td>2017-04-21 00:00:00</td>\n",
              "      <td>2017-04-21 22:02:06</td>\n",
              "      <td>1.0</td>\n",
              "      <td>52c80cedd4e90108bf4fa6a206ef6b03</td>\n",
              "      <td>a1043bafd471dff536d0c462352beb48</td>\n",
              "      <td>2017-04-13 17:55:19</td>\n",
              "      <td>179.99</td>\n",
              "      <td>42.85</td>\n",
              "      <td>de6dff97e5f1ba84a3cd9a3bc97df5f6</td>\n",
              "      <td>delivered</td>\n",
              "      <td>2017-04-09 17:41:13</td>\n",
              "      <td>2017-04-09 17:55:19</td>\n",
              "      <td>2017-04-10 14:24:47</td>\n",
              "      <td>2017-04-20 09:08:35</td>\n",
              "      <td>2017-05-10 00:00:00</td>\n",
              "      <td>c8cf6cb6b838dc7a33ed199b825e8616</td>\n",
              "      <td>88735</td>\n",
              "      <td>gravatal</td>\n",
              "      <td>SC</td>\n",
              "      <td>33.0</td>\n",
              "      <td>2188.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>7650.0</td>\n",
              "      <td>20.0</td>\n",
              "      <td>20.0</td>\n",
              "      <td>20.0</td>\n",
              "      <td>garden_tools</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                          review_id  ... product_category_name_eng\n",
              "0  7bc2406110b926393aa56f80a40eba40  ...            sports_leisure\n",
              "1  7bc2406110b926393aa56f80a40eba40  ...            sports_leisure\n",
              "2  80e641a11e56f04c1ad469d5645fdfde  ...     computers_accessories\n",
              "3  228ce5500dc1d8e020d8d1322874b6f0  ...     computers_accessories\n",
              "4  e64fb393e7b32834bb789ff8bb30750e  ...              garden_tools\n",
              "\n",
              "[5 rows x 32 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lihkSpd2DMUL",
        "colab_type": "text"
      },
      "source": [
        "Although some items seem duplicated their order_item_id indicates multiple orders of same item, so not dropping them."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2QihnOy_CePl",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "3d564cb8-bc2a-4c69-8a4c-903b22a345ba"
      },
      "source": [
        "# Shape of the dataset after merging\n",
        "orders.shape"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(114100, 32)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9wuZF13rxuQV",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# converting to datetime\n",
        "orders['order_purchase_timestamp'] = pd.to_datetime(orders.order_purchase_timestamp).dt.date\n",
        "orders['order_approved_at'] = pd.to_datetime(orders.order_approved_at).dt.date  \n",
        "orders['order_estimated_delivery_date'] = pd.to_datetime(orders.order_estimated_delivery_date).dt.date  \n",
        "orders['order_delivered_customer_date'] = pd.to_datetime(orders.order_delivered_customer_date).dt.date  "
      ],
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QhtHRyVHt6bP",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "orders['order_purchase_timestamp'] = pd.to_numeric(orders['order_purchase_timestamp'],errors='ignore')\n",
        "orders['order_approved_at'] = pd.to_numeric(orders['order_approved_at'],errors='ignore')\n",
        "orders['order_estimated_delivery_date'] = pd.to_numeric(orders['order_estimated_delivery_date'],errors='ignore')  \n",
        "orders['order_delivered_customer_date'] = pd.to_numeric(orders['order_delivered_customer_date'],errors='ignore')  "
      ],
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BkAFM3IuxKVA",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 693
        },
        "outputId": "134d362d-7090-4d1f-8cdf-e2d9f8108ad1"
      },
      "source": [
        "orders.info()"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 114100 entries, 0 to 114099\n",
            "Data columns (total 32 columns):\n",
            " #   Column                         Non-Null Count   Dtype  \n",
            "---  ------                         --------------   -----  \n",
            " 0   review_id                      114100 non-null  object \n",
            " 1   order_id                       114100 non-null  object \n",
            " 2   review_score                   114100 non-null  int64  \n",
            " 3   review_comment_title           13714 non-null   object \n",
            " 4   review_comment_message         49135 non-null   object \n",
            " 5   review_creation_date           114100 non-null  object \n",
            " 6   review_answer_timestamp        114100 non-null  object \n",
            " 7   order_item_id                  113322 non-null  float64\n",
            " 8   product_id                     113322 non-null  object \n",
            " 9   seller_id                      113322 non-null  object \n",
            " 10  shipping_limit_date            113322 non-null  object \n",
            " 11  price                          113322 non-null  float64\n",
            " 12  freight_value                  113322 non-null  float64\n",
            " 13  customer_id                    114100 non-null  object \n",
            " 14  order_status                   114100 non-null  object \n",
            " 15  order_purchase_timestamp       114100 non-null  object \n",
            " 16  order_approved_at              113938 non-null  object \n",
            " 17  order_delivered_carrier_date   112120 non-null  object \n",
            " 18  order_delivered_customer_date  110847 non-null  object \n",
            " 19  order_estimated_delivery_date  114100 non-null  object \n",
            " 20  customer_unique_id             114100 non-null  object \n",
            " 21  customer_zip_code_prefix       114100 non-null  int64  \n",
            " 22  customer_city                  114100 non-null  object \n",
            " 23  customer_state                 114100 non-null  object \n",
            " 24  product_name_lenght            111710 non-null  float64\n",
            " 25  product_description_lenght     111710 non-null  float64\n",
            " 26  product_photos_qty             111710 non-null  float64\n",
            " 27  product_weight_g               113304 non-null  float64\n",
            " 28  product_length_cm              113304 non-null  float64\n",
            " 29  product_height_cm              113304 non-null  float64\n",
            " 30  product_width_cm               113304 non-null  float64\n",
            " 31  product_category_name_eng      111686 non-null  object \n",
            "dtypes: float64(10), int64(2), object(20)\n",
            "memory usage: 28.7+ MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0n-2u99V1N2d",
        "colab_type": "text"
      },
      "source": [
        "# Defining the problem\n",
        "Our problem is to find a way to estimate, based on data about the product and order, what will be the customer review score.\n",
        "# The hypothesis\n",
        "Our main hypothesis is that the product and how the order was fulfilled might influence the customer review score. Keep in mind that each feature we create is a new hypothesis we are testing.\n",
        "\n",
        "#Designing an Experiment\n",
        "To answer that question we must implement collect data from each order up to delivery phase. With that, we should implement a model that estimates what will be the score given by the customer at the review phase."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f5AOvmTgxuJ6",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "orders = orders[['order_status', 'price',\n",
        "                 'freight_value', 'order_item_id', \n",
        "                 'order_purchase_timestamp', 'order_approved_at', 'order_estimated_delivery_date', \n",
        "                 'order_delivered_customer_date', 'customer_state', \n",
        "                 'product_category_name_eng', 'product_name_lenght', 'product_description_lenght', \n",
        "                 'product_photos_qty', 'review_score']]"
      ],
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YFwp1Kl0VrtM",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "orders = orders[['order_status', 'price',\n",
        "                 'freight_value', 'order_item_id', \n",
        "                'customer_state', \n",
        "                 'product_category_name_eng', 'product_name_lenght', 'product_description_lenght', \n",
        "                 'product_photos_qty', 'review_score']]"
      ],
      "execution_count": 231,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "g37HeCy0Ep_G",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 222
        },
        "outputId": "e6ad7bbd-dafc-42f7-e227-b4acfbf616d7"
      },
      "source": [
        "orders.head()"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>order_status</th>\n",
              "      <th>price</th>\n",
              "      <th>freight_value</th>\n",
              "      <th>order_item_id</th>\n",
              "      <th>order_purchase_timestamp</th>\n",
              "      <th>order_approved_at</th>\n",
              "      <th>order_estimated_delivery_date</th>\n",
              "      <th>order_delivered_customer_date</th>\n",
              "      <th>customer_state</th>\n",
              "      <th>product_category_name_eng</th>\n",
              "      <th>product_name_lenght</th>\n",
              "      <th>product_description_lenght</th>\n",
              "      <th>product_photos_qty</th>\n",
              "      <th>review_score</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>delivered</td>\n",
              "      <td>185.00</td>\n",
              "      <td>13.63</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2018-01-11</td>\n",
              "      <td>2018-01-11</td>\n",
              "      <td>2018-02-02</td>\n",
              "      <td>2018-01-17</td>\n",
              "      <td>SP</td>\n",
              "      <td>sports_leisure</td>\n",
              "      <td>42.0</td>\n",
              "      <td>858.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>delivered</td>\n",
              "      <td>185.00</td>\n",
              "      <td>13.63</td>\n",
              "      <td>2.0</td>\n",
              "      <td>2018-01-11</td>\n",
              "      <td>2018-01-11</td>\n",
              "      <td>2018-02-02</td>\n",
              "      <td>2018-01-17</td>\n",
              "      <td>SP</td>\n",
              "      <td>sports_leisure</td>\n",
              "      <td>42.0</td>\n",
              "      <td>858.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>delivered</td>\n",
              "      <td>79.79</td>\n",
              "      <td>8.30</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2018-02-28</td>\n",
              "      <td>2018-02-28</td>\n",
              "      <td>2018-03-14</td>\n",
              "      <td>2018-03-09</td>\n",
              "      <td>SP</td>\n",
              "      <td>computers_accessories</td>\n",
              "      <td>47.0</td>\n",
              "      <td>493.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>delivered</td>\n",
              "      <td>149.00</td>\n",
              "      <td>45.12</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2018-02-03</td>\n",
              "      <td>2018-02-03</td>\n",
              "      <td>2018-03-09</td>\n",
              "      <td>2018-02-16</td>\n",
              "      <td>BA</td>\n",
              "      <td>computers_accessories</td>\n",
              "      <td>59.0</td>\n",
              "      <td>1893.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>delivered</td>\n",
              "      <td>179.99</td>\n",
              "      <td>42.85</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2017-04-09</td>\n",
              "      <td>2017-04-09</td>\n",
              "      <td>2017-05-10</td>\n",
              "      <td>2017-04-20</td>\n",
              "      <td>SC</td>\n",
              "      <td>garden_tools</td>\n",
              "      <td>33.0</td>\n",
              "      <td>2188.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  order_status   price  ...  product_photos_qty  review_score\n",
              "0    delivered  185.00  ...                 1.0             4\n",
              "1    delivered  185.00  ...                 1.0             4\n",
              "2    delivered   79.79  ...                 1.0             5\n",
              "3    delivered  149.00  ...                 1.0             5\n",
              "4    delivered  179.99  ...                 2.0             5\n",
              "\n",
              "[5 rows x 14 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-OPTp6ZhWK9r",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "orders.dropna(axis=0,how='any', inplace=True)"
      ],
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tR0Eml1DMfLI",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "877cf617-45dd-4f47-ab4c-e652e04c7e7e"
      },
      "source": [
        "orders.shape"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(109266, 14)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "y5ldWM-HFx-g",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 435
        },
        "outputId": "abc71c90-1b06-4b42-ca5b-5402a4ba7344"
      },
      "source": [
        "X = orders.iloc[:,0:13]\n",
        "y = orders.iloc[:,-1]\n",
        "X"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>order_status</th>\n",
              "      <th>price</th>\n",
              "      <th>freight_value</th>\n",
              "      <th>order_item_id</th>\n",
              "      <th>order_purchase_timestamp</th>\n",
              "      <th>order_approved_at</th>\n",
              "      <th>order_estimated_delivery_date</th>\n",
              "      <th>order_delivered_customer_date</th>\n",
              "      <th>customer_state</th>\n",
              "      <th>product_category_name_eng</th>\n",
              "      <th>product_name_lenght</th>\n",
              "      <th>product_description_lenght</th>\n",
              "      <th>product_photos_qty</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>delivered</td>\n",
              "      <td>185.00</td>\n",
              "      <td>13.63</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2018-01-11</td>\n",
              "      <td>2018-01-11</td>\n",
              "      <td>2018-02-02</td>\n",
              "      <td>2018-01-17</td>\n",
              "      <td>SP</td>\n",
              "      <td>sports_leisure</td>\n",
              "      <td>42.0</td>\n",
              "      <td>858.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>delivered</td>\n",
              "      <td>185.00</td>\n",
              "      <td>13.63</td>\n",
              "      <td>2.0</td>\n",
              "      <td>2018-01-11</td>\n",
              "      <td>2018-01-11</td>\n",
              "      <td>2018-02-02</td>\n",
              "      <td>2018-01-17</td>\n",
              "      <td>SP</td>\n",
              "      <td>sports_leisure</td>\n",
              "      <td>42.0</td>\n",
              "      <td>858.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>delivered</td>\n",
              "      <td>79.79</td>\n",
              "      <td>8.30</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2018-02-28</td>\n",
              "      <td>2018-02-28</td>\n",
              "      <td>2018-03-14</td>\n",
              "      <td>2018-03-09</td>\n",
              "      <td>SP</td>\n",
              "      <td>computers_accessories</td>\n",
              "      <td>47.0</td>\n",
              "      <td>493.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>delivered</td>\n",
              "      <td>149.00</td>\n",
              "      <td>45.12</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2018-02-03</td>\n",
              "      <td>2018-02-03</td>\n",
              "      <td>2018-03-09</td>\n",
              "      <td>2018-02-16</td>\n",
              "      <td>BA</td>\n",
              "      <td>computers_accessories</td>\n",
              "      <td>59.0</td>\n",
              "      <td>1893.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>delivered</td>\n",
              "      <td>179.99</td>\n",
              "      <td>42.85</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2017-04-09</td>\n",
              "      <td>2017-04-09</td>\n",
              "      <td>2017-05-10</td>\n",
              "      <td>2017-04-20</td>\n",
              "      <td>SC</td>\n",
              "      <td>garden_tools</td>\n",
              "      <td>33.0</td>\n",
              "      <td>2188.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>114095</th>\n",
              "      <td>delivered</td>\n",
              "      <td>199.99</td>\n",
              "      <td>9.77</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2017-12-03</td>\n",
              "      <td>2017-12-03</td>\n",
              "      <td>2017-12-20</td>\n",
              "      <td>2017-12-08</td>\n",
              "      <td>RJ</td>\n",
              "      <td>toys</td>\n",
              "      <td>51.0</td>\n",
              "      <td>465.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>114096</th>\n",
              "      <td>delivered</td>\n",
              "      <td>215.97</td>\n",
              "      <td>15.59</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2018-03-18</td>\n",
              "      <td>2018-03-18</td>\n",
              "      <td>2018-04-06</td>\n",
              "      <td>2018-03-21</td>\n",
              "      <td>MG</td>\n",
              "      <td>stationery</td>\n",
              "      <td>45.0</td>\n",
              "      <td>283.0</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>114097</th>\n",
              "      <td>delivered</td>\n",
              "      <td>50.95</td>\n",
              "      <td>15.46</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2018-06-22</td>\n",
              "      <td>2018-06-22</td>\n",
              "      <td>2018-07-16</td>\n",
              "      <td>2018-06-30</td>\n",
              "      <td>MG</td>\n",
              "      <td>sports_leisure</td>\n",
              "      <td>58.0</td>\n",
              "      <td>998.0</td>\n",
              "      <td>5.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>114098</th>\n",
              "      <td>delivered</td>\n",
              "      <td>10.00</td>\n",
              "      <td>7.78</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2017-12-10</td>\n",
              "      <td>2017-12-12</td>\n",
              "      <td>2017-12-29</td>\n",
              "      <td>2017-12-14</td>\n",
              "      <td>SP</td>\n",
              "      <td>auto</td>\n",
              "      <td>58.0</td>\n",
              "      <td>954.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>114099</th>\n",
              "      <td>delivered</td>\n",
              "      <td>32.90</td>\n",
              "      <td>7.78</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2017-06-29</td>\n",
              "      <td>2017-06-30</td>\n",
              "      <td>2017-07-12</td>\n",
              "      <td>2017-07-02</td>\n",
              "      <td>SP</td>\n",
              "      <td>computers_accessories</td>\n",
              "      <td>56.0</td>\n",
              "      <td>482.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>109266 rows × 13 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "       order_status   price  ...  product_description_lenght  product_photos_qty\n",
              "0         delivered  185.00  ...                       858.0                 1.0\n",
              "1         delivered  185.00  ...                       858.0                 1.0\n",
              "2         delivered   79.79  ...                       493.0                 1.0\n",
              "3         delivered  149.00  ...                      1893.0                 1.0\n",
              "4         delivered  179.99  ...                      2188.0                 2.0\n",
              "...             ...     ...  ...                         ...                 ...\n",
              "114095    delivered  199.99  ...                       465.0                 1.0\n",
              "114096    delivered  215.97  ...                       283.0                 3.0\n",
              "114097    delivered   50.95  ...                       998.0                 5.0\n",
              "114098    delivered   10.00  ...                       954.0                 1.0\n",
              "114099    delivered   32.90  ...                       482.0                 2.0\n",
              "\n",
              "[109266 rows x 13 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NeDYzIje9Ryt",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# selecting the numerical and text attributes\n",
        "cat_attribs = ['order_status', 'customer_state', 'product_category_name_eng']\n",
        "num_attribs = X.drop(cat_attribs, axis=1).columns"
      ],
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PXC85AHgdZx4",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "outputId": "18f72e20-013c-4d93-93a9-02c53bd76eed"
      },
      "source": [
        "pip install --upgrade category_encoders"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Collecting category_encoders\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/44/57/fcef41c248701ee62e8325026b90c432adea35555cbc870aff9cfba23727/category_encoders-2.2.2-py2.py3-none-any.whl (80kB)\n",
            "\r\u001b[K     |████                            | 10kB 16.4MB/s eta 0:00:01\r\u001b[K     |████████▏                       | 20kB 1.7MB/s eta 0:00:01\r\u001b[K     |████████████▏                   | 30kB 2.3MB/s eta 0:00:01\r\u001b[K     |████████████████▎               | 40kB 2.5MB/s eta 0:00:01\r\u001b[K     |████████████████████▎           | 51kB 2.0MB/s eta 0:00:01\r\u001b[K     |████████████████████████▍       | 61kB 2.2MB/s eta 0:00:01\r\u001b[K     |████████████████████████████▍   | 71kB 2.5MB/s eta 0:00:01\r\u001b[K     |████████████████████████████████| 81kB 2.1MB/s \n",
            "\u001b[?25hRequirement already satisfied, skipping upgrade: scipy>=1.0.0 in /usr/local/lib/python3.6/dist-packages (from category_encoders) (1.4.1)\n",
            "Requirement already satisfied, skipping upgrade: patsy>=0.5.1 in /usr/local/lib/python3.6/dist-packages (from category_encoders) (0.5.1)\n",
            "Requirement already satisfied, skipping upgrade: pandas>=0.21.1 in /usr/local/lib/python3.6/dist-packages (from category_encoders) (1.0.5)\n",
            "Requirement already satisfied, skipping upgrade: numpy>=1.14.0 in /usr/local/lib/python3.6/dist-packages (from category_encoders) (1.18.5)\n",
            "Requirement already satisfied, skipping upgrade: statsmodels>=0.9.0 in /usr/local/lib/python3.6/dist-packages (from category_encoders) (0.10.2)\n",
            "Requirement already satisfied, skipping upgrade: scikit-learn>=0.20.0 in /usr/local/lib/python3.6/dist-packages (from category_encoders) (0.22.2.post1)\n",
            "Requirement already satisfied, skipping upgrade: six in /usr/local/lib/python3.6/dist-packages (from patsy>=0.5.1->category_encoders) (1.15.0)\n",
            "Requirement already satisfied, skipping upgrade: pytz>=2017.2 in /usr/local/lib/python3.6/dist-packages (from pandas>=0.21.1->category_encoders) (2018.9)\n",
            "Requirement already satisfied, skipping upgrade: python-dateutil>=2.6.1 in /usr/local/lib/python3.6/dist-packages (from pandas>=0.21.1->category_encoders) (2.8.1)\n",
            "Requirement already satisfied, skipping upgrade: joblib>=0.11 in /usr/local/lib/python3.6/dist-packages (from scikit-learn>=0.20.0->category_encoders) (0.16.0)\n",
            "Installing collected packages: category-encoders\n",
            "Successfully installed category-encoders-2.2.2\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "z_oSHGACcuCE",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import category_encoders as ce\n",
        "# create an object of the OneHotEncoder\n",
        "OHE = ce.OneHotEncoder(cols=cat_attribs,use_cat_names=True)\n",
        "# encode the categorical variables\n",
        "X = OHE.fit_transform(X)"
      ],
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NN3QvvtAV_U_",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 124
        },
        "outputId": "a686179a-6212-48af-a11c-c7cbffc0ae31"
      },
      "source": [
        "import imblearn\n",
        "from imblearn.under_sampling import RandomUnderSampler\n",
        "print(imblearn.__version__)"
      ],
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/sklearn/externals/six.py:31: FutureWarning: The module is deprecated in version 0.21 and will be removed in version 0.23 since we've dropped support for Python 2.7. Please rely on the official version of six (https://pypi.org/project/six/).\n",
            "  \"(https://pypi.org/project/six/).\", FutureWarning)\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "0.4.3\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/sklearn/utils/deprecation.py:144: FutureWarning: The sklearn.neighbors.base module is  deprecated in version 0.22 and will be removed in version 0.24. The corresponding classes / functions should instead be imported from sklearn.neighbors. Anything that cannot be imported from sklearn.neighbors is now part of the private API.\n",
            "  warnings.warn(message, FutureWarning)\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uyJpzLG90li7",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 72
        },
        "outputId": "6c938433-6038-4bca-f20c-9cc031967e33"
      },
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)\n",
        "# define undersample strategy\n",
        "undersample = RandomUnderSampler(sampling_strategy={1:2607,2:2607,3:2607,4:2607,5:2607})\n",
        "X_over, y_over = undersample.fit_resample(X_train,y_train)"
      ],
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/sklearn/utils/deprecation.py:87: FutureWarning: Function safe_indexing is deprecated; safe_indexing is deprecated in version 0.22 and will be removed in version 0.24.\n",
            "  warnings.warn(msg, category=FutureWarning)\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KzAoW6WLymHM",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 121
        },
        "outputId": "579b2fcf-584b-480c-bacd-b6f3a548e011"
      },
      "source": [
        "y_train.value_counts()"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5    43809\n",
              "4    14638\n",
              "1     8971\n",
              "3     6461\n",
              "2     2607\n",
              "Name: review_score, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VfZ-EHoVTyjP",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "ce319f6f-1b95-4116-926d-b25def711ac0"
      },
      "source": [
        "y_over"
      ],
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1, 1, 1, ..., 5, 5, 5])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QA6Qq8KIxtIU",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 121
        },
        "outputId": "a96da2e0-bb97-4f6a-f836-115848769fa4"
      },
      "source": [
        "# Simple Split\n",
        "#\n",
        "# split\n",
        "#train_set, test_set = train_test_split(orders, test_size=0.2, random_state=42)\n",
        "#test_set['review_score'].value_counts() / len(test_set['review_score'])"
      ],
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5    0.559202\n",
              "4    0.185714\n",
              "1    0.138650\n",
              "3    0.082121\n",
              "2    0.034312\n",
              "Name: review_score, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VXsIfwK83E2R",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Stratified Split\n",
        "#from sklearn.model_selection import StratifiedShuffleSplit\n",
        "\n",
        "#split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)\n",
        "#for train_index, test_index in split.split(orders, orders['review_score']):\n",
        " #   strat_train_set = orders.loc[train_index]\n",
        "  #  strat_test_set = orders.loc[test_index]"
      ],
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "14Unmg2s3awc",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 121
        },
        "outputId": "54bd9e82-bcf7-49eb-d704-6f07ca67980b"
      },
      "source": [
        "#strat_train_set['review_score'].value_counts() / len(strat_train_set['review_score'])"
      ],
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5    0.558260\n",
              "4    0.187686\n",
              "1    0.134465\n",
              "3    0.084115\n",
              "2    0.035473\n",
              "Name: review_score, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mV8Ys7qP3jjP",
        "colab_type": "text"
      },
      "source": [
        "By doing a stratified split we keep the same proportion between classes. This split better represent the original data and will possibli reduce any bias.\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-4EaHHvr45R5",
        "colab_type": "text"
      },
      "source": [
        "# Feature Engineering"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Z0NRjuW56f0K",
        "colab_type": "text"
      },
      "source": [
        "# Creating a Custom Transformer for FeatEng\n",
        "We need to guarantee that we are apply exactly the same transformation to new/unseen data. To do that we will create custom transformers using scikit-learn BaseEstimator.\n",
        "\n",
        "This first custom transformer will do the feature engineering that we just described earlier."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Hqn6OmsA41Bv",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 156
        },
        "outputId": "0794209c-9930-4532-b034-a5d4e763d6af"
      },
      "source": [
        "corr_matrix = strat_train_set.corr()\n",
        "corr_matrix['review_score'].sort_values(ascending=False)"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "review_score                  1.000000\n",
              "product_photos_qty            0.022280\n",
              "product_description_lenght    0.013805\n",
              "price                        -0.000592\n",
              "product_name_lenght          -0.013109\n",
              "freight_value                -0.035872\n",
              "order_item_id                -0.140872\n",
              "Name: review_score, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "I3Khikeh4_YR",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 713
        },
        "outputId": "7f5c4202-61a6-4a23-a701-34cf303d9890"
      },
      "source": [
        "# To consider Brazilian calendar and hollidays\n",
        "!pip install workalendar\n",
        "from workalendar.america import Brazil\n",
        "cal = Brazil()"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Collecting workalendar\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/36/48/969cfccf5bab55a337a1d2e4486aec41f212d34f74d0d91641d29206de3c/workalendar-10.3.0-py3-none-any.whl (170kB)\n",
            "\u001b[K     |████████████████████████████████| 174kB 8.8MB/s \n",
            "\u001b[?25hCollecting skyfield-data\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/c7/f0/5e40d2ae2cb78148193c24b36c8881c3b94a92d77e3d9d16b3a652f64524/skyfield_data-1.1.0-py2.py3-none-any.whl (16.0MB)\n",
            "\u001b[K     |████████████████████████████████| 16.0MB 284kB/s \n",
            "\u001b[?25hCollecting lunardate\n",
            "  Downloading https://files.pythonhosted.org/packages/4e/7e/377a3cbba646ec0cf79433ef858881d809a3b87eb887b0901cb83c66a758/lunardate-0.2.0-py3-none-any.whl\n",
            "Requirement already satisfied: pytz in /usr/local/lib/python3.6/dist-packages (from workalendar) (2018.9)\n",
            "Collecting pyluach\n",
            "  Downloading https://files.pythonhosted.org/packages/31/f3/852eb6be0788cb58095567f2f3e794a4c1571d13e29265416bfb8e6d9a41/pyluach-1.1.0-py3-none-any.whl\n",
            "Requirement already satisfied: setuptools>=1.0 in /usr/local/lib/python3.6/dist-packages (from workalendar) (49.2.0)\n",
            "Collecting pyCalverter\n",
            "  Downloading https://files.pythonhosted.org/packages/4f/5c/57c6853f7a5bc41fc9da7651ae67b9c76381083742613faa7381724081e9/pyCalverter-1.6.1.tar.gz\n",
            "Collecting skyfield\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/86/45/be4db25075fd588a9b3ed9cce3a4c6713e4c9c6ba5e9a1b713d5e6a22512/skyfield-1.26.tar.gz (289kB)\n",
            "\u001b[K     |████████████████████████████████| 296kB 48.9MB/s \n",
            "\u001b[?25hRequirement already satisfied: python-dateutil in /usr/local/lib/python3.6/dist-packages (from workalendar) (2.8.1)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.6/dist-packages (from skyfield->workalendar) (2020.6.20)\n",
            "Collecting jplephem>=2.13\n",
            "  Downloading https://files.pythonhosted.org/packages/6c/5b/f3228acdd1b7bba4573d2ea816a8da3193c03b16fe1b4955892cf663abc2/jplephem-2.14.tar.gz\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.6/dist-packages (from skyfield->workalendar) (1.18.5)\n",
            "Collecting sgp4>=2.2\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/1a/2c/c42c37a1b42595fb382e599d056c88c75bedb4a881da8f3789710f8ae65c/sgp4-2.12-cp36-cp36m-manylinux2010_x86_64.whl (247kB)\n",
            "\u001b[K     |████████████████████████████████| 256kB 55.0MB/s \n",
            "\u001b[?25hRequirement already satisfied: six>=1.5 in /usr/local/lib/python3.6/dist-packages (from python-dateutil->workalendar) (1.15.0)\n",
            "Building wheels for collected packages: pyCalverter, skyfield, jplephem\n",
            "  Building wheel for pyCalverter (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pyCalverter: filename=pyCalverter-1.6.1-cp36-none-any.whl size=4201 sha256=3d9617fed64152cfa9399222c0bb80a4378fc02b62612660e14f172ee1b6f7fd\n",
            "  Stored in directory: /root/.cache/pip/wheels/77/4d/86/db4ff4eca6178dbbd5a365d095f97f6021e2a48f09908be79c\n",
            "  Building wheel for skyfield (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for skyfield: filename=skyfield-1.26-cp36-none-any.whl size=327089 sha256=6f641923f672f7274efc59e4639a852a705b0c0ef4245a8763561dcefa26b8e8\n",
            "  Stored in directory: /root/.cache/pip/wheels/3b/58/4d/8a902f01263af264eb9826a8d44a8bf0daa5f18d4342a1f80f\n",
            "  Building wheel for jplephem (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for jplephem: filename=jplephem-2.14-cp36-none-any.whl size=45388 sha256=6b1385ca28197ae1b289991da9c8ca4ab90c65d713bb4bd6a0cf224e4d4c92bb\n",
            "  Stored in directory: /root/.cache/pip/wheels/cb/5e/34/8bebf91e6563267b99c908325b7cc5df4d24c7826ce174db19\n",
            "Successfully built pyCalverter skyfield jplephem\n",
            "Installing collected packages: skyfield-data, lunardate, pyluach, pyCalverter, jplephem, sgp4, skyfield, workalendar\n",
            "Successfully installed jplephem-2.14 lunardate-0.2.0 pyCalverter-1.6.1 pyluach-1.1.0 sgp4-2.12 skyfield-1.26 skyfield-data-1.1.0 workalendar-10.3.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fUfFbdR06UYf",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from sklearn.base import BaseEstimator, TransformerMixin\n",
        "class AttributesAdder(BaseEstimator, TransformerMixin):\n",
        "    def __init__(self):\n",
        "        pass    \n",
        "    \n",
        "    def fit(self, X, y=None):\n",
        "        return self\n",
        "    \n",
        "    def transform(self, X, y=None):\n",
        "        df = X.copy()\n",
        "        \n",
        "        # Calculate the estimated delivery time and actual delivery time in working days. \n",
        "        # This would allow us to exclude hollidays that could influence delivery times.\n",
        "        # If the order_delivered_customer_date is null, it returns 0.\n",
        "        df['wd_estimated_delivery_time'] = df.apply(lambda x: cal.get_working_days_delta(x.order_approved_at, \n",
        "                                                                                      x.order_estimated_delivery_date), axis=1)\n",
        "        df['wd_actual_delivery_time'] = df.apply(lambda x: cal.get_working_days_delta(x.order_approved_at, \n",
        "                                                                                   x.order_delivered_customer_date), axis=1)\n",
        "\n",
        "        # Calculate the time between the actual and estimated delivery date. If negative was delivered early, if positive was delivered late.\n",
        "        df['wd_delivery_time_delta'] = df.wd_actual_delivery_time - df.wd_estimated_delivery_time\n",
        "\n",
        "\n",
        "        # Calculate the time between the actual and estimated delivery date. If negative was delivered early, if positive was delivered late.\n",
        "        df['is_late'] = df.order_delivered_customer_date > df.order_estimated_delivery_date\n",
        "        \n",
        "        # Calculate the average product value.\n",
        "        df['average_product_value'] = df.price / df.order_item_id\n",
        "\n",
        "        # Calculate the total order value\n",
        "        df['total_order_value'] = df.price + df.freight_value\n",
        "        \n",
        "        # Calculate the order freight ratio.\n",
        "        df['order_freight_ratio'] = df.freight_value / df.price\n",
        "        \n",
        "        # Calculate the order freight ratio.\n",
        "        df['purchase_dayofweek'] = df.order_purchase_timestamp.dt.dayofweek\n",
        "                       \n",
        "        # With that we can remove the timestamps from the dataset\n",
        "        cols2drop = ['order_purchase_timestamp', 'order_approved_at', 'order_estimated_delivery_date', \n",
        "                     'order_delivered_customer_date']\n",
        "        df.drop(cols2drop, axis=1, inplace=True)\n",
        "        \n",
        "        return df"
      ],
      "execution_count": 329,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "U7B5khLp6UUy",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 161
        },
        "outputId": "604229be-c50c-4b50-f296-2feb44374c85"
      },
      "source": [
        "# Executing the estimator we just created\n",
        "attr_adder = AttributesAdder()\n",
        "feat_eng = attr_adder.transform(strat_train_set)\n",
        "feat_eng.head(3)"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>order_status</th>\n",
              "      <th>price</th>\n",
              "      <th>freight_value</th>\n",
              "      <th>order_item_id</th>\n",
              "      <th>customer_state</th>\n",
              "      <th>product_category_name_eng</th>\n",
              "      <th>product_name_lenght</th>\n",
              "      <th>product_description_lenght</th>\n",
              "      <th>product_photos_qty</th>\n",
              "      <th>review_score</th>\n",
              "      <th>wd_estimated_delivery_time</th>\n",
              "      <th>wd_actual_delivery_time</th>\n",
              "      <th>wd_delivery_time_delta</th>\n",
              "      <th>is_late</th>\n",
              "      <th>average_product_value</th>\n",
              "      <th>total_order_value</th>\n",
              "      <th>order_freight_ratio</th>\n",
              "      <th>purchase_dayofweek</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>32719</th>\n",
              "      <td>delivered</td>\n",
              "      <td>39.9</td>\n",
              "      <td>18.23</td>\n",
              "      <td>1.0</td>\n",
              "      <td>MG</td>\n",
              "      <td>computers_accessories</td>\n",
              "      <td>55.0</td>\n",
              "      <td>197.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>4</td>\n",
              "      <td>19</td>\n",
              "      <td>7</td>\n",
              "      <td>-12</td>\n",
              "      <td>False</td>\n",
              "      <td>39.9</td>\n",
              "      <td>58.13</td>\n",
              "      <td>0.456892</td>\n",
              "      <td>4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>43987</th>\n",
              "      <td>delivered</td>\n",
              "      <td>22.5</td>\n",
              "      <td>15.10</td>\n",
              "      <td>1.0</td>\n",
              "      <td>RJ</td>\n",
              "      <td>housewares</td>\n",
              "      <td>51.0</td>\n",
              "      <td>444.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>5</td>\n",
              "      <td>15</td>\n",
              "      <td>10</td>\n",
              "      <td>-5</td>\n",
              "      <td>False</td>\n",
              "      <td>22.5</td>\n",
              "      <td>37.60</td>\n",
              "      <td>0.671111</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2976</th>\n",
              "      <td>delivered</td>\n",
              "      <td>69.9</td>\n",
              "      <td>24.71</td>\n",
              "      <td>1.0</td>\n",
              "      <td>RS</td>\n",
              "      <td>furniture_decor</td>\n",
              "      <td>44.0</td>\n",
              "      <td>903.0</td>\n",
              "      <td>6.0</td>\n",
              "      <td>5</td>\n",
              "      <td>22</td>\n",
              "      <td>10</td>\n",
              "      <td>-12</td>\n",
              "      <td>False</td>\n",
              "      <td>69.9</td>\n",
              "      <td>94.61</td>\n",
              "      <td>0.353505</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "      order_status  price  ...  order_freight_ratio  purchase_dayofweek\n",
              "32719    delivered   39.9  ...             0.456892                   4\n",
              "43987    delivered   22.5  ...             0.671111                   0\n",
              "2976     delivered   69.9  ...             0.353505                   0\n",
              "\n",
              "[3 rows x 18 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "y0GD8p1W6URj",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "ab10f63a-e7f6-4cb6-c56c-9c25c9b2666d"
      },
      "source": [
        "corr_matrix = feat_eng.corr()\n",
        "corr_matrix['review_score'].sort_values(ascending=False)"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "review_score                  1.000000\n",
              "product_photos_qty            0.022280\n",
              "average_product_value         0.014869\n",
              "product_description_lenght    0.013805\n",
              "price                        -0.000592\n",
              "total_order_value            -0.003569\n",
              "purchase_dayofweek           -0.009580\n",
              "product_name_lenght          -0.013109\n",
              "freight_value                -0.035872\n",
              "order_freight_ratio          -0.038214\n",
              "wd_estimated_delivery_time   -0.062350\n",
              "order_item_id                -0.140872\n",
              "wd_delivery_time_delta       -0.229488\n",
              "wd_actual_delivery_time      -0.307135\n",
              "is_late                      -0.356554\n",
              "Name: review_score, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sp6mwx7n6TFe",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 451
        },
        "outputId": "259d7a8f-40aa-4c0c-d04e-4974a98e7345"
      },
      "source": [
        "feat_eng.info()"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 87421 entries, 32719 to 56558\n",
            "Data columns (total 18 columns):\n",
            " #   Column                      Non-Null Count  Dtype  \n",
            "---  ------                      --------------  -----  \n",
            " 0   order_status                87421 non-null  object \n",
            " 1   price                       87421 non-null  float64\n",
            " 2   freight_value               87421 non-null  float64\n",
            " 3   order_item_id               87421 non-null  float64\n",
            " 4   customer_state              87421 non-null  object \n",
            " 5   product_category_name_eng   87421 non-null  object \n",
            " 6   product_name_lenght         87421 non-null  float64\n",
            " 7   product_description_lenght  87421 non-null  float64\n",
            " 8   product_photos_qty          87421 non-null  float64\n",
            " 9   review_score                87421 non-null  int64  \n",
            " 10  wd_estimated_delivery_time  87421 non-null  int64  \n",
            " 11  wd_actual_delivery_time     87421 non-null  int64  \n",
            " 12  wd_delivery_time_delta      87421 non-null  int64  \n",
            " 13  is_late                     87421 non-null  bool   \n",
            " 14  average_product_value       87421 non-null  float64\n",
            " 15  total_order_value           87421 non-null  float64\n",
            " 16  order_freight_ratio         87421 non-null  float64\n",
            " 17  purchase_dayofweek          87421 non-null  int64  \n",
            "dtypes: bool(1), float64(9), int64(5), object(3)\n",
            "memory usage: 12.1+ MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NkPGkLnm9TBJ",
        "colab_type": "text"
      },
      "source": [
        "# Dealing with Categorical and Numerical Attributes"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ggm301R19R_1",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "class DataFrameSelector(BaseEstimator, TransformerMixin):\n",
        "    def __init__(self, attribute_names):\n",
        "        self.attribute_names = attribute_names\n",
        "    \n",
        "    def fit(self, X, y=None):\n",
        "        return self\n",
        "    \n",
        "    def transform(self, X, y=None):\n",
        "        return X[self.attribute_names]"
      ],
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NNqu5i0B9SLi",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from sklearn.pipeline import Pipeline\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "\n",
        "# for now we wont work with categorical data. Planning to add it on next releases\n",
        "num_pipeline = Pipeline([('selector', DataFrameSelector(num_attribs)),\n",
        "                         ('attribs_adder', AttributesAdder()),\n",
        "                         ('std_scaller', StandardScaler())\n",
        "                        ])"
      ],
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xq2Cwio69SGi",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 243
        },
        "outputId": "e0e46799-23da-4e82-bda2-efd31049ff1b"
      },
      "source": [
        "# lets see how the resulting data looks like\n",
        "orders_features_prepared = num_pipeline.fit_transform(orders_features)\n",
        "orders_features_prepared"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[-0.44131459, -0.11008851, -0.27982497, ..., -0.43407026,\n",
              "         0.40466955,  0.63861471],\n",
              "       [-0.53735833, -0.30902296, -0.27982497, ..., -0.54316711,\n",
              "         1.03639195, -1.39637208],\n",
              "       [-0.27572195,  0.30176298, -0.27982497, ..., -0.24021478,\n",
              "         0.09978501, -1.39637208],\n",
              "       ...,\n",
              "       [-0.44081781, -0.39736764, -0.27982497, ..., -0.45761137,\n",
              "         0.0683217 ,  0.63861471],\n",
              "       [-0.17029463, -0.40181666, -0.27982497, ..., -0.19754319,\n",
              "        -0.49073367,  1.6561081 ],\n",
              "       [ 0.33145109,  0.16511473, -0.27982497, ...,  0.33290236,\n",
              "        -0.57287814, -1.39637208]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8UPyZp1A-I12",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "6f3bfe8b-3318-422f-9650-43a8281f006e"
      },
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "\n",
        "lin_reg = LinearRegression()\n",
        "lin_reg.fit(orders_features_prepared, orders_labels)"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "L5xhIT33-Iw7",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "some_data = orders_features.iloc[:8]\n",
        "some_labels = orders_labels.iloc[:8]\n",
        "some_data_prepared = num_pipeline.transform(some_data)"
      ],
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6MBxVJKeV7e_",
        "colab_type": "text"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wkNB4VkE-Iqe",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 72
        },
        "outputId": "2c061097-33f5-4f83-e0c1-7287aed86a21"
      },
      "source": [
        "print('Predicted: {} \\n Labels: {}'.format(list(lin_reg.predict(some_data_prepared)), list(some_labels.values)))"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Predicted: [4.200990438393185, 4.164893735056262, 4.220587093283143, 4.35703562563107, 4.278321832870888, 4.35741398908125, 2.1552175818279866, 4.170959230377667] \n",
            " Labels: [4, 5, 5, 4, 4, 5, 5, 5]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5VCY1BVb9SEK",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "bb8abdf3-7da8-4a15-c353-c34e34d7ee6e"
      },
      "source": [
        "from sklearn.metrics import mean_squared_error\n",
        "\n",
        "predictions = lin_reg.predict(orders_features_prepared)\n",
        "lin_mse = mean_squared_error(orders_labels, predictions)\n",
        "lin_rmse = np.sqrt(lin_mse)\n",
        "lin_rmse"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1.2409979983355306"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GsXUnaI8D6_f",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "db69918d-2f5a-4dfa-95f2-18958fa5accc"
      },
      "source": [
        "from sklearn.ensemble import RandomForestRegressor\n",
        "\n",
        "forest_reg = RandomForestRegressor()\n",
        "forest_reg.fit(orders_features_prepared, orders_labels)\n",
        "\n",
        "predictions = forest_reg.predict(orders_features_prepared)\n",
        "forest_mse = mean_squared_error(orders_labels, predictions)\n",
        "forest_rmse = np.sqrt(forest_mse)\n",
        "forest_rmse"
      ],
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.46348915678698616"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-svHyjYeD_6D",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "outputId": "fdb2b11b-6fac-41bc-edb5-1abc47b3254c"
      },
      "source": [
        "print('Predicted: {} \\n Labels: {}'.format(list(forest_reg.predict(some_data_prepared)), list(some_labels.values)))"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Predicted: [3.97, 4.7, 4.35, 4.04, 3.89, 4.88, 4.73, 4.88] \n",
            " Labels: [4, 5, 5, 4, 4, 5, 5, 5]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fYWgSR3icCYF",
        "colab_type": "text"
      },
      "source": [
        "Note: Nan values dropped for now but can be imputed. Categorical values changed to one hot encoded. Classification instead of regression starting from logistic regression then others.\n",
        "Using cross validation set later and grid search. Ending with pipeline to predict."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "n_uxJdBmEEKq",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from sklearn.linear_model import LogisticRegression\n",
        "\n",
        "clf = LogisticRegression(random_state=0).fit(orders_features_prepared, orders_labels)"
      ],
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Csr2AB11CS6o",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "2327cc2f-8d6c-4c55-d016-35535a2e7179"
      },
      "source": [
        "clf.score(orders_features_prepared, orders_labels)"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.5978311847267819"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hwVTtuIGCaNW",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "some_data_prepared = num_pipeline.transform(strat_test_set)"
      ],
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ajg0pIeiC52m",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}