import json
import hashlib

# On this section mask PII using hash
def mask_pii(message):
    message["masked_device_id"] = hashlib.sha256(message["device_id"].encode()).hexdigest()
    message["masked_ip"] = hashlib.sha256(message["ip"].encode()).hexdigest()
    return message

# Created file with data hashed using the original data
with open("emulated_data.json", "r") as json_file:
    messages = json.load(json_file)

# Mask the PII fields in each message
masked_messages = [mask_pii(message) for message in messages]


with open("masked_messages.json", "w") as json_file:
    json.dump(masked_messages, json_file, indent=4)
