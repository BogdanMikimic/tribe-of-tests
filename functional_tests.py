from selenium import webdriver

browser = webdriver.Firefox()
# David hears about this new cool game. He goes to check out it's homepage
browser.get('http://localhost:8000')

# He notices that the game has a "Congratulation" word in the title
assert 'Congratulations' in browser.title

# He goes and he checks the first page of the game where he understood that the Tests tribe have their village
# and notices that the page is called Tests Village

# He clicks on the main house and reads about the

browser.quit()