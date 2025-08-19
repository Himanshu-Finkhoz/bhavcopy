import requests
import datetime
import pandas as pd

def download_csv(save=True):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0 Safari/537.36",
        "Referer": "https://www.bseindia.com/"
    }
   
    target_date = datetime.datetime.today() - datetime.timedelta(days=1)
    
    while True:
        day_name = target_date.strftime("%A")
        
        if day_name in ["Saturday", "Sunday"]:
            target_date -= datetime.timedelta(days=1)
            continue
        
        date_str = target_date.strftime("%Y%m%d")
        url = (
            "https://www.bseindia.com/download/BhavCopy/Equity/"
            f"BhavCopy_BSE_CM_0_0_0_{date_str}_F_0000.CSV"
        )
        filename = f"bhavcopy_{date_str}.csv"
        
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            if save:
                with open(filename, "wb") as f:
                    f.write(r.content)
                return filename
            else:
                return r.content
        else:
            target_date -= datetime.timedelta(days=1)
            continue

def bhavcopy_derivative(save=True):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0 Safari/537.36",
        "Referer": "https://www.bseindia.com/"
    }
   
    target_date = datetime.datetime.today() - datetime.timedelta(days=1)
    
    while True:
        day_name = target_date.strftime("%A")
        
        if day_name in ["Saturday", "Sunday"]:
            target_date -= datetime.timedelta(days=1)
            continue
        
        date_str = target_date.strftime("%Y%m%d")
        url = (
            
            "https://www.bseindia.com/download/BhavCopy/Derivative/"
            f"BhavCopy_BSE_FO_0_0_0_{date_str}_F_0000.CSV"
        )
        filename2 = f"bhavcopy_{date_str}.csv"
        
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            if save:
                with open(filename2, "wb") as f:
                    f.write(r.content)
                return filename2
            else:
                return r.content
        else:
            target_date -= datetime.timedelta(days=1)
            continue

def bhavcopy_derivative_NSE(save=True):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0 Safari/537.36",
        "Referer": "https://www.nseindia.com/"
    }
   
    target_date = datetime.datetime.today() - datetime.timedelta(days=1)
    
    while True:
        day_name = target_date.strftime("%A")
        
        if day_name in ["Saturday", "Sunday"]:
            target_date -= datetime.timedelta(days=1)
            continue
        
        date_str = target_date.strftime("%Y%m%d")
        url = (
            
            "https://www.bseindia.com/download/BhavCopy/Derivative/"
            f"BhavCopy_BSE_FO_0_0_0_{date_str}_F_0000.CSV"
        )
        filename2 = f"bhavcopy_{date_str}.csv"
        
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            if save:
                with open(filename2, "wb") as f:
                    f.write(r.content)
                return filename2
            else:
                return r.content
        else:
            target_date -= datetime.timedelta(days=1)
            continue

import requests
import datetime
import zipfile
import io
import pandas as pd

def BhavCopy_NSE_CM(save=True):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/139.0 Safari/537.36",
        "Referer": "https://www.nseindia.com/"
    }

    target_date = datetime.datetime.today() - datetime.timedelta(days=1)

    while True:
        if target_date.strftime("%A") in ["Saturday", "Sunday"]:
            target_date -= datetime.timedelta(days=1)
            continue

        date_str = target_date.strftime("%Y%m%d")

        url = f"https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_{date_str}_F_0000.csv.zip"

        #https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_20250818_F_0000.csv.zip

        filename = f"bhavcopy_nse_{date_str}.csv"

        print("Trying:", url)

        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                for f in z.namelist():
                    if f.endswith(".csv"):
                        with z.open(f) as zf:
                            df = pd.read_csv(zf)
                            if save:
                                df.to_csv(filename, index=False)
                                print(f"✅ Saved {filename}")
                                return filename
                            else:
                                return df
        else:
            print(f"Failed ({r.status_code}), checking previous day...")
            target_date -= datetime.timedelta(days=1)
