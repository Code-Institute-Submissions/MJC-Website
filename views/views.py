from django.shortcuts       import render, redirect, get_object_or_404
from django.http            import FileResponse, Http404
from activities.models      import Venue, Host
from news.models            import News




# Testing PDF file
# def get_pdf_file(request, filename):
    
#     try:
#         return FileResponse(open('media/files-download/' + str(filename), 'rb'), content_type='application/pdf')
    
#     except FileNotFoundError:
#         raise Http404()



def get_home_page(request):
    
    last_news    = News.objects.order_by('-published_date')[:3]
    
    return render(request, "views/index.html", {'last_news': last_news})
    # return render(request, "views/test.html")



def get_info_page(request):
    return render(request, "views/info.html")



def get_calendar_activities_page(request):
    return render(request, "views/calendar_activities.html")



def get_about_page(request):
    return render(request, "views/about.html")

   
   
def get_rate_and_registration_activities_page(request):
    return render(request, "views/rate_and_registration_activities.html")



def get_rate_and_registration_workshop_page(request):
    return render(request, "views/rate_and_registration_workshops.html")



def get_youth_mauguio_page(request):
    return render(request, "views/youth_mauguio.html")



def get_youth_carnon_page(request):
    return render(request, "views/youth_carnon.html")



def get_venue(request, name_venue):
    
    venue        = get_object_or_404(Venue, name=name_venue)
    
    return render(request, "views/venue.html", {'venue': venue} )



def get_venues_list(request):
    
    venues        = Venue.objects.all
    
    return render(request, "views/venues_list.html", {'venues': venues} )



def get_host(request, id):
    
    host        = get_object_or_404(Host, pk=id)
    
    return render(request, "views/host.html", {'host': host} )



def get_admin_panel(request):
    return redirect("/admin")
    
    
    
def edit_activity(request, activity_slot_id):
    return redirect("/admin/activities/activity_animation_slot/" + str(activity_slot_id) + "/change")
    
    

def edit_workshop(request, workshop_slot_id):
    return redirect("/admin/workshops/workshop_animation_slot/" + str(workshop_slot_id) + "/change")
    
    
    
# To be deleted :
# 
# activities   = get_object_or_404(Event_Type, event_type="ACTIVITY")
# courses      = get_object_or_404(Event_Type, event_type="TRAININGCOURSE")
# events       = get_object_or_404(Event_Type, event_type="EVENT")