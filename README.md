# Laptop Price Predictor 💻

## Overview

Laptop Price Predictor is an innovative tool designed to estimate the market value of laptops. This project leverages machine learning techniques to analyze various features of laptops, providing users with accurate price predictions. Check out the Laptop Price Predictor [here](https://laptop-price-ml.streamlit.app/).

![Screenshot](https://github.com/aliyusifov99/laptop_price_predictor/blob/main/Assets/Screenshot.png)



## Inspiration 💡

This project was inspired by the challenge of finding fair market prices for laptops. Whether buying or selling, users often struggle to determine the appropriate price for a laptop, considering its features and condition. This tool aims to bring transparency and ease to this process, benefiting both buyers and sellers.

## Features 🌟

- **Accurate Price Estimation**: Provides reliable price predictions based on laptop specifications.
- **Comprehensive Data Analysis**: Utilizes a diverse dataset, encompassing various brands and specifications.
- **User-Friendly Interface**: Simple and intuitive, allowing for quick and easy price estimations.

## Installation 🔧

Clone the project using: `git clone git@github.com:aliyusifov99/laptop_price_predictor.git`


## Usage 🚀

The tool is straightforward to use. Simply input the laptop's specifications, and the system will provide an estimated market value. This process involves sophisticated machine learning algorithms working behind the scenes to ensure accuracy.

## Technical Details 🔍

### Data Preparation and Feature Engineering

The foundation of the predictive model lies in meticulous data preparation and feature engineering. The dataset, comprising diverse laptop specifications and their market prices, undergoes a thorough cleaning process. Features with low correlation to the price, such as Flash storage and Hybrid types, are strategically dropped to streamline the model.

A significant aspect of our feature engineering involves the categorization of GPU options. Given the wide variety of GPUs, they are classified into three main categories: Intel, Nvidia, and AMD. This simplification aids in reducing complexity and improving the model's interpretability.

Additionally, the operating systems are categorized to create a more structured dataset. This step ensures that the model accurately captures the influence of different operating systems on laptop pricing.

### Visualization and Analysis

Data visualization plays a crucial role in our analysis, offering insights into the various features and their relationship with laptop prices. Through detailed visualizations, we identify patterns and trends that inform the model development process.

### Model Building and Evaluation

The core of the project is the machine learning model, trained on this carefully prepared dataset.Random Forest  regression techniques were utilized to build a model that can accurately predict laptop prices based on their specifications. The model's performance is rigorously evaluated to ensure reliability and accuracy in price estimation.

### Implementation and Tools

The model is implemented in Python, leveraging libraries like `pandas` for data manipulation and `scikit-learn` for the machine learning tasks. The project's codebase is structured to be transparent and easily understandable, encouraging contributions and collaborations.

## Contributions 👥

Contributions are always welcome! Whether it's by adding new data, improving the model, or suggesting new features, your input can help make the Laptop Price Predictor even better.

## References 📚

- [Scikit-learn Machine Learning in Python](https://scikit-learn.org/stable/)
- [Pandas: Python Data Analysis Library](https://pandas.pydata.org/)

## Connect with me

Feel free to reach out or follow my work through the following platforms:

- [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aliyusifov99)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ali-yusifov/)
- [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/aliyusifovpy)
- [![Portfolio](https://img.shields.io/badge/Personal_Website-4CAF50?style=for-the-badge&logo=google-earth&logoColor=white)](https://www.aliyusifovai.com/)
- [![Support](https://img.shields.io/badge/Buy_Me_A_Coffee-F7DF1E?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/aliyusifov)
