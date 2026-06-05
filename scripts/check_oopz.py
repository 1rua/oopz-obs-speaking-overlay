import socket
import sys
import time


def main() -> int:
    max_retries = 10
    host = "127.0.0.1"
    port = 10274
    for i in range(1, max_retries + 1):
        print(f"正在检测OOPZ连接... (第{i}次/{max_retries})")
        try:
            s = socket.create_connection((host, port), timeout=2)
            s.close()
            print("OOPZ已检测到，正在启动服务器...")
            return 0
        except Exception:
            if i < max_retries:
                time.sleep(2)

    print("无法连接到OOPZ，请确认OOPZ已启动且屏幕覆盖已开启。")
    while True:
        try:
            choice = input("是否继续启动服务器？(y/n): ").strip().lower()
        except EOFError:
            choice = "n"
        if choice in ("y", "yes", "是"):
            print("继续启动服务器...")
            return 0
        elif choice in ("n", "no", "否"):
            return 1
        else:
            print("请输入 y 或 n")


if __name__ == "__main__":
    sys.exit(main())
