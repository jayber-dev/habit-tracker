import requests
import datetime

# ----------------------- date handling -----------------------------
current_date = datetime.datetime.today()

date_argu = ("{:04d}{:02d}{:02d}".format(current_date.date().year,current_date.date().month,current_date.date().day))

print(date_argu)
# ----------------------- user creation -----------------------------
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "mnbfskskje23j3j42bb2"
PIXELA_PARAMS = {
    "token": TOKEN,
    "username":"jayber1",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# pixela_user_creation = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_PARAMS)

# print(pixela_user_creation.text)

# ------------------------- grapgh setting -----------------------------
PIXELA_GRAPH_ENDPOINT = "https://pixe.la/v1/users/jayber1/graphs"
HEADERS = {'X-USER-TOKEN':TOKEN}
PIXELA_GRAPH_SETTINGS = {
    "id":"p00nani",
    "name":"quit smoking",
    "unit":"graph",
    "type":"int",
    "color":"shibafu"


}

# pixela_graph_set = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=PIXELA_GRAPH_SETTINGS, headers=HEADERS)

# print(pixela_graph_set.text)

# ------------------------- posting a value ---------------------------------
PIXEL_POSING_ENDPOINT = 'https://pixe.la/v1/users/jayber1/graphs/p00nani'

PIXEL_POSING_VALUE = {
    "date":date_argu,
    "quantity":"5"
}

posting_value = requests.post(url=PIXEL_POSING_ENDPOINT, json=PIXEL_POSING_VALUE, headers=HEADERS)

print(posting_value.text)
