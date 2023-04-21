# Script: Ops 401 Lab 4
# Joshua Phipps
# 4/20/2023
# Purpose: Lab 4 

# Reverse your configuration changes to:
# 1.1.5 (L1)
# 18.3.2 (L1)

# Disable SMB v1 client driver
Set-SmbClientConfiguration -EnableSMB1Protocol $false
# Enable password complexity requirements
$LocalPolicy = Get-Item -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters"
$LocalPolicy."requirecomplexpasswords" = 1


# Write a PowerShell script that automates the configuration of the required settings:

# 1.1.5 (L1)

# Define the registry key path and value data
$keyPath = "HKLM:\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters"
$valueName = "RequireComplexPassword"
$valueData = "1"
# Set the registry key value to enable the policy
Set-ItemProperty -Path $keyPath -Name $valueName -Value $valueData -Type DWORD

# 18.3.2 (L1)

# Define the registry key path and value data
$keyPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
$valueName = "ConsentPromptBehaviorAdmin"
$valueData = "2"
# Set the registry key value to enable the policy
Set-ItemProperty -Path $keyPath -Name $valueName -Value $valueData -Type DWORD

