import os
from typing import List, Union
import csv
from collections import Counter

# Constants
QUIT = 99
DATA_FILE = 'FirewallFile.txt'
OUTPUT_FILE = 'firewall_stats.csv'

def main():
    # Check if the data file exists
    try:
        if not os.path.isfile(DATA_FILE):
            print(f"Error: {DATA_FILE} file not found.")
            return
        else:
            print(f"File {DATA_FILE} found.")
    except Exception as e:
        print(f"Error checking file: {e}")
        return

    port_list = read_txt(DATA_FILE)
    if not port_list:
        print(f"Error: {DATA_FILE} is empty or could not be read.")
        return
    

    # Initialize statistics dictionary
    firewall_stats = {}
    choice = 0
    menu = (
        "Firewall Statistics Menu\n"
        "1. Calculate descriptive statistics\n"
        "2. Analyze FTP Traffic\n"
        "3. Analyze Telnet and Secure Shell traffic\n"
        "4. Analyze DHCP and BOOTP traffic\n"
        "5. Count packets\n"
        "6. Save statistics to file\n"
        "99. Quit"
    )
    
    while choice != QUIT:
        choice = input_menu_choice(menu, [1, 2, 3, 4, 5, 6, 99])

        if choice == 1:
            firewall_stats = calc_descriptive_stats(port_list)
            display_stats(firewall_stats)
        elif choice == 2:
            firewall_stats = analyze_ftp_traffic(port_list, firewall_stats)
            display_stats(firewall_stats)
        elif choice == 3:
            firewall_stats = analyze_telnet_ssh_traffic(port_list, firewall_stats)
            display_stats(firewall_stats)
        elif choice == 4:
            firewall_stats = analyze_dhcp_bootp_traffic(port_list, firewall_stats)
            display_stats(firewall_stats)
        elif choice == 5:
            firewall_stats = count_packets_by_port(port_list, firewall_stats)
            display_stats(firewall_stats)
        elif choice == 6:
            save_stats(firewall_stats)
        elif choice == 99:
            print("Exiting the program.")

def input_menu_choice(menu: str, valid_choices: List[int]) -> int:
    while True:
        print('-' * 50)
        print(menu)
        print('-' * 50)
        try:
            choice = int(input('Enter your choice: '))
            if choice in valid_choices:
                return choice
            print(f'Invalid choice. Valid choices are: {valid_choices}')
        except ValueError:
            print('Error: Please enter a number.')

def read_txt(file_name: str) -> List[List[Union[int, str]]]:
    try:
        with open(file_name, 'r') as f:
            content = f.readlines()

        data = []
        for line in content:
            stripped = line.strip()
            if stripped:
                parsed = []
                for item in stripped.split('\t'):
                    try:
                        parsed.append(int(item))
                    except ValueError:
                        parsed.append(item)
                data.append(parsed)

        return data

    except Exception as e:
        print(f'Error reading TXT: {e}')
        return []

def calc_descriptive_stats(data: List[List[Union[int, str]]]) -> dict:
    stats = {}
    byte_values = [row[3] for row in data if isinstance(row[3], int)]

    if not byte_values:
        print("No valid byte data found.")
        return stats

    most_bytes = max(byte_values)
    least_bytes = min(byte_values)
    avg_bytes = sum(byte_values) / len(byte_values)

    # Print in two-column format
    print("\nByte Statistics:")
    print(f"{'Most Bytes':<20}{most_bytes}")
    print(f"{'Least Bytes':<20}{least_bytes}")
    print(f"{'Average Bytes':<20}{avg_bytes:.1f}")

    # Populate the stats dictionary
    stats['Most Bytes'] = most_bytes
    stats['Least Bytes'] = least_bytes
    stats['Average Bytes'] = avg_bytes

    return stats

def analyze_ftp_traffic(data: List[List[Union[int, str]]], firewall_stats: dict) -> dict:
    ftp_ports = {20, 21}
    ftp_rows = []
    row_counter = 0

    print("\nRow    Source  Dest.  Action  Bytes  Packets")
    
    for i, row in enumerate(data, start=1):
        src, dst = row[0], row[1]
        if isinstance(src, int) and isinstance(dst, int) and (src in ftp_ports or dst in ftp_ports):
            row_counter += 1
            ftp_rows.append(row)
            action = row[2]
            bytes_val = row[3]
            packets = row[4]
            print(f"{i:<6} {src:<7} {dst:<6} {action:<7} {bytes_val:<6} {packets:<7}")

    # After loop
    total_rows = len(data)
    percent_ftp = (row_counter / total_rows * 100) if total_rows > 0 else 0

    print(f"\n{'Count FTP':<15}{row_counter}")
    print(f"{'Percent FTP':<15}{percent_ftp:.5f}")

    # Update the dictionary
    firewall_stats['Count FTP'] = row_counter
    firewall_stats['Percent FTP'] = percent_ftp

    return firewall_stats

def analyze_telnet_ssh_traffic(data: List[List[Union[int, str]]], firewall_stats: dict) -> dict:
    telnet_ssh_ports = {22, 23}
    match_count = 0

    print("\nRow    Source  Dest.  Action  Bytes  Packets")

    for i, row in enumerate(data, start=1):
        src, dst = row[0], row[1]
        if isinstance(src, int) and isinstance(dst, int) and (src in telnet_ssh_ports or dst in telnet_ssh_ports):
            match_count += 1
            action = row[2]
            bytes_val = row[3]
            packets = row[4]
            print(f"{i:<6} {src:<7} {dst:<6} {action:<7} {bytes_val:<6} {packets:<7}")

    total_rows = len(data)
    percent_telnet_ssh = (match_count / total_rows * 100) if total_rows > 0 else 0

    print(f"\n{'Count Telnet or SSH':<25}{match_count}")
    print(f"{'Percent Telnet or SSH':<25}{percent_telnet_ssh:.5f}")

    firewall_stats['Count Telnet or SSH'] = match_count
    firewall_stats['Percent Telnet or SSH'] = percent_telnet_ssh

    return firewall_stats

def analyze_dhcp_bootp_traffic(data: List[List[Union[int, str]]], firewall_stats: dict) -> dict:
    bootp_dhcp_ports = {67, 68}
    match_count = 0

    print("\nRow    Source  Dest.  Action  Bytes  Packets")

    for i, row in enumerate(data, start=1):
        src, dst = row[0], row[1]
        if isinstance(src, int) and isinstance(dst, int) and (src in bootp_dhcp_ports or dst in bootp_dhcp_ports):
            match_count += 1
            action = row[2]
            bytes_val = row[3]
            packets = row[4]
            print(f"{i:<6} {src:<7} {dst:<6} {action:<7} {bytes_val:<6} {packets:<7}")

    total_rows = len(data)
    percent_bootp_dhcp = (match_count / total_rows * 100) if total_rows > 0 else 0

    print(f"\n{'Count Bootp or DHCP':<25}{match_count}")
    print(f"{'Percent Bootp or DHCP':<25}{percent_bootp_dhcp:.5f}")

    firewall_stats['Count Bootp or DHCP'] = match_count
    firewall_stats['Percent Bootp or DHCP'] = percent_bootp_dhcp

    return firewall_stats

def count_packets_by_port(data: List[List[Union[int, str]]], firewall_stats: dict) -> dict:
    dest_ports_set = set()

    # Step 1: Collect unique destination ports
    for row in data:
        if isinstance(row[1], int):
            dest_ports_set.add(row[1])

    # Step 2: Create dictionary with each port and initialize count to 0
    port_count_dict = dict.fromkeys(dest_ports_set, 0)

    # Step 3: Count how many rows each destination port appears in
    for key in port_count_dict:
        count = 0
        for row in data:
            if row[1] == key:
                count += 1
        port_count_dict[key] = count

    # Step 4: Print result
    print(f"\n{'Port #':<10} {'Traffic Count'}")
    total_count = 0
    for port, count in sorted(port_count_dict.items()):
        print(f"{port:<10} {count}")
        total_count += count

    print(f"\nTotal Packet Count: {total_count}")

    # Optional: Store total in stats
    firewall_stats['Total Packet Rows'] = total_count

    return firewall_stats

def save_stats(stats: dict):
    try:
        with open(OUTPUT_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            for key, val in stats.items():
                writer.writerow([key, val])
        print(f'Statistics saved to {OUTPUT_FILE}')
    except Exception as e:
        print(f'Error writing to file: {e}')


def display_stats(stats: dict):
    print("\nFirewall Statistics:")
    for key, val in stats.items():
        print(f"{key:30s}: {val}")

if __name__ == "__main__":
    main()
