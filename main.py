import requests
from bs4 import BeautifulSoup
from smtplib import SMTP_SSL
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_password = "cccnjjteocbqkbtd"
MY_EMAIL = "kobbygilbert233@gmail.com"
URL = ("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")



headers ={
    'authority': 'www.amazon.com',
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari"
                 "/537.36",
    "Accept-Language":"en-US,en;q=0.9",

}
response = requests.get(url=URL,headers=headers)
response_text = response.text
# with open(file="response.html",mode="r",encoding="utf-8") as file:
#     response_text=file.read()
# print(response_text)

#
soup = BeautifulSoup(response_text,"lxml")
heading = soup.select_one(selector="h1 span").text.encode("utf-8").strip()
currency_sign = soup.select_one(selector="span .a-price-symbol").text.strip()
print(type(heading))

#
price = soup.select_one(selector="span .a-price-whole").text.strip()
# print(price)

try:
    num_price = int(price)
except ValueError:
    price_str = ""
    if "," in price:
        price_sep = price.split(",")
        for _ in price_sep:
            price_str += _
        price = price_str
        print(",")
    if "." in price:
        price_sep = price.split(".")
        price = price_sep[0]
        print(".")
    num_price = int(price)


finally:
    if num_price <= 100:
        print("send email")


subject = "Amazon Price Alert"
body = f"{heading} is now {currency_sign}{num_price}"
port = 465

with SMTP_SSL("smtp.gmail.com",port) as server:
    server.login(user=MY_EMAIL,password=email_password)
    send = server.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:Amazon Price Alert\n\n{body}")






