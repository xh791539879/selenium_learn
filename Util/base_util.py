from selenium import webdriver


class BaseUtil:
    def setup_class(self) -> None:
        # 创建 Chrome 浏览器选项对象
        options = webdriver.ChromeOptions()

        # 启用“开发者模式”，避免浏览器被自动关闭
        options.add_experimental_option('detach', True)

        # 添加启动参数：最大化窗口
        options.add_argument('--start-maximized')

        # 创建 Chrome 浏览器实例
        self.driver = webdriver.Chrome(options=options)

    def teardown_class(self) -> None:
        # 关闭浏览器
        self.driver.quit()
