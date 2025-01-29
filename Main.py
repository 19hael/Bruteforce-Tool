import os
import time
import random
import requests
import colorama
from colorama import Fore
import psutil
import scrapy
from datetime import datetime
from itertools import cycle

colorama.init()
CARPETA_LICENCIAS = "https://drive.google.com/drive/folders/1NVJIcM9ynjfhPOsqfVsMo6kG6AR2UK-w"
CARPETA_REGISTROS = "https://drive.google.com/drive/folders/1NVJIcM9ynjfhPOsqfVsMo6kG6AR2UK-w"
ARCHIVO_PASSWORDS = "passwords.txt"

class ProxyScraper(scrapy.Spider):
    name = "proxy_scraper"
    start_urls = ["https://www.sslproxies.org/"]

    def parse(self, response):
        proxies = response.xpath('//tbody/tr')[:20]  
        return [f"http://{p.xpath('td[1]/text()').get()}:{p.xpath('td[2]/text()').get()}" for p in proxies]

def obtener_proxies():
    process = ProxyScraper()
    return process.parse(requests.get(process.start_urls[0]))

PROXIES = cycle(obtener_proxies())

INSTAGRAM = "@rhaelxyz"
TWITTER = "HaelXyz"
EMAIL = "hael7legion@proton.me"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_banner():
    clear()
    print(Fore.RED + "=" * 40)
    print("        HAEL TOOLKIT BRUTEFORCE")
    print("        [⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠤⠔⠒⠒⠦⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣤⣤⡄⠀⠀⠀⠀⠀⣸⠁⠀⠀⣀⠀⠀⠀⠀⠀⠀⣀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣏⣀⣤⣾⡄⠀⠀⠀⢠⡇⡰⠲⣯⣀⣀⡀⠀⠀⣀⣀⣤⠷⠲⡀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢹⠯⣤⣞⣳⡀⠀⠀⢸⠀⣇⠀⠀⠀⠉⠉⢉⠉⢉⡉⠀⠀⠀⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢷⠧⣴⣏⣇⠀⠀⢸⠀⢹⠒⣦⣤⣄⣀⣥⣖⣉⣤⣤⠔⢺⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⡟⢠⡴⣿⡆⠀⢸⠀⢸⡀⠙⢭⣽⣾⣀⣼⣿⣭⠝⠁⣸⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢱⡛⣲⠯⣽⡄⢸⠀⠏⢱⠴⠊⠁⠀⠀⠀⠈⠉⠲⣴⠙⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢳⣳⣞⣷⣷⣸⡇⣞⠁⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢹⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣈⠿⣟⣫⢭⡟⠣⠸⣦⠀⠀⠀⠈⠉⠉⠀⠀⠀⢀⣾⢠⠛⣦⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣴⠿⢤⣼⡃⠀⠈⢧⠀⠀⠳⡱⣄⠀⠀⠀⢀⣿⣿⣤⣿⠃⠀⢠⠇⠀⠀⡿⠤⠤⣤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⢘⣿⠶⣄⠀⣿⣇⠀⠀⠀⠳⣀⠀⠈⠙⠓⠦⢤⣿⡟⣻⠟⠁⢀⡠⠃⠀⠀⣰⠃⠀⢀⠾⢿⣻⠀⠀⠀⠀⠀⠀
⠀⢀⡾⠁⠀⠈⢧⣼⡟⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⠁⠙⡇⠀⠈⠀⠀⠀⣰⠃⠀⢠⡏⠀⠀⠹⡆⠀⠀⠀⠀⠀
⠀⢸⡇⠀⠀⠀⠈⣧⢣⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⡸⡞⠀⠛⣇⣀⠀⠀⠀⡴⠃⠀⠀⡞⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀
⢀⡟⢧⠀⠀⣀⠤⠾⡈⢆⠈⠙⢦⣀⠀⠀⠀⠀⢰⣧⣤⡦⠶⠧⠼⢤⣠⠞⠁⠀⠀⢸⠧⣄⡀⠀⠀⢸⠹⡄⠀⠀⠀
⣼⠀⠘⡆⠊⡀⠀⠀⠙⣌⢢⡀⠀⠈⠙⢶⣒⡶⠋⠙⡌⢧⠀⠀⠀⠚⠳⡄⠀⠀⠀⣾⠎⠀⠙⠀⠀⠀⢧⢹⡀⠀⠀
⡏⠀⠀⠀⡰⠀⠀⠀⠀⢸⣄⢑⣄⠀⢀⡠⢿⡱⡀⠀⡽⣸⣄⣷⠴⡄⢰⡇⠀⠀⢠⠃⠀⠀⠀⢰⠀⠀⠀⠉⢧⠀⠀
⣧⢠⠀⠀⣇⣠⣤⠖⠋⠉⠁⠀⠀⠀⠀⠀⠈⢧⠑⣴⠃⡿⠤⡽⠒⠒⠋⠀⠀⠀⣾⠀⠀⠀⠀⠈⡆⠀⠀⠘⣼⡀⠀
⢹⢸⠀⢀⣽⡇⢸⠀⠀⠀⠀⠀⠀⠀⢀⡠⠂⠀⠳⣌⣾⡦⣞⠁⠀⠀⠀⠀⠀⠀⢻⠀⠀⢀⣴⡚⠳⣄⠀⠀⠘⡇⠀
⠀⢻⡇⠸⠁⢧⠀⢇⠀⠀⣀⡠⠴⠚⠉⠀⠀⠀⢠⠟⠉⠀⠀⠙⢦⡀⠀⠀⠀⢀⡸⠗⠉⠀⠀⠱⡀⠹⡉⠳⠄⢸⠀
⠀⠈⡇⠀⠀⠈⢧⡈⢦⠀⠀⠀⠀⠀⠀⠀⢀⡴⢛⣟⡭⠿⠿⠿⢿⡿⡿⠖⠒⠉⠀⠀⠀⠀⠀⠀⢣⠀⡇⠀⠀⠘⡇
⠀⠀⣷⠀⠀⠀⠈⠳⣄⠑⢄⡀⠀⣀⠤⢺⠿⢂⣎⡏⠀⠀⠀⠀⠀⢹⣽⡄⠀⣀⣀⣀⠀⣀⣀⡀⠸⠀⠀⠀⠀⢠⠇
⠀⠀⠘⠷⣄⣀⣀⣀⣉⣷⠤⠽⠋⠁⢠⡧⠔⣻⡏⣇⠀⠀⠀⠀⠀⠀⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⢀⡴⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡤⠚⠁⣴⣜⠦⣤⣤⣤⣤⣴⣧⢇⣀⡀⠀⠀⠀⢀⣀⣀⣼⣀⠟⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠢⠤⠤⠛⠉⠉⠉⠉⠉⠁⠁⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠀⠖⠒⠒⠒⠀⠀⠀⠀⠠⣀⠀⢀⠀⡀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀]")
    print("=" * 40)
    print("\n× Instagram:", INSTAGRAM: @RhaelXyz)
    print("× Twitter:", TWITTER: @HaelXyz)
    print("× Email:", EMAIL: hael7legion@proton.me)
    print("\n" + "=" * 40 + "\n")

def verificar_licencia():
    print(Fore.RED + "× Introducir nombre del archivo de licencia ×")
    archivo_licencia = input(Fore.RED + "→ ").strip()
    ruta_licencia = os.path.join(CARPETA_LICENCIAS, archivo_licencia)

    if not os.path.exists(ruta_licencia):
        print(Fore.RED + "\nLicencia no encontrada!\n")
        return False

    with open(ruta_licencia, "r") as f:
        licencia = f.read().strip()

    if licencia.startswith("HAEL-"):
        print(Fore.GREEN + "\nLicencia válida. Accediendo...\n")
        time.sleep(2)
        registrar_uso(licencia)
        return True
    else:
        print(Fore.RED + "\nLicencia no reconocida!")
        print(f"Necesitas una licencia? Escribeme: {INSTAGRAM}\n")
        return False

def registrar_uso(licencia):
    if not os.path.exists(CARPETA_REGISTROS):
        os.makedirs(CARPETA_REGISTROS)

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_local = requests.get("https://api64.ipify.org").text
    cpu_info = psutil.cpu_percent(interval=1)
    ram_info = psutil.virtual_memory().percent

    log = f"{fecha} | Licencia: {licencia} | IP: {ip_local} | CPU: {cpu_info}% | RAM: {ram_info}%\n"

    with open(os.path.join(CARPETA_REGISTROS, "usos.log"), "a") as f:
        f.write(log)

def seleccionar_red():
    print(Fore.RED + "× Seleccionar Social Media ×")
    print(Fore.RED + "[1] Twitter (X)")
    print(Fore.RED + "[2] Instagram")
    print(Fore.RED + "[3] Facebook")
    
    opcion = input(Fore.RED + "→ ").strip()
    if opcion not in ["1", "2", "3"]:
        print(Fore.RED + "\nSelección inválida.\n")
        return seleccionar_red()
    
    return opcion

def obtener_user_id():
    print(Fore.RED + "\n× Ingresar link del perfil ×")
    link = input(Fore.RED + "→ ").strip()
    user_id = "12345678"
    print(Fore.GREEN + f"\nUser ID obtenido: {user_id}\n")
    return user_id

def cambiar_proxy():
    proxy = next(PROXIES)
    print(Fore.RED + f"\nUsando proxy: {proxy}\n")
    return {"http": proxy, "https": proxy}

def cargar_diccionario():
    if not os.path.exists(ARCHIVO_PASSWORDS):
        print(Fore.RED + "\nNo se encontró el archivo de contraseñas.\n")
        return []

    with open(ARCHIVO_PASSWORDS, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def ataque_bruteforce(user_id):
    contraseñas = cargar_diccionario()
    
    if not contraseñas:
        print(Fore.RED + "\nNo hay contraseñas en el diccionario.\n")
        return

    print(Fore.RED + f"\nIniciando ataque contra {user_id}...\n")
    
    for i, password in enumerate(contraseñas):
        proxy = cambiar_proxy()
        print(Fore.RED + f"Probando {i+1}/{len(contraseñas)} → {password}")

        time.sleep(random.uniform(1, 3))  

        if password == "password_correcta":  
            print(Fore.GREEN + f"\nUser: {user_id}")
            print(Fore.GREEN + f"Contraseña: {password}\n")
            registrar_exito(user_id, password)
            return
    
    print(Fore.RED + "\nFallo 443 | Ataque no autorizado.\n")

def registrar_exito(user_id, password):
    with open(os.path.join(CARPETA_REGISTROS, "exitos.log"), "a") as f:
        f.write(f"User: {user_id} | Password: {password}\n")

def iniciar_ataque():
    print(Fore.RED + "\n× Iniciar ataque? [Y/N] ×")
    confirmacion = input(Fore.RED + "→ ").strip().lower()

    if confirmacion == "y":
        user_id = obtener_user_id()
        ataque_bruteforce(user_id)
    else:
        print(Fore.RED + "\nAtaque cancelado.\n")

def main():
    mostrar_banner()
    if not verificar_licencia():
        return
    
    seleccionar_red()
    iniciar_ataque()

if __name__ == "__main__":
    main()
