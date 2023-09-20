import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
       # Send a GET request to the URL and return the response content (body) 
        response = requests.get(self.url)
        return response.content
    
     
    def load_json(self):
       # Use get_response_body to get the response content and parse it as JSON
      response_body = self.get_response_body()
      return json.load(response_body)
    
    # Example usage:
if __name__ == "__main__":
    url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
    get_requester = GetRequester(url)
    json_data = get_requester.load_json()
    print(json_data)