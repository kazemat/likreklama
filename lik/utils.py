from .models import Category, Settings


class GetMenuItems(object):

    def process_request(self, request):
        categories = Category.objects.order_by('name').all()
        if len(categories) > 0:
            request.session['menu_items'] = categories


class GetSettings(object):

    def process_request(self, request):
        settings_ = Settings.objects.all()
        settings = dict.fromkeys(['phone', 'fax', 'email', 'sidebar_title'])
        for i in settings.keys():
            value = list(filter(lambda x: x.name == i, settings_))
            if len(value) == 1:
                settings[i] = value[0].value
            else:
                settings[i] = ''
        request.session['settings'] = settings
        print(settings)