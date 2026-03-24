import time
now = int(time.time())
print(f'Current timestamp: {now}')
print(f'Next 15min: {now + 900} ({time.strftime("%H:%M", time.gmtime(now + 900))} UTC)')
