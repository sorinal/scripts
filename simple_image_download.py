# pip install simple_image_download

from simple_image_download import simple_image_download as simp

response = simp.simple_image_download
response().download('cat', 10000)
# print(response().urls('bear', 5))
