# CS440-Ransomware
Project component of SMU CS440 module where our team was taked to  implement a ransomware

### This Ransomware musn't be used to harm/threat/hurt other person's computer. It's purpose is only to share knowledge and awareness about Malware/Cryptography/Operating Systems/Programming. This ransomware made for learning and awareness about security/cryptography.

## Installation
Ensure that you have `python 3.10.0` or higher, `tkinter`, `Pillow`, `auto-py-to-exe` installed
```
pip install <required libraries>
```
Once that's done, run `auto-py-to-exe` to convert `koufu.py` to exe file. You should see a popup like this:
<img width="476" alt="image" src="https://github.com/S3annnyyy/CS440-Ransomware/assets/67400060/da4c01ad-592a-45b7-9063-5343743563c0">

Configure as follows:
1. Select path to koufu.py
2. Select one file option
3. Click on additional files option and import entire `img` folder as folder option
4. Click on `convert .py to exe`
5. You should see an `output` folder with the `exe` file inside 

Once done, you can execute exe file as administrator to run ransomware.  

To enable remote server, ensure that firewall for both Virtual Machine and local machine are set to off
<img width="691" alt="image" src="https://github.com/S3annnyyy/CS440-Ransomware/assets/67400060/78861387-5dee-4a6c-bc2e-e55add3f2299">

Once turned off run the following command:
```
python server.py
```
## Configuring IP Address
On your command prompt run the following command:
```
ipconfig
```
Configure IP_ADDRESS based `Ethernet adapter VMware Network Adapter VMnet8:` for both `koufu.py` and `server.py`  
