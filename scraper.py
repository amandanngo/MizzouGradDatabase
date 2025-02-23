import requests
from bs4 import BeautifulSoup

# # Making a GET request
# r = requests.get('https://studenthonors.missouri.edu/grad-lists/2024-spring-grad/missouri/index.html')

# # Parse the content
# soup = BeautifulSoup(r.content, 'html.parser')

# # Find the container with the class
# container = soup.find(attrs={"class": "miz-page-content__full"})

# if container:
#     # Find the first <ul> inside the container
#     ul = container.find('ul')

#     if ul:
#         # Get all <a> elements inside the <ul>
#         links = ul.find_all('a')

#         # Print the links
#         for link in links:
#             print(link['href'])  # Prints the href attribute
#     else:
#         print("No <ul> found in the container.")
# else:
#     print("Container with class 'miz-page-content__full' not found.")


county = requests.get(f'https://studenthonors.missouri.edu/grad-lists/2024-spring-grad/missouri/adair')

county_soup = BeautifulSoup(county.content, 'html.parser')


print(county_soup)