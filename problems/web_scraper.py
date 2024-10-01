import requests
from bs4 import BeautifulSoup

def scrape_all_inputs(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
  except requests.exceptions.RequestException as e:
    print(f"Error getting the URL: {e}")
    return []

  soup = BeautifulSoup(response.content, 'html.parser')
  all_inputs = soup.find_all('input')

  input_data = []
  for input_element in all_inputs:
    input_dict = {
        'type': input_element.get('type'),
        'name': input_element.get('name'),
        'value': input_element.get('value'),
    }
    input_data.append(input_dict)

  return input_data

url = 'https://www.google.com/'
all_inputs = scrape_all_inputs(url)

if all_inputs:
  for input_info in all_inputs:
    print(input_info)
else:
  print("No <input> elements found on the page.")