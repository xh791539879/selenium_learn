import os

import pytest

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate D:\\workspace-python\\HNSGW\\Temp -o D:\\workspace-python\\HNSGW\\AllureReport --clean')
