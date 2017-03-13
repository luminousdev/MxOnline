
plugins = (
    'actions',
    'filters',
    'bookmark',
    'export',
    'layout',
    'refresh',
    'details',
    'editable',
    'relate',
    'chart',
    'ajax',
    'relfield',
    'inline',
    'topnav',
    'portal',
    'quickform',
    'wizard',
    'images',
    'auth',
    'multiselect',
    'themes',
    'aggregation',
    'mobile',
    'passwords',
    'sitemenu',
    'language',
    'quickfilter',
    'sortablelist',
    'ueditor',
    'excel',
)


def register_builtin_plugins(site):
    from importlib import import_module
    from django.conf import settings

    exclude_plugins = getattr(settings, 'xadmin_exclude_plugins', [])

    [import_module('xadmin.plugins.%s' % plugin) for plugin in plugins if plugin not in exclude_plugins]
