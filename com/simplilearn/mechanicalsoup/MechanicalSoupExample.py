import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
browser.open('https://steemit.com')
articles = list(browser.get_current_page().find('ul', class_='PostsList__summaries'))[:10]
for child in articles:
    user = child.find('span', class_='author').text
    title = child.h2.text
    link = 'https://steemit.com' + child.h2.a.get('href')
    summary = child.find('div', class_='PostSummary__body').text
    # Printing the collected data
    print('User : ' + user)
    print('Post title : ' + title)
    print('Post summary : ' + summary)
    print('Post link : ' + link)
    print()