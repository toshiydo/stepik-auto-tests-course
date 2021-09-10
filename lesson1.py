# import time

# # webdriver это и есть набор команд для управления браузером
# from selenium import webdriver

# # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# driver = webdriver.Chrome()

# # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
# time.sleep(1)

# # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# driver.get("https://stepik.org/lesson/25969/step/12")
# time.sleep(5)

# submit_button = driver.find_element_by_css_selector('.navbar__auth')
# submit_button.click()

# login = driver.find_element_by_id('id_login_email')
# login.send_keys('toshiydo@gmail.com')

# password = driver.find_element_by_name('password')
# password.send_keys('qw11wq11')

# button = driver.find_element_by_css_selector(".sign-form__btn")
# button.click()

# time.sleep(5)

# # Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# # Ищем поле для ввода текста
# textarea = driver.find_element_by_css_selector(".textarea")

# # Напишем текст ответа в найденное поле
# textarea.send_keys("get()")


# # Найдем кнопку, которая отправляет введенное решение
# submit_button = driver.find_element_by_css_selector('.submit-submission')

# # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
# submit_button.click()
# time.sleep(7)

# # После выполнения всех действий мы должны не забыть закрыть окно браузера
# driver.quit()











# from selenium import webdriver
# import time 
# import math

#1.5 Задание: поиск элементов с помощью Selenium###########################################

# link = "http://suninjuly.github.io/simple_form_find_task.html"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)

#     input1 = browser.find_element_by_tag_name('input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name('last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name('city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id('country')
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#     browser.
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(6)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# # не забываем оставить пустую строку в конце файла


#1.6 Задание: поиск элемента по тексту в ссылке############################################

# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/find_link_text')
    
#     find = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
#     find.click()

#     fname = browser.find_element_by_tag_name('input')
#     fname.send_keys('Ivan')

#     lname = browser.find_element_by_name('last_name')
#     lname.send_keys('Petrov')

#     city = browser.find_element_by_class_name('city')
#     city.send_keys('Smolensk')

#     country = browser.find_element_by_id('country')
#     country.send_keys('Russia')

#     button = browser.find_element_by_css_selector('button.btn')
#     button.click()
#     browser.find
# finally:
#     time.sleep(4)
#     browser.quit()



#Задание: использование метода find_elements_by############################################


# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements_by_tag_name('input')
#     for element in elements:
#         element.send_keys("Слава пидорас")

#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# # не забываем оставить пустую строку в конце файла


##############################Задание: поиск элемента по XPath###############################

# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/find_xpath_form')

#     fn = browser.find_element_by_tag_name('input')
#     fn.send_keys('Ivan')

#     ln = browser.find_element_by_name('last_name')
#     ln.send_keys('Zaycev')

#     city = browser.find_element_by_class_name('city')
#     city.send_keys('Moscow')

#     country = browser.find_element_by_id('country')
#     country.send_keys('Russia')

#     browser.find_element_by_xpath("//button[@type='submit' and starts-with(text(), 'Submit')]").click() 
#     #//button[text()='Submit']  #//button[@type='submit'] #//button[contains(text(), 'Submit')]
#     #//button[@type='submit' and contains(text(), 'Submit')]


# finally:
#     time.sleep(6)
#     browser.quit()

##################Уникальность селекторов: часть 2########################################

# try: 
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     # Ваш код, который заполняет обязательные поля
#     fn = browser.find_element_by_tag_name('input')
#     fn.send_keys('Ivan')
    
#     ln = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
#     ln.send_keys('Zaycev')

#     mail = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
#     mail.send_keys('rtyrtyr@mail.ru')
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)

#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text

#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


#####################Задание: уникальность селекторов#############################
# from selenium import webdriver
# import time 

# try: 
#     link = "http://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     # Ваш код, который заполняет обязательные поля
#     fn = browser.find_element_by_tag_name('input')
#     fn.send_keys('Ivan')
    
#     ln = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
#     ln.send_keys('Zaycev')

#     mail = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
#     mail.send_keys('rtyrtyr@mail.ru')
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)

#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text

#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()