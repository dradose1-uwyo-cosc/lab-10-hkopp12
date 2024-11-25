# Your Name Here
# UWYO COSC 1010
# Submission Date
# Lab XX
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.

# - Read in the value stored within `hash`.
#   - You must use a try and except block.
# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.


hash_file_path = Path("hash")
rockyou_file_path = Path("rockyou.txt")

def crack_password():
    try:
        with open(hash_file_path, "r") as hash_file:
            stored_hash = hash_file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file '{hash_file_path}' was not found.")
        return
    except Exception as e:
        print(f"Error reading the hash file: {e}")
        return

    try:
        with open(rockyou_file_path, "r", encoding="utf-8", errors="ignore") as rockyou_file:
            passwords = rockyou_file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{rockyou_file_path}' was not found.")
        return
    except Exception as e:
        print(f"Error reading the rockyou file: {e}")
        return
    else:
        for password in passwords:
            password = password.strip() 
            if get_hash(password) == stored_hash:
                print(f"Password found: {password}")
                break
        else:
            print("Password not found in the provided list.")

crack_password()
