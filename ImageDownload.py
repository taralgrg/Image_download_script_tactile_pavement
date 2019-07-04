from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Blister Surface pavement,Blister Surface pavement,blister surface tactile pavement,blister surface tactile pavement for visually impaired","limit":1000,"chromedriver":"/usr/local/bin/chromedriver","print_urls":True}   #creating list of arguments
#Make sure to set chromedrive is the appropriate director if you want to download more than 100 images
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images

