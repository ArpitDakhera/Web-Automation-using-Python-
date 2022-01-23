
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys
# import mysql.connector
import random
import pandas as pd
import os
#connection to database
# mydb=mysql.connector.connect(host="127.0.0.1",user='root',password='password',database='central',auth_plugin='mysql_native_password')
# cursor=mydb.cursor()
from joblib import Parallel, delayed

# torexe = os.popen(r'C:\Users\Asus\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
# PROXY = "socks5://localhost:9050" # IP:PORT or HOST:PORT
# options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=%s' % PROXY)

# options = Options()
# options.binary_location = r'C:\Users\Asus\Desktop\Tor Browser\Browser\firefox.exe'

def insert_records(client_gender, client_name, mob_no, a):
    try:
        # options = Options()
        # options.binary_location = r'C:\Users\Asus\Desktop\Tor Browser\Browser\firefox.exe'
        web = webdriver.Chrome(executable_path=r"E:\hackingpyhton\chromedriver.exe")
        web.implicitly_wait(20)
        web.get('https://ssg2021.in/CitizenFeedback')

        time.sleep(1)

        state = web.find_element(By.ID, "State")
        sta = Select(state)
        sta.select_by_visible_text('Rajasthan')

        district = web.find_element(By.ID, 'District')
        dist = Select(district)
        dist.select_by_value("409")

        age = web.find_element(By.XPATH,
                               '//*[@id="zed_user_form"]/div/div[1]/div[2]/div/div/div[1]/form/div[4]/div[1]/div/div/input')
        age.click()
        agee = random.randint(20, 70)
        age.send_keys(agee)

        print(a)

        name = web.find_element(By.NAME, 'RespondentName')
        name.click()
        # cursor.execute("SELECT name from entries")
        # naam=cursor.fetchall()
        # nam=naam[flag]
        name.send_keys(client_name)

        mobile = web.find_element(By.NAME, 'RespondentMobileNo')
        mobile.click()
        # cursor.execute("SELECT mobile from entries")
        # mob=cursor.fetchall()
        # number=mob[flag]
        mob_no += 1
        print(mob_no)
        mobile.send_keys(mob_no)

        gender = web.find_element(By.NAME, 'RespondentGender')
        gender.click()
        # cursor.execute("SELECT gender from entries")
        # gen=cursor.fetchall()
        # ling=gen[flag]
        gender.send_keys(client_gender)

        web.find_element(By.XPATH, '//*[@id="zed_user_form"]/div/div[1]/div[2]/div/div/div[1]/form/div[5]/input').click()
        web.find_element(By.NAME, 'FQ1').click()
        web.find_element(By.NAME, 'FQ2').click()
        web.find_element(By.NAME, 'FQ3').click()
        web.find_element(By.NAME, 'FQ4').click()
        web.find_element(By.NAME, 'FQ5').click()

        web.find_element(By.XPATH, '//*[@id="zed_user_form"]/div/div[1]/div[2]/div/div/div[2]/form/div[2]/input').click()
        a = a + 1
        alert = web.switch_to.alert
        print(alert.text)
        # if alert.text == 'Your quota exceeded for the day.' or alert.text == 'This Mobile No is already attached to a submitted feedback.':
        #     mob_no += 1
        time.sleep(5)
        web.close()
        
        return alert.text
    
    except Exception as e:
        print(e)
        time.sleep(5)
        web.close()
        return alert.text

if __name__ == '__main__':
    mob_no = 6376046259
    with Parallel(max_nbytes = None, n_jobs = 5) as parallel:
        for i in range(10000000):
            df = pd.read_csv('file.csv')
            for i in range(0, df.shape[0], 5):
                df_subset = df.iloc[i:i + 5]      
                try:
                    text = parallel(
                        delayed(insert_records)(
                            row['M/F'], row['name'], mob_no+index, index)
                            for index, row in df_subset.iterrows())

                    text_list = [text_final for text_final in text if text is not None]
                    mob_no += 400
                
                except Exception as e:
                    print(e)
                    time.sleep(5)
                    continue

