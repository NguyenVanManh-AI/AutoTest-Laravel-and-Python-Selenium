from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  
import time

# driver = webdriver.Edge()
driver = webdriver.Chrome() # sử dụng gg chrome thay vì edge 

def go_article():
    li_element = get_element(By.ID, 'list_6')
    li_element.click()
    li_element.click()

def go_article_create():
    add_btn = get_element(By.ID, 'btn_add_article')
    add_btn.click()

def get_element(by, selector):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, selector)))

def get_elements(by, selector):
    return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((by, selector)))

def delete_article(nth):
    go_article()
    btn_deletes = get_elements(By.CLASS_NAME, 'btn.btn-sm.btn-danger.ml-8')
    btn_delete = btn_deletes[nth]
    btn_delete.click()
    time.sleep(2) # quan trọng , đợi cho model được render ra 
    delete_button = get_element(By.CSS_SELECTOR, '#deleteOneModal .btn.btn-danger.w-150px')
    delete_button.click()
    time.sleep(2) 

def hidden_article(nth):
    go_article()
    btn_hiddens = get_elements(By.CLASS_NAME, 'btn.btn-sm.btn-success.ml-8.ng-star-inserted')
    btn_hidden = btn_hiddens[nth]
    btn_hidden.click()
    time.sleep(2) # quan trọng , đợi cho model được render ra 
    hidden_button = get_element(By.CSS_SELECTOR, '#changeShowModal .btn.btn-primary-1.w-150px')
    hidden_button.click()
    time.sleep(2) 

def accept_article(nth):
    go_article()
    btn_accepts = get_elements(By.CLASS_NAME, 'btn.btn-sm.btn-success.ng-star-inserted')
    btn_accept = btn_accepts[nth]
    btn_accept.click()
    time.sleep(2) # quan trọng , đợi cho model được render ra 
    accept_button = get_element(By.CSS_SELECTOR, '#changeAcceptModal .btn.btn-primary-1.w-150px')
    accept_button.click()
    time.sleep(2) 


def create_article(title, content, img, category):
    time.sleep(2)
    go_article()
    go_article_create()

    title_input = get_element(By.CSS_SELECTOR, '[ng-reflect-name="title"]')
    title_input.send_keys(title)

    div_element = get_element(By.CLASS_NAME, "ql-editor")
    div_element.send_keys(content)
    time.sleep(2)

    if(category):
        div_element = get_element(By.CLASS_NAME, 'ng-input')
        div_element.click()
        option_elements = get_elements(By.CLASS_NAME, 'ng-option')
        selected_option = option_elements[category]
        selected_option.click()

    if(img): 
        input_element = get_element(By.ID, 'thumbnail')
        input_element.send_keys(img)

    submit_button = get_element(By.CLASS_NAME, 'btn-primary-1')
    time.sleep(2)
    submit_button.click()
    time.sleep(2)

def edit_article(title, content, img, category):
    go_article()
    btn_edits = get_elements(By.CLASS_NAME, 'btn.btn-sm.btn-primary.ml-8')
    btn_edit = btn_edits[0]
    btn_edit.click()

    title_input = get_element(By.CSS_SELECTOR, '[ng-reflect-name="title"]')
    time.sleep(2)
    title_input.clear() 
    title_input.send_keys(title)

    div_element = get_element(By.CLASS_NAME, "ql-editor")
    time.sleep(2)
    div_element.clear() 
    div_element.send_keys(content)

    time.sleep(2)
    div_element = get_element(By.CLASS_NAME, 'ng-input')
    div_element.click()
    option_elements = get_elements(By.CLASS_NAME, 'ng-option')
    selected_option = option_elements[category]
    selected_option.click()

    if(img): 
        input_element = get_element(By.ID, 'thumbnail')
        input_element.send_keys(img)

    submit_button = get_element(By.CLASS_NAME, 'btn-primary-1')
    time.sleep(2)
    submit_button.click()

def login(email, password):
    driver.refresh()
    email_input = get_element(By.CSS_SELECTOR, '[ng-reflect-name="email"]')
    password_input = get_element(By.CSS_SELECTOR, '[ng-reflect-name="password"]')
    email_input.clear() 
    password_input.clear() 

    show = get_element(By.ID, 'toggleButton')
    show.click()
    
    if(email):
        email_input.send_keys(email)

    time.sleep(2)
    if(password):
        password_input.send_keys(password)

    btn_submits = get_elements(By.CLASS_NAME, 'btn.btn-secondary.d-flex.justify-content-center')
    btn_submit = btn_submits[0]
    btn_submit.click()
    btn_submit.click()
    time.sleep(2)

def page():
    go_article()
    time.sleep(2)
    # cuộn đến cuối trang 
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.END)
    time.sleep(2)
    end_input = get_element(By.CSS_SELECTOR, '[aria-label="End page"]')
    end_input.click()
    
    time.sleep(2)
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.END)
    time.sleep(2)
    first_input = get_element(By.CSS_SELECTOR, '[aria-label="First page"]')
    first_input.click()
    time.sleep(2)

try:
    # LOGIN 
    driver.maximize_window()
    driver.get("http://localhost:4200")
    login_button = get_element(By.CSS_SELECTOR, ".btn-outline-gray.btn-login.ng-star-inserted")
    ActionChains(driver).move_to_element(login_button).click().perform()

    time.sleep(2)
    login(None, "123456")
    login("benhviengiadinh@yopmail.com", None)
    login("benhviengiadinh7@yopmail.com", "1234567")
    login("benhviengiadinh@yopmail.com", "123456")
    time.sleep(2)

    for i in range(5):
        #PAGE
        page()
        # CREATE 
        create_article('', "Nội dung của bài viết !", r"c:\Users\ADMIN\Downloads\Infinity\abinhyen2.jpg", 2)
        create_article("Tiêu đề của bài viết !", "", r"c:\Users\ADMIN\Downloads\Infinity\abinhyen2.jpg", 2)
        create_article('Tiêu đề của bài viết !', "Nội dung của bài viết !", None, 2)
        create_article("Nội dung của bài viết !", "Nội dung của bài viết !", r"c:\Users\ADMIN\Downloads\Infinity\abinhyen2.jpg", None)
        create_article("Nội dung của bài viết !", "Nội dung của bài viết !", r"c:\Users\ADMIN\Downloads\Infinity\abinhyen2.jpg", 2)
        # EDIT
        edit_article("Cập nhật Tiêu đề của bài viết !", "", r"c:\Users\ADMIN\Downloads\Infinity\an.jpg", 0)
        edit_article("Cập nhật Tiêu đề của bài viết !", "Cập nhật Nội dung của bài viết !", r"c:\Users\ADMIN\Downloads\Infinity\an.jpg", 0)
        # HIDDEN 
        hidden_article(0)
        # ACCEPT
        accept_article(0)
        # DELETE 
        delete_article(0)

    time.sleep(20)

except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

finally:
    driver.quit()
