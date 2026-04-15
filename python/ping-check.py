import subprocess
import datetime

servers = [
  "8.8.8.8",        #Google
  "1.1.1.1",        #Cloudflare
  "9.9.9.9"         #Quad9 
]

print("==== PING CHECK ====")
print(f"Datum:  {datetime.datetime.now().strftime('%d.%m.%Y %H.%M')}")
print("")

for server in servers:
    result = subprocess.run(
        ["ping", "-n", "1", server]
        capture_output=True
    )
    if result.returncode == 0
        print(f"V ERREICHBAR - {server}")
    else:
        print(f"X NICHT ERR. - {server}")    
print("============================")