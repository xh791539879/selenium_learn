from selenium import webdriver


class ChromeDriver:
    def __init__(self, headless=False):
        """
        初始化谷歌浏览器驱动
        :param headless: 是否开启无界面模式，默认为 False
        """
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)

    def teardown(self):
        """
        关闭浏览器并退出驱动程序
        """
        self.driver.quit()
