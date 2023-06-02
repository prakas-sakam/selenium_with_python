import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='class')
def strat_and_stop(request):

    s = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=s)
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver

    yield
    driver.close()
