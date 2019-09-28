Attribute VB_Name = "Module1"
Option Explicit

Public Const MODULE_TITLE = "Create csv"


Public Sub createCsv(forCsvRange As Range, pathToSave As String)

    Dim fso As Object
    Set fso = CreateObject("Scripting.FileSystemObject")
    
    Dim file As Object
    Set file = fso.CreateTextFile(pathToSave)

    writeRows forCsvRange, file
    
    file.Close
    Set fso = Nothing
    Set file = Nothing
    
    Dim message As String
    message = "Saved table of " & forCsvRange.Columns.Count & " by " & forCsvRange.Rows.Count & ", to " & pathToSave
    
    MsgBox message, , MODULE_TITLE
    
End Sub


Private Sub writeRows(forCsvRange As Range, file As Object)
    
    Dim row As Long
    For row = 1 To forCsvRange.Rows.Count
    
        Dim rowText As String
        rowText = ""
        
        Dim col As Long
        For col = 1 To forCsvRange.Columns.Count
        
            Dim cell As Range
            Set cell = forCsvRange.Cells(row, col)
            
            rowText = rowText & getSeparator(rowText) & cell.Text
        
        Next col
        
        Debug.Print rowText
        
        file.writeline rowText
        
    Next row
    
End Sub
