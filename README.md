# Notepad++ Tab Colour Organizer

**Version 1.0.0**

## What it does

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
Orange and Pink look Red and Purple in darkmode but are still refered to as Pink and Orange in the code.

## Requirements

- Windows
- Notepad++
- PythonScript plugin

Version 1.0.0 is written for PythonScript 2.1 (Python 2.7).
PythonScript 3.x compatibility has not yet been tested and is not guaranteed.

## Installation

1. Install PythonScript through Notepad++:
   **Plugins > Plugins Admin > Available > PythonScript > Install**.
2. Close/restart Notepad++ if requested.
3. Download `TabColourOrganizer.zip` from the
   [Releases](../../releases) page and extract it.
4. Run `Install.bat`.
5. Restart Notepad++.
6. Open **Plugins > PythonScript > Scripts**.
7. Run **ConfigureTabColourOrder** first to set your preferred order.
8. Run **TabColourOrganizer** to group the tabs.

The installer uses the standard per-user Notepad++ configuration path:

```
%APPDATA%\Notepad++\plugins\Config\PythonScript\scripts
```

### Portable or custom installations

The installer targets the standard per-user Notepad++ location. For a portable
or custom installation, manually copy the two `.py` files from the package's
`scripts` folder into that installation's PythonScript scripts folder.

## Configuration

The saved order is stored in:

```
%APPDATA%\Notepad++\plugins\Config\TabColourOrganizer_order.txt
```

The configuration file is separate from the scripts. Reinstalling or updating
the scripts does not overwrite this file.

## Uninstallation

Run `Uninstall.bat`. It removes the two scripts but intentionally keeps your
saved colour order. Delete `TabColourOrganizer_order.txt` separately if you
also want to remove your settings.

## Important

- This is a PythonScript script bundle, not a native Notepad++ DLL plugin.
- PythonScript is a separate prerequisite and is not included in this package.
- The script rearranges open tabs. It does not intentionally save, close, or
  modify document contents.
- Back up important work and test on a small set of tabs before relying on it
  with a large working session.
- Version 1.0.0 has not yet been tested on 64-bit installations of Notepad++.

## Troubleshooting

If the scripts do not appear:

- Restart Notepad++.
- Confirm PythonScript is installed and enabled.
- Confirm the `.py` files are in PythonScript's scripts folder.

If sorting reports an error:

- Open **Plugins > PythonScript > Show Console**.
- Copy the complete error output when reporting the problem.

## License

[MIT](LICENSE.txt)
