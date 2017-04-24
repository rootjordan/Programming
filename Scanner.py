import subprocess
import sys
import os
import threading

"""
Created By: Jordan
Usage: python [file name]
Purpose:
Scans an ip that the user entered with nmap and nikto
Requirements: Nmap installed, Nikto installed, Linux
"""

print "Thank you for using this program\n"

class colors:
    RED = '\033[93m'
    WHITE = '\033[0m'
    GREEN = '\033[92m'


def Nmap_scan():
    print colors.RED + "Nmap scan starting[\n"+ IP + "]" + colors.WHITE
    subprocess.Popen("nmap -p- " +IP+ " > Desktop/Scanning/nmap.txt", shell=True)
def Nikto_scan():
    print colors.RED + "Nikto scan starting on [\n" + IP + "]" +colors.WHITE
    subprocess.Popen("nikto -h " +IP+ "> Desktop/Scanning/nikto.txt", shell=True)

def main():
    if len(sys.argv) > 1:
        print colors.RED + "Usage: python [file name]" + colors.WHITE
        sys.exit()
    IP = raw_input("Enter the IP> ")
    print colors.GREEN + "Scanning IP Address: " +IP+ colors.WHITE
    Directory = "Desktop/Scanning"
    os.mkdir(Directory)
    try:
        os.mkdir(Directory)
    except OSError:
        if not os.path.isdir(Directory):
            raise

main()

#Our threading
T1 = threading.Thread(target = Nmap_scan)
T2 = threading.Thread(target = Nikto_scan)
T1.start()
T2.start()
T1.join()
T2.join()
