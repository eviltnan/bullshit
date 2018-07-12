import schedule
import time


def job():
    print("I'm working...")


schedule.every().day.at("11:23").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
