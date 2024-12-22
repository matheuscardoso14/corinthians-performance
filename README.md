# **Corinthians' performance in the 2024 Brazilian Soccer Championship**

## Overview
This is a project that tells a little about how Sport Club Corinthians Paulista has performed in their national soccer championship: Brasileirão, how we're accustomed to call it in Brazil. This project has three files:

- **A Python script** that scrapes a website about soccer statistics. This script will get data about all the matches that Corinthians has played and save them as a .csv file.
- **A .csv file** (you'll need to generate it first) with all the data about the matches. This file has five columns:
    - **Date**: the date when the match has been played.
    - **Home**: the home team.
    - **Goals_Home**: goals scored by the home team.
    - **Goals_Away**: goals scored by the away team.
    - **Away**: the away team.

- **A Jupyter Notebook**, where the data are manipulated and used to plot two charts:
    - **A pie chart**, comparing the number of wins, defeats and draws.
    - **A stacked vertical bar chat**, comparing the number of wins, defeats and draws by month, from April to December.

## Installation
Follow these steps to set up the project:

1. **Clone the repository:**

    ``` bash
    git clone <"link">
    cd corinthians-performance
    ```
2. **Install Jupyter Notebook (if you don't have it):**
    ```
    pip install jupyter notebook
    jupyter notebook
    ```
    You can also install Jupyter Notebook in Visual Studio Code by installing its extension, whose name is "Jupyter".

3. **Install the necessary libraries:**
    ``` bash
    pip install selenium numpy pandas matplotlib seaborn
    ```

4. **Install a Chromium-based browser (I do recommend Google Chrome)**

    If you prefer Google Chrome, you can download it [here](https://www.google.com/intl/en-US/chrome/).


5. **Download the ChromeDriver:**

    The ChromeDriver will allow us to use the browser to scrape. To install it, follow these steps:
    
    1. Access the [ChromeDriver download page](https://googlechromelabs.github.io/chrome-for-testing/).

    2. Select the channel correspondent to your browser (it will be easier if you had installed Google Chrome before).

    3. Find the URL correspondent to your platform (also check if the binary's name is "chromedriver"), copy and paste it in your search bar.

    4. Save your ChromeDrive where you wish.

    5. Extract the files from the .zip file (I recommend use [WinRAR](https://www.win-rar.com/) to do this).
    
## Usage
Here's a step-by-step on how to use the project:

1. **Replace the paths in *scraper.py* with the paths where your ChromeDriver is and where you wish to save the .csv file:**

    ``` python
    # Initalizing the driver
    options = Options()
    service = Service("<Path where your ChromeDriver is (include the executable file)>")
    driver = webdriver.Chrome(service=service, options=options)
    ```
    ``` python
    # Saving the DataFrame into a .csv file
    df.to_csv("Path where you'll save your .csv file (include the file)", sep=",", index=False, encoding="1252")
    ```

2. **Run the scraper:**

    ``` bash
    python scraper.py
    ```
    You will have generated a .csv file with the name you defined (e.g.: *stats.csv*).

3. **Open Jupyter Notebook (skip this if you're in VS Code):**

    ``` bash
    jupyter notebook
    ```
    In Jupyter Notebook, find and open *analysis.ipynb*

4. **In *analysis.ipynb*, replace the path in the first cell with the path where you saved the .csv file:**

    ``` python
    # Creating a DataFrame based on the .csv file that contains data about all Corinthians" matches
    df = pd.read_csv("<Path where your .csv file is>", sep=",", encoding="1252")
    ```

5. **Execute all the cells**
    
    You will have successfully generated two plots:

    ![Plots](.gitignore/plot.png)