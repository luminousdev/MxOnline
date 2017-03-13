# _*_ coding: utf-8 _*_
__author__ = 'luminous'
__date__ = '2017/3/13 19:32'

import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from django.template import loader


# excel 导入
class ListImprotExcelPlugin(BaseAdminPlugin):
    import_excel = False

    def init_request(self, *args, **kwargs):  # 插件入口函数，如果为True加载插件
        return bool(self.import_excel)

    def block_top_toolbar(self, context, nodes):
        nodes.append(loader.render_to_string('xadmin/excel/model_list.top_toolbar.import.html', context_instance=context))

xadmin.site.register_plugin(ListImprotExcelPlugin, ListAdminView)
