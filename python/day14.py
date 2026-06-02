# import datetime
# date = "2-6-2026"
# x = datetime.datetime.now()
# print(x)
# print(x.year)



# import random
# cnum = random.randrange(0,100)
# unum = int(input("enter Your number:"))
# if cnum > unum:
#     print("computer number",cnum,"is greater")
# elif unum > cnum:
#     print("computer number",cnum,"is smaller")
# else:
#     print("computer number", cnum,"is equal") 




# import math
# a = math.acos(-1)
# print(a)




# import secrets
# import string
# alphabet = string.ascii_letters + string.digits
# password = ''.join(secrets.choice(alphabet) for i in range(20))
# print(password)



# import qrcode
# data = "https://www.youtube.com/channel/UCWv7vMbMWH4-V0ZXdmDpPBA"
# img = qrcode.make(data)
# img.save("youtube.png")     module not found error: qrcode





import cv2
image = cv2.imread("youtube.png")
detector = cv2.QRCodeDetector()
data,vertices_array,binary_qrcode = detector.detectAndDecode(image)
if vertices_array is not None and data:
    print("Decoded data:", data)
else:
    print("QR code not detected or data could not be decoded.")