from selenium import webdriver
import threading

driver = None
lock = threading.Lock()


def get_driver():
    global driver
    if driver is None:
        lock.acquire()
        if driver is None:
            driver = webdriver.Chrome()
        lock.release()
    return driver
