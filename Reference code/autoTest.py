from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  
import time

# driver = webdriver.Edge()
driver = webdriver.Chrome() # sử dụng gg chrome thay vì edge 

driver.get("http://localhost:4200/")

def delete_article():
    # DELETE 
    btn_deletes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'btn.btn-sm.btn-danger.ml-8'))
    )
    print(btn_deletes)
    btn_delete = btn_deletes[0]
    btn_delete.click()
    
    time.sleep(1) # quan trọng , đợi cho model được render ra 
    
    delete_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#deleteOneModal .btn.btn-danger.w-150px'))
    )
    delete_button.click()
    time.sleep(1) 

def create_article():
    time.sleep(3)
    driver.get("http://localhost:4200/admin/article/create")

    # title 
    title_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[ng-reflect-name="title"]'))
    )
    title_input.send_keys("Tiêu đề của bài viết !")

    # content 
    div_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ql-editor"))
    )
    div_element.send_keys("Nội dung của bài viết !")

    time.sleep(3)
    # danh mục 
    div_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ng-input'))
    )
    div_element.click()
    option_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'ng-option'))
    )
    # chọn danh mục 
    selected_option = option_elements[2]
    selected_option.click()

    # Thực hiện click vào ảnh
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'thumbnail'))
    )
    input_element.send_keys(r"c:\Users\ADMIN\Downloads\Infinity\abinhyen2.jpg")

    # submit 
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary-1'))
    )
    time.sleep(5)

    submit_button.click()

    time.sleep(5)

def edit_article():
    btn_edits = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'btn.btn-sm.btn-primary.ml-8'))
    )
    print(btn_edits)
    btn_edit = btn_edits[0]
    btn_edit.click()

    # title 
    title_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[ng-reflect-name="title"]'))
    )
    time.sleep(1)
    title_input.clear() 
    title_input.send_keys("Cập nhật Tiêu đề của bài viết !")

    # content 
    div_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ql-editor"))
    )
    time.sleep(1)
    div_element.clear() 
    div_element.send_keys("Cập nhật Nội dung của bài viết !")

    time.sleep(3)
    # danh mục 
    div_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ng-input'))
    )
    div_element.click()
    option_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'ng-option'))
    )
    # chọn danh mục 
    selected_option = option_elements[1]
    selected_option.click()

    # Thực hiện click vào ảnh
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'thumbnail'))
    )
    input_element.send_keys(r"c:\Users\ADMIN\Downloads\Infinity\an.jpg")

    # submit 
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary-1'))
    )
    time.sleep(5)

    submit_button.click()

try:

    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-outline-gray.btn-login.ng-star-inserted"))
    )
    ActionChains(driver).move_to_element(login_button).click().perform()

    # time.sleep(3)

    # Đặt kích thước cửa sổ trình duyệt là kích thước tối đa
    driver.maximize_window()

    # time.sleep(3)

    # # tùy chỉnh 
    # driver.set_window_size(1200, 800) 

    # time.sleep(3)

    # # test đăng kí 
    # tab_register = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '[ng-reflect-router-link="/auth/sign-up"]'))
    # )
    # ActionChains(driver).move_to_element(tab_register).click().perform()

    # name_input = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '[ng-reflect-name="name"]'))
    # )
    # email_input = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '[ng-reflect-name="email"]'))
    # )
    # password_input = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '[ng-reflect-name="password"]'))
    # )
    # confirm_input = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '[ng-reflect-name="confirm"]'))
    # )

    # name_input.send_keys("Nguyễn Văn Mạnh")
    # email_input.send_keys("nguyenvanmanh2001it1@yopmail.com")
    # password_input.send_keys("123456")
    # confirm_input.send_keys("123456")
    # btn_register = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-secondary.d-flex.justify-content-center"))
    # )
    # ActionChains(driver).move_to_element(btn_register).click().perform()


    # # Lưu ID của tab hiện tại
    # current_tab = driver.current_window_handle
    # # Mở tab mới
    # driver.execute_script("window.open('', '_blank');")
    # # Switch đến tab mới mở
    # new_tab = [handle for handle in driver.window_handles if handle != current_tab][0]
    # driver.switch_to.window(new_tab)
    # # Mở trang https://yopmail.com/wm trong tab mới
    # driver.get("https://yopmail.com/wm")
    # time.sleep(3)

    # # Quay lại tab trước đó
    # driver.switch_to.window(current_tab)

    # test đăng nhập 
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[ng-reflect-name="email"]'))
    )

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[ng-reflect-name="password"]'))
    )

    # email_input.send_keys("benhviengiadinh1111@yopmail.com")
    # password_input.send_keys("123456")
    # password_input.send_keys(Keys.RETURN)
    # time.sleep(3)

    # email_input.clear() 
    # password_input.clear() 
    # email_input.send_keys("benhviengiadinh@yopmail.com")
    # password_input.send_keys("1111111")
    # password_input.send_keys(Keys.RETURN)
    # time.sleep(3)

    email_input.clear() 
    password_input.clear() 
    email_input.send_keys("benhviengiadinh@yopmail.com")
    password_input.send_keys("123456")
    password_input.send_keys(Keys.RETURN)

    # create article 
    time.sleep(3)
    driver.get("http://localhost:4200/admin/article")

    # CREATE 
    create_article()

    # EDIT
    edit_article()

    # DELETE 
    delete_article()

    time.sleep(20)

except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

finally:
    driver.quit()



# https://www.selenium.dev/documentation/webdriver/elements/file_upload/