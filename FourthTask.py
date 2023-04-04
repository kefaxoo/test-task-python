import json
from datetime import datetime

def main():
    file_json = open('resultJson.json')
    data = json.load(file_json)
    for item in data:
        if "updated" in item.keys():
            item["updated"] = datetime.now().isoformat()

    file_json = open('resultJson.json', 'w')
    json.dump(data, file_json)

if __name__ == "__main__":
    main()