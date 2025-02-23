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

# print(county_soup)

#find all county headings
county_names = county_soup.find_all(attrs={"class": "miz-graphik"})

for county in county_names:
    print(county.text)

tables = county_soup.find_all(attrs={"class": "table table-hover"})

student_degrees = list()

# print(table)
for table in tables:
    table_bodies = table.find_all('tbody')

    for body in table_bodies:
        rows = body.find_all('tr')

        # print(rows)
    for row in rows:
        cells = row.find_all('td')
        cell_texts = [cell.get_text(strip=True) for cell in cells]
        print(cell_texts)  # Prints as a list for better clarity
        student_degrees.append(cell_texts)

print(student_degrees[0][1])