import os
import platform
import datetime

print("==== SYSTEM INFO ====")
print(f"Hostname:  {platform.node()}")
print(f"OS:  {platform.system()} {platform.release()}")
print(f"Datum:  {datetime.datetime.now().strftime('%d.%m.%Y %H.%M')}")
print(f"CPU Kerne:  {os.cpu_count()}")
print(f"Python:  {platform.python_version()}")
print("============================")
