import requests



def site_is_up(url):
    try:
        session = requests.Session()
        code = session.get(f"https://{url}", verify=False).status_code
        if code == 200:
            return(True)

        else:
            code = session.get(f"http://{url}", verify=False).status_code
            if code == 200:
                return(True)
            else:
                print("target not available")
                print("site is down, status code: ", code)
                return(False)

    except Exception as e:
        print("target not available")
        print("Error: ", e)
        return(False)
