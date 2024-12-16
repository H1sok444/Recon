#!/usr/bin/python3

import socket
import subprocess
import platform

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

ascii_art = """

                        𝘞𝘦𝘭𝘤𝘰𝘮𝘦! 𝘴𝘤𝘢𝘯𝘯𝘦𝘳, ʜᴏᴘᴇ ʏᴏᴜ ɢᴏᴛ ɢᴏᴏᴅ ɪɴᴛᴇɴᴛɪᴏɴs :)

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡠⣐⠂⠀⠀⠀⠐⠋⠀⠤⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠘⣜⢫⠙⡑⣵⡴⢞⠘⡘⢊⠳⣠⣁⢠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⡁⡚⢑⠄⠠⠨⢜⡂⢑⢐⡊⢡⠐⡃⡚⡁⣊⠖⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⠼⡕⠀⠄⠀⠘⠂⠈⠁⠠⠤⠀⠐⠈⡕⠔⠡⢨⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢆⠎⢈⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠸⡞⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠊⠁⣤⢈⠀⠠⢄⠀⠀⢀⣀⡀⠀⠀⢀⠄⠀⡐⠉⠀⡉⠀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡀⡘⠀⠃⠀⠘⠃⠤⢟⣿⢣⣄⠣⡸⠼⠣⢧⢣⣀⠃⢀⣼⣃⡣⠀⠀⠠⠘⠠⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡠⠈⠀⣦⡣⠟⠋⠋⠐⠲⡐⢏⢻⡼⡳⢌⣶⣹⡶⢥⡱⣾⠟⢥⢢⠔⠚⠁⠐⠩⠓⢄⠈⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠌⣠⡟⠠⠁⡠⠂⠀⠀⡁⠂⠄⠡⡁⢳⢛⣯⠚⠛⣿⣮⣿⠏⣜⠎⠀⢐⡈⠉⠁⠂⠀⠡⠁⠀⠈⢄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⢊⡜⠧⠀⠃⠐⠀⢀⡂⠀⠃⠢⡈⠂⢀⣈⡟⠃⠀⠀⠘⣣⢕⡬⡎⠐⢁⣭⠀⠀⠈⣗⡈⡄⠂⠀⣧⠀⠢⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠐⠁⠈⠈⠃⠀⠆⢠⠀⠨⠡⡀⠀⡁⡀⡀⠸⠫⠈⢀⠀⠀⠀⠣⡳⠻⢀⢁⠀⡴⠱⠂⠠⢾⠀⡀⠎⠠⠁⡆⠀⠑⡀⠀⠀⠀⠀⠀
⡀⢐⠰⣂⡀⠀⠀⠀⠈⠄⠢⢈⠈⠨⠊⡈⠄⡠⡢⠀⠠⡈⣀⠀⣀⠱⠀⡀⠒⢆⠢⢂⠀⠀⢂⠡⢈⢔⡄⠘⠨⢠⠢⡀⠈⠢⡀⠀⢀⠀
⠨⡀⠭⣐⣷⡀⠀⢀⡂⢀⠇⠐⡨⠭⢡⠂⡨⠚⠌⠀⠀⠀⠀⠉⠈⠀⠀⠊⡀⢁⢅⢂⠤⢤⠀⠢⣡⠈⡨⢦⠐⠑⠀⡈⡣⠀⠈⢠⠂⠃
⠀⠑⠄⠀⠁⠀⣠⠕⠂⠁⠑⠀⠀⠀⠀⡤⣚⠁⠤⠀⠤⠶⠻⠴⠻⠳⠒⠂⠀⢂⡂⡈⠀⠀⠑⠀⡁⠘⠔⠔⠅⠀⠈⠀⠀⠀⠀⠑⠐⡄
⠀⠀⠈⢂⠐⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠈⣤⠐⢐⠕⠀⠀⠐⠒⠂⠀⠀⠀⠀⠀⡔⢀⠀⠀⠀⠀⠀⠈⠀⠀⠐⡄⡀⢐⢐⠄⠀⡂⠘⠀
⠀⠀⠀⠈⡀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠔⠁⡇⡴⡦⡀⠀⠈⠀⠀⠀⢄⡠⠆⣠⠪⠀⠀⠐⢀⡀⠀⠀⠀⠀⠀⠀⠈⢒⠀⠀⠂⠁⠀⠀⠀
⠀⠀⠀⠐⠀⠀⡁⠄⠀⠀⠒⡠⡊⡂⡂⠀⠇⠘⢩⣒⢂⠤⢄⠴⡥⠝⠞⡉⡦⠃⢰⠀⠀⠀⠐⠄⠀⠀⠈⠉⠈⠉⠁⠑⠀⠀⠀⠀⠀⠀
⠀⠐⠁⠀⠀⠀⠀⠀⠀⠀⠈⠀⠂⢂⠌⠄⠰⡀⢦⡈⠲⡉⢠⡑⠔⠈⡡⠋⠄⠆⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠁⠀⠀⠀⠃⠐⠉⡄⠀⢡⠀⠀⢣⠀⢡⢨⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠕⠑⠅⠀⢸⠈⢬⢀⠔⠁⠀⠀⠀⠈⠂⡐⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠆⠂⠢⠂⠀⠐⡆⠠⠂⠈⠠⡀⠀⡠⢊⠐⠈⡢⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠃⡑⡀⠀⠀⠄⠡⡈⠊⠀⠀⠀⠀⢆⠅⢄⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠄⠀⠀⠬⠨⢈⠂⢰⠀⠀⠀⠈⡀⡡⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠊⠀⠀⠐⢑⠀⠀⡌⠀⠀⠀⠀⢡⠐⡢⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⢢⠊⠀⠀⠀⠀⠀⠀⠈⡄⠛⠨⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
~𝑯𝟏𝒔𝒐𝒌𝟒~

"""
print(ascii_art)
host = input("Please enter the IP you want to scan: ")

#Ping process
def ping_host(host):
    # Determine the ping command based on the OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]

    # Execute the ping command and hide the output
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

if ping_host(host):
    print(f"Good! {host} is reachable.")
else:
    print(f":( {host} is unreachable.")
    continue_choice = input("Would you like to continue (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print("Exiting the program...")
        exit()

choice = input("Would you like to scan known ports (yes/no): ").strip().lower()

topPorts = [21, 22, 25, 67, 80, 110, 123, 443, 3306, 3389, 8080]

#Single port scan
def portScanner(port):
    if s.connect_ex((host, port)):
        print(f"Port {port} is closed.")
    else:
        print(f"Port {port} is open.")

#Multi port scan
def topScanner(ports):
    for port in ports:
        portScanner(port)

if choice == 'yes':
    topScanner(topPorts)
else: 
    port = int(input("Please enter the port you want to scan: "))
    portScanner(port)