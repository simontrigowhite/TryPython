Attribute VB_Name = "Tools"
Option Explicit

' Tools

Public Function getNamedRange(oExcelApp As Application, sRangeName As String) As Range
    
    Set getNamedRange = Nothing
    On Error Resume Next
    Set getNamedRange = oExcelApp.Names(sRangeName).RefersToRange
    On Error GoTo 0
    
    If getNamedRange Is Nothing Then
        Call MsgBox("The report template must contain the name " & sRangeName, , MODULE_TITLE)
    End If

End Function

Public Function getSeparator(existing As String) As String

    If (existing = "") Then
        getSeparator = ""
        
    Else
        getSeparator = ","
    End If
    
End Function

