from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://shiksha.iiit.ac.in/asgn/app/grade/view/86469/')
# driver.find_element_by_name("Login").click()

# uname = args.username + '@' + args.type
username = driver.find_element_by_id("username")
username.clear()
username.send_keys("anchit.gupta@r")

password = driver.find_element_by_id("password")
password.clear()
password.send_keys("##########") # your password

driver.find_element_by_name("submit").click()

# driver.find_element_by_link_text("Principles of Information Security").click()
# driver.find_element_by_link_text("Questionnaire").click()
# driver.find_element_by_link_text("Answer the questions...").click()

# opt = 'auto-rb{:04d}'.format(args.option)
# # print(opt)
# driver.find_element_by_id(opt).click()
with open('marks.csv','r') as f:
	lines = f.readlines()
	for l in lines:
		m, ID = l.strip().split(',')
		# print(m, ID)
		driver.get('http://shiksha.iiit.ac.in/asgn/app/grade/view/{}/'.format(ID))

		marks = driver.find_element_by_id("criterion_1")
		marks.clear()
		marks.send_keys(m)
		driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div/form/fieldset/div/input").click()

		# btn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div/form/fieldset/div/input")

# # print(btn)
# btn.click()
