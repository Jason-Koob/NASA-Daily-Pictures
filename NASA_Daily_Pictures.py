URL_1 = "https://apod.nasa.gov/apod/ap"
URL_2 = ".html"

num = 230725


while num >= 1 and num >= 140000:
    f_URL = URL_1 +  str(num) + URL_2

    num = num - 1

    with open('records.txt', 'a') as docWrite:
        docWrite.write(f_URL + "\n")

    print("num " + str(num) + ": URL recorded.")