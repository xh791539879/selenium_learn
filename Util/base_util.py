from selenium import webdriver


def get_webdriver():
    # 设定 Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')  # 禁用 "--no-sandbox" 无沙箱模式
    chrome_options.add_argument(
        '--disable-dev-shm-usage')  # 禁用 "--disable-dev-shm-usage" 属性。这个属性是为了解决 Docker 容器内存不足问题的，但是在一些情况下会出现问题，所以建议关闭。

    # 实例化 webdriver 对象
    driver = webdriver.Chrome(options=chrome_options)

    # 最大化窗口
    driver.maximize_window()

    return driver
