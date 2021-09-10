from typing import final
from selenium import webdriver
import time
import math
import random
from selenium.webdriver.support.ui import Select
###################################2.1 Основные методы Selenium###############################

# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/math.html')

#     def calc(x):
#         return str(math.log(abs(12*math.sin(int(x)))))

#     x_element = browser.find_element_by_id('input_value')
#     x = x_element.text
#     y = calc(x)

#     input = browser.find_element_by_id('answer')
#     input.send_keys(y)

#     cheked = browser.find_element_by_id('robotCheckbox')
#     cheked.click()
#     radiobatton = browser.find_element_by_id('robotsRule').click()

#     button = browser.find_element_by_css_selector('button.btn.btn-default').click()


# finally:
#     time.sleep(5)
#     browser.quit()

#####################################################################################
# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/math.html')

#     def calc(x):
#         return str(math.log(abs(12*math.sin(int(x)))))

#     x_element = browser.find_element_by_id('input_value')
#     x = x_element.text
#     y = calc(x)

#     input = browser.find_element_by_id('answer')
#     input.send_keys(y)

#     people_radio = browser.find_element_by_id("peopleRule")
#     people_checked = people_radio.get_attribute("checked")
#     print("value of people radio: ", people_checked)
#     assert people_checked is not None, "People radio is not selected by default"

# finally:
#     time.sleep(5)
#     browser.quit()

############Задание: поиск сокровища с помощью get_attribute##############################

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')

    def func(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    picture = browser.find_element_by_id('treasure')
    value = picture.get_attribute('valuex')
    x = func(value)

    input = browser.find_element_by_id('answer')
    input.send_keys(x)

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    browser.find_element_by_css_selector('button.btn.btn-default').click()


finally:
    time.sleep(6)
    browser.quit()


#############2.2 Работа с файлами, списками и js-скриптами###############################

# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/selects1.html')

#     #или
#     browser.find_element_by_tag_name("select").click()
#     browser.find_element_by_css_selector("option:nth-child(2)").click()
#     #или
#     browser.find_element_by_css_selector("[value='1']").click()
#     #или
#     from selenium.webdriver.support.ui import Select
#     select = Select(browser.find_element_by_tag_name("select"))
#     select.select_by_value("1") # ищем элемент с текстом "Python"
#     #или 
#     #ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.
#     select.select_by_visible_text("text")
#     #ищет элемент по его индексу или порядковому номеру. Индексация начинается с нуля
#     select.select_by_index(1)

# finally:
#     time.sleep(6)
#     browser.quit()

#################Задание: работа с выпадающим списком####################################

# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/selects2.html')

#     num1 = browser.find_element_by_id('num1').text
#     num2 = browser.find_element_by_id('num2').text
#     summ = str(int(num1) + int(num2))
# 1    
#     from selenium.webdriver.support.ui import Select
#     select = Select(browser.find_element_by_tag_name('select'))
#     select.select_by_visible_text(summ)
# 2
#     browser.find_element_by_css_selector(f"[value='{summ}']").click()
# 3
#     select = Select(browser.find_element_by_tag_name('select'))
#     select.select_by_visible_text(summ)
#     browser.find_element_by_tag_name('button').click()

# finally:
#     time.sleep(4)
#     browser.quit()









##########################Метод execute_script############################


# browser = webdriver.Chrome()
# browser.execute_script("alert('Слава тебя бона в рот ебал');")
# browser.execute_script("document.title='Script executing';")
# browser.execute_script("document.title='Script executing';alert('Robots at work');")

# Вдруг будет кому-нибудь интересно. Выполнение JavaScript на странице - это неописанный в документации Selenium способ поиска элемента.
# Вместо встроенных find_element_by... можно использовать вот такую конструкцию:
# element = browser.execute_script('document.getElementsByName("name")')

# Так же есть конструкции:
# getElementById
# getElementsByTagName
# getElementsByClassName
# querySelector - для CSS
# querySelectorAll - для CSS (находит все совпадения)

# evaluate - для XPATH.

# Погуглите.

#############################Пример задачи для execute_script##########################


# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
# #Также можно проскроллить всю страницу целиком на строго заданное количество пикселей. Эта команда проскроллит страницу на 100 пикселей вниз:
# browser.execute_script("window.scrollBy(0, 100);")

# в консоле разработчика
# // javascript
# button = document.getElementsByTagName("button")[0];
# button.scrollIntoView(true);

####################################Задание на execute_script##############################

# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/execute_script.html')

#     x = browser.find_element_by_id('input_value').text
#     y = math.log(abs(12*math.sin(int(x))))

#     browser.find_element_by_id('answer').send_keys(str(y))

#     browser.find_element_by_id('robotCheckbox').click()
    
#     button = browser.find_element_by_tag_name('button')
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)

#     browser.find_element_by_id('robotsRule').click()
#     browser.find_element_by_css_selector('button.btn.btn-primary').click()

# finally:
#     time.sleep(5)
#     browser.quit()

##################################Загрузка файлов###############################

# import os 

# current_dir = os.path.abspath(r'C:\Python\Python_work_place')    # получаем путь к директории текущего исполняемого файла 
# print(current_dir)
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
# print(os.path.abspath(r'C:\Python\Python_work_place\file.txt'))


# element.send_keys(file_path)

##############################Задание: загрузка файла###############################
# import os

# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/file_input.html')

# browser.find_element_by_name('firstname').send_keys('Ivan')
# browser.find_element_by_name('lastname').send_keys('Zaycev')
# browser.find_element_by_name('email').send_keys('rtyrtyrty@mail.ru')


# current_dir = os.path.abspath(r'C:\Python\Python_work_place') 
# file_path = os.path.join(current_dir, 'file.txt')
# print(file_path)
# browser.find_element_by_name('file').send_keys(file_path)


# browser.find_element_by_css_selector('button.btn').click()










##########################Alerts и как с ними жить################################

# alert = browser.switch_to.alert
# alert.accept()

# Чтобы получить текст из alert, используйте свойство text объекта alert:
# alert = browser.switch_to.alert
# alert_text = alert.text

# confirm = browser.switch_to.alert
# confirm.accept()

# confirm.dismiss()

# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()



#################################Задание: принимаем alert############################

# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/alert_accept.html')

# browser.find_element_by_xpath('//button[@type="submit"]').click()

# confirm = browser.switch_to.alert
# confirm.accept()

# x = browser.find_element_by_id('input_value').text
# score = math.log(abs(12*math.sin(int(x))))


# browser.find_element_by_id('answer').send_keys(str(score))

# browser.find_element_by_xpath("//button[@type='submit']").click()

########################Переход на новую вкладку браузера#############################

# browser.switch_to.window(window_name)

# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles,
# который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, 
# выбираем вторую вкладку:
# new_window = browser.window_handles[1]

# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
# first_window = browser.window_handles[0]

# Текущую вкладку можно узнать так:
# current_window = browser.current_window_handle

#############################Задание: переход на новую вкладку##############################

# from selenium.webdriver.support.ui import Select

# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/redirect_accept.html')

# browser.find_element_by_xpath('//button[@type="submit" and contains(text(), "I want to go on a magical journey!")]').click()

# new_window  = browser.window_handles[1]
# browser.switch_to.window(new_window)

# x = browser.find_element_by_id('input_value').text
# y = math.log(abs(12*math.sin(int(x))))

# browser.find_element_by_id('answer').send_keys(str(y))

# browser.find_element_by_css_selector('button.btn').click()







##############################Как работают методы get и find_element#################################
# from selenium import webdriver

# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)

# browser.get("http://suninjuly.github.io/wait1.html")

# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")

# assert "successful" in message.text

###############################Explicit Waits (WebDriverWait и expected_conditions)#####################

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver

# browser = webdriver.Chrome()

# browser.get("http://suninjuly.github.io/wait2.html")

# #говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element_by_id("verify_message")

# assert "successful" in message.text

##############################Задание: ждем нужный текст на странице###################################

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/explicit_wait2.html')

# price = WebDriverWait(browser, 12).until(
#     EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
# )
# browser.find_element_by_id('book').click()

# x = browser.find_element_by_id('input_value').text
# score = math.log(abs(12*math.sin(int(x))))

# browser.find_element_by_id('answer').send_keys(str(score))
# browser.find_element_by_id('solve').click()










########################################Итоги модуля########################################

