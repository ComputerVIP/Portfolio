import requests
from bs4 import BeautifulSoup
import urllib.request
import os

def download_all(url):
  """Downloads a webpage, its links, images, and text."""
  try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    # Download text
    text = ""
    for paragraph in soup.find_all('p'):
      text += paragraph.get_text() + "\n\n"
    with open('downloaded_text.txt', 'w', encoding='utf-8') as f:
      f.write(text)
    # Download links
    links = []
    for link in soup.find_all('a', href=True):
      links.append(link['href'])
    with open('downloaded_links.txt', 'w', encoding='utf-8') as f:
      for link in links:
        f.write(link + "\n")
    # Download images
    '''
    images = []
    for img in soup.find_all('img', src=True):
      img_url = img['src']
      img_name = img_url.split('/')[-1]
      images.append((img_url, img_name))
    for img_url, img_name in images:
      urllib.request.urlretrieve(img_url, img_name)
    print("Webpage, links, images, and text downloaded successfully.")
    '''
  except requests.exceptions.RequestException as e:
    print(f"Error fetching webpage: {e}")
input()
if __name__ == "__main__":
  a = input("1 for download webpage text and links, 2 for exit\n")
  try:
    a = int(a)
    if a == 1:
      url = input("Enter the URL of the webpage: ")
      download_all(url)
    elif a == 2:
        video_script_path = os.path.abspath("main_menu.py")
        os.system(f'python "{video_script_path}"')
    else:
      print("Invalid input. Please enter 1 or 2.")
  except ValueError:
    print("Invalid input. Please enter 1 or 2.")