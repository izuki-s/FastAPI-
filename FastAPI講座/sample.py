import requests
import json

def main():
     url = "https://deploy_api-1-b8259602.deta.app"
     data = {
          'x': 3,
          'y': 4
     }
     res = requests.post(url,json.dumps(data),verify = False)
     print (res.json())

if __name__ == "__main__":
    main()