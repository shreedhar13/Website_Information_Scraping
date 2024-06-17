# Website_Information_Scraping

# Web Scraping Project

This project is designed to scrape various websites, extract relevant information, and store it in a structured format. The project includes multiple steps: setting up the environment, scraping the website, storing the scraped data, and cleaning the data.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
    - [Step 1: Install Dependencies](#step-1-install-dependencies)
    - [Step 2: Scrape Website](#step-2-scrape-website)
    - [Step 3: Store Scraped Data](#step-3-store-scraped-data)
    - [Step 4: Clean Scraped Data](#step-4-clean-scraped-data)
    - [Step 5: Get Cleaned Data](#step-5-get-cleaned-data)

## Installation

1. Clone the repository:

    ```sh
    https://github.com/shreedhar13/Website_Information_Scraping.git
    cd Website_Information_Scraping
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

## Usage

### Step 1: Install Dependencies

Ensure all necessary libraries are installed by using the `1_requirements.txt` file.

```sh
pip install -r 1_requirements.txt
```

### Step 2: Scrape Website
Run the 2_Scraping_Website.py script to scrape data from various websites. This script will extract information such as social media links, tech stack, meta title, meta description, payment gateways, language, and category.

```sh
python 2_Scraping_Website.py
```

### Step 3: Store Scraped Data
The scraped data is stored in a file named 3_Scraped_Website_Info.csv.

### Step 4: Clean Scraped Data
Run the 4_Cleaning_Scraped_Data.py script to clean the scraped data.
```sh
python 4_Cleaning_Scraped_Data.py
```

### Step 5: Get Cleaned Data
The final cleaned data is stored in a file named 5_Cleaned_Data.csv

```sh
web-scraping-project/
│
├── 1_requirements.txt          # List of required packages
├── 2_Scraping_Website.py       # Script to scrape websites
├── 3_Scraped_Website_Info.csv  # File to store scraped data
├── 4_Cleaning_Scraped_Data.py  # Script to clean scraped data
├── 5_Cleaned_Data.csv          # File to store cleaned data
├── README.md                   # Project documentation
├── venv/                       # Virtual environment directory
└── data/                       # Directory to store data files
```

### step 6: Create DataBase Named "Website_Information" And Table Named "websites_info" In MySQL WorkBench 
```sh
create database website_information;

use website_information;

CREATE TABLE web_page (
    id INT AUTO_INCREMENT PRIMARY KEY,
    URL VARCHAR(500),
    Social_Media_Links VARCHAR(500),
    Tech_Stack VARCHAR(500),
    Meta_Title VARCHAR(500),
    Meta_Description VARCHAR(500),
    Payment_Gateways VARCHAR(500),
    Language VARCHAR(500),
    Category VARCHAR(500)
);
```
![Screenshot (166)](https://github.com/shreedhar13/Website_Information_Scraping/assets/153434680/1ddd86c1-f499-435f-9fd9-e715ec3e876b)








