import requests
from bs4 import BeautifulSoup

# URL of the web page you want to extract text from
url = 'https://github.com/tolinkshare/freenode'

# Send a GET request to the URL and fetch the HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content,'html.parser')

# Find all the text within HTML tags
text = soup.get_text()

# Find the nodes
start_phrase = "🚀免费v2rayN节点列表"
end_phrase = "相关工具教程："

# Find the indices of the start and end phrases
start_index = text.find(start_phrase)
end_index = text.find(end_phrase)

# Extract the chunk of text between the phrases
if start_index != -1 and end_index != -1:
    chunk = text[start_index + len(start_phrase):end_index].strip()
else:
    print("Start or end phrase not found in the text.")
file = open('nodes.txt','w')
file.write(text)
