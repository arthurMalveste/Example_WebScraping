
# 🤖 AI News Scraper

An automated system built with Python to track and collect the latest news about Artificial Intelligence.

This project was developed as a practical study on **Web Scraping**, focusing on handling dynamic web pages, data extraction from HTML, and structured data storage.

## ⚙️ Features

* **Automated Browsing:** Uses Selenium to handle dynamic content and ensure the page is fully loaded before extraction.
* **Intelligent Parsing:** Leverages BeautifulSoup to navigate the HTML tree and isolate news blocks (titles and URLs).
* **Data Persistence:** Automatically exports the gathered data into a `noticias.json` file for easy access and future integration.
* **Modular Code:** Designed with reusable functions to allow scraping from different news sources with minimal adjustments.

## 🛠️ Tech Stack

* **Python 3**
* **Selenium:** Web automation and browser control.
* **BeautifulSoup 4:** HTML parsing and data extraction.
* **JSON:** Light-weight data interchange format.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed and a modern web browser (like Google Chrome).

### 1. Installation
Clone this repository or download the files. Then, install the required dependencies:
```bash
pip install selenium beautifulsoup4

```

### 2. Running the Scraper

Execute the main script:

```bash
python main.py

```

### 3. Checking Results

After the browser closes, a file named `noticias.json` will be generated in the root folder containing the scraped data.

## 🗺️ Roadmap & Future Enhancements

This project is part of an ongoing learning journey. Future updates will include:

* [x] Base scraper with JSON output.
* [x] Refactoring into reusable functions.
* [ ] Content extraction (scraping the full article text from the links).
* [ ] Integration with LLM (Large Language Models) for automatic summarization.
* [ ] Web Dashboard for interactive news reading.

---

*Developed for learning purposes by [Arthur Malveste / ArthurMalveste]*

