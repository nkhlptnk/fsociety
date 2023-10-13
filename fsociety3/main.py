import os
import sys
import hashlib
import time
import subprocess
from scripts import distro,requirements,nmap,android

def run():
    print("1. Install Dependencies")
    print("2. Nmap")
    print("3. SQLMap")
    print("4. HashBash")
    print("5. Android tools")
    print("9. Go Back To Main Menu")
    choice = int(input("fsociety# "))
    if choice == 1:
        dist = distro.get_distro()
        requirements.install_requirements(distro)
    elif choice == 2:
        options = nmap.get_nmap_options()
        host = nmap.get_host()
        command = ['nmap'] + options + [host]
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
    elif choice == 4:
        hashbash_path = os.path.join(os.path.dirname(__file__), 'fsociety3', 'scripts')  
        sys.path.append(hashbash_path)
        if __name__ == "__main__":
            print("Welcome to the MD5 Hash Generator and Cracker Tool.")
            password = input("Please enter the password to generate the MD5 hash: ")

            md5_hashed_value = generate_md5_hash(password)

            print(f"The MD5 hash of the password '{password}' is: {md5_hashed_value}")

            potential_passwords = ["password", "letmein", "qwerty", "123456", "secret", "admin"]  # You can add more passwords to the list

            cracked_password = crack_md5_hash(md5_hashed_value, potential_passwords)

            if cracked_password:
                print(f"The cracked password for the hash {md5_hashed_value} is: {cracked_password}.")
            else:
                print("Password not found in the dictionary.")
    elif choice == 5:
        print("1. Bypass 4 digit lockscreen")
        print("2. Bypass 6 digit lockscreen")
        choice = int(input("fsociety# "))
        if choice == 1:
            android.bypass(4)
        else:
            android.bypass(6)
