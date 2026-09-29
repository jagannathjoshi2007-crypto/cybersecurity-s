import socket
import platform


def get_network_information():
    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = "Unable to determine"

    return hostname, ip_address


def main():
    print("=" * 55)
    print("          NETWORK INFORMATION TOOL")
    print("=" * 55)

    hostname, ip_address = get_network_information()

    print(f"\nHostname       : {hostname}")
    print(f"IP Address     : {ip_address}")
    print(f"Operating System: {platform.system()}")
    print(f"OS Version     : {platform.version()}")
    print(f"Machine        : {platform.machine()}")
    print(f"Python Version : {platform.python_version()}")

    print("\nNetwork information collected successfully.")


if __name__ == "__main__":
    main()