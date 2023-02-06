import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import progressbar
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
    a_href = soup.find_all('table', class_= "standard_tabelle")[-1]
    a_href = a_href.find('a', href= True)
    a_href = str(a_href['href'])
    url = link2 + a_href

    return url
# =============================================================================
# /////////////////////////////////////////////////////////////////////////////
# =============================================================================
 

# =============================================================================
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# =============================================================================
# Function to Scrape for the match details. Link must be a string
# Returns a list with variables in this order
#[home_team, home_score, away_team, away_score, day_of_week, month, day_of_month, year, time, attendance, stadium]
# =============================================================================

def scrape_match(link, link2):
# =============================================================================
#     Parser
# =============================================================================

    url = link
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

# =============================================================================
#     Scrape
# =============================================================================
    try:
        score = soup.find('div', class_= 'resultat')
    except:
        score = None
    try:
        home_team = soup.find('th', align='center')
    except: 
        home_team = None
    try:
        full_date = home_team.find_next('th', align='center')
    except:
        full_date = None
    try:
        away_team = full_date.find_next('th', align='center')
    except:
        away_team = None
    try:
        match_info_grouped = soup.find_all('table', class_= "standard_tabelle")[-1]
    except:
        match_info_grouped = None
    try:
        attendance = match_info_grouped.find_all('td', class_='dunkel')[5]
    except:
        attendance = None
    try:
        stadium = match_info_grouped.find_all('td', class_='dunkel')[2]
    except: 
        stadium = None

    score = score.get_text().strip()
    home_team = home_team.get_text().strip()        
    full_date = full_date.get_text().strip()
    away_team = away_team.get_text().strip()
    attendance = attendance.get_text().strip().replace(".", "")
    stadium = stadium.get_text().strip()


    full_date = full_date.split(",")
    day_of_week = full_date[0]
    full_date2 =full_date[1].split(".")
    day_of_month = full_date2[0].strip()
    full_date3 = full_date2[1].split(" ")
    month = full_date3[1]
    year_and_time = full_date3[2]
    year = year_and_time[:4]
    time = year_and_time[-5:]

    home_score = score.split(":")[0]
    away_score = score.split(":")[1]
    try:
        a_href = scrape_a_href(link, link2)
    except:
        a_href = None
    match_details = [home_team, home_score, away_team, away_score, day_of_week, month, day_of_month, year, time, attendance, stadium, a_href]
    return match_details
# =============================================================================
# /////////////////////////////////////////////////////////////////////////////
# =============================================================================





#    for a_href in td.find_all("a", href =True):

        # a_href = str(a_href["href"])
        # if a_href.startswith("/report/"):
        #     url = link2 + a_href
        #     a_href_list.append(url)



# =============================================================================
#     read url to scrape
# =============================================================================




url_list = pd.read_csv("src\scrape_games\individual_match_summary_list.csv", index_col = 0)
url_list = url_list[url_list.columns[0]].values.tolist()
# url_list = pd.read_csv("src\scrape_games\dummy_match_list.csv", index_col = 0)
# url_list = url_list[url_list.columns[0]].values.tolist()
url2 = 'https://www.worldfootball.net'
x = 0
stadium_list = []
error_links = []
error_stadium_links =[]
match_data_df = pd.DataFrame(columns=['home_team', 'home_score', 'away_team', 'away_score', 'day_of_week', 'month', 'day_of_month', 'year', 'time', 'attendance', 'stadium', 'a_href'])

widgets = [' [',
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
         '] ',
           progressbar.Bar('*'),' (',
           progressbar.ETA(), ') ',
          ]
 
bar = progressbar.ProgressBar(max_value=79677,
                              widgets=widgets).start()
x = 1
for url in url_list:
    try:
        match_data=scrape_match(url, url2)
    except:
        error_links += [url]
        print("ERROR" + url)
    try:
        stadium_link =scrape_a_href(url, url2)
    except:
        error_stadium_links += [url]
    column_list = ['home_team', 'home_score', 'away_team', 'away_score', 'day_of_week', 'month', 'day_of_month', 'year', 'time', 'attendance', 'stadium', 'a_href']
    match_dict = dict(zip(column_list, match_data))
    temp_df = pd.DataFrame.from_dict(match_dict, orient = 'index').T
    stadium_list.append(stadium_link)
    match_data_df = pd.concat([match_data_df, temp_df], axis = 0)
    x +=1
    if x % 25 == 0:
        match_data_df.to_csv('data/RAWDATA/individual_match_data.csv')
    time.sleep(0.1)
    bar.update(x)

match_data_df.to_csv('data/RAWDATA/individual_match_data.csv')
df = pd.DataFrame(stadium_list)
df.to_csv('src/scrape_games/stadium_url_list.csv')

