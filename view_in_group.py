import sublime_plugin


def move_view_in_group(window, amount):
    active_group = window.active_group()
    active_view = window.active_view()
    group, index = window.get_view_index(active_view)
    active_group_views = window.views_in_group(active_group)

    index += amount
    if index == len(active_group_views):
        index = 0
    elif index == -1:
        index = len(active_group_views) - 1

    activate = active_group_views[index]
    window.focus_view(activate)


class NextViewInGroupCommand(sublime_plugin.WindowCommand):
    def run(self):
        move_view_in_group(self.window, 1)


class PrevViewInGroupCommand(sublime_plugin.WindowCommand):
    def run(self):
        move_view_in_group(self.window, -1)
