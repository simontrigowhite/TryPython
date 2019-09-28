Attribute VB_Name = "Module1"
Option Explicit

Const MODULE_TITLE = "Create csv"


Public Sub createCsv()


    Dim forCsvRange As Range
    Set forCsvRange = getNamedRange(Application, "for_csv")
    
    Dim pathRange As Range
    Set pathRange = getNamedRange(Application, "file_to_save")
    
    Dim pathToSave As String
    pathToSave = pathRange.Formula
    
    
    Dim fso As Object
    Set fso = CreateObject("Scripting.FileSystemObject")
    Dim file As Object
    Set file = fso.CreateTextFile(pathToSave)


    Dim row As Long
    For row = 1 To forCsvRange.Rows.Count
    
        Dim rowText As String
        rowText = ""
        
        Dim col As Long
        For col = 1 To forCsvRange.Columns.Count
        
            Dim cellText As String
            
            Dim cell As Range
            Set cell = forCsvRange.Cells(row, col)
            
            cellText = cell.Text
            
            rowText = rowText & getSeparator(rowText) & cellText
        
        Next col
        
        Debug.Print rowText
        
        file.writeline rowText
        
    Next row
    
    
    file.Close
    Set fso = Nothing
    Set file = Nothing
    
    Dim message As String
    message = "Saved table of " & forCsvRange.Columns.Count & " by " & forCsvRange.Rows.Count & ", to " & pathToSave
    
    MsgBox message, , MODULE_TITLE
    
End Sub


' Tools

Function getNamedRange(oExcelApp As Application, sRangeName As String) As Range
    
    Set getNamedRange = Nothing
    On Error Resume Next
    Set getNamedRange = oExcelApp.Names(sRangeName).RefersToRange
    On Error GoTo 0
    
    If getNamedRange Is Nothing Then
        Call MsgBox("The report template must contain the name " & sRangeName, , MODULE_TITLE)
    End If

End Function

Function getSeparator(existing As String) As String

    If (existing = "") Then
        getSeparator = ""
        
    Else
        getSeparator = ","
    End If
    
End Function
