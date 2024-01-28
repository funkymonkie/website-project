from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


html_text = requests.get(
    "https://funkymonkie.github.io/website-project/"
).text

souped_html = BeautifulSoup(html_text, "lxml")

# Extract data from the My Top 3 Favourite section
categories = souped_html.select(".sections .category")

data = {"Category": [], "First Favourite": [], "Second Favourite": [], "Third Favourite": []}

for category in categories:
    category_name = category.select_one(".title h3").text.strip()
    items = [item.text.strip() for item in category.find_all("dd")[:3]]

    data["Category"].append(category_name)
    data["First Favourite"].append(items[0] if len(items) > 0 else "")
    data["Second Favourite"].append(items[1] if len(items) > 1 else "")
    data["Third Favourite"].append(items[2] if len(items) > 2 else "")
    
    # Delay in requests to not get banned from site
    time.sleep(2)
    

# Create a Pandas DataFrame from the extracted data
df = pd.DataFrame(data)

#df = pd.DataFrame.from_dict(data, orient="index").T
print(df)

# create excel
excel_filename = "scraped_Fav_3_data.xlsx"
df.to_excel(excel_filename, index=False)
print(f"Scraped data has been saved to {excel_filename}.")
