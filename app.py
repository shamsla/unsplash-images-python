import requests

width = input("Width:")
height = input("Height:")
keyword = input("Keyword:")
num = input("How many images to download?:")
save_to = input("Enter path to save the images: ")

url = f"https://source.unsplash.com/{width}x{height}/?{keyword}"

image_data = requests.get(url)

# to download the x number of images
for i in range(1, int(num)+1):
	image_data = requests.get(url)
	
	with open(rf"{save_to}\{keyword}-{i}.jpg", "wb") as image:
	 	image.write(image_data.content)