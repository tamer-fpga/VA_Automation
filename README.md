This script automates the process of running vulnerability scans on a list of targets and provides a simple way to review identified vulnerabilities directly from the command line.


How to Use This Script"
Prepare Your Environment: Ensure Python, Nmap, Pandas, and OpenPyXL are installed on your system.

**pip install pandas openpyxl**

Excel File: Place your Excel file, Target_servers_IPs.xls, in /home/kali/VA/. The file should contain a list of IP addresses in the first column, with one IP address per row. 
Script File: Save the script as nmap_scan_parse.py (or another preferred name) in the /home/kali/VA/ directory.
Run the Script: Open a terminal, navigate to /home/kali/VA/, and run the script using Python by executing:

**python3 nmap_scan_parse.py**

**Note :** feel free to edit the path of the sheet at the script if you have to.

**Review Results:** The script will output the progress of scans and parsing results to the terminal. Each IP's scan results will be saved as an XML file in /home/kali/VA/, and vulnerabilities detected by scripts (specifically those with an id of 'vulners') will be printed to the console.
