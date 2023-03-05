while(1 -eq 1)
{
Set-NetAdapterAdvancedProperty -name "Ethernet 2" -DisplayName "Speed & Duplex" -DisplayValue "10 Mbps Full Duplex"
echo "10 Mbps Full Duplex"

Set-NetAdapterAdvancedProperty -name "Ethernet 2" -DisplayName "Speed & Duplex" -DisplayValue "100 Mbps Full Duplex"
echo "1.0 Gbps Full Duplex"

}