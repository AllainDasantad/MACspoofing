
import subprocess
import re


def get_interfaces():
    """Return network interface details from Linux."""
    try:
        result = subprocess.run(
            ["ip", "-j", "link", "show"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5,
        )
    except (subprocess.CalledProcessError, FileNotFoundError,
            subprocess.TimeoutExpired) as error:
        print(f"Could not read interfaces: {error}")
        return []

    import json
    interfaces = json.loads(result.stdout)
    return interfaces


def is_valid_mac(mac):
    """Check standard six-byte MAC address formatting."""
    return bool(
        re.fullmatch(
            r"(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}",
            mac,
        )
    )


def main():
    interfaces = get_interfaces()

    if not interfaces:
        print("No interface information available.")
        return

    for interface in interfaces:
        name = interface.get("ifname", "unknown")
        mac = interface.get("address", "unavailable")

        print(f"Interface: {name}")
        print(f"MAC address: {mac}")
        print(f"Valid format: {is_valid_mac(mac)}")
        print("-" * 30)


if __name__ == "__main__":
    main()

