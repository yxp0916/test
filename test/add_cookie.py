from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.add_cookie({'name':'BAIDUID','value':'490A56609EAEB8F8F49B3DA5A01B3CFC:SL=0:NR=10:FG=1'})
driver.add_cookie({'name':'BDUSS','value':'pFc09SWXhyZGgxdWl0bk1-Q3FvcG5UenQ0YlU1UDhHeDl2dDdIalJqRVM0MkphQVFBQUFBJCQAAAAAAAAAAAEAAACCRU44eXhwXzE5ODQwOTE2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABJWO1oSVjtaZn'})

driver.refresh()
# print(driver.find_element_by_class_name("user-name").text)
# driver.quit()