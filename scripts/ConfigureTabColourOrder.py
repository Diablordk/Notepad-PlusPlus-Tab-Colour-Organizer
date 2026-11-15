# ============================================================
# Tab Colour Organizer
# Configure Colour Order
#
# Version: 1.0.0
# Notepad++ 8.9.1
# PythonScript 2.1 / Python 2.7
# Created by DiabloRDK
# ============================================================

from Npp import *
import os

COLOURS = [
    "No colour",
    "Yellow",
    "Green",
    "Blue",
    "Orange",
    "Pink"
]

CONFIG_FILE = os.path.join(
    notepad.getPluginConfigDir(),
    "TabColourOrganizer_order.txt"
)


def load_order():
    if os.path.exists(CONFIG_FILE):
        try:
            f = open(CONFIG_FILE, "r")
            values = f.read().strip().split(",")
            f.close()
            values = [v.strip() for v in values]

            if len(values) == 6 and set(values) == set(COLOURS):
                return values
        except:
            pass

    return COLOURS[:]


def configure_order():
    current_order = load_order()
    default_text = ", ".join(current_order)

    prompt_text = (
        "Enter the six groups in the desired order, "
        "separated by commas.\n"
        "Orange and Pink look Red and Purple in darkmode respectively."
    )

    result = notepad.prompt(
        prompt_text,
        "Tab Colour Organizer - Colour Order",
        default_text
    )

    if result is None:
        return

    new_order = [item.strip().lower() for item in result.split(",")]

    valid_names = dict((name.lower(), name) for name in COLOURS)

    if len(new_order) != 6 or set(new_order) != set(valid_names.keys()):
        notepad.messageBox(
            "Invalid colour order.\n\n"
            "Enter each of these groups exactly once:\n\n"
            "No colour, Yellow, Green, Blue, Orange, Pink",
            "Tab Colour Organizer"
        )
        return

    new_order = [valid_names[name] for name in new_order]

    try:
        config_dir = os.path.dirname(CONFIG_FILE)
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)

        f = open(CONFIG_FILE, "w")
        f.write(", ".join(new_order))
        f.close()

        notepad.messageBox(
            "Colour order saved successfully.\n\n"
            + "\n".join(
                str(i + 1) + ". " + colour
                for i, colour in enumerate(new_order)
            ),
            "Tab Colour Organizer"
        )
    except Exception as e:
        notepad.messageBox(
            "Could not save colour order:\n\n" + str(e),
            "Tab Colour Organizer"
        )


configure_order()
