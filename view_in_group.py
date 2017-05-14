import sublime
import sublime_plugin

# The API for tabs up until version 3055 was 'views', then it got wrapped with
# 'sheets' which allow opening images.

USE_SHEETS = int(sublime.version()) >= 3055


class NextViewInGroupCommand(sublime_plugin.WindowCommand):

    def run(self):
        if USE_SHEETS:
            move_sheet_in_group(self.window, 1)
        else:
            move_view_in_group(self.window, 1)


class PrevViewInGroupCommand(sublime_plugin.WindowCommand):

    def run(self):
        if USE_SHEETS:
            move_sheet_in_group(self.window, -1)
        else:
            move_view_in_group(self.window, -1)


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
