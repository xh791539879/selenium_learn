import os

import pytest

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate D:\\HNSGW\\Temp -o D:\\HNSGW\\AllureReport --clean')
