from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 1. Khởi chạy trình duyệt (Chrome)
driver = webdriver.Chrome()

try:
    # 2. Mở URL https://www.godaddy.com/
    driver.get("https://www.godaddy.com/")

    # 3. Tối đa hóa cửa sổ trình duyệt
    driver.maximize_window()

    # Hoặc có thể đặt kích thước cửa sổ bằng cách sử dụng:
    # driver.set_window_size(width, height)

    # 4. Lấy Tiêu đề của trang và xác thực nó với giá trị mong đợi
    expected_title = "Domain Names, Websites, Hosting & Online Marketing Tools - GoDaddy"
    actual_title = driver.title
    assert actual_title == expected_title, f"Tiêu đề không khớp. Đang chờ '{expected_title}', nhưng nhận được '{actual_title}'"

    # 5. Nhận URL của trang hiện tại và xác thực nó với giá trị mong đợi
    expected_url = "https://www.godaddy.com/"
    actual_url = driver.current_url
    assert actual_url == expected_url, f"URL không khớp. Đang chờ '{expected_url}', nhưng nhận được '{actual_url}'"

    # 6. Lấy nguồn trang của trang web
    page_source = driver.page_source

    # 7. Và xác thực rằng tiêu đề trang có trong nguồn trang
    assert expected_title in page_source, f"Tiêu đề trang không xuất hiện trong nguồn trang"

finally:
    # 8. Đóng trình duyệt
    driver.quit()
