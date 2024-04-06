import pandas as pd
import subprocess
import xml.etree.ElementTree as ET

def read_ips_from_excel(file_path):
    """Read server IPs from an Excel file."""
    df = pd.read_excel(file_path, header=None, engine='openpyxl')
    ips = df[0].dropna().tolist()
    return ips

def run_nmap_scan(ip_list, output_directory):
    """Run Nmap scan for a list of IPs and save the output in the specified directory."""
    for ip in ip_list:
        report_path = f'{output_directory}report_{ip.replace(".", "_")}.xml'
        scan_command = ['nmap', '-oX', report_path, '--script=vuln', ip]
        print(f"Running Nmap scan for {ip}...")
        subprocess.run(scan_command, check=True)
        print(f"Scan report for {ip} saved to {report_path}")
        parse_nmap_xml_report(report_path)

def parse_nmap_xml_report(xml_file):
    """Parses an Nmap XML output file to extract and print vulnerability details."""
    print(f"Parsing Nmap scan results for vulnerabilities in {xml_file}...")
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        for host in root.findall('./host'):
            ip = host.find('./address[@addrtype="ipv4"]').get('addr')
            print(f"\nIP: {ip}")
            
            for script in host.findall('.//script[@id="vulners"]'):
                # This example specifically looks for scripts with id 'vulners'. Adjust as needed.
                print(f"Vulnerabilities found by {script.get('id')}:")
                print(f"{script.get('output')}\n")
                
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")

# Define paths
excel_file_path = '/home/kali/VA/Target_servers_IPs.xls'
output_directory = '/home/kali/VA/'

# Main process
if __name__ == '__main__':
    server_ips = read_ips_from_excel(excel_file_path)
    run_nmap_scan(server_ips, output_directory)
