import json
from pathlib import Path



def load_device(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)



if __name__ == "__main__":
    path = Path(__file__).with_name("device.json")
    device = load_device(path)\
    
    print(f"Device: {device['name']}")
    print(f"Host: {device['host']}")
    print(f"Port: {device['port']}")