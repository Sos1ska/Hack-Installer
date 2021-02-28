import os
import random
from time import sleep

Red = '\033[91m'
Green = '\033[92m'
Blue = '\033[94m'
Cyan = '\033[96m'
White = '\033[97m'
Yellow = '\033[93m'
Magenta = '\033[95m'
Grey = '\033[90m'
Black = '\033[90m'
Default = '\033[99m'
Underline = '\033[4m'
end       = '\033[0m'

def banner():
    print('''
          /~_________________~\ 
          .-------------------. 
         (| Sos1ska - Hackers |)
          '-------------------' 
          \_~~~~~~~~~~~~~~~~~_/
    ''', '''
          ░██████╗░█████╗░░██████╗░░███╗░░░██████╗██╗░░██╗░█████╗░  ░░░░░░
          ██╔════╝██╔══██╗██╔════╝░████║░░██╔════╝██║░██╔╝██╔══██╗  ░░░░░░
          ╚█████╗░██║░░██║╚█████╗░██╔██║░░╚█████╗░█████═╝░███████║  █████╗
          ░╚═══██╗██║░░██║░╚═══██╗╚═╝██║░░░╚═══██╗██╔═██╗░██╔══██║  ╚════╝
          ██████╔╝╚█████╔╝██████╔╝███████╗██████╔╝██║░╚██╗██║░░██║  ░░░░░░
          ╚═════╝░░╚════╝░╚═════╝░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░░░░░░

          ██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░░██████╗
          ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔════╝
          ███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝╚█████╗░
          ██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗░╚═══██╗
          ██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║██████╔╝
          ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░
    ''')

def  cl():
    os.system("clear")

try:
    cl()
    print(f"S"),sleep(0.5),print(f" O"),sleep(0.5),print(f"  S"),sleep(0.5),print(f"   1"),sleep(0.5),print(f"    S"),sleep(0.5),print(f"     K"),sleep(0.5),print(f"      A"),sleep(2)
    print(random.choice(banner))
    print(f"\t\t\tWelcome\n")
    print(f"\t\t\t {Red}{Underline}Hack-Installer FULL")
    print(f"\t\t\t {Yellow}{Underline} Наши профили ВК {end}{Green}--->{end}{Blue} https://vk.com/nikitasos1ska, https://vk.com/2pac_jdm, https://vk.com/covidone, https://vk.com/paket20{end}")
    print(f"\t\t\t {Yellow}{Underline} Наша почта {end}{Green}--->{end}{Blue} soshack00@gmail.com{end}")
    print(f"\t\t\t {Yellow}{Underline} Наши GitHub профили {end}{Green}--->{end}{Blue} https://github.com/Sos1ska, https://github.com/Ki11sesh, https://github.com/Cool-Hackers{end}"),sleep(2)

    start_input = input(f"{Yellow}Начать установку? {end}[{Green}y{end}/{Red}n{end}]: ")

    if str(start_input) == "n":
        cl()
        print(f"Код остановил свою работу")
        print(f"\t\t\t {Yellow}{Underline} Наши профили ВК {end}{Green}--->{end}{Blue} https://vk.com/nikitasos1ska, https://vk.com/2pac_jdm, https://vk.com/covidone, https://vk.com/paket20{end}")
        print(f"\t\t\t {Yellow}{Underline} Наша почта {end}{Green}--->{end}{Blue} soshack00@gmail.com{end}")
        print(f"\t\t\t {Yellow}{Underline} Наши GitHub профили {end}{Green}--->{end}{Blue} https://github.com/Sos1ska, https://github.com/Ki11sesh, https://github.com/Cool-Hackers{end}"),sleep(2)
        quit()
    if str(start_input) == "y":
        cl()
        print("Начинаю установку компонентов")
        sleep(2)
        mod = ("update", "upgrade")
        for i in range(len(mod)):
            print("Проверка...")
            os.system("apt "+mod[i])
            cl()
        cl()
        print("Проверка завершена !")
        sleep(2)
        cl()
        print("Обновление pip")
        sleep(2)
        os.system("pip install --upgrade pip")
        cl()
        print("Обновление pip завершена !")
        sleep(2)
        cl()
        print("Начинается установка через pip")
        mod = ("html2tetx", "requests", "bs4", "vk_api", "urllib3")
        for i in range(len(mod)):
            print(f"Установка "+mod[i]+"...")
            os.system("pip install "+mod[i])
            cl()
        cl()
        print("Установка через pip завершена !")
        sleep(2)
        cl()
        print("Начинаю установку нужных пакетов")
        os.system("pkg install git -y")
        cl()
        os.system("pkg install tor -y")
        cl()
        os.system("pkg install root-repo -y")
        cl()
        os.system("pkg install unstable-repo -y")
        cl()
        os.system("pkg install x11-repo -y")
        cl()
        os.system("pkg install php")
        cl()
        os.system("pkg install cowsay -y")
        cl()
        os.system("pkg install toilet -y")
        cl()
        os.system("pkg install msfconsole -y")
        cl()
        os.system("pkg install dos2unix -y")
        cl()
        cont_input = input(Yellow + "Начать установку через git? [Enter для продолжения]")
        os.system("cd ~/")
        os.system("git clone https://github.com/Sos1ska/IP-System")
        cl()
        os.system("git clone https://github.com/SenTDI/Infinite-Bomber-android")
        cl()
        cont_input_1 = input(Yellow + "От кого хотите начать установку [Sos1ska/Coo-Hackers]: ")
        if str(cont_input_1) == "Sos1ska":
            cl()
            os.system("git clone https://github.com/Sos1ska/Spider-Breaking")
            cl()
            os.system("git clone https://github.com/Sos1ska/Number-System")
            cl()
            os.system("git clone https://github.com/Sos1ska/Sms-BomberSos1.0")
            cl()
        if str(cont_input_1) == "Cool-Hackers":
            cl()
            os.system("git clone https://github.com/Cool-Hackers/Number-System")
            cl()
            cont_input_2 = input(Yellow + "Какую вам версию пробива? [1.0/2.0]: ")
            if str(cont_input_2) == "1.0":
                cl()
                os.system("git clone https://github.com/Cool-Hackers/Spider-Breaking1.0")
                cl()
            if str(cont_input_2) == "2.0":
                cl()
                os.system("git clone https://github.com/Cool-Hackers/Spider-Breaking2.0")
                cl()
        os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
        cl()
        os.system("git clone https://github.com/tchelospy/termux-ngrok.git")
        cl()
        os.system("git clone https://github.com/artem-cell/wifi-dosser")
        cl()
        os.system("git clone https://github.com/DataSC3/No-BlackM")
        cl()
        os.system("git clone https://github.com/websploit/websploit.git")
        cl()
        os.system("git clone https://github.com/Hydra7/Planetwork-DDOS")
        cl()
        os.system("git clone https://github.com/evait-security/weeman")
        cl()
        cont_input_3 = input(f"{Yellow}Помочь настроить? {end}[{Green}y{end}/{Red}n{end}]")
        if str(cont_input_3) == "n":
            cl()
            cont_input_3_1 = input(f"{Yellow}Огласить ли список чего было установлено? {end}[{Green}y{end}/{Red}n{end}]")
            if str(cont_input_3_1) == "n":
                cl()
                print(f"\t\t\t {Yellow}{Underline} Наши профили ВК {end}{Green}--->{end}{Blue} https://vk.com/nikitasos1ska, https://vk.com/2pac_jdm, https://vk.com/covidone, https://vk.com/paket20{end}")
                print(f"\t\t\t {Yellow}{Underline} Наша почта {end}{Green}--->{end}{Blue} soshack00@gmail.com{end}")
                print(f"\t\t\t {Yellow}{Underline} Наши GitHub профили {end}{Green}--->{end}{Blue} https://github.com/Sos1ska, https://github.com/Ki11sesh, https://github.com/Cool-Hackers{end}")
                quit()
            if str(cont_input_3_1) == "y":
                cl()
                print(f"Установлено: \n git\n tor\n root-repo\n unstable-repo\n x11-repo\n php\n cowsay\n toilet\n msfconsole\n")
                print(f"\t\t\t {Yellow}{Underline} Наши профили ВК {end}{Green}--->{end}{Blue} https://vk.com/nikitasos1ska, https://vk.com/2pac_jdm, https://vk.com/covidone, https://vk.com/paket20{end}")
                print(f"\t\t\t {Yellow}{Underline} Наша почта {end}{Green}--->{end}{Blue} soshack00@gmail.com{end}")
                print(f"\t\t\t {Yellow}{Underline} Наши GitHub профили {end}{Green}--->{end}{Blue} https://github.com/Sos1ska, https://github.com/Ki11sesh, https://github.com/Cool-Hackers{end}")
                quit()
        if str(cont_input_3) == "y":
            os.system("cd ~/Infinite-Bomber-android/Infinite-Bomber-arm")
            os.system("chmod 777 infinite-bomber")
            os.system("cd ~/Infinite-Bomber-android/Infinite-Bomber-arm-without-tor")
            os.system("chmod 777 infinite-bomber")
            os.system("cd ~/Infinite-Bomber-android/Infinite-Bomber-arm64")
            os.system("chmod 777 infinite-bomber")
            os.system("cd ~/Infinite-Bomber-android/Infinite-Bomber-arm64-without-tor")
            os.system("chmod 777 infinite-bomber")
            os.system("cd ~/Infinite-Bomber-android/Infinite-Bomber-x64")
            os.system("chmod 777 infinite-bomber")
            os.system("cd ~/Infinite-Bomber-android/Infinite-Bomber-x64-without-tor")
            os.system("chmod 777 infinite-bomber")
            os.system("cd ~/Infinite-Bomber-android/Infinite-Bomber-x86")
            os.system("chmod 777 infinite-bomber")
            os.system("cd ~/Infinite-Bomber-android/Infinite-Bomber-x86-without-tor")
            os.system("chmod 777 infinite-bomber")
            os.system("cd ~/IPGeoLocation && chmod 777 ipgeolocation.py")
            os.system("cd ~/IPGeoLocation && pip3 install -r requirements.txt")
            cl()
            os.system("cd ~/RED_HAWK && chmod 777 rhawk.php")
            os.system("cd ~/termux-ngrok && chmod +x termux-ngrok.sh")
            os.system("cd ~/websploit && python setup.py")
            cl()
            os.system("cd ~/wifi-dosser && bash installer.sh")
            cl()
            os.system("cd ~/Number-System && bash install.sh")
            os.system("cd ~/Spider-Breaking/Spider-Breaking2.0/Unix && chmod 777 ")
            cl()
            os.system("cowsay -f dragon 'Made Script By user: https://vk.com/nikitasos1ska' ")

            print(f"\t\t\tКод написан им ---> https://vk.com/nikitasos1ska")
            print(f"\t\t\tТе кто присоединён к Cool-Hackers ---> https://vk.com/nikitasos1ska, https://vk.com/paket20, https://vk.com/covidone, https://vk.com/2pac_jdm")
            print(f"\t\t\tНаши Git профили --> https://github.com/Sos1ska, https://github.com/Ki11sesh, https://github.com/Cool-Hackers")
except KeyboardInterrupt:
    cl()
    print(f"\t\t\tКод остановил свою работу")

    print(f"\t\t\t {Yellow}{Underline} Наши профили ВК {end}{Green}--->{end}{Blue} https://vk.com/nikitasos1ska, https://vk.com/2pac_jdm, https://vk.com/covidone, https://vk.com/paket20{end}")
    print(f"\t\t\t {Yellow}{Underline} Наша почта {end}{Green}--->{end}{Blue} soshack00@gmail.com{end}")
    print(f"\t\t\t {Yellow}{Underline} Наши GitHub профили {end}{Green}--->{end}{Blue} https://github.com/Sos1ska, https://github.com/Ki11sesh, https://github.com/Cool-Hackers{end}"),sleep(2)

    print("Вы прожали CTRL+C")
    quit()