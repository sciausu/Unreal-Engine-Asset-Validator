# Unreal-Engine-Asset-Validator
Simple to use tool that validates assets used in an Unreal Engine project, specifically naming conventions and dependencies.
The tool validates asset naming conventions against Epic Games recommended standard. Dependency and orphaned asset checking is currently on the roadmap

Below is the command to run the program in the Command Terminal / Console / CMD:

"<Enter Path to file>\UnrealEditor-Cmd.exe" "<Enter Path to file>.uproject" -run=pythonscript -script="<Enter Path to file>\assetValidator.py" -stdout -FullStdOutLogOutput

Roadmap:
- Checking against naming conventions has been added and works. It specifically looks for assets within the \Game folder to limit scope
- Asset dependencies is currently being worked on 



Naming conventions used as reference for this tool
https://dev.epicgames.com/documentation/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects

NOTE: As names are currently stored in a dict, feel free to make adjustments to the dict to better suit your needs

