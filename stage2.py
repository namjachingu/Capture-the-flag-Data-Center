
import requests
import json
from env import config
import csv

from utils.auth import get_authenticated_aci_session


# Check for ACI simulator access
aci_session = get_authenticated_aci_session(config['ACI_USER'], config['ACI_PASSWORD'], config['ACI_BASE_URL'])

def healthScore(): 
    response = aci_session.get(f"{config['ACI_BASE_URL']}/api/class/fabricHealthTotal.json")
    #print(response.json())
    for resp in response.json()["imdata"]:
        print("Total health: ", resp["fabricHealthTotal"])
        print("Timestamp: ", resp["fabricHealthTotal"]["attributes"]["modTs"])
        print("Maximum severity: ", resp["fabricHealthTotal"]["attributes"]["maxSev"])

        return resp["fabricHealthTotal"], "\n\n", resp["fabricHealthTotal"]["attributes"]["modTs"], "\n\n", \
            resp["fabricHealthTotal"]["attributes"]["maxSev"]
    


with open('health.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(healthScore())


if __name__ == '__main__':
    healthScore()

