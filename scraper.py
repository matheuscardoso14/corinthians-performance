## Importing the necessary libraries and functions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Website to be scraped
website = "https://www.adamchoi.co.uk/overs/detailed"

# Initalizing the driver
options = Options()
service = Service("<Path where your ChromeDriver is (include the executable file)>")
driver = webdriver.Chrome(service=service, options=options)

# Getting the website and maximizing the navigator"s window
driver.get(website)
driver.maximize_window()

# Waiting 3 seconds before starting the scraping process
time.sleep(3)

# Selecting the league of Brazil (Brasileirão Série A)
dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("Brazil")

# Waiting 3 seconds before the next step
time.sleep(3)

# Selecting all team"s matches
all_matches_button = driver.find_element(By.XPATH, "//label[@analytics-event='All matches']")
all_matches_button.click()

# Waiting 3 seconds before collect the data
time.sleep(3)

# Getting a table that has data about all Corinthians" matches
team = driver.find_elements(By.TAG_NAME, "tbody")[5]
team_matches = team.find_elements(By.XPATH, "./tr[contains(@class, 'ng-scope is')]")

# The data will be stored in these lists
date = []
home = []
score = []
away = []

# Storing the data about each match
for match in team_matches:
    date.append(match.find_element(By.XPATH, "./td[1]").text)
    home.append(match.find_element(By.XPATH, "./td[2]").text)
    score.append(match.find_element(By.XPATH, "./td[3]").text)
    away.append(match.find_element(By.XPATH, "./td[4]").text)

# Stopping the driver
driver.quit()

## Importing the necessary libraries for the next step
import pandas as pd
import datetime

# Creating a DataFrame based on the data that we"ve collected before
df = pd.DataFrame({"Date": date, "Home": home, "Score": score, "Away": away})

# Dividing the column "Score" into two columns: "Goals_Home" and "Goals_Away"
df[["Goals_Home", "Goals_Away"]] = df["Score"].str.split(" - ", expand=True)

# Deleting the column "Score" because we won"t need it anymore
df.drop("Score", axis=1, inplace=True)

# Organizing the order of the columns
df = df[["Date", "Home", "Goals_Home", "Goals_Away", "Away"]]

# Transforming the column "Data" into a datetime column
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# Sorting the matches based on the "Date" column
df.sort_values("Date", ascending=True, inplace=True)

# Displaying the DataFrame
print(df)

# Saving the DataFrame into a .csv file
df.to_csv("Path where you'll save your .csv file (include the file)", sep=",", index=False, encoding="1252")