import json
import time
import http.client
import pprint
import os

MID_API_KEY = os.getenv('MID_API_KEY')
image_url = 'https://greedotstorage.blob.core.windows.net/greefile/upload/0741ec81-096e-466b-8521-05ddc37bc738.png'

data = {
    "prompt": f"""
    {image_url}
    A simple and abstract green character with distinct outlines, human-like form featuring two arms, two legs, and a torso. 
    The character has a pointed decoration or horn-like feature on its head, and its face is marked with simple lines for eyes and a mouth. 
    At the center of the face, there's a symbol resembling a crown, suggesting royal or noble attributes. 
    The character is set against a pure white background with no other elements or scenery, evoking an image as if it's floating without any ground contact. 
    The design emphasizes cuteness and coolness while maintaining a minimalistic approach, suitable for a child's drawing interpretation.
    """
}
 
headers = {
    'Authorization': f'Bearer {MID_API_KEY}',  
    'Content-Type': 'application/json'
}
 
def send_request(method, path, body=None, headers={}):
    conn = http.client.HTTPSConnection("cl.imagineapi.dev")
    conn.request(method, path, body=json.dumps(body) if body else None, headers=headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    conn.close()
    return data
 
prompt_response_data = send_request('POST', '/items/images/', data, headers)
pprint.pp(prompt_response_data)
 
def check_image_status():
    response_data = send_request('GET', f"/items/images/{prompt_response_data['data']['id']}", headers=headers)
    if response_data['data']['status'] in ['completed', 'failed']:
        print('Completed image details',)
        pprint.pp(response_data['data'])
        return True
    else:
        print(f"Image is not finished generation. Status: {response_data['data']['status']}")
        return False
 
while not check_image_status():
    time.sleep(5) 