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
