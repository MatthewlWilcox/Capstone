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

def scrape_a_href(link, link2):

# =============================================================================
#     Parser
# =============================================================================


    url = link
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")



# =============================================================================
#     Scrape
# =============================================================================
    a_href_list = []
    for td in soup.find_all("td"):
        for a_href in td.find_all("a", href =True):
            a_href = str(a_href["href"])
            if a_href.startswith("/report/"):
                url = link2 + a_href
                a_href_list.append(url)
    return a_href_list
# =============================================================================
# /////////////////////////////////////////////////////////////////////////////
# =============================================================================
 


# =============================================================================
#     Bringing in the teams to set up the loop of 
# =============================================================================

tempdf = pd.read_csv("src/scrape_games/league_header_list.csv")
list_of_headers = tempdf[tempdf.columns[0]].values.tolist()

url2 = "https://www.worldfootball.net/"

url_front = "https://www.worldfootball.net/all_matches/"

url_list = []
for header in list_of_headers:
    url = url_front + header
    years_range = range(2010,2023)
    for year in years_range:
        year_0 = year
        year_1 = year + 1 
        final_url = url + str(year_0) + "-" + str(year_1) + "/"
        url_list.append(final_url)


all_a_href = []

for url in url_list:
    temp_a_href = scrape_a_href(url, url2)
    all_a_href += temp_a_href

df = pd.DataFrame(all_a_href)
df.to_csv('src/scrape_games/individual_match_list.csv')
