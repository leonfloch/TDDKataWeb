__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains, keys
import time

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("/Users/leonardovalbuena/Downloads/chromedriver")
        self.browser.set_window_size(1024, 768)
        self.browser.implicitly_wait(5000)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://127.0.0.1:8000/#')
        self.assertIn('BuscoAyuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://127.0.0.1:8000/#')

        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Leonardo')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Valbuena')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='TiposDeServicio object']").click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('/Users/leonardovalbuena/Downloads/developer.jpeg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('leo1234')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Leonardo Valbuena"]')

        self.assertIn('Leonardo Valbuena', span.text)




    def test_verDetalle(self):
        self.browser.get('http://127.0.0.1:8000/#')
        span = self.browser.find_element(By.XPATH, '//span[text()="Leonardo Valbuena"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Leonardo Valbuena"]')

        self.assertIn('Leonardo Valbuena', h2.text)


    def test_login(self):
        self.browser.get('http://127.0.0.1:8000/#')

        link = self.browser.find_element_by_id('id_login')
        link.click()

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('leo1234')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_login')
        botonGrabar.click()

        linkLogout = self.browser.find_element_by_id('id_logout')
        self.assertIn('Logout', linkLogout.text)


    def test_add_coment(self):
        self.browser.get('http://127.0.0.1:8000/#')
        span = self.browser.find_element(By.XPATH, '//span[text()="Leonardo Valbuena"]')
        span.click()

        nombre = self.browser.find_element_by_id('correo')
        nombre.send_keys('demo@demo.com')

        nombre = self.browser.find_element_by_id('comentario')
        nombre.send_keys('texto coment')

        botonComentar = self.browser.find_element_by_id('id_coment')
        botonComentar.click()
        self.browser.implicitly_wait(3)








