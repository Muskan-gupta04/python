from datetime import datetime
current_time = datetime.now()
formatted_time = current_time.strftime("%a %B %d %H:%M:%S IST %Y")
print(formatted_time)
