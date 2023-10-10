import subprocess

print("""
███╗   ██╗███╗   ███╗ █████╗ ██████╗   ██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗
████╗  ██║████╗ ████║██╔══██╗██╔══██╗  ██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║
██╔██╗ ██║██╔████╔██║███████║██████╔╝  ██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝   ╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║        ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝         ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝                                                                           
""")

print("""__   __ __ _        _ _            ___  _       _           
\ \ / // _(_)     (_) |           / _ \| |     | |          
 \ V /| |_ _ _ __  _| |_ _   _   / /_\ \ |_ __ | |__   __ _ 
 /   \|  _| | '_ \| | __| | | |  |  _  | | '_ \| '_ \ / _` |
/ /^\ \ | | | | | | | |_| |_| |  | | | | | |_) | | | | (_| |
\/   \/_| |_|_| |_|_|\__|\__, |  \_| |_/_| .__/|_| |_|\__,_|
                          __/ |          | |                 
                         |___/           |_|                 
""")

import subprocess

def basic_scan():
    print("Basic Scan Options:")
    print("1. TCP Connect Scans (-sT)")
    print("2. SYN 'Half-open' Scans (-sS)")
    print("3. UDP Scans (-sU)")
    print("4. TCP Null Scans (-sN)")
    print("5. TCP FIN Scans (-sF)")
    print("6. TCP Xmas Scans (-sX)")
    print("7. Aggressive Scanning (-A)")

    scan_choice = input("Enter the number corresponding to the basic scan type: ")

    if scan_choice == "1":
        scan = "-sT"
        return scan
    elif scan_choice == "2":
        scan = "-sS"
        return scan
    elif scan_choice == "3":
        scan = "-sU"
        return scan
    elif scan_choice == "4":
        scan = "-sN"
        return scan
    elif scan_choice == "5":
        scan = "-sF"
        return scan
    elif scan_choice == "6":
        scan = "-sX"
        return scan
    elif scan_choice == "7":
        scan = "-A"
        return scan
    else:
        print("Invalid scan type selected.")

def advanced_preloaded_scan():
    print("Advanced Preloaded Scan Options:")
    print("1. Intense scan (-T4 -A -v)")
    print("2. Intense scan plus UDP (-sS -sU -T4 -A -v)")
    print("3. Intense scan, no ping (-T4 -A -v -Pn)")
    print("4. Quick scan (-T4 -F)")
    print("5. Quick scan plus (-sV -T4 -O -F --version-light)")
    print("6. Quick traceroute (-sn --traceroute)")

    scan_choice = input("Enter the number corresponding to the advanced preloaded scan type: ")

    if scan_choice == "1":
        scan = "-T4 -A -v"
        return scan
    elif scan_choice == "2":
        scan = "-sS -sU -T4 -A -v"
        return scan
    elif scan_choice == "3":
        scan = "-T4 -A -v -Pn"
        return scan
    elif scan_choice == "4":
        scan = "-T4 -F"
        return scan
    elif scan_choice == "5":
        scan = "-sV -T4 -O -F --version-light"
        return scan
    elif scan_choice == "6":
        scan = "-sn --traceroute"
        return scan
    else:
        print("Invalid scan type selected.")


def manual_scan():
    try:
        scan=input("Enter Scan type/s Manually :")
    except:
        print("Error occurred")
    return scan
    

def func():
    target = input("Enter HostName or IP of the TARGET: ")
    port = "-p"
    port_num = input("Enter port Number or range: ")

    print("Select the type of scan:")
    print("1. Basic Scan")
    print("2. Advanced Preloaded Scan")
    print("3. Manual Scan")

    scan_option = input("Enter the scan option (1/2/3): ")
    if scan_option == '1':
        scan = basic_scan()
    elif scan_option == '2':
        scan = advanced_preloaded_scan()
    elif scan_option == '3':    
        scan = manual_scan()
    else:
        print("Invalid scan option. Using SYN scan by default.")
        scan = "-sS"
    
    try:
        p1 = subprocess.run(["nmap", scan, port, port_num, target], shell=True, capture_output=True, text=True)

        if p1.returncode == 0:
            print("Nmap scan successful!")
            print("Scan results:")
            print(p1.stdout)
        else:
            print("Nmap scan failed. Error output:")
            print(p1.stderr)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

func()
