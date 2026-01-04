#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Starter template for PowerShell Core
.DESCRIPTION
    Entrypoint: Run with `pwsh starter.ps1` or `./starter.ps1`
    Sample I/O:
      Input: (via Read-Host or parameters)
      Output: (via Write-Output)
#>

# Read input
$UserInput = Read-Host "Enter your name"

# Process
$Result = "Hello, $UserInput!"

# Write output
Write-Output $Result
