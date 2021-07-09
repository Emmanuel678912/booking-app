from django.shortcuts import render
import datetime
from .calendar_API import *
import stripe

# Create your views here.
def home(request):
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)

    month_from_now = datetime.date.today() + datetime.timedelta(days=30)

    if request.method == "POST":
        subject = request.POST.get('subject')
        desc = request.POST.get("desc")
        date = request.POST.get("daterange") 

        date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    
        hour_later = date + timedelta(minutes=60)

        hour_later = hour_later.isoformat()

        date = date.isoformat()


        def create_event():

            service = build_service()

            # start_datetime = datetime.datetime.now(tz=pytz.utc)
            event = (
                service.events()
                .insert(
                    calendarId="02g427gf151ggdmcas2pui1suo@group.calendar.google.com",
                    body={
                        "summary": subject,
                        "description": desc,
                        "start": {
                            "dateTime": date,
                            "timeZone":"Europe/London"
                            },
                        "end": {
                            "dateTime": hour_later,
                            "timeZone":"Europe/London"
                        },
                    },
                )
                .execute()
            )

            print(event)


        create_event()

    context = {'tomorrow' : tomorrow, 'month' : month_from_now}

    return render(request, 'index.html', context)


