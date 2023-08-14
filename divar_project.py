import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://divar.ir/s/tehran'

# Add headers to the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Send a GET request to the URL and get the response
response = requests.get(url, headers=headers)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the div elements with the specified class
objs = soup.find_all('div', {'class': "post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46"})

# Initialize empty lists to store the titles
list_x = []
list_y = []

# Loop through each object
for obj in objs:
    try:
        # Find the title and label of the object
        title = obj.find('h2', {'class': 'kt-post-card__title'}).text.strip()
        label = obj.find('div', {'class': 'kt-post-card__description'}).text.strip()

        # Check the label and append the title to the appropriate list
        if label == 'نو':
            list_x.append(title)
        if label == 'کارکرده':
            list_y.append(title)
    except:
        pass

# Print the titles for 'نو'
print('نو:')
[print(i) for i in list_x]

# Print a separator
print('----------------------')

# Print the titles for 'کارکرده'
print('کارکرده:')
[print(i) for i in list_y]
