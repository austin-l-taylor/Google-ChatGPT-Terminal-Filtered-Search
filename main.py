import webbrowser
import sys

# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' # May need to change read and write permisisons for chrome.exe location
url = 'https://www.google.com/search?q='
chat_gpt = 'https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx'

website_filter = [
    'reddit.com', 
    'stackoverflow.com', 
    'stackexchange.com', 
    'medium.com'
]

#-----EXAMPLE OUTPUT-----#
# why don't my parents like me? (site:reddit.com OR stackoverflow.com OR stackexchange.com OR medium.com)
def create_filter():
    filter = '('
    for index, website in enumerate(website_filter):
        filter += 'site:' + website 
        if index == len(website_filter) - 1:
            filter += ')'
        else:
            filter += ' OR '
    return filter

# Takes input from the Terminal
def create_query():
    query = sys.argv[1:]
    return ' '.join(query)

# Adds URL + Terminal Input + Web Filter Also chatGPT option 
def create_url():
    if len(sys.argv[1:]) == 0:
        print('Error: Please enter a valid search query')
    elif create_query() == 'chat':
        complete_url = chat_gpt + create_query()
        webbrowser.get(chrome_path).open(chat_gpt)
    else:
        complete_url =  url + create_query() + create_filter()
        webbrowser.get(chrome_path).open(complete_url)

create_url()