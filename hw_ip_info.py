import json
import requests


# INPUT and VERIFY

def inputDomain():
    print("\n")
    print(f"{'#'*7} WELCOME TO IP / DOMAIN INFO APP {'#'*7} \n\n")
    query = input("Enter an IP or DOMAIN name: ")
    print(f"{'#'*47} ")
    if len(query.strip()) == 0:
        print("Error... Try Again... ENTER IP or DOMAIN name ")
        exit()

    if len(query.strip()) != 0:
        endpoint = f"http://ip-api.com/json/{query}?fields=22278143"
        response = requests.get(endpoint)
        data = json.loads(response.text)
        print(f"Your enter :  {query}, with IP: {data['query']}")
        print(f"{'#'*47} ")
        return data


# VERIFY STATUS and new var

data = inputDomain()
if data['status'] == 'success':
    orig = f"{data['country']} / {data['city']}"
    lat_lot = f"{data['lat']} / {data['lon']}"
    org = data['org']
    isp = data['isp']
else:
    print('Error... Try Again... ENTER REAL IP or DOMAIN name')
    exit()


# INFO DETAILS

def inf_dom():
    print(f"\nThe domain is located in {data['continent']} / {data['country']} [{data['countryCode']}],\n\
    \rRegion/State: {data['regionName']} / City: {data['city']},\n\
    \rLatitude of {data['city']}: {data['lat']} and Longitude of {data['city']}: {data['lon']}\n")
    print(f"Internet service provider: {data['isp']}")
    print(f"Organisation: {data['org']},\n\
    \rNumber and Organisation: {data['as']}")
    print(f"IP: {data['query']}")


# MENU APP

def menu():
    try:
        option = -1
        while option != 0:
            print("\n")
            print("##### MENU ##### APP ##### IP ##### INFO ######")
            print("> 1. ALL INFO ABOUT YOUR IP / DOMAIN")
            print("> 2. COUNTRY / CITY OF IP / DOMAIN")
            print("> 3. LATITUDE AND LONGITUDE OF CITY")
            print("> 4. ORGANIZATION")
            print("> 5. Internet service provider IP/DOMAIN")
            print("> 0. Exit")
            print("##############################################")
            print("CHOOSE OPTION > ")

            option = int(input())
            if option == 1:
                data = inf_dom()
            if option == 2:
                print(orig)
            if option == 3:
                print(lat_lot)
            if option == 4:
                print(org)
            if option == 5:
                print(isp)
            if option >= 6 or option <= -1:
                print("##### ERROR ##### TRY AGAIN ##### ERROR #####")
            if option == 0:
                print("##### GOODBYE ##### EXIT ##### GOODBYE #####")
                exit()
    except ValueError:
        menu()
menu()
