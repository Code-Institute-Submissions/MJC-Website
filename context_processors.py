# from django.shortcuts       import get_object_or_404
# from activities.models      import Event, Event_Type, Event_Subtype


# def get_list_of_type_subtypes(request):
    
    # If context processor still required, do it by objects.filter instead of get_object_or_404
    # event_type_ACTIVITY       = Event_Type.objects.filter(event_type='ACTIVITY')
    
    # return { 'event_subtypes_ACTIVITY'  : event_subtypes_ACTIVITY }
    
    # -----------------------------------------------------------------------------------------------------------
    
#     event_type_ACTIVITY       = get_object_or_404(Event_Type, event_type='ACTIVITY')
#     event_subtypes_ACTIVITY   = Event_Subtype.objects.filter(Event__event_type = event_type_ACTIVITY.id).distinct().order_by('event_subtype')
    
#     event_type_COURSE         = get_object_or_404(Event_Type, event_type='TRAININGCOURSE')
#     event_subtypes_COURSE     = Event_Subtype.objects.filter(Event__event_type = event_type_COURSE.id).distinct().order_by('event_subtype')
    
#     event_type_EVENT          = get_object_or_404(Event_Type, event_type='EVENT')
#     event_subtypes_EVENT      = Event_Subtype.objects.filter(Event__event_type = event_type_EVENT.id).distinct().order_by('event_subtype')
    
    
    # return { 'event_subtypes_ACTIVITY'  : event_subtypes_ACTIVITY, 
#              'event_subtypes_COURSE'    : event_subtypes_COURSE, 
#              'event_subtypes_EVENT'     : event_subtypes_EVENT }
    
    