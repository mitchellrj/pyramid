def includeme(config):
    config.add_view('.views.PetPOSTView',
                    permission='view',
                    renderer='json',
                    context='pyramid.interfaces.IDefaultRootFactory',
                    request_method='POST')

    # Catchall
    config.add_view('.views.PetGETView',
                    permission='view',
                    renderer='json')
