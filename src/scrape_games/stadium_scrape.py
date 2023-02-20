import pandas as pd
from bs4 import BeautifulSoup
import requests
import progressbar
import time
# =============================================================================
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# =============================================================================
# Function to Scrape for the stadium details
# Returns a data frame with the stadium data 
#
# =============================================================================


def scrape_stadium(link, error):
# =============================================================================
#     Parser
# =============================================================================

    url = link
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

# =============================================================================
#     Scrape
# =============================================================================
    error_list = []
    try:
        stadium = soup.find_all('div', class_= 'head')[-1].get_text().strip()
        table =  soup.find('table', class_ = 'standard_tabelle yellow')
        rows = table.find_all('tr')
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            data.append(cols)
        df = pd.DataFrame(data[0:3], columns =['0','1']).set_index('0').T
        df.columns = df.columns.str.replace(':', '')
        df = df.replace('\.', '', regex = True)
        df.insert(0, 'stadium', stadium)
        return df
    except:
        error_list =error_list+ [url]
        error_list.to_pickle(error)
        print('error ', url)
    
# =============================================================================
# /////////////////////////////////////////////////////////////////////////////
# =============================================================================
test_link = "https://www.worldfootball.net/venues/la-rosaleda-malaga/"
stadium_url_list = pd.read_pickle('D:/Python Projects/Capstone/src/scrape_games/stadium_url_list.pkl')
test_link_list = ['https://www.worldfootball.net/venues/memorial-stadium-bristol/', 'https://www.worldfootball.net/venues/huish-park-yeovil-somerset/', 'https://www.worldfootball.net/venues/county-ground-swindon/', 'https://www.worldfootball.net/venues/victoria-park-hartlepool/', 'https://www.worldfootball.net/venues/st-james-park-exeter/', 'https://www.worldfootball.net/venues/boundary-park-oldham/']
error_loc ='D:/Python Projects/Capstone/src/scrape_games/error_stadium_scrape_list.pkl'

stadium_data = pd.DataFrame(columns = ['stadium', 'City', 'Country', 'Capacity', 'url'])

widgets = [' [',
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
         '] ',
           progressbar.Bar('#'),' (',
           progressbar.ETA(), ') ',progressbar.Percentage(), 
          ]
 


bar = progressbar.ProgressBar(max_value=len(stadium_url_list)//100,
                              widgets=widgets).start()

x = 0
for stadium_url in stadium_url_list:
    try:
        temp_df = scrape_stadium(stadium_url,error_loc)
        temp_df['url'] = stadium_url
        stadium_data = pd.concat([stadium_data, temp_df])
        x += 1
        if  x % 100 == 0:
            y = str(x)
            try:
                stadium_data.to_pickle('D:/Python Projects/Capstone/data/RAWDATA/stadium_data_pkl/stadium_data' + y +'.pkl')
            except:
                print(stadium_url)
            bar.update(x//100)
    except:
            print(stadium_url)
        
stadium_data.to_csv('D:/Python Projects/Capstone/data/RAWDATA/stadium_data.csv')

print(stadium_data)