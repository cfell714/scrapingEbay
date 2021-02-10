from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

html = urlopen('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=camera&_sacat=0') #change the link was tryingn something for amazon code
bs = BeautifulSoup(html, 'html.parser')

csvFile = open('listOfCameras.csv', 'w+', newline='')
writer = csv.writer(csvFile)

table = bs.find('ul', {'class': 'srp-results srp-list clearfix'})
children = table.findChildren('a', recursive='True')
cameraList = []


for child in children:
    word = child.get('href')
#    print(word)
    if word in cameraList:
        print(' ')
    else:
        if "itm" in word:
            cameraList.append(word)
            writer.writerow([word])
            print(word)

csvFile.close()

csvFile = open('listOfCameras.csv', 'r')
csvFileNew = open('informationForCameras.csv', 'w+', newline='')
writerNew = csv.writer(csvFileNew)

for row in csvFile:
    newHtml = urlopen(row)
    bsNew = BeautifulSoup(newHtml, 'html.parser')
    newList = []

    try:
        title = bsNew.find('h1', {'id': 'itemTitle'}).text
        titleNew = title[16:]
        print("Title: " + titleNew)
        newList.append(titleNew)
    except:
        newList.append("No Title Showing")
        print("NO TITLE SHOWING")

    try:
        condition = bsNew.find('div', {'class': 'u-flL condText'}).text
        newList.append(condition)
        print("Condition: " + condition)
    except:
        newList.append("No Condition Showing")
        print("NO CONDITION SHOWING")

    try:
        price = bsNew.find('span', {'class': 'notranslate'}).text
        priceNew = price.strip()
        priceNew = priceNew.strip("\n")
        priceNew = priceNew.strip("\t")
        newList.append(priceNew)
        print("Price: " + priceNew)
    except:
        newList.append("No Price Showing")
        print("NO PRICE SHOWING")

    try:
        shipping = bsNew.find('span', {'id': 'fshippingCost'}).text
        shippingNew = shipping.strip()
        shippingNew = shippingNew.strip("\n")
        newList.append(shippingNew)
        print("Shipping: " + shippingNew)
    except:
        newList.append("No Shipping Showing")
        print("NO SHIPPING SHOWING")

    try:
        returns = bsNew.find('span', {'id': 'vi-ret-accrd-txt'}).text
        returns = returns.strip("\xa0")
        newList.append(returns)
        print("Returns: " + returns)
    except:
        newList.append("No returns showing")
        print("NO RETURNS SHOWING")

    try:
        delivery = bsNew.find('span', {'class': 'vi-acc-del-range'}).text
        deliveryNew = delivery.strip()
        newList.append(deliveryNew)
        print("Delivery: " + deliveryNew)
    except:
        newList.append("No Delivery Showing")
        print("NO DELIVERY SHOWING")

    try:
        rating = bsNew.find('span', {'class': 'ebay-review-start-rating'}).text
        ratingNew = rating.strip()
        ratingNew = ratingNew.strip("\n")
        ratingNew = ratingNew.strip("\t")
        newList.append(ratingNew)
        print("Rating: " + ratingNew)
    except:
        newList.append("No Rating Showing")
        print("NO RATING SHOWING")

    writerNew.writerow([newList])

csvFile.close()
csvFileNew.close()
