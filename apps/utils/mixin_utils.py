# _*_ coding: utf-8 _*_
__author__ = 'luminous'
__date__ = '2017/3/6 21:14'

"""
def函数 @login_require 装饰器。 mixin 提供能够被一个或者一组子类简单继承功能的类
"""

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
