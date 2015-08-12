from cms.models import Settings


def get_settings(request):
    settings_ = Settings.objects.all()
    settings = dict.fromkeys(['phone', 'fax', 'email', 'sidebar_title'])
    for i in settings.keys():
        value = list(filter(lambda x: x.name == i, settings_))
        if len(value) == 1:
            settings[i] = value[0].value
        else:
            settings[i] = ''
    return dict(settings=settings)