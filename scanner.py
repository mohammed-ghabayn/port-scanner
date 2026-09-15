import socket

from concurrent.futures import ThreadPoolExecutor

import datetime

BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

banner = f"""
{CYAN}
   ___            _     ___                                   
  / _ \___  _ _ _| |_  / __| __ __ _ _ _  _ _  ___ _ _        
 | ___/ _ \|'_||_   _| \__ \/ _| _` | ' \| ' \/ -_) '_|       
 |_|  \___/|_|   |_|   |___/\__|\__,_|_||_|_||_\___|_|        
                                                            
{RESET}
{BLUE}==============================================================={RESET}
{BOLD}{GREEN}[+] Port Scanner v1.0 | Network Reconnaissance Tool{RESET}
{YELLOW}[*] Started at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}
{BLUE}==============================================================={RESET}
"""

print(banner)

#  قاموس الخدمات 
SERVICES = {
    20: "FTP-Data", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 67: "DHCP Server", 68: "DHCP Client", 80: "HTTP",
    110: "POP3", 143: "IMAP", 443: "HTTPS", 445: "SMB", 3306: "MySQL",
    3389: "RDP", 8080: "HTTP-Proxy" }




def scanPort(ip,port):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      try:
        s.settimeout(0.3)
        result = s.connect_ex((ip,port))  #اخترنا  connect_ex  لانها ترجع 0 عند نجاح الاتصال وهاذا يوفر من موارد الجهاز 
        if result == 0:
           serviceName = SERVICES.get(port ,"UnKnow Service")
           print(f"Port {port:<5} is Open >> {serviceName}") 
           print("---------------------------------------------------------------")
         
      except:
       pass 
      finally:
        s.close()
       





binary = True

while binary:

    targetInput = input("Enter Target IP or Domain:").strip()

    target = targetInput.replace("http://","").replace("https://","").split("/")[0] # نقصقص الرابظ من خلال السلاش ثم نأخذ القصاصة الاولى

   # مثلا 
   #"scanme.nmap.org/test/page"
   #بتصير ["scanme.nmap.org", "test", "page"]
   # واهم شي نحذف ال  http://  او ال  https://
    try:
       ip= socket.gethostbyname(target)
       binary = False
    except socket.gaierror:
       print(f"[!] Unable to resolve hostname {target}")   
       print("\n--------------------------------------------------------------\n")



print("\n---------------------------------------------------------------\n")

print(f"{YELLOW}[*] Scanning started... Press 'Ctrl + C' to stop at any time.{RESET}")



# صندوق الخيوط التي  ستعمل معا في الدالة الفحص
with ThreadPoolExecutor(max_workers=100) as executor:
   for port in range(1,1024):
    executor.submit(scanPort,ip,port)

print(f"{GREEN}[+] Scan completed successfully.{RESET}")   
exit()

   