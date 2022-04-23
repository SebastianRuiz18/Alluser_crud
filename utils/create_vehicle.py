import requests

URL = "http://127.0.0.1:5000/vehicles/"
SAMPLE_vehicle = {
    "color": "red",
    "licence_plate":"test1",
    "v_type": "car",
}


def create_vehicle(color, licence_plate, v_type, owner_id, active):
    vehicle_data = SAMPLE_vehicle
    vehicle_data["color"] = color
    vehicle_data["licence_plate"] = licence_plate
    vehicle_data["v_type"] = v_type
    response = requests.post(URL, json=vehicle_data)
    if response.status_code == 204:
        print("Successfully created a new vehicle.")
    else:
        print("Something went wrong while trying to create a vehicle.")
    

if __name__ == "__main__":
    color = input("Enter a color: ")
    licence_plate = input("Enter a licence plate: ")
    v_type = input("Enter v_type: ") 
    create_vehicle(color, licence_plate, v_type)
