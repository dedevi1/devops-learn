import urllib.request
import datetime

websites = [
  "https://www.google.com",
  "https://www.github.com",
  "https://www.python.org"
]

print("==== WEBSITE CHECK ====")
print(f"Datum:  {datetime.datetime.now().strftime('%d.%m.%Y %H.%M')}")
print("")

for site in websites:
    try:
        urllib.request.urlopen(site, timeout=5)
        print(f"V ONLINE - {site}")
    except:
        print(f"X OFFLINE - {site}")
print("============================")
