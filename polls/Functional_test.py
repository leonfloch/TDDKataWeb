__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("/Users/leonardovalbuena/Downloads/chromedriver")

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('BuscoAyuda', self.browser.title)



