from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Task 6: Extract OWASP Top 10 vulnerabilities
# Step 1: Load the OWASP project page
base_url = "https://owasp.org/www-project-top-ten/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(base_url)

wait = WebDriverWait(driver, 15)

# Step 2: Navigate to the OWASP Top Ten 2025 page
link_2025 = wait.until(
    EC.presence_of_element_located((By.LINK_TEXT, "OWASP Top Ten 2025"))
)
page_2025 = link_2025.get_attribute("href")
driver.get(page_2025)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))

# Step 3: Find the top 10 vulnerability links using XPath
xpath_expr = (
    "//main//a[starts-with(normalize-space(.), 'A01:2025') or "
    "starts-with(normalize-space(.), 'A02:2025') or "
    "starts-with(normalize-space(.), 'A03:2025') or "
    "starts-with(normalize-space(.), 'A04:2025') or "
    "starts-with(normalize-space(.), 'A05:2025') or "
    "starts-with(normalize-space(.), 'A06:2025') or "
    "starts-with(normalize-space(.), 'A07:2025') or "
    "starts-with(normalize-space(.), 'A08:2025') or "
    "starts-with(normalize-space(.), 'A09:2025') or "
    "starts-with(normalize-space(.), 'A10:2025')]"
)
items = driver.find_elements(By.XPATH, xpath_expr)

# Step 4: Extract title and link for each vulnerability
results = []
for item in items:
    title = item.text.strip()
    href = item.get_attribute("href")
    results.append({"Title": title, "Link": href})

# Step 5: Save results to CSV and print them
if results:
    df = pd.DataFrame(results)
    print(df)
    df.to_csv("owasp_top_10.csv", index=False)
else:
    print("No OWASP top 10 items found.")

driver.quit()
