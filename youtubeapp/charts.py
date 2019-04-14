import matplotlib
import matplotlib.pyplot as plt
from . models import *
from django.shortcuts import render,redirect,reverse,HttpResponseRedirect


def vidstatsplot(request):
    """Plotly chart for the Individual Video stats this is: views vs date time

    using the video id from the UI and collects the related data from DB
    and plots the views vs datatime Chart using the matplotlib

    Charts can be configured as per wish
    Below one is just a basic Line chart

    """
    if request.method == 'GET':  # If the form is submitted
        search_query = request.GET.get('search_box', None)
        print("i am in this method")
        datelist=list()
        valuelist=list()
        for i in VideoStats.objects.all():
            if(i.video_master.video_id==search_query):
                valuelist.append(i.total_views)
                datelist.append(i.time_stamp)

        q=VideoMaster.objects.get(video_id=search_query)
        n=ChannelMaster.objects.get(pk=q.channel_master_id)
        s=n.channel_name+"---"+q.video_name
        plt.title(s)
        plt.xlabel('DateTime', fontsize=15)
        plt.ylabel('Number of Views', fontsize=15)
        plt.plot(datelist, valuelist)
        plt.show()
    return HttpResponseRedirect('/youtube/getvideostatsui')

def chanstatplot(request):
    """Plotly chart for the Individual Video stats this is: views vs date time

    using the Channel id from the UI and collects the related data from DB
    and plots the views vs datatime Chart using the matplotlib

    Charts can be configured as per wish
    Below one is just a basic Line chart"""

    if request.method=='GET':
        search_query=request.GET.get('search_box',None)
        datelist = list()
        valuelist = list()
        for i in ChannelStats.objects.all():
            if (i.channel_master.channel_id== search_query):
                valuelist.append(i.total_views)
                datelist.append(i.time_stamp)
        q = ChannelMaster.objects.get(channel_id=search_query)
        plt.title(q.channel_name)
        plt.xlabel('DateTime', fontsize=15)
        plt.ylabel('Number of Views', fontsize=15)
        plt.plot(datelist, valuelist)
        plt.show()
    return HttpResponseRedirect('/youtube/getchannelstatsui')

