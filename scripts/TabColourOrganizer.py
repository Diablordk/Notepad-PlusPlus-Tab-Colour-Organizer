# ============================================================
# Tab Colour Organizer
# Group Tabs by Colour
#
# Version: 1.0.0
# Notepad++ 8.9.1
# PythonScript 2.1 / Python 2.7
# Created by DiabloRDK
# ============================================================

from Npp import *
import os

COLOURS = {
    -1: "No colour",
     0: "Yellow",
     1: "Green",
     2: "Blue",
     3: "Orange",
     4: "Pink"
}

DEFAULT_ORDER = [
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
    if not os.path.exists(CONFIG_FILE):
        return DEFAULT_ORDER[:]

    try:
        f = open(CONFIG_FILE, "r")
        values = f.read().strip().split(",")
        f.close()
        values = [v.strip() for v in values]

        if len(values) == 6 and set(values) == set(DEFAULT_ORDER):
            return values
    except:
        pass

    return DEFAULT_ORDER[:]


def collect_tabs():
    result = {}

    for filename, buffer_id, index, view in notepad.getFiles():
        colour_id = notepad.getTabColorID(view, index)

        if colour_id not in COLOURS:
            colour_id = -1

        if view not in result:
            result[view] = []

        result[view].append({
            "filename": filename,
            "buffer_id": buffer_id,
            "index": index,
            "colour": COLOURS[colour_id]
        })

    return result


def find_tab_index(buffer_id, view):
    for filename, bid, index, current_view in notepad.getFiles():
        if bid == buffer_id and current_view == view:
            return index
    return -1


def group_tabs():
    order = load_order()
    colour_rank = {}

    for position, colour in enumerate(order):
        colour_rank[colour] = position

    active_buffer = notepad.getCurrentBufferID()
    tabs_by_view = collect_tabs()
    move_count = 0

    # Sort each Notepad++ view independently.
    for view in sorted(tabs_by_view.keys()):
        sorted_tabs = sorted(
            tabs_by_view[view],
            key=lambda tab: (
                colour_rank[tab["colour"]],
                tab["index"]
            )
        )

        for target_index, tab in enumerate(sorted_tabs):
            buffer_id = tab["buffer_id"]
            current_index = find_tab_index(buffer_id, view)

            if current_index < 0:
                raise Exception(
                    "Could not find open document: " + tab["filename"]
                )

            if current_index > target_index:
                notepad.activateIndex(view, current_index)

                while notepad.getCurrentDocIndex(view) > target_index:
                    notepad.menuCommand(
                        MENUCOMMAND.VIEW_TAB_MOVEBACKWARD
                    )
                    move_count += 1

                actual_index = find_tab_index(buffer_id, view)
                if actual_index != target_index:
                    raise Exception(
                        "Could not position tab: " + tab["filename"]
                    )

    # Restore the previously active document.
    for filename, buffer_id, index, view in notepad.getFiles():
        if buffer_id == active_buffer:
            notepad.activateIndex(view, index)
            break

    return move_count


try:
    moved = group_tabs()
    notepad.messageBox(
        "Tab grouping completed.\n\n"
        "Tab moves performed: " + str(moved) + "\n\n"
        "Colour order:\n" + "\n".join(load_order()),
        "Tab Colour Organizer"
    )
except Exception as e:
    console.show()
    console.write("TAB COLOUR ORGANIZER ERROR\n")
    console.write(str(e) + "\n")
    notepad.messageBox(
        "Tab grouping could not be completed.\n\n"
        + str(e)
        + "\n\nPlease copy the PythonScript console output when reporting this issue.",
        "Tab Colour Organizer"
    )
