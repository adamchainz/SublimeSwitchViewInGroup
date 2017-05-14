
import sublime, sublime_plugin

# Sublime Text added the ability to open images in version 3055.
# From then onwards every ST buffer has a sheet, which can hold
# either a view or an image. By using sheets instead of views to
# switch focus through the group's tabs, the plugin continues to
# function correctly when an image is open in a ST 3055+ group.

SHEETS_ADDED_VERSION = 3055
SUBLIME_TEXT_VERSION = int(sublime.version())


def move_sheet_in_group(window, amount):

    active_group = window.active_group()
    active_sheet = window.active_sheet()
    group, index = window.get_sheet_index(active_sheet)
    active_group_sheets = window.sheets_in_group(active_group)

    if index == -1:
        return

    index += amount

    if index >= len(active_group_sheets):
        index = 0
    elif index < 0:
        index = len(active_group_sheets) - 1

    sheet_to_focus = active_group_sheets[index]
    window.focus_sheet(sheet_to_focus)


def move_view_in_group(window, amount):

    active_group = window.active_group()
    active_view = window.active_view()
    group, index = window.get_view_index(active_view)
    active_group_views = window.views_in_group(active_group)

    if index == -1:
        return

    index += amount

    if index >= len(active_group_views):
        index = 0
    elif index < 0:
        index = len(active_group_views) - 1

    view_to_focus = active_group_views[index]
    window.focus_view(view_to_focus)


class NextViewInGroupCommand(sublime_plugin.WindowCommand):

    def run(self):

        if SUBLIME_TEXT_VERSION >= SHEETS_ADDED_VERSION:
            move_sheet_in_group(self.window, 1)
        else:
            move_view_in_group(self.window, 1)


class PrevViewInGroupCommand(sublime_plugin.WindowCommand):

    def run(self):

        if SUBLIME_TEXT_VERSION >= SHEETS_ADDED_VERSION:
            move_sheet_in_group(self.window, -1)
        else:
            move_view_in_group(self.window, -1)
