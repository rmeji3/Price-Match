import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the HTML from the website
url = 'https://www.google.com/search?q=uic&sca_esv=4100df04cd8ca781&sca_upv=1&hl=en&authuser=0&sxsrf=ADLYWILDmBqPZc2Z9VwyE3W5vF8LqyJyVA:1727740636635&source=hp&biw=1920&bih=911&ei=3Dr7ZpurJJKQ0PEPgfHv0QQ&iflsig=AL9hbdgAAAAAZvtI7OrPPcjr4y2Fwd6Lp_HFSNYSfbzc&ved=0ahUKEwibiaK37-uIAxUSCDQIHYH4O0oQ4dUDCBA&uact=5&oq=uic&gs_lp=EgNpbWciA3VpYzIIEAAYgAQYsQMyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARI1QtQ4whY_QpwAXgAkAEAmAE5oAGjAaoBATO4AQPIAQD4AQGKAgtnd3Mtd2l6LWltZ5gCBKACrgGoAgrCAgcQIxgnGOoCwgIEECMYJ8ICCxAAGIAEGLEDGIMBmAMEkgcBNKAHpg8&sclient=img&udm=2'  # Replace with the target website's URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    html_content = response.text  # Get the HTML content of the page

    # Step 2: Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')

    # Step 3: Extract information (Example: Get the title of the page)
    page_title = soup.title.string
    print("Page Title:", page_title)

    # Example: Find all links on the page
    for link in soup.find_all('img'):
        print(link.get('src'))
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

    #test
