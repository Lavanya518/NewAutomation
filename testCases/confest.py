# import pytest
# from selenium import webdriver

# @pytest.fixture()
# def setup():
#     driver=webdriver.Chrome()
#     return driver

# @pytest.fixture(scope="class")
# def setup(request):
#     driver = webdriver.Chrome()
#     request.cls.driver = driver
#     yield
#     driver.close()

import pytest
from selenium import webdriver
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



@pytest.fixture(scope="function")
def driver(browser):
    if browser=='chrome':
       driver = webdriver.Chrome()
       print("Lanching chrome browser....")

    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("launching Firefox browser.....")
    else:
        driver=webdriver.Ie()
    yield driver
    driver.close()

    def pytest_addoption(parser):
        parser.addoption("--browser")

    @pytest.fixture()
    def browser(request):
        return request.config.getoption("--browser")

    def pytest_configure(config):
        '''
        It is hook for adding environment info to the HTML report
        :param config: Configure the html report
        :return:
        '''
        config._metadata['Project Name'] = 'NOP COMMERCE'
        config._metadata['Module Name'] = 'Customer'
        config._metadata['Tester'] = 'Lavanya'

        def pytest_metadata(metadata):
            '''
            Hook for delete/modify environment info to the HTML report
            :param metadata:
            :return:
            '''
            metadata.pop("JAVA_HOME", None)
            metadata.pop("Plugins", None)

# from selenium import webdriver
# import pytest
#
#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver
