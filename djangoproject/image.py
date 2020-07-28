#200630 업데이트 이후로 방법 막힘 ㅅㄱ

from google_images_download import google_images_download #라이브러리 접근

response = google_images_download.googleimagesdownload()
arguments  = {"keywords" : "Polarbears, baloons, Beaches", 
"limit" : 20, "print_urls" : True}
paths = response.download(arguments)
print(paths)