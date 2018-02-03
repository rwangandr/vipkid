# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
ORDER_TIMES = 1

time_dic_array = [
                {"date":1,"time":"20:00"},
                  {"date":2,"time":"20:00"},
                   {"date":3,"time":"20:00"},
                  {"date":4,"time":"20:00"},
                  {"date":5,"time":"20:00"},
               #   {"date":6,"time":"20:00"},
               #   {"date":7,"time":"20:00"},
                  {"date": 1,"time": "20:30"},
                  {"date": 2, "time": "20:30"},
                  {"date": 3, "time": "20:30"},
                  {"date": 4, "time": "20:30"},
                  {"date": 5, "time": "20:30"},
                #  {"date": 6, "time": "20:30"},
               #   {"date": 7, "time": "20:30"},
                  {"date": 1, "time": "19:30"},
                  {"date": 2, "time": "19:30"},
                  {"date": 3, "time": "19:30"},
                  {"date": 4, "time": "19:30"},
                  {"date": 5, "time": "19:30"},
                #  {"date": 6, "time": "19:30"},
                #  {"date": 7, "time": "19:30"},
                  {"date": 1, "time": "19:00"},
                  {"date": 2, "time": "19:00"},
                   {"date": 3, "time": "19:00"},
                  {"date": 4, "time": "19:00"},
                   {"date": 5,"time":  "19:00"},
               #   {"date": 6, "time": "19:00"}
                #  {"date": 7, "time": "19:00"}
               #    {"date": 1, "time": "21:00"},
               #   {"date": 2, "time": "21:00"},
               #    {"date": 3, "time": "21:00"},
               #   {"date": 4, "time": "21:00"},
               #    {"date": 5,"time":  "21:00"},
               #   {"date": 6, "time": "21:00"}
                #  {"date": 7, "time": "21:00"}
                #   {"date": 1, "time": "21:30"},
                #  {"date": 2, "time": "21:30"},
                #   {"date": 3, "time": "21:30"},
                #  {"date": 4, "time": "21:30"},
                #   {"date": 5,"time":  "21:30"},
               #  {"date": 6, "time": "21:30"}
                #  {"date": 7, "time": "21:30"}
                ]
ordered_arry = []
#teacher_array = ["Junel H","Justin JG","Melissa VUP","Jared VB"]
#teacher_array = ["Junel H","Justin JG","Jared VB"]
#teacher_array = ["Junel H"]
#teacher_array = ["Junel H","Justin JG","Melissa VUP","Jared VB","Carrie HQP"]
teacher_array = ["Melissa VUP"]
#teacher_array = ["Lindsey PZ"]
#teacher = "Carrie HQP"
#teacher = "Junel H" #teacher name
browser = webdriver.Safari()
#browser = webdriver.Chrome()
#browser.maximize_window()

#chromedriver = "/Applications/Google Chrome.app/Contents/MacOS/chromedriver"
#browser = webdriver.Chrome(chromedriver)
#browser = webdriver.Chrome()
browser.get('https://www.vipkid.com.cn/login')
browser.maximize_window()
#browser.implicitly_wait(6)
#
#browser.set_window_size(500,500,'current')
#time.sleep(2)
browser.find_element_by_name("username").send_keys('15522850688')
browser.find_element_by_name("password").send_keys('bang1125')
browser.find_element_by_id("js-submit-btn").click()
time.sleep(2)
for i in (0,10):
    try:
        temp = browser.find_element_by_id("js-submit-btn")
        time.sleep(1)
        break
    except:
        pass
try:
    temp = browser.find_element_by_id("js-submit-btn")
    verify_code = raw_input("Enter verify_code: ")
    browser.find_elements_by_class_name("login-input")[2].send_keys(verify_code.strip())
    time.sleep(2)
    browser.find_element_by_id("js-submit-btn").click()
    time.sleep(2)
except:
    pass

print "Login Done"

order_class = browser.find_element_by_class_name("with-icon icon-clock")
if order_class:
    order_class.click()
    time.sleep(2)
else:
    print "Failed"
    exit(0)



def book_class(ordered):
    n = 0

    for time_dic in time_dic_array:
        while True:
            try:
                trlist = browser.find_element_by_class_name("schedule-table-body").find_elements_by_xpath("tbody/tr")
                break
            except:
                time.sleep(1)
        # print("get list")
        n = n + 1
        nowhandle = browser.current_window_handle
        if ordered >= ORDER_TIMES:  # 预约次数
            break
        for tr in trlist:
            if ordered >= ORDER_TIMES: #预约次数
                break
            c_time = tr.find_element_by_xpath("th").text
            #if c_time == "19:30" or c_time == "19:00" or c_time == "20:00" or c_time == "20:30": # 打算预约的时间段
            if c_time == time_dic["time"]:  # 打算预约的时间段
                tdlist = tr.find_elements_by_xpath("td")
                date = 0
                for td in tdlist:
                    if ordered >= ORDER_TIMES:
                        break
                    date = date + 1 #星期几
                    #if date != 2 and date != 3 and date != 5: #跳过星期二,星期三和星期五
                    #if date != 3 and date != 5:  # 跳过星期三和星期五
                    if date == time_dic["date"]:
                        #print u"星期"+str(date) + " " + c_time + ":" + "=="+td.text.strip()+"=="
                        if td.text.strip() == u"可预约":
                            print u"星期" + str(date) + " " + c_time + ":" + "==" + td.text.strip() + "=="
                            td.find_element_by_xpath("div").click()

                            ####CANCEL#####

                            btn_lst = browser.find_elements_by_class_name("cancel-btn")
                            for btn in btn_lst:
                                print btn.text
                                if btn.text == u"再想想": ##debug
                                    btn.click()
                                    ordered = ordered + 1
                                    ordered_arry.append(time_dic)
                            '''
                            ####CONFIRM#####
                            while True:
                               try:
                                    btn_lst = browser.find_elements_by_class_name("confirm-btn")
                                    break
                               except:
                                    time.sleep(1)
                            for btn in btn_lst:
                                print btn.text
                                if btn.text == u"确定预约": ##release
                                    btn.click()

                                    while True:
                                        try:
                                            btn_confirm = browser.find_element_by_class_name("confirm-btn")
                                            break
                                        except:
                                            time.sleep(1)
                                    print btn_confirm.text
                                    if btn_confirm.text == u"确定": ##release
                                        print "Get it!!!"
                                        btn_confirm.click()
                                        #time.sleep(2)
                                        ordered = ordered + 1
                                        ordered_arry.append(time_dic)
                            '''
    return ordered

order_count = 0
while True:
    for teacher in teacher_array:
        ordered_arry = []
        # browser.find_element_by_class_name("teacher-input")
        teacher_search = browser.find_element_by_class_name("teacher-input").find_element_by_xpath("input[@type='text']")
        # it.send_keys("Junel") #teacher name
        print teacher
        teacher_search.send_keys(teacher)  # teacher name
        teacher_search.send_keys(Keys.ENTER)
        #time.sleep(2)
        # browser.find_element_by_xpath("//*[@id='js-teacher-input']/*/input[@type='Jtext']").send_keys("Junel")
        # browser.find_element_by_xpath("//a[contains(text(), '退出')]")
        order_count = book_class(order_count)
        if order_count >= ORDER_TIMES:
            break
        for ordered in ordered_arry:
            for tmp_dic in time_dic_array:
                if tmp_dic["date"] == ordered["date"]:
                    time_dic_array.remove(tmp_dic)
    if order_count >=ORDER_TIMES:
        break
    else:
        browser.refresh()  # 刷新方法 refresh
        print "Refresh"
        time.sleep(1)

time.sleep(5)
browser.quit()
