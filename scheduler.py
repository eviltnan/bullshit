import schedule
import time

from tweet import tweet

schedule.every().day.at("08:00").do(tweet)

if __name__ == '__main__':
    print("Started scheduler")
    while True:
        print("Entering the scheduling loop")
        schedule.run_pending()
        time.sleep(1)
