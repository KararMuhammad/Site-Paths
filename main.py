import requests
def func():
	website = str(input("Enter target website : "))
	Words = open("words.txt","r")
	read = Words.read()
	words = read.splitlines()
	try:
	    for page in words:
	        link = f"{website}/{page}"
	        req = requests.get(link,"html.parser")
	        if req.status_code == 200:
	            print(True, link)
	            with open("pages.txt","a") as Pages:
	            	Pages.write(f"{link}\n")
	        else:
	        	print(False, link)
	except:
		print("Not found any thing !!")
func()
