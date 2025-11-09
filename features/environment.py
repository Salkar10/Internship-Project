from allure_behave.utils import scenario_name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from app.application import Application
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#def browser_init(context):
# def browser_init(context, scenario_name):
#
#
#     mobile_emulation = {
#         "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
#         "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
#         "clientHints": {"platform": "Android", "mobile": True}
#     }
#
#     chrome_options = Options()
#     chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#     context.driver = webdriver.Chrome(options = chrome_options)

# def after_scenario(context, scenario):
#      context.driver.quit()
#def browser_init(context, scenario_name):
    # """
    # ##:param context: Behave context
    # :type context: object
    # """
    # ## CHROME CONFIGURATION ###
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # ### BROWSERSTACK CONFIGURATION ###
    # BROWSERSTACK_USERNAME = "hamzamechou_Wh3pcM"
    # BROWSERSTACK_ACCESS_KEY = "JmHL7q59zCXfpGqTJmky"
    #
    # url = f'https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub'
    #
    # # options = Options()
    # # bstack_options = {
    #      "os": "Windows",
    #      "osVersion": "10",
    #      "browserName": "Chrome",
    #      "browserVersion": "latest",
    #      "buildName": "bstack-Internship",
    #      "projectName": "BrowserStack product sale status",
    #      "sessionName": scenario_name
    #}

def browser_init(context, scenario_name):


    ### BROWSERSTACK CONFIGURATION ###
    BROWSERSTACK_USERNAME = "hamzamechou_Wh3pcM"
    BROWSERSTACK_ACCESS_KEY = "JmHL7q59zCXfpGqTJmky"
    url = f'https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {

        "deviceName": "Samsung Galaxy S25 Ultra",
        "realMobile": "true",
        "osVersion": "15.0",
        "browserName": "chrome",
        "deviceOrientation": "portrait",
        "buildName": "bstack-Internship",
        "projectName": "BrowserStack product sale status",
        "sessionName": scenario_name,

    }

    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    ##HEADLESS CONFIGURATION ###
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(5)
    # context.driver.set_window_size(1800, 1500)

    ##FIREFOX CONFIGURATION###
#def browser_init(context):
    # """
    # :param context: Behave context
    # """
    # from selenium.webdriver.firefox.service import Service as FirefoxService
    # from webdriver_manager.firefox import GeckoDriverManager
    #
    # driver_path = GeckoDriverManager().install()
    # service = FirefoxService(driver_path)
    # context.driver = webdriver.Firefox(service=service)
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)


    #context.driver.maximize_window()
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
