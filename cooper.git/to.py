from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)# 启动 chromium 浏览器
    page = browser.new_page()# 打开一个标签页
    page.goto("https://cooper.didichuxing.com")# 打开地址
    print(page.title())# 打印当前页面title

    page.pause()

    browser.close()# 关闭浏览器对象
