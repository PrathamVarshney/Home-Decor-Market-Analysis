# 🏠 Home Decor Data Analysis & Visualization Project
This project performs a simple analysis and visualization of the home decor product market. It includes web scraping, sentiment analysis, and several visual representations of sales and demand trends.

## 🔧 Features
- **Web Scraping**: Extracts product names and prices from IKEA’s home decor page.
- **Sentiment Analysis**: Analyzes sample customer reviews using TextBlob.
- **Sales Trend Visualization**: Plots monthly and extended sales data.
- **Market Demand Chart**: Bar chart showing demand for different decor categories.
- **Price Range Comparison**: Box plot comparison between IKEA, West Elm, and Etsy Sellers.
- **Customer Sentiment Pie Chart**: Visualizes overall customer opinion distribution.
- **Social Media Impact**: Scatter plot showing correlation between Instagram followers and sales.

## 🧰 Libraries Used
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `requests`
- `beautifulsoup4`
- `textblob`

## ▶️ How to Run

1. Install dependencies:
    pip install numpy pandas matplotlib seaborn requests beautifulsoup4 textblob

2. Run the script:
    python main.py

3. Ensure you have internet access to fetch live data from IKEA.

## 📈 Output
- Console output of scraped product names and prices.
- Sentiment polarity of 3 example customer reviews.
- Visualizations rendered using Matplotlib and Seaborn.

## ⚠️ Notes
- Web scraping may fail if IKEA changes its website structure.
- For consistent results, replace live scraping with stored HTML or use an API if available.
- This is a simplified demo; data volumes and accuracy may vary.
