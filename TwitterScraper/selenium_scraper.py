from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your Chrome WebDriver executable
webdriver_path = "C:\\Users\\carso\\OneDrive\\Documents\\Code\\MiniCenter\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# Create a WebDriver instance
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

# Load Twitter login page
driver.get('https://twitter.com/login')

# Find username and password fields and enter credentials
# Credentials are currently hard coded
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="text"][autocomplete="username"]'))
    #[type="text"]
)
username_field.send_keys('dev_eloper1110')

next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Next")]'))
)
next_button.click()

password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"][type="password"]'))
)
password_field.send_keys('MiniCenterRocks!')

#Credentials are entered, next we login

login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Log in")]'))
)
login_button.click()

# Once we are logged in search for a user
# Can me modified to search for different things or start reading from the timeline
#username = input("What user would you like to search?: ")

#TEMPORARY
username = 'elonmusk'
#TEMPORARY

search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]'))
)
search_bar.send_keys(username)
search_bar.send_keys(Keys.ENTER)

#Click on the user in the search results
search_result = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[@href="/elonmusk"]'))
)
search_result.click()

input("Press Enter to close the browser window...")
# Now, you can navigate to the user's profile page
#driver.get('https://twitter.com/' + username)

# Perform further interactions as needed, such as scraping tweets
# For example, to get the text of tweets, you can find tweet elements and extract text
tweet_elements = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
with open('selenium_out.txt', 'w') as output :
    for tweet_element in tweet_elements:
        tweet_text = tweet_element.find_element_by_xpath('.//div[@lang="en"]').text
        output.write(tweet_text)

# Close the browser window when done
driver.quit()
