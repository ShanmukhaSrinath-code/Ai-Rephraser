^!r::
ClipSaved := ClipboardAll
Clipboard := ""

; Force select all (fixes Ctrl+A timing issues)
SendInput, ^a
Sleep, 200

; Copy selection
SendInput, ^c

; Wait for clipboard to be ready
if !ClipWait(2)
{
    Clipboard := ClipSaved
    return
}

; Safety check
if (Clipboard = "")
{
    Clipboard := ClipSaved
    return
}

FileEncoding, UTF-8

; Write clipboard to temp file (prevents curl breaking)
TempInput := A_Temp "\input.txt"
FileDelete, %TempInput%
FileAppend, %Clipboard%, %TempInput%, UTF-8

command := "curl -s http://localhost:8000/rephrase -H ""Content-Type: text/plain; charset=utf-8"" --data-binary @" TempInput

RunWait, %ComSpec% /c chcp 65001 > nul & %command% > "%TEMP%\out.txt",, Hide

FileRead, Response, %TEMP%\out.txt

; Replace selection with response
Clipboard := Response
SendInput, ^v

Clipboard := ClipSaved
return
