import pywin32api

drives = pywin32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print drives
