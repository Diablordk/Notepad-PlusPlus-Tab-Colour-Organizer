TAB COLOUR ORGANIZER
Version 1.0.0
===================

WHAT IT DOES
------------
Tab Colour Organizer groups open Notepad++ tabs according to their built-in
tab colours. You can choose the order of all six groups:

- No colour
- Yellow
- Green
- Blue
- Orange
- Pink

Tabs within each colour group retain their existing relative order.
Each Notepad++ view is sorted independently.

REQUIREMENTS
------------
- Windows
- Notepad++
- PythonScript plugin

Version 1.0.0 is written for PythonScript 2.1 (Python 2.7).
PythonScript 3.x compatibility has not yet been tested and is not guaranteed.

INSTALLATION
------------
1. Install PythonScript through Notepad++:
   Plugins > Plugins Admin > Available > PythonScript > Install.
2. Close/restart Notepad++ if requested.
3. Extract this ZIP package.
4. Run Install.bat.
5. Restart Notepad++.
6. Open Plugins > PythonScript > Scripts.
7. Run ConfigureTabColourOrder first to set your preferred order.
8. Run TabColourOrganizer to group the tabs.

The installer uses the standard per-user Notepad++ configuration path:
%APPDATA%\Notepad++\plugins\Config\PythonScript\scripts

PORTABLE OR CUSTOM INSTALLATIONS
--------------------------------
The installer targets the standard per-user Notepad++ location. For a portable
or custom installation, manually copy the two .py files from the package's
scripts folder into that installation's PythonScript scripts folder.

CONFIGURATION
-------------
The saved order is stored in:
%APPDATA%\Notepad++\plugins\Config\TabColourOrganizer_order.txt

The configuration file is separate from the scripts. Reinstalling or updating
the scripts does not overwrite this file.

UNINSTALLATION
--------------
Run Uninstall.bat. It removes the two scripts but intentionally keeps your
saved colour order. Delete TabColourOrganizer_order.txt separately if you
also want to remove your settings.

IMPORTANT
---------
- This is a PythonScript script bundle, not a native Notepad++ DLL plugin.
- PythonScript is a separate prerequisite and is not included in this package.
- The script rearranges open tabs. It does not intentionally save, close, or
  modify document contents.
- Back up important work and test on a small set of tabs before relying on it
  with a large working session.
- Version 1.0.0 has not yet been independently tested on clean installations
  or on both 32-bit and 64-bit Notepad++.

TROUBLESHOOTING
---------------
If the scripts do not appear:
- Restart Notepad++.
- Confirm PythonScript is installed and enabled.
- Confirm the .py files are in PythonScript's scripts folder.

If sorting reports an error:
- Open Plugins > PythonScript > Show Console.
- Copy the complete error output when reporting the problem.
