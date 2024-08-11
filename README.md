# GenSPScanner
is a simple and efficient port scanner that quickly identifies open ports on a target IP or domain

# EN
## Overview
**GenSPScanner** is a simple and efficient port scanning tool. It allows users to scan a range of ports on a specified target IP address or domain, identifying open ports and potential vulnerabilities.

## Features
- **Multithreaded Scanning**: Utilizes multiple threads to accelerate the scanning process.
- **Color-Coded Output**: Provides color-coded output for better readability.
- **Error Handling**: Includes checks for valid IP addresses, domain names, and port ranges.

## Requirements
- Python 3.x
- `colorama` package (for colored output in the terminal)

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/geniuszlyy/GenSPScanner.git
   ```
2. **Install dependencies**:
   ```bash
   pip install colorama
   ```

## Usage
To use GenSPScanner, execute the script with the following command:
```bash
python GenSPScanner.py [target] [start_port] [end_port]
```
- **target**: The IP address or domain name to scan.
- **start_port**: The starting port number in the range.
- **end_port**: The ending port number in the range.

![image](https://github.com/user-attachments/assets/70d24f99-3a73-4c5f-a492-32e600200363)


## Example
```bash
python GenSPScanner.py 192.168.1.1 1 65535
```
This command scans ports 1 to 65535 on the IP address `192.168.1.1`.

![image](https://github.com/user-attachments/assets/652b1926-046b-46ff-9ae9-ba32e5528e45)


## Output
- Open ports are displayed in a color-coded format indicating successful connections.
- Errors such as invalid IP addresses, domain names, or port ranges are highlighted with specific messages.

# RU
## Обзор
**GenSPScanner** - это простой и эффективный инструмент для сканирования портов. Он позволяет пользователям сканировать диапазон портов на указанном целевом IP-адресе или домене, выявляя открытые порты и потенциальные уязвимости.

## Особенности
- **Многопоточное сканирование**: Использует несколько потоков для ускорения процесса сканирования.
- **Цветной вывод**: Обеспечивает цветное отображение для лучшей читаемости.
- **Обработка ошибок**: Включает проверки на допустимость IP-адресов, доменных имен и диапазонов портов.

## Требования
- Python 3.x
- Пакет `colorama` (для цветного вывода в терминале)

## Установка
1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/geniuszlyy/GenSPScanner.git
   ```
2. **Установите зависимости**:
   ```bash
   pip install colorama
   ```

## Использование
Для использования GenSPScanner выполните скрипт с помощью следующей команды:
```bash
python GenSPScanner.py [target] [start_port] [end_port]
```
- **target**: IP-адрес или доменное имя для сканирования.
- **start_port**: Начальный номер порта в диапазоне.
- **end_port**: Конечный номер порта в диапазоне.

![image](https://github.com/user-attachments/assets/3599ae8c-dc93-4aad-b4c7-e90adb8bc0d0)


## Пример
```bash
python GenSPScanner.py 192.168.1.1 1 65535
```
Эта команда сканирует порты с 1 по 65535 на IP-адресе `192.168.1.1`.

![image](https://github.com/user-attachments/assets/1c9c05ac-dc7b-4f1e-9658-ddccc08e1989)


## Вывод
- Открытые порты отображаются в цветном формате, указывающем на успешные подключения.
- Ошибки, такие как недопустимые IP-адреса, доменные имена или диапазоны портов, выделяются специальными сообщениями.
