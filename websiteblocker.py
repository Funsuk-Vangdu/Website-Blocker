import time
from datetime import datetime

# Path to the hosts file (may vary by OS)
hosts_path = "/etc/hosts"  # For macOS and Linux
# For Windows, it would be "C:\\Windows\\System32\\drivers\\etc\\hosts"

redirect_ip = "127.0.0.1"
# List of websites you want to block
blocked_websites = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]

# Define blocking hours
start_block = datetime.strptime("08:00", "%H:%M").time()
end_block = datetime.strptime("18:00", "%H:%M").time()

while True:
    # Check if current time is within the blocking hours
    current_time = datetime.now().time()
    if start_block <= current_time <= end_block:
        print("Blocking websites...")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in blocked_websites:
                # If website is not already blocked
                if website not in content:
                    file.write(f"{redirect_ip} {website}\n")
    else:
        print("Unblocking websites...")
        with open(hosts_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)  # Move to the beginning of the file
            for line in lines:
                # Write only lines that are not blocked websites
                if not any(website in line for website in blocked_websites):
                    file.write(line)
            file.truncate()  # Remove any extra lines left over

    time.sleep(5)  # Check every 5 seconds
