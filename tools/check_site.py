import requests


def site_is_up(url):
    try:
        code = requests.get(f"http://{url}").status_code
        if code == 200:
            return(True)
        
        else:
            return(False)
    except:
        return(False)
  