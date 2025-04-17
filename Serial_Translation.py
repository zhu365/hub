import serial
import serial.tools.list_ports

# 检测可用串口
ports = serial.tools.list_ports.comports()
print("可用串口：")
for port in ports:
    print(port.device)

# 配置串口
port_name = 'COM7'  # 修改为你的端口
baudrate = 115200
try:
    ser = serial.Serial(port_name, baudrate, timeout=1)
    print(f"已连接到 {ser.name}")

    while True:
        cmd = input("请输入指令 (true/exit): ").strip()
        if cmd.lower()== "exit":
            break
        elif cmd.lower() == "true":
            data = bytearray([0xFA, 0xAF, 0x01, 0xFB, 0xBF])
            ser.write(data)
            print(f"已发送: {data.hex()}")
        else:
            data = bytearray([0xFA, 0xAF, 0x00, 0xFB, 0xBF])
            ser.write(data)
            print(f"已发送: {data.hex()}")
except serial.SerialException as e:
    print("串口错误:", e)
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
    print("串口已关闭")