from django.conf.urls.static    import static
from django.views.static        import serve
from django.conf                import settings
from django.urls                import path
# from .views                     import get_type_subtypes, get_subtype_list, get_event_details, register_to_event



urlpatterns = [
    # path('<event_type>', get_type_subtypes, name='subtypes'),
    # path('<event_type>/<event_subtype>', get_subtype_list, name='list'),
    # path('<event_type>/<event_subtype>/<event_id>', get_event_details, name='details'),
    # path('<event_type>/<event_subtype>/<event_id>/registration', register_to_event, name='register_to_event'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})
]