# System32-Zone-Identifier-checker

Checking Zone Identifier is a on of important way to check the file how to came to system and you will being able to prove a file came from a USB or Download from internet.
Can check Zone Identifier file with blow command:

ps > Get-Content --path <File Path> -Stream Zone.identifier

We can see that some malware might have this trigger as well. It is useful to scan C:\Windows\System32 to see whether any files have the "Zone.Identifier" ADS. It could be malicious.

This tools can Check System32 Directories and files to find ADS files.
