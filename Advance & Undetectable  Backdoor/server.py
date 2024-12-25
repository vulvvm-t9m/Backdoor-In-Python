import socket
from termcolor import colored

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the specified address and port
s.bind(("192.168.29.186", 12345))
s.listen(5)

print(colored("[+] Listening for Incoming Connections", "green"))

# Accept a connection
target, ip = s.accept()  # Corrected this line

print(colored("[+] Connection Established From: %s" % str(ip), "green"))

# Optionally, you can close the socket after use~
# target.close()
# s.close()