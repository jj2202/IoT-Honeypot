## Project Description
**Project Scope**:
- Deploying and configuring IoT devices and IT Infrastructure within the lab. 
- Deploying and configuring EdgeX as IoT gateway and Logstash. 
- Creating Log Parser and Correlation Rules specific to IoT on Netwitness Platform 
- Creating data visualization

**Project Details**:
- Build a robust and attractive IoT Honeypot Environment with the available IoT devices and IT infrastructure. 
- Deploying open-source technologies such as EdgeX as an IoT an gateway to collect traffic from the edge devices. 
- Create Content on NetWitness Platform to ingest IoT devices’ logs. 
- (Optional) Deploying NetWitness UEBA to the production IoT environment. 
- Create Hunting Packages and Alerts to detect the following use cases for IoT (not limited to) : 
- Availability of the devices 
- Integrity of the data send to the devices 
- Map and visualize the data on NetWitness Platform

**Extra**:
- Used SNORT IDS to alert for attackers' movements
- Used NetWitness Investigator to make application rules. 

NetWitness Investigator was used for detailed analysis, and Snort for network intrusion detection. This comprehensive approach ensured effective identification and mitigation of potential security threats within the IoT environment. In a real world environment, it is best to have a centralised log server for logs from both these sources.

--------------


## Network Diagram


![networkdiagram](https://github.com/user-attachments/assets/1b530a16-75dc-4c0a-b79b-917c622cc183)


Virtual Machine (EdgeX IoT Gateway)
The IoT sensor and engineering workstation were implemented using Raspberry Pi 3B+ and Raspberry Pi 5 hardware, respectively.

Both the IoT sensor and engineering workstation were exposed to the internet due to their public IP addresses, making them potential attack vectors. These devices were made to have insecure configurations and the following services and ports open: 

**IoT Sensor**
Port 22 (SSH)
Port 5900 (VNC)
Port 80 (HTTP)

**Engineering Workstation** 
Port 22 (SSH)
Port 21 (FTP)
Port 80 (HTTP)
Port 445 (SMB)
Port 139 (NetBIOS)

--------------

**Please note, this GitHub repo was written with the assumption that the reader understands how to setup the project (EdgeX, configure Raspberry Pi, set up Docker containers etc.)**
