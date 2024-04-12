from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome",args=['--start-maximized '])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://cooper.didichuxing.com/")
    page.goto("https://me.xiaojukeji.com/project/stargate-auth/html/login.html?redirect_uri=http%3A%2F%2Fmis.diditaxi.com.cn%2Fauth%2F%3Fjumpto%3D%252F%26app_id%3D2176%26callback_index%3D1")
    page.get_by_placeholder("账户").click()
    page.get_by_placeholder("账户").fill("ip019_test_v")
    page.get_by_placeholder("密码").click()
    page.get_by_placeholder("密码").fill("NVFykp+9")
    page.locator("#submit").click()
    print(page.title())

    #dropdown = page.locator('.ant-btn-primary')
    #dropdown.hover()

    #dropdown.locator('.create-collab >> text=协作表格').click()
    #dropdown.get_by_role("create-folder").filter(has_text="新建文件夹").click()

    #page.pause()  # 断点
    # ---------------------
    context.close()
    browser.close()



