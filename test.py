import requests
import datetime
import os
import pandas as pd

def download_csv_FO():
    today = datetime.date.today()
    date = today - datetime.timedelta(days=4)  
    formatted_date = date.strftime("%Y%m%d")   

    url = f"https://www.bseindia.com/download/BhavCopy/Derivative/BhavCopy_BSE_FO_0_0_0_20250818_F_0000.CSV"

   
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0 Safari/537.36",
        "Referer": "https://www.bseindia.com/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        filename = f"bhavcopy_{formatted_date}.csv"
        with open(filename, "wb") as f:
            f.write(r.content)
        print(f" Downloaded: {filename}")
        return filename
    else:
        print(f" Download failed (HTTP {r.status_code}) — possibly holiday or no trading.")
        return None

filename = download_csv_FO()
if filename and os.path.exists(filename):
    df = pd.read_csv(filename)
    print(df.head())