from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import sys
import time



"""
TODO
    If a quoted tweet quotes or is replied to another tweet add that as an input
    When reading from a reply quoted tweets should be inputs instead of instructions
    Specify retweets when reading from timeline
    Timing can cause issues when scrolling
        Stale reference
        Click errors on quotes
"""

"""
SHOULD-DO
    Find a better way to stop from reading duplicate tweets
        Currently stores all read text (not quotes) in a set and checks set before writing a tweet to output, moves to next if it has
            If a quoted tweet is far on the page when it goes back it will have to read alot before it gets back to where it was
        Add a tag to specify if a tweet was a RT
            Currently appears as Original Tweet
    Scraper doesn't print emojis
        Unsure what to do about that
        I think they have a text "description" I could take but idk if that information would be worth anything
    Adjust the function to look for quotes to check in the original tweet instead of the reply when on the replies page
"""

"""
CURRENT STATE
    Scraper works to scrape a specified # of tweets from the users posts page or replies
    On the timeline:
        If a quoted tweet appears it navigates to that quoted tweet, scrapes the text and goes back
            Once it gets back its relocates the tweets on the page
            Starts reading at start of the list and ignores tweets it has read before
    In replies:
        Scraper searches for tweets posted by @{username}
        Needs to handle quotes differently and add inputs
    After each tweet it checks if the quota has been reached and stops once it has
"""

#scroll down to the bottom of the page
def scroll(distance):
    driver.execute_script(f"window.scrollBy(0, {distance});")

username = input("What user do you want to scrape from? ")
tweet_num_str = input("How many tweets do you want to scrape (daily max 600) ")
tweet_num = int(tweet_num_str)

# Path to your Chrome WebDriver executable
webdriver_path = "C:\\Users\\carso\\Documents\\Code\\MiniCenter\\X_Scraper\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# Restrict Chrome errors to only fatal errors
chrome_options = Options()
chrome_options.add_argument("--log-level=3")

# Create a WebDriver instance
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()


# Load Twitter login page
driver.get('https://twitter.com/login')

# Find username and password fields and enter credentials
# Credentials are currently hard coded
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="text"][autocomplete="username"]'))
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

# Credentials are entered, next login

login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Log in")]'))
)
login_button.click()

search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]'))
)
search_bar.send_keys(username)
search_bar.send_keys(Keys.ENTER)

# Click on the user in the search results
result_link = '//a[@href="/' + username + '"]'
search_result = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, result_link))
)
search_result.click()

#Take CLA tag to determine whether or not to go to replies page
if sys.argv[1] == '-r':
    replies_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Replies")]'))
    )
    replies_tab.click()

# Scrape specified # of tweets
tweets_scraped = 0
tweets_read = []

with open("selenium_tweets.txt","w", encoding="utf-8") as output:    
        relocate_bool = False

        #Keep scraping until quota is reached
        while tweets_scraped < tweet_num:
            #Determine tweet_elements differently depending on where we look
            #Look through the entire loaded page and get every element with the tag "tweet"
            if sys.argv[1] == '-t':
                tweet_elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//article[@data-testid="tweet"]'))
                )
            # Search for tweets with a reference to the username and do not have a specific class which identifies the original tweet
            elif sys.argv[1] == '-r':
                tweet_elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, f'//article[@data-testid="tweet" and not(contains(@class, "r-1ut4w64")) and .//a[contains(@href, "{username}")]]'))
                )
            # Check if CLA was taken
            else:
                    print("invalid argument passed")
                    exit(1)

            # Find the body of every tweet in the detected elements
            # For each tweet already detected, read it and increment the total number of scraped tweets
            for tweet_element in tweet_elements:
                pinned_tweet = False
                # Try to find a tweetText element in the current tweet
                try:
                    body = tweet_element.find_element(By.XPATH, './/div[@data-testid="tweetText" and contains(@style, "webkit-line-clamp: 10")]')
                # If it can't find it look for an image
                except NoSuchElementException:
                    try:
                        # If the tweet consists of only an image, iterate past it
                        body = tweet_element.find_element(By.XPATH, './/div[@data-testid="tweetPhoto"]')
                        continue
                    # If no image was found print error to console
                    except NoSuchElementException:
                        # If neither text nor an image are found, print an error
                        print("ERROR: No tweet body could be found")
                        continue  # Continue to the next iteration
                # Check if we have read this tweet already and move past it if we have, or write it to output
                if body.text not in tweets_read:
                    output.write("OUTPUT:" + body.text + " ")
                    tweets_read.append(body.text)
                else:
                    continue
                
                # Find the INSTRUCTION for replies
                # If we are in the replies and not on a pinned tweet page find the input
                if sys.argv[1] == '-r' and not tweet_element.find_elements(By.XPATH, './/descendant::*[contains(text(), "Pinned")]'):
                    # Follow the css layout to navigate to the input tweet ("1 tweet above" the current tweet in the css)
                    great_great_grandparent = tweet_element.find_element(By.XPATH, "../../..")
                    sibling_element = great_great_grandparent.find_element(By.XPATH, "preceding-sibling::div[1]")
                    #Try to find the text of the original tweet and write it to output
                    try:
                        replied_to_tweet = sibling_element.find_element(By.XPATH, './/article[@data-testid="tweet" and contains(@class, "r-1ut4w64")]')
                        replied_to_tweet_text = replied_to_tweet.find_element(By.XPATH, './/div[@data-testid="tweetText"]')
                        output.write("INSTUCTION:" + replied_to_tweet_text.text + "\n")
                    # Check for an image
                    except NoSuchElementException:
                        try:
                            # State the original was an iamge
                            body = replied_to_tweet.find_element(By.XPATH, './/div[@data-testid="tweetPhoto"]')
                            output.write("INSTRUCTION: IMAGE\n")
                        # If not text or image are found print error
                        except NoSuchElementException:
                            print("ERROR: No orignal tweet body found")
                    
                #Try to find a descendant of the current tweet that contains the word pinned to see if the current tweet is a pinned tweet
                try:
                    tweet_element.find_element(By.XPATH, './/descendant::*[contains(text(), "Pinned")]')
                    pinned_tweet = True
                except NoSuchElementException:
                    pinned_tweet = False
                #Increment # of tweets scraped and see if we are at the quota
                tweets_scraped += 1

                # Determine if the current tweet has a quote in the timeline or on a pineed tweet
                if sys.argv[1] == '-t' or pinned_tweet == True:
                    try:
                        #Use the specified classes of a quoted tweet to find the element and click on it to ensure we get the full body
                        quoted_tweet_element = tweet_element.find_element(By.XPATH, ".//div[contains(@class, 'r-adacv') and @role='link']")
                        quote_tweet_text = quoted_tweet_element.find_element(By.XPATH, './/div[@data-testid="tweetText"]')
                        #navigate to quoted tweet
                        quote_tweet_text.click()
                        #Find the body of the quoted tweet on new page
                        quote_body = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, './/div[@data-testid="tweetText"]'))
                        )
                        #Print the quote as the instruction
                        output.write("INSTRUCTION:" + quote_body.text + "\n")
                        #Go back to user page
                        driver.back()
                        relocate_bool = True
                    # If no quote is found then the tweet is not a reply
                    except NoSuchElementException:
                        relocate_bool = False
                        output.write("INSTRUCTION:Original Tweet\n")

                    # If we navigated away for a quote break to loop to relocate tweets
                    if relocate_bool:
                        break
                # If we are looking at replies define the instruction as an Original Tweet
                if tweets_scraped == tweet_num:
                    break
            #If we have scraped all the tweets in tweet elements since last loading, scroll down before loading more
            if sys.argv[1] == '-t' and not relocate_bool and tweets_scraped != tweet_num:
                scroll(2000)
                time.sleep(1)
            elif sys.argv[1] == '-r':
                scroll(2000)
                time.sleep(1)

            #If we read through all the tweets break the while loop
            if tweets_scraped == tweet_num:
                break

# Close the browser window when done
driver.quit()
