from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Create a WebDriver instance (you'll need to provide the path to your WebDriver executable)
driver = webdriver.Chrome()

# Define the URL of the page to scrape
url = "https://swappa.com/listings/google-pixel-6?carrier=unlocked&exclude_businesses=on"

# Send an HTTP GET request to the URL
response = driver.get(url)

try:
    # Wait for some time to allow JavaScript to load content (adjust as needed)
    driver.implicitly_wait(10)

    # Find all div elements with the specified class
    table = driver.find_element(By.ID, "listings_table")

    headers = []
    table_headers = table.find_element(By.TAG_NAME, "thead").find_elements(By.TAG_NAME, "th")
    for item in table_headers:
        headers.append(item.text)
    
    listings = []
    # Extract data from the table
    for row in table.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, 'tr'):
        item = []
        for cell in row.find_elements(By.TAG_NAME, 'td'):
            item.append(cell.text)
        item.pop()
        listings.append(item)

finally:
    # Close the WebDriver
    driver.quit()

df = pd.DataFrame(listings, columns=headers)
df.set_index(headers[0], inplace=True)
print(df)