# HTML/DOM Exploration Notes
# ===========================
# URL scraped: https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart
#
# Search result list item:
#   Tag: li
#   Class: cp-search-result-item
#
# Title element:
#   Tag: span or a
#   Class: title-content
#
# Author element:
#   Tag: a (link)
#   Class: author-link
#   Note: multiple authors joined with semicolon ;
#
# Format/Year element:
#   Tag: span inside div
#   Class: manifestation-item-format-info-wrap
#   Note: we grab the first span inside that div

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
# Task 3: Load the Durham County search page
# Step 1: Load the web page
url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

# Step 2: Wait until result items appear on the page
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.cp-search-result-item")))

# Step 3: Find all the li elements
books = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")

# Step 4: Create an empty list to store results
results = []

# Step 5: Main loop - extract data from each book
for book in books:
    # Extract the title
    title = book.find_element(By.CSS_SELECTOR, ".title-content").text
    
    # Extract all author elements and join with semicolons
    authors = book.find_elements(By.CSS_SELECTOR, ".author-link")
    author_text = "; ".join([author.text for author in authors])

    # Extract the format and year
    format_year = ""
    format_elements = book.find_elements(By.CSS_SELECTOR, ".manifestation-item-format-info-wrap span")
    if format_elements:
        format_year = format_elements[0].text

    # Create a dict and add it to results list
    results.append({
        "Title": title,
        "Author": author_text,
        "Format-Year": format_year,
    })

# Task 4: Prepare the DataFrame and save files
# Step 1: Create a DataFrame from the results list
df = pd.DataFrame(results)
print(df)

# Step 2: Write the DataFrame to get_books.csv
df.to_csv("get_books.csv", index=False)

# Step 3: Write the results list to get_books.json
with open("get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

driver.quit()