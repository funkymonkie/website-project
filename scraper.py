from bs4 import BeautifulSoup
import requests
import pandas as pd


html_text = requests.get(
    "https://wearecodenation.com/2024/01/23/data-course-playground/"
).text

souped_html = BeautifulSoup(html_text, "lxml")

h5s = souped_html.find_all(
    "h5", class_="elementor-heading-title elementor-size-default"
)

h6s = souped_html.find_all("h6")
# print(h5s)

# for h5 in h5s:
#     if ":" in h5.text:
#         print(h5.text)
#         h6_match = h5.find_next('h6')
#         for single_date in h6_match.strings:
#             print(single_date)


# months = [
#         'January','February','March','April','May','June','July',
#         'August','September','October','November','December']


# for h6 in h6s:
#     if any(month in h6.text for month in months):
#         print(h6.text)
#         course_dates.append(h6.text)


# for h6 in h6s:

# create dict
course_dates_dict = {}

# add values to dict
for h5 in h5s:
    if ":" in h5.text:
        key = h5.text
        values = []

        h6_match = h5.find_next("h6")
        for single_date in h6_match.stripped_strings:
            values.append(single_date)

        course_dates_dict[key] = values

# for key, values in course_dates_dict.items():
#     print(f"{key}: {values}")


# Create Dataframe from dict
# df = pd.DataFrame(list(course_dates_dict.items()), columns=["COURSE", "DATES"])

# df = pd.DataFrame({key:pd.Series(value) for key value in courses.items()})

df = pd.DataFrame.from_dict(course_dates_dict, orient="index").T
print(df)

# create excel
excel_filename = "scraped_cn_data.xlsx"
df.to_excel(excel_filename, index=False)
print(f"Scraped data has been saved to {excel_filename}.")
