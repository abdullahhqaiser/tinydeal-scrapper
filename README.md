# Tinydeal Web Scraper Project

This project utilizes Scrapy to scrape special offers data from the Tinydeal website (accessed via [web.archive.org](https://web.archive.org/)). It extracts key product information, including URLs, titles, normal prices, and sale prices, navigating through multiple pages to ensure comprehensive data collection.

## Project Description

The scraper collects the following information about discounted products:

-   **Product URL:** The link to the product page.
-   **Product Title:** The name of the product.
-   **Normal Price:** The original price of the product.
-   **Sale Price:** The discounted price of the product.

The spider automatically navigates through the "next page" links to gather data from all available pages within the special offers section.

## Project Structure
-   `items.py`: Defines the data structure for scraped items.
-   `spiders/special_offers.py`: Contains the Scrapy spider for scraping Tinydeal's special offers.
-   `settings.py`: Configures Scrapy settings, including user agent and pagination handling.
-   `pipelines.py`: Handles post-processing of scraped data (if needed).
-   `middlewares.py`: Handles middleware for request and response processing (if needed).

## Setup Instructions

1.  **Install Python:** Ensure you have Python installed on your system.
2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**

    -   **Windows:**

        ```bash
        venv\Scripts\activate
        ```

    -   **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install Scrapy:**

    ```bash
    pip install scrapy
    ```

## Run Commands

-   **Run the spider and collect data:**

    ```bash
    scrapy crawl special_offers
    ```

-   **Save the scraped data to a JSON file:**

    ```bash
    scrapy crawl special_offers -o special_offers.json
    ```

-   **Save the scraped data to a CSV file:**

    ```bash
    scrapy crawl special_offers -o special_offers.csv
    ```

-   **Save the scraped data to an XML file:**

    ```bash
    scrapy crawl special_offers -o special_offers.xml
    ```

## Project Workflow

![ChatGPT Image Apr 9, 2025, 02_32_18 AM](https://github.com/user-attachments/assets/d13780c0-fe5f-4dc8-acda-714d1d6bde23)



## Key Features

-   **Custom User Agent:** Configured to avoid getting blocked by the website.
-   **Pagination Handling:** Scrapes multiple pages of special offers.
-   **XPath Selectors:** Uses XPath for precise data extraction.
-   **Modern Python Practices:** Follows best practices for project structure and code organization.
-   **Respects robots.txt:** Adheres to the website's robots.txt rules (`ROBOTSTXT_OBEY = True`).
-   **Twisted AsyncIO Reactor:** Configured for better performance.
-   **Web Archive usage:** Project scrapes data from web.archive.org for historical data.

## Notes

-   This project uses [web.archive.org](https://web.archive.org/) to access historical snapshots of the Tinydeal website.
-   The `ROBOTSTXT_OBEY` setting in `settings.py` is set to `True` to respect the website's robots.txt rules.
-   The Twisted AsyncIO reactor is configured for improved performance, which is default in recent Scrapy versions, but is good to be aware of.
