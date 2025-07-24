from selenium.webdriver.common.by import By

H1_TITLE = '//h1'
PARAGRAPH_WITH_HANDS_ON_EXPERIENCE = '//p[contains(text(), "hands-on experience")]'

SIGN_UP_BUTTON = '//button[text()="Sign up"]'
SIGN_IN_BUTTON = '//button[contains(@class, "header_signin")]'
CONTACTS_BUTTON = '//button[contains(text(), "Contacts")]'
ABOUT_BUTTON_IN_NAV = '//nav//button[text()="About"]'
CONTACTS_BUTTON_IN_NAV = '//nav//button[text()="Contacts"]'
TRY_FREE_BUTTON = '//button[text()="Try for free"]'

HOME_LINK = '//a[@routerlink="/" and text()="Home"]'
HILLEL_LOGO_LINK = '//a[contains(@href, "ithillel.ua") and contains(@class, "display-4")]'
FACEBOOK_LINK = '//a[contains(@href, "facebook.com")]'
TELEGRAM_LINK = '//a[contains(@href, "t.me/ithillel")]'
FOOTER_LOGO_LINK = '//a[contains(@class, "footer_logo")]'

LOG_FUEL_EXPENSES_TEXT = '//p[text()="Log fuel expenses"]'
VEHICLE_MAINTENANCE_TEXT = '//p[text()="Keep track of your replacement schedule and plan your vehicle maintenance expenses in advance."]'
INSTRUCTIONS_AND_MANUALS_TEXT = '//p[text()="Instructions and manuals"]'
REPAIR_YOUR_CAR_TEXT = '//p[contains(text(), "repair your car")]'
EASILY_TRACK_TEXT = '//h2[text()="Easily track vehicle expenses and service history"]'
GET_STARTED_FOR_FREE_TEXT = '//h2[text()="Get started for free"]'

CONTACTS_SECTION_DIV = '//div[@id="contactsSection"]'
ABOUT_BLOCK_TITLE_FIRST = '(//p[@class="about-block_title h2"])[1]'
ABOUT_BLOCK_DESCRIPTION = '//p[contains(@class, "about-block_descr")]'
APP_WRAPPER_DIV = '//div[@class="app-wrapper"]'
CONTACTS_SOCIALS_DIV = '//div[contains(@class, "contacts_socials")]'
ABOUT_US_SECTION = '//section[@id="aboutSection"]'
HERO_SECTION = '//section[contains(@class, "hero-section")]'

INFO_IMAGE = '//img[contains(@src, "info_1.jpg")]'
HERO_VIDEO_IFRAME = '//div[contains(@class, "hero-video")]//iframe'
APPLE_STORE_IMAGE = '//img[contains(@src, "appstore") or contains(@alt, "App Store")]'
GOOGLE_PLAY_IMAGE = '//img[contains(@src, "googleplay") or contains(@alt, "Google Play")]'

FOOTER_PURPOSES_PARAGRAPH = '//footer//p[contains(text(), "educational purposes")]'