import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np



# =============================================================================
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# =============================================================================
# Function to Scrape for the a_href. Link input must be a string
# Returns a list of a_href
#
# =============================================================================

# def scrape_a_href(link, link2):

# =============================================================================
#     Parser
# =============================================================================

    # url = link
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, "html.parser")

# =============================================================================
#     Scrape
# =============================================================================
    # a_href_list = []
    # for td in soup.find_all("td"):
    #     for a_href in td.find_all("a", href =True):
    #         a_href = str(a_href["href"])
    #         if a_href.startswith("/report/"):
    #             url = link2 + a_href
    #             a_href_list.append(url)
    # return a_href_list
# =============================================================================
# /////////////////////////////////////////////////////////////////////////////
# =============================================================================

url = "https://www.worldfootball.net/report/premier-league-2022-2023-afc-bournemouth-aston-villa/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

match_details = []
stadium_link = []

score = soup.find_all('div', class_= 'resultat')
home_team = soup.find('th', align='center').text
time = home_team.find_next('th', align='center').text
away_team = time.find_next('th', align='center').text

match_info_grouped = soup.find_all('table', class_= "standard_tabelle")[-1]
attendance = match_info_grouped.find_all('td', class_='dunkel')[5]
stadium = match_info_grouped.find_all('td', class_='dunkel')[2]

print(home_team)
print("3")
print(time)
print("34")
print(away_team)