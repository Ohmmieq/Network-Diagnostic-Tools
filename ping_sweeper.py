import os
import platform
import subprocess

def ping_host(ip_address):
    """
    Automates network diagnostic pings across local infrastructure variables.
    Determines OS type to format the diagnostic tracking packets accurately.
    """
    # Determine the operating system command flag
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip_address]
    
    # Execute backend systems process without dumping raw text to user screen
    response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if response == 0:
        print(f"[+] Local Node {ip_address} is ACTIVE / RESPONDING")
    else:
        print(f"[-] Local Node {ip_address} is UNREACHABLE / DOWN")

if __name__ == "__main__":
    print("--- INTJ Systems Automation Engine: Automated Local Subnet Scan ---")
    # Scan local network loop variables from 192.168.1.1 to 192.168.1.10
    base_net = "192.168.1."
    for host in range(1, 11):
        target_ip = f"{base_net}{host}"
        ping_host(target_ip)
