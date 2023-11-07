URL_1 = "https://apod.nasa.gov/apod/ap"
URL_2 = ".html"

num = 230730

with open('outputs.html', 'a') as docWrite:
    docWrite.write("<body>\n")

while num >= 1 and num > 140000:
    f_URL = "<a href=" + URL_1 + \
        str(num) + URL_2 + ">" + str(num) + "</a><br>"

    num = num - 1

    with open('outputs.html', 'a') as docWrite:
        docWrite.write(f_URL + "\n")

    print("Astonomy Picture of the Day " + str(num) + ": recorded.")


with open('outputs.html', 'a') as docWrite:
    docWrite.write("</body>")
