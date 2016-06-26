#!/virtualenv/lik/bin/python
# -*- coding: utf-8 -*-
from lik.models import Category


class ActiveMenuItem(object):

    def process_request(self, request):
        path = request.path_info
        if 'admin' in path or 'static' in path or 'media' in path:
            return None
        elif path == '/':
            request.session['active'] = 'main'
        elif path == '/about/':
            request.session['active'] = 'about'
        elif path == '/contacts/':
            request.session['active'] = 'contacts'
        else:
            split_path = path.split('/')
            split_path.remove("")
            cat_id = int(split_path[0])
            category = Category.objects.filter(id=cat_id).first()
            if category is None:
                return None
            request.session['active'] = category.name
