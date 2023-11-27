from selenium import webdriver

# 1. Khởi chạy trình duyệt (Chrome)
driver = webdriver.Chrome()

try:
    # 2. Mở URL https://www.godaddy.com/
    driver.get("https://www.godaddy.com/")

    # 3. Tối đa hóa cửa sổ trình duyệt
    driver.maximize_window()

    # Hoặc có thể đặt kích thước cửa sổ bằng cách sử dụng:
    # driver.set_window_size(width, height)

    # 4. Lấy nguồn trang và in nó
    page_source = driver.page_source
    print(f"Nguồn trang:\n{page_source}")

finally:
    # 5. Đóng trình duyệt
    driver.quit()
