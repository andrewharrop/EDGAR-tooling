import requests

def get_submissions(CIK:str):
    pass

def get_concepts(CIK:str, concept:str,data_class="us-gaap"):
    url = "https://data.sec.gov/api/xbrl/companyconcept/CIK" + CIK + "/" + data_class + "/" + concept + ".json"
    user_agent = "Standard Analytics"
    headers = {'User-Agent': user_agent}
    try:
        r = requests.get(url, headers=headers)
    except:
        print("Error in request:get_concepts")
        return None
    
    try:
        return r.json()
    except:
        print("Error in json:get_concepts")
        return None
def get_facts(CIK:str):
    pass

