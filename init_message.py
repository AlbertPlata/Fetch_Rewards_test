import datetime
import json

filename = "emulated_data.json"

data = list()

# Generate messages
for i in range(1, 101):
    message = {
        'user_id': f'User{i}',
        'device_type': f'DeviceType{i}',
        'ip': f'192.168.0.{i}',
        'device_id': f'DeviceID{i}',
        'locale': f'Locale{i}',
        'app_version': f'AppVersion{i}',
        'create_date': str(datetime.datetime.now())
    }
    data.append(message)

# Create File
with open(filename, "w") as file:
    json.dump(data, file, indent=4)


