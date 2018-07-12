import schedule
import time

from tweet import tweet

schedule.every().day.at("08:00").do(tweet)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
