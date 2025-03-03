# Scrapy-HandsOn

## 📌 Overview
Scrapy-HandsOn is a web scraping project built using **Scrapy**, designed to extract product information from e-commerce websites. The project fetches details like **title, price, and description** and stores them in a structured format.

## 🛠️ Tech Stack
- **Python** 🐍
- **Scrapy** 🕷️
- **Pandas** (For data processing)
- **CSV/JSON** (For data storage)

## 📂 Project Structure
```
Scrapy-HandsOn/
│── price_tracker/        # Scrapy spider for scraping products
│   ├── spiders/          # Directory for spider scripts
│   │   ├── products.py   # Main spider file
│   ├── items.py          # Defines data structure
│   ├── pipelines.py      # Data processing pipelines
│   ├── settings.py       # Scrapy settings
│── output/               # Stores scraped data (CSV/JSON)
│── README.md             # Project documentation
│── requirements.txt      # Dependencies
```

## 🚀 Installation & Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/GauravSighariya/Scrapy-HandsOn.git
   cd Scrapy-HandsOn
   ```

2. **Create a virtual environment (Optional but recommended)**
   ```sh
   python -m venv env
   source env/bin/activate  # For Mac/Linux
   env\Scripts\activate  # For Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## 🕷️ Running the Scraper
Run the Scrapy spider to start scraping:
```sh
scrapy crawl products -o output/products.json
```
This will store the scraped data in **output/products.json**.

## 📊 Output Format
Example of extracted data:
```json
[
    {
        "title": "Airflow Plus",
        "price": "Rs. 2,299.37",
        "description": "TWS | 13mm Sound Drivers"
    },
    {
        "title": "BASH 2.0",
        "price": "Rs. 1,999.00",
        "description": "Wireless Headphones | Deep Bass"
    }
]
```

## 🛠️ Customization
Modify `spiders/products.py` to customize:
- The target website URL
- The data fields being scraped
- Output format (CSV, JSON, Database)

## 📜 License
This project is licensed under the **MIT License**.

---
### 🎯 Author: **Gaurav Yadav**  
Connect with me on [GitHub](https://github.com/GauravSighariya) 🚀

