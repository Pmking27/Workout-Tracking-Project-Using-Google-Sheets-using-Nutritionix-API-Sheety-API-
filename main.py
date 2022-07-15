import requests
from datetime import datetime

GENDER ="ENTER YOUR GENDER"
WEIGHT_KG =" WEIGHT_KG"
HEIGHT_CM =  "ENTER YOUR HEIGHT_CM"
AGE =  "ENTER YOUR AGE"

#https://www.nutritionix.com/business/api 

APP_ID= "Nutritionix-API APP_ID"
API_KEY= "Nutritionix.-API API_KEY"

#https://sheety.co/
BEARER_TOKEN= "Sheety-API BEARER_TOKEN"

EXERCISE_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT= "Sheety-API SHEETY_ENDPOINT"

exercise_text = input("Tell me which exercises you did: ")

header={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

param={
 "query":exercise_text,
 "gender":GENDER,
 "weight_kg":WEIGHT_KG,
 "height_cm":HEIGHT_CM,
 "age":AGE
}


response=requests.post(url=EXERCISE_ENDPOINT,json=param,headers=header)
response.raise_for_status()
data=response.json()

bearer_headers = {
    "Authorization": BEARER_TOKEN
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs,headers=bearer_headers)

    print(sheet_response.text)
