from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a WebDriver instance (you'll need to provide the path to your WebDriver executable)
driver = webdriver.Chrome()

# Define the URL of the page to scrape
url = "https://obsidian.md/plugins"

# Send an HTTP GET request to the URL
response = driver.get(url)

try:
    # Wait for some time to allow JavaScript to load content (adjust as needed)
    driver.implicitly_wait(10)

    # Find all div elements with the specified class
    divs_with_class = driver.find_elements(By.CSS_SELECTOR, 'div.p-5.flex.flex-col.rounded-lg.bg-secondary.transition-all.hover\\:shadow-2xl.hover\\:bg-gray-800')

    plugins = []
    # Print the content of each matching div
    for div in divs_with_class:
        # Extract the download number
        downloads = div.find_elements(By.TAG_NAME, 'p')[1].text.strip()
        downloads = int(downloads.replace(" downloads", "").replace(",", ""))
        
        # Extract the name of the plugin
        plugin_name = div.find_element(By.TAG_NAME, 'div').text.strip()
        
        # Extract the "Learn More" link
        learn_more_link = div.find_element(By.PARTIAL_LINK_TEXT, 'Learn more').get_attribute('href')

        plugins.append({"name": plugin_name, "downloads": downloads, "learn_more_link": learn_more_link})
finally:
    # Close the WebDriver
    driver.quit()
    
# Sort the list of plugins_info by the number of downloads in descending order
sorted_plugins = sorted(plugins, key=lambda x: x["downloads"], reverse=True)

# Print the sorted plugins
for plugin in sorted_plugins:
    if plugin["downloads"] > 20000:
        print("Plugin Name:", plugin["name"])
        print("Downloads:", plugin["downloads"])
        print("Learn More Link:", plugin["learn_more_link"])
        print()