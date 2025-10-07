import qrcode

url = "https://bidulgirin.github.io/birthday/"

# QR 코드 생성~
img = qrcode.make(url)

# 파일로 저장
img.save("my_qr.png")

print("QR 코드 생성 완료! (my_qr.png)")
