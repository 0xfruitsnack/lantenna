# lantenna

## Setup

[SDRSharp](https://airspy.com/download/),
[Python 3.7.0](https://www.python.org/downloads/release/python-370/),
Pyrtlsdr 0.2.93

Download the [rtlsdr-bin-w64_static.zip](https://github.com/librtlsdr/librtlsdr/releases) from librtlsdr GitHub page. Then, extract this and add the folder to PATH.

## Running

1. Configure SDRSharp to monitor the 250.002.7 GHz band
2. Manually configure the expected x-coordinate in Working_Morse.py to match the red band displayed on SDRSharp
3. Configure the message you want to send in PowerShellToggle.ps1
4. Run PowerShellToggle.ps1 and then Working_Morse.py in quick succession

## Example

Todo

## Credit

A special thanks to Mordechai Guri of the Ben-Gurion University of the Negev, Israel for the inspiration behind this project.

M. Guri, "LANTENNA: Exfiltrating Data from Air-Gapped Networks via Ethernet Cables Emission," 2021 IEEE 45th Annual Computers, Software, and Applications Conference (COMPSAC), Madrid, Spain, 2021, pp. 745-754, doi: 10.1109/COMPSAC51774.2021.00106.
