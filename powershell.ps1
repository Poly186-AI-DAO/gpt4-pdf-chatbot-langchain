# PowerShell script to list all files and folders in a directory

# Request administrative privileges
If (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    # Relaunch the script with administrative privileges
    Start-Process PowerShell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File $($MyInvocation.MyCommand.Path)" -Verb RunAs
    Exit
}

# Specify the directory to list files and folders
$directoryPath = 'C:\Users\eagle\OneDrive\Documents\Dev\gpt4-pdf-chatbot-langchain\'

# Check if the directory exists
if (Test-Path $directoryPath) {
    # Get the list of all files and folders in the directory
    $filesAndFolders = Get-ChildItem -Path $directoryPath -Recurse

    # Output the list of files and folders
    Write-Output "Files and folders in directory '$directoryPath':"
    $filesAndFolders | ForEach-Object {
        Write-Output $_.FullName
    }
} else {
    Write-Output "The specified directory '$directoryPath' does not exist."
}
