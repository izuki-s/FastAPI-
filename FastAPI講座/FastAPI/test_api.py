import requests
import json

def main():
    url =  'http://localhost:8000/item'
    body = {
        "name": "T-shirts",
        "description": "string",
        "price": 5980,
        "tax": 1.1
    }   
    res = requests.post(url,json.dumps(body))
    print(res.json())

if __name__ == "__main__":
    main()