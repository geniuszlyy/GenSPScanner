import os
import re
import sys
import threading
import socket
from queue import Queue
from colorama import Fore, init

# Инициализация colorama для поддержки цветного текста в консоли
init(autoreset=True)

# Логотип программы
LOGO = f"""
{Fore.LIGHTRED_EX}   _____             _____ _____   _____                                 
  / ____|           / ____|  __ \ / ____|                                
 | |  __  ___ _ __ | (___ | |__) | (___   ___ __ _ _ __  _ __   ___ _ __ 
 | | |_ |/ _ \ '_ \ \___ \|  ___/ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |__| |  __/ | | |____) | |     ____) | (_| (_| | | | | | | |  __/ |   
  \_____|\___|_| |_|_____/|_|    |_____/ \___\__,_|_| |_|_| |_|\___|_|                                                                                                                                                                                                      
"""
print(LOGO)

# Проверка на корректное количество аргументов командной строки
if len(sys.argv) != 4:
    print(f"""
        {Fore.LIGHTYELLOW_EX}╭────────────────────━━━━━━━━━━━━━━━━━━━━━────────────────╮
        | {Fore.LIGHTGREEN_EX}Use » python {os.path.basename(__file__)} [target] [start_port] [end_port]   {Fore.LIGHTYELLOW_EX}| 
        ╰────────────────────━━━━━━━━━━━━━━━━━━━━━────────────────╯
    """)
    sys.exit(1)

# Получение целевого IP-адреса и диапазона портов
target_ip = str(sys.argv[1])
port_start = int(sys.argv[2])
port_end = int(sys.argv[3])

# Проверка корректности IP-адреса или доменного имени
ip_pattern = re.compile(
    r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"  # IPv4
    r"|"
    r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"  # Доменное имя
)
if not ip_pattern.match(target_ip):
    print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenSPScanner {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Ошибка! Неверный IP-адрес или доменное имя.")
    sys.exit(1)

# Проверка корректности ввода диапазона портов
try:
    port_start = int(port_start)
    port_end = int(port_end)
    if port_start < 0 or port_end > 65535 or port_start > port_end:
        raise ValueError
except ValueError:
    print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenSPScanner {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Ошибка! Недопустимый диапазон портов. Порты должны быть в диапазоне 0-65535.")
    sys.exit(1)

# Создание блокировки для синхронизации вывода
output_lock = threading.Lock()

# Функция для сканирования порта
def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # Установка тайм-аута для ускорения сканирования
        try:
            sock.connect((target_ip, port))
            with output_lock:
                 print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenSPScanner {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTMAGENTA_EX}{target_ip}:{port} {Fore.LIGHTGREEN_EX}(Открыт)")
        except:
            pass

# Функция потока, выполняющая сканирование портов из очереди
def worker_thread():
    while True:
        port = port_queue.get()
        if port is None:
            break
        scan_port(port)
        port_queue.task_done()

# Создание очереди для управления потоками
port_queue = Queue()

# Создание и запуск потоков
threads = []
for _ in range(500):
    thread = threading.Thread(target=worker_thread)
    thread.daemon = True
    thread.start()
    threads.append(thread)

# Добавление диапазона портов в очередь
for port in range(port_start, port_end + 1):
    port_queue.put(port)

# Ожидание завершения всех задач
port_queue.join()

# Остановка потоков
for _ in range(500):
    port_queue.put(None)
for thread in threads:
    thread.join()

print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenSPScanner {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Сканирование завершено.")
