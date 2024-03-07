import socket

print(" /\︵-︵/\ ")
print(" |(◉)(◉)| ")
print(" \ ︶V︶ /")
print(" /↺↺↺↺\ ")
print(" ↺↺↺↺↺\ ")
print("  \↺↺↺↺/ ")
print("    ¯¯/\¯/\¯   ")
def scan_port(domain, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((domain, port))
        if result == 0:
            print(f"Port {port} on {domain} is open")
        else:
            print(f"Port {port} on {domain} is closed")
        sock.close()
    except socket.error:
        print("Error during connection")

def main():
    domain = input("Masukkan nama domain website, contoh www.google.com: ")
    port = int(input("Masukkan port website: "))

    print(f"Scanning {domain} on port {port}...")
    scan_port(domain, port)

if __name__ == "__main__":
    main()
