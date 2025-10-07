import birthday

url = "https://bidulgirin.github.io/birthday/birthday.html"

# QR 코드 생성~
img = birthday.make(url)

# 파일로 저장
img.save("my_qr.png")

print("")
