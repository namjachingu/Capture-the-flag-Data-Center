import requests
import json

from env import config

from utils.auth import IntersightAuth


auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'],
                      api_key_id=config['INTERSIGHT_API_KEY'])

BASE_URL='https://www.intersight.com/api/v1'
url = f"{BASE_URL}/cond/Alarms"
response = requests.(url, auth=auth)


#Make the request to the required endpoint to retreive the ntp policies
url = f"{BASE_URL}/ntp/Policies"
response = requests.get(url, auth=auth)
#print(response.json())


### STAGE 1 ###
#Retrieve alarm description
def alamDescription():
    url = f"{BASE_URL}/cond/Alarms" 
    response = requests.get(url, auth=auth)
    for i in response.json()["Results"]:
        print("Description of Alarm: ", i["Description"])

def physicalSummaries():
    #A summary of the physical infrastructure. 
    url = f"{BASE_URL}/compute/PhysicalSummaries"
    response = requests.get(url, auth=auth)
    for i in response.json()["Results"]:
        print("Management mode: ", i["ManagementMode"])
        print("Management IP address: ", i["MgmtIpAddress"])
        print("Name: ", i["Name"])
        print("Number of CPUs", i["NumCpus"])
        print("Number of CPU Cores", i["NumCpuCores"])
        print("Powerstate: ", i["OperPowerState"])
        print("Firmware: ", i["Firmware"])
        print("Model: ", i["Model"])
        print("Serial: ", i["Serial"])
        #Intersight.LicenseTier = 'Premier'

def complianceHCL():
    #Retrieve compliance with Hardware compatibility list (HCL)
    url = f"{BASE_URL}/cond/HclStatuses"
    response = requests.get(url, auth=auth)
    for i in response.json()["Results"]:
        print(i['HclOsVendor'])
        print(i["HclOsVersion"])

def kubernetesClusterNames():
    #Overview of all kubernetes clusters running on this cluster
    url = f"{BASE_URL}/kubernetes/Clusters"
    response = requests.get(url, auth=auth)
    for i in response.json()["Results"]:
        print(i["Name"])

def numberOfDeployements():
    #Overivew of deployments running in the kubernetes cluster. 
    url = f"{BASE_URL}/kubernetes/Deployments"
    response = requests.get(url, auth=auth)
    print(len(response.json()["Results"])) #=100


