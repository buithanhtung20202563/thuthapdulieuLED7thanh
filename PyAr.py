import serial
import time
import cv2
# Kết nối với cổng Serial của Arduino
ser = serial.Serial('COM3', 9600)  # Thay 'COM3' bằng cổng Serial của Arduino

# Chờ Arduino khởi động
time.sleep(2)

# Nhập một số bất kỳ từ bàn phím trong khoảng từ 0 đến 9999
number = int(input("Nhập số cần Arduino hiển thị: "))
while number < 0 or number > 9999:
    print("Nhập lại")
    exit()

# Gửi số từ Python đến Arduino 
ser.write(str(number).encode())

# Đọc tín hiệu từ Arduino
arduino_signal = ser.readline().decode().strip()

# Nếu nhận được tín hiệu "OK" từ Arduino
if arduino_signal == "OK":
    # Chụp 3 bức ảnh liên tiếp
    for i in range(3):
        # Sử dụng webcam để chụp ảnh
        camera = cv2.VideoCapture(0)  # Số 0 đại diện cho camera mặc định

        # Đọc một khung hình từ webcam
        _, frame = camera.read()

        # Lưu ảnh với tên tương ứng số đã gửi và số thứ tự ảnh
        filename = "/Users/hatru/OneDrive - Hanoi University of Science and Technology/PROJECT1/data/Trong phong/"+str(number) + "_" + str(i+1) + ".jpg"
        cv2.imwrite(filename, frame)

        # Đóng webcam
        camera.release()
    f = open("/Users/hatru/OneDrive - Hanoi University of Science and Technology/PROJECT1/data/Trong phong/"+str(number)+".csv", "w")
    f.write("Goc chup(do),Tan so(Hz),So hien thi "+"\n")
    # Góc chụp từ camera laptop là từ trên xuống
    f.write("45,100,"+str(number)+"\n")
    f.close()
# Đóng kết nối Serial
ser.close()
