import json

FILE = "data/gastos.json"

def load():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)