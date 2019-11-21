from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
class ExteriorAuthMiddleware(MiddlewareMixin):
    # 判断登录 权限控制
    def process_request(self, request):
        if request.method == 'GET':
            requestData = request.GET
        else:
            requestData = request.POST
        request.session['errmsg'] = ''
        # 如果用户已经登录
        if request.session.has_key('_auth_user_id') and 'logout' not in request.path:
            ###权限检验
            try:
                u = User.objects.get(username=request.user)
                # 判断token是否过期
                url = request.META['PATH_INFO']
                request.get_full_path()
                # 判断用户是否有某些页面的访问权限，如果没有，转到404页面
                if not u.is_superuser:
                    if url.startswith('/create_entry/'):
                        return HttpResponseForbidden(content='没有权限访问')
            except Exception as e:
                return redirect('entries:login')
        # 用户已登录，而且url是login,将转到首页
        if request.session.has_key('_auth_user_id') and 'login' in request.path:
            return redirect('entries:blog-home')



