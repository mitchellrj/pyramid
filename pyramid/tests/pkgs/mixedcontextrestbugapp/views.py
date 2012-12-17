from pyramid.response import Response

class BaseRESTView(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

class PetGETView(BaseRESTView):
    def __init__(self, context, request):
        super(PetGETView, self).__init__(context, request)

    def __call__(self):
        return Response('gotten')

class PetPOSTView(BaseRESTView):
    def __init__(self, context, request):
        super(PetPOSTView, self).__init__(context, request)

    def __call__(self):
        return Response('posted')
