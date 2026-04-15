import os
import platform
import datetime

print("==== SYSTEM INFO ====")
print(f"Hostname:  {platform.node()}")
print(f"OS:  {platform.system()} {latform.release()}")
print(f"Datum:  {platform.datetime.now().strftime('%d.%m.%Y %H.%M')}")
print(f"CPU Kerne:  {platform.cpu_xount()}")
print(f"Python:  {platform.python.version()}")
print("============================")
