from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException   
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from PIL import Image, ExifTags
import imghdr


#web = webdriver.Chrome()
ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("user-data-dir=/home/wieb/.config/google-chrome")
#ChromeOptions.add_argument("user-data-dir=C:\\Users\\Wieb\\AppData\\Local\\Google\\Chrome\\User Data")
ChromeOptions.add_argument("disable-blink-features=AutomationControlled")
ChromeOptions.add_argument("--ignore-certificate-errors")
ChromeOptions.add_argument('--allow-running-insecure-content')
#ChromeOptions.add_argument("--headless")
#ChromeOptions.add_argument("--window-size=1920,1080")
WebDriver = webdriver.Chrome(options = ChromeOptions)
time.sleep(2)

def check_exists_by_xpath(xpath):
    try:
        WebDriver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

WebDriver.maximize_window()
time.sleep(2)

WebDriver.get('https://www.marktplaats.nl')
time.sleep(3)

cookies = '//*[@id="gdpr-consent-banner-accept-button"]'
if check_exists_by_xpath(cookies) != False:
    cookies = WebDriver.find_element(By.XPATH, '//*[@id="gdpr-consent-banner-accept-button"]')
    cookies.click()
    time.sleep(5)

inloggen_popup = '/html/body/div[4]/div/div/div[1]/div[1]/button'
if check_exists_by_xpath(inloggen_popup) != False:
    inloggen_popup = WebDriver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[1]/div[1]/button')
    inloggen_popup.click()
    time.sleep(5)

naam_zwm = '//*[@id="header-root"]/header/div[1]/div[2]/div/ul[2]/li[3]/div/button/span'
naam_mwm = '//*[@id="header-root"]/header/div[1]/div[2]/div/ul[2]/li[4]/div/button/span'

if check_exists_by_xpath(naam_zwm) != True and check_exists_by_xpath(naam_mwm) != True:
    inloggen_header = WebDriver.find_element(By.XPATH, '//*[@id="header-root"]/header/div[1]/div[2]/div/ul[2]/li[4]/a')
    inloggen_header.click()
    time.sleep(5)

    # email = ''
    form_email = WebDriver.find_element(By.XPATH, '//*[@id="account-login-form"]/fieldset/div/div[1]/input')

    if form_email != email:
        form_email.send_keys('')
        time.sleep(2)
        form_email.send_keys(email)
    
    time.sleep(2)

    # password = ''
    form_password = WebDriver.find_element(By.XPATH, '//*[@id="password"]')

    if form_password != password:
        form_password.send_keys('')
        time.sleep(2)
        form_password.send_keys(password)
    
    time.sleep(2)    

    inloggen_submit = WebDriver.find_element(By.XPATH, '//*[@id="account-login-button"]')
    inloggen_submit.click()
    time.sleep(5)

if check_exists_by_xpath('//*[@id="header-root"]/header/div[1]/div[2]/div/ul[2]/li[3]/div/button') != False:
    naam_dropdown = WebDriver.find_element(By.XPATH, '//*[@id="header-root"]/header/div[1]/div[2]/div/ul[2]/li[3]/div/button')
    naam_dropdown.click()
    time.sleep(1)
    mijn_advertenties = WebDriver.find_element(By.XPATH, '//*[@id="header-root"]/header/div[1]/div[2]/div/ul[2]/li[3]/div/ul/li[1]/a')
    mijn_advertenties.click()
    time.sleep(2)
else:
    naam_dropdown = WebDriver.find_element(By.XPATH, '//*[@id="header-root"]/header/div[1]/div[2]/div/ul[2]/li[4]/div/button')
    naam_dropdown.click()
    time.sleep(1)
    mijn_advertenties = WebDriver.find_element(By.XPATH, '//*[@id="header-root"]/header/div[1]/div[2]/div/ul[2]/li[4]/div/ul/li[1]/a')
    mijn_advertenties.click()
    time.sleep(2)

meer_advertenties = '//*[@id="load-more-row"]/div/a'

while check_exists_by_xpath(meer_advertenties) != False:

    toon_meer_advertenties = WebDriver.find_element(By.XPATH, '//*[@id="load-more-row"]/div/a')
    toon_meer_advertenties.click()
    time.sleep(3)

my_list = os.listdir('advertenties')

advertentie_naam_div = WebDriver.find_elements(By.XPATH, '//*[@class="row ad-listing"]/div/div[3]/div[1]')
print(len(advertentie_naam_div))

advertentie_online_list = []

for i in advertentie_naam_div:

    advertenties_op_marktplaats = i.find_element(By.TAG_NAME, 'span').text
    advertentie_online_list.append(advertenties_op_marktplaats)

print(len(advertentie_online_list))

advertenties_niet_op_marktplaats = []

for i in my_list:

    if i not in advertentie_online_list:

        advertenties_niet_op_marktplaats.append(i)
        print(i)
        
print(len(advertenties_niet_op_marktplaats))


for i in advertenties_niet_op_marktplaats:

    homepage = WebDriver.find_element(By.XPATH, '/html/body/mp-header/div[1]/div[2]/div/a')
    homepage.click()
    time.sleep(10)

    if check_exists_by_xpath('//*[@id="header-root"]/header/div[1]/div[2]/div/ul[2]/li[6]/a') != False:
        plaats_advertentie = WebDriver.find_element(By.XPATH, '//*[@id="header-root"]/header/div[1]/div[2]/div/ul[2]/li[6]/a')
        plaats_advertentie.click()
        time.sleep(3)

    elif check_exists_by_xpath('//*[@id="header-root"]/header/div[1]/div[2]/div/ul[2]/li[5]/a') != False:
        plaats_advertentie = WebDriver.find_element(By.XPATH, '//*[@id="header-root"]/header/div[1]/div[2]/div/ul[2]/li[5]/a')
        plaats_advertentie.click()
        time.sleep(3)

    input_advertentienaam = WebDriver.find_element(By.XPATH, '//*[@id="category-keywords"]')
    input_advertentienaam.send_keys(i)
    time.sleep(2)

    f = open(f'advertenties/{i}/Categorie.txt', 'r')
    file_contents = f.read()
    file_contents = file_contents.split("--")

    eerste_select = Select(WebDriver.find_element(By.XPATH, '//*[@id="cat_sel_1"]'))
    eerste_select.select_by_visible_text(file_contents[0])
    time.sleep(2)

    tweede_select = Select(WebDriver.find_element(By.XPATH, '//*[@id="cat_sel_2"]'))
    tweede_select.select_by_visible_text(file_contents[1])
    time.sleep(2)

    derde_select = Select(WebDriver.find_element(By.XPATH, '//*[@id="cat_sel_3"]'))
    derde_select.select_by_visible_text(file_contents[2])
    time.sleep(2)

    submit_advertentienaam = WebDriver.find_element(By.XPATH, '//*[@id="category-selection-submit"]')
    submit_advertentienaam.click()
    time.sleep(5)

    beschrijving_path = f'advertenties/{i}/Beschrijving.txt' 
    photos_folder = f'advertenties/{i}/fotos'
    my_photos = os.listdir(photos_folder)
    upload_vak = 0

    for i in my_photos:
        path = f'{photos_folder}/{i}'
        newphoto = i
        if imghdr.what(path) != 'png':
            try:

                image = Image.open(path)

                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation]=='Orientation':
                        break
                    
                exif = image._getexif()
                print(exif[orientation])
                image.close()
                image = Image.open(path).convert('RGBA')

                if exif[orientation] == 3:
                    image=image.rotate(180, expand=True)
                    image.save(path  + ".PNG", "PNG")
                    os.remove(path)
                    newphoto = i + ".PNG"
                elif exif[orientation] == 6:
                    image=image.rotate(270, expand=True)
                    image.save(path  + ".PNG", "PNG")
                    os.remove(path)
                    newphoto = i + ".PNG"
                elif exif[orientation] == 8:
                    image=image.rotate(90, expand=True)
                    image.save(path  + ".PNG", "PNG")
                    os.remove(path)
                    newphoto = i + ".PNG"
                        
            except (AttributeError, KeyError, IndexError, TypeError):
                # cases: image don't have getexif
                pass

        while True:
            foto_upload_div = WebDriver.find_elements(By.XPATH, '//*[@class="moxie-shim moxie-shim-html5"]')
            try:
                foto_upload = foto_upload_div[upload_vak].find_element(By.TAG_NAME, 'input')
            except IndexError:
                time.sleep(1)
                continue
            else:
       		       
                path = f'{os.getcwd()}/{photos_folder}/{newphoto}'
                foto_upload.send_keys(path)
                upload_vak+=1
                break
    time.sleep(1)

    beschrijving = open(beschrijving_path, 'r')
    beschrijving_text = beschrijving.read()
    textvak_beschrijving_frame = WebDriver.find_element(By.XPATH, '//*[@id="description_nl-NL_ifr"]')
    WebDriver.switch_to.frame(textvak_beschrijving_frame)
    textvak_beschrijving = WebDriver.find_element(By.XPATH, "//body")
    textvak_beschrijving.send_keys(beschrijving_text)
    time.sleep(2)

    WebDriver.switch_to.default_content()
    if check_exists_by_xpath('//*[@id="syi-attribute-condition"]/div/select') != False:
        conditie_select = Select(WebDriver.find_element(By.XPATH, '//*[@id="syi-attribute-condition"]/div/select'))
        conditie_select.select_by_visible_text(file_contents[3])
        time.sleep(2)

    prijstype_select = Select(WebDriver.find_element(By.XPATH, '//*[@id="syi-price-type-dropdown"]/div/select'))
    prijstype_select.select_by_visible_text(file_contents[4])
    time.sleep(2)

    if file_contents[4] == 'Vraagprijs':
        vraagprijs = WebDriver.find_element(By.XPATH, '//*[@id="syi-bidding-price"]/input')
        vraagprijs.send_keys(file_contents[5])
        time.sleep(3)

        bieden = WebDriver.find_element(By.XPATH, '//*[@id="syi-bidding-accept"]/span/label')
        biedprijs = WebDriver.find_element(By.XPATH, '//*[@id="syi-price-type"]/div[1]/div[2]/div[2]')
        biedprijs_stijl = biedprijs.get_attribute("style")
        print(biedprijs_stijl)
        if biedprijs_stijl == 'display: none;':
            bieden.click()
        time.sleep(1)

    verzendmethode = WebDriver.find_element(By.XPATH, '//*[@id="shippingMethod0"]')
    verzendmethode.click()
    time.sleep(2)

    if file_contents[5] == 'Klein' or file_contents[6] == 'Klein':
        past_door_bus = WebDriver.find_element(By.XPATH, '//*[@id="PostNLShippingProducts"]/div[1]/div[2]/div/div/div[2]/label[1]/input')
        past_door_bus.click()
        time.sleep(2)

        envelop = WebDriver.find_element(By.XPATH, '//*[@id="1000_letters_175"]')
        envelop.click()
        time.sleep(2)

        verzendmethode_opslaan = WebDriver.find_element(By.XPATH, '//*[@id="PostNLShippingProducts"]/div[1]/div[3]/button[2]')
        verzendmethode_opslaan.click()

    elif file_contents[5] == 'Licht' or file_contents[6] == 'Licht':
        past_door_bus = WebDriver.find_element(By.XPATH, '//*[@id="PostNLShippingProducts"]/div[1]/div[2]/div/div/div[2]/label[1]/input')
        past_door_bus.click()
        time.sleep(2)

        brievenbuspakje = WebDriver.find_element(By.XPATH, '//*[@id="1018_parcels_1000"]')
        brievenbuspakje.click()
        time.sleep(2)

        verzendmethode_opslaan = WebDriver.find_element(By.XPATH, '//*[@id="PostNLShippingProducts"]/div[1]/div[3]/button[2]')
        verzendmethode_opslaan.click()

    elif file_contents[5] == 'Groot' or file_contents[6] == 'Groot':
        past_niet_door_bus = WebDriver.find_element(By.XPATH, '//*[@id="PostNLShippingProducts"]/div[1]/div[2]/div/div/div[2]/label[2]/input')
        past_niet_door_bus.click()
        time.sleep(2)

        pakket_0_tot_10_kg = WebDriver.find_element(By.XPATH, '//*[@id="3000_parcels_5000"]')
        pakket_0_tot_10_kg.click()
        time.sleep(2)

        verzendmethode_opslaan = WebDriver.find_element(By.XPATH, '//*[@id="PostNLShippingProducts"]/div[1]/div[3]/button[2]')
        verzendmethode_opslaan.click()

    elif file_contents[5] == 'Zwaar' or file_contents[6] == 'Zwaar':
        past_niet_door_bus = WebDriver.find_element(By.XPATH, '//*[@id="PostNLShippingProducts"]/div[1]/div[2]/div/div/div[2]/label[2]/input')
        past_niet_door_bus.click()
        time.sleep(2)

        pakket_10_tot_23_kg = WebDriver.find_element(By.XPATH, '//*[@id="3001_parcels_16500"]')
        pakket_10_tot_23_kg.click()
        time.sleep(2)

        verzendmethode_opslaan = WebDriver.find_element(By.XPATH, '//*[@id="PostNLShippingProducts"]/div[1]/div[3]/button[2]')
        verzendmethode_opslaan.click()

    time.sleep(2)

    kopersbescherming = WebDriver.find_element(By.XPATH, '//*[@id="syi-buyer-protection"]/div[2]/label')
    kopersbescherming.click()
    time.sleep(2)

    gratis = WebDriver.find_element(By.XPATH, '//*[@id="js-products"]/div[1]/div/div/div[1]/div[1]/span')
    gratis.click()
    time.sleep(2)

    plaatsen = WebDriver.find_element(By.XPATH, '//*[@id="syi-place-ad-button"]')
    plaatsen.click()
    time.sleep(5)
  
    feedback = '//*[@id="survey-web-page-wrapper"]/div/div[4]/button[1]'

    if check_exists_by_xpath(feedback) != False:
        feedback_sluit = WebDriver.find_element(By.XPATH, feedback)
        feedback_sluit.click()
        time.sleep(2)

time.sleep(20)
WebDriver.close()
