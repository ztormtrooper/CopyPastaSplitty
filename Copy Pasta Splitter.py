# This takes in a string ( a copy pasta) and divides it up into segments that are equal to or less than the character limit
# for a game's char and then plugs it into an ahk script with a predetermined hotkey and sends it in chunks
# charLim should be the actual amount you can put in

def findSplitIndex(charLim, string, splitList):
   
    puncList = ['.', '!', '?']
    splitIndex = 0
  

    for i in range(len(puncList)):
        if string.rfind(puncList[i], 0, charLim) > splitIndex:
            splitIndex = string.rfind(puncList[i], 0, charLim)

    rfindSpace = string.rfind(' ', 0, charLim)

    if splitIndex == 0 and rfindSpace != -1:
        splitIndex =  rfindSpace

    if splitIndex == 0:
        splitIndex = charLim - 1

    splitList.append(string[0:splitIndex + 1])

    if len(string[splitIndex + 1:]) <= charLim:
        if len(string[splitIndex + 1:]) != 0:
             splitList.append(string[splitIndex + 1:])
        return
    
    else:
        findSplitIndex(charLim, string[splitIndex + 1:], splitList)

#This is to write out split up phrase into a macro.

def writeScript(splitString,script):
    script.write('#NoEnv \n; #Warn \nSendMode Input \nSetWorkingDir %A_ScriptDir%\n^!+w:: \n{\n\t')
    for i in range(len(splitString)):
        script.write("SendRaw," + splitString[i] + '\n\tSleep, 1000 \n\tSend, {Enter} \n\tSleep, 1000 \n\tSend, {Enter} \n\t')
    script.write("\n}")
    script.close()
    return


splitString = []
ahkScript = open(r"C:\Users\Kacper\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\CopyPastaMacro.ahk", "w")
charLimDict = {'hots': 255, 'blah': 100}

phrase = str(input("Please enter some text."))
charLim = 255

findSplitIndex(charLim, phrase, splitString)
print(splitString)
writeScript(splitString, ahkScript)