#!/usr/bin/python3
import gi
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
gi.require_version("Gtk", "3.0")
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository import WebKit2
from .vaccine import list,cases
from .top_provinces import canvas
from .least_provinces import canvas1
from .one_month_daily_dose import one_month_dose_canvas
from .three_month_daily_dose import three_month_dose_canvas
from .total_daily_dose import total_daily_dose_canvas
from .total_dose import total_dose_canvas
from .one_month_daily_case import one_month_case_canvas
from .three_month_daily_case import three_month_case_canvas
from .total_daily_case import total_daily_case_canvas
from .one_month_daily_death import one_month_death_canvas
from .three_month_daily_death import three_month_death_canvas
from .total_daily_death import total_daily_death_canvas
from .top_case_province import top_case_canvas
from .least_case_province import least_case_canvas
from .news import news


NEWS_IMG_DIR = "/home/huydq/ITSS Linux/CovidTracking/news/images/"

@Gtk.Template(resource_path='/org/example/App/window.ui')
class CovidtrackingWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'CovidtrackingWindow'


    # For vaccine
    vaccine_date = Gtk.Template.Child()
    vaccinated_number = Gtk.Template.Child()
    vaccinated_percentage = Gtk.Template.Child()
    two_dose_number = Gtk.Template.Child()
    two_dose_percentage = Gtk.Template.Child()
    one_dose_number = Gtk.Template.Child()
    one_dose_percentage = Gtk.Template.Child()

    enough_dose_number = Gtk.Template.Child()
    progress_bar = Gtk.Template.Child()

    distribution = Gtk.Template.Child()
    vaccination = Gtk.Template.Child()

    vaccination_table = Gtk.Template.Child()

    total_dose = Gtk.Template.Child()
    dose_by_day = Gtk.Template.Child()
    dose_by_day_box =Gtk.Template.Child()
    top_provinces = Gtk.Template.Child()
    least_provinces = Gtk.Template.Child()

    # For vaccine

    # For cases
    case_date = Gtk.Template.Child()
    total_cases = Gtk.Template.Child()
    today_cases = Gtk.Template.Child()
    total_recover = Gtk.Template.Child()
    today_recover = Gtk.Template.Child()
    total_death = Gtk.Template.Child()
    today_death = Gtk.Template.Child()
    total_treated = Gtk.Template.Child()
    today_treated = Gtk.Template.Child()

    case_by_day = Gtk.Template.Child()
    case_by_day_box =Gtk.Template.Child()
    death_by_day = Gtk.Template.Child()
    death_by_day_box =Gtk.Template.Child()

    cases_map = Gtk.Template.Child()
    death_map = Gtk.Template.Child()
    cases_table = Gtk.Template.Child()

    recover_progess_bar = Gtk.Template.Child()
    recover_number = Gtk.Template.Child()

    top_case_provinces = Gtk.Template.Child()
    least_case_provinces = Gtk.Template.Child()
    # For cases
    # For news
    news_notebook = Gtk.Template.Child()
    news_box = Gtk.Template.Child()
    news_box1 = Gtk.Template.Child()
    news_title = Gtk.Template.Child()
    # For news
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Vaccine
        self.vaccine_date.set_text(cases[0]['date'])
        self.vaccinated_number.set_text(list[0]["vaccinated_population"])
        self.vaccinated_percentage.set_text(list[0]["vaccinated_percentage"])
        self.two_dose_number.set_text(list[1]["two_dose_population"])
        self.two_dose_percentage.set_text(list[1]["two_dose_percentage"])
        self.one_dose_number.set_text(list[2]["one_dose_population"])
        self.one_dose_percentage.set_text(list[2]["one_dose_percentage"])


        fully_vaccinated_progress = float(list[1]["two_dose_percentage"].replace("% population",""))/100
        self.enough_dose_number.set_text("Fully vaccinated population: "+list[1]["two_dose_population"])
        self.progress_bar.set_fraction(fully_vaccinated_progress)

        self.webview = WebKit2.WebView()
        uri = "https://api.ncovtrack.com/vaccine/vietnam/provinces?metric=doses_available&showTable=false&showMap=true"
        self.webview.load_uri(uri)
        self.distribution.pack_start(self.webview,True,True,0)

        self.webview1 = WebKit2.WebView()
        uri1 = "https://api.ncovtrack.com/vaccine/vietnam/provinces?metric=second_dose&showTable=false&showMap=true"
        self.webview1.load_uri(uri1)
        self.vaccination.pack_start(self.webview1,True,True,0)

        self.webview2 = WebKit2.WebView()
        uri2 = "https://api.ncovtrack.com/vaccine/vietnam/provinces?metric=second_dose&showTable=true&showMap=false"
        self.webview2.load_uri(uri2)
        # self.webview2.run_javascript_in_world('document.getElementsByClassName("text-lightMode  m-0 p-2")[0].style.display = "none" ','',None,None,None)
        self.vaccination_table.pack_start(self.webview2,True,True,0)

        self.top_provinces.pack_start(canvas,True,True,0)
        self.least_provinces.pack_start(canvas1,True,True,0)


        self.dose_by_day_box.add(one_month_dose_canvas)

        self.three_month_dose_page = Gtk.Box()
        self.three_month_dose_page.add(three_month_dose_canvas)
        self.dose_by_day.append_page(self.three_month_dose_page,Gtk.Label("3 month"))

        self.total_daily_dose_page = Gtk.Box()
        self.total_daily_dose_page.add(total_daily_dose_canvas)
        self.dose_by_day.append_page(self.total_daily_dose_page,Gtk.Label("All time"))

        self.total_dose.pack_start(total_dose_canvas,True,True,0)
        # Vaccine

        # Case
        self.case_date.set_text(cases[0]['date'])
        self.total_cases.set_text(cases[0]['total_cases'])
        self.today_cases.set_text(cases[0]['today_cases'])
        self.total_recover.set_text(cases[0]['total_recover'])
        self.today_recover.set_text(cases[0]['today_recover'])
        self.total_death.set_text(cases[0]['total_death'])
        self.today_death.set_text(cases[0]['today_death'])
        self.total_treated.set_text(cases[0]['total_treated'])
        if cases[0]['today_treated'] is None:
            self.today_treated.set_text("Công bố hôm qua N/A")
        else:
            self.today_treated.set_text(cases[0]['today_treated'])
        self.case_by_day_box.add(one_month_case_canvas)

        self.three_month_case_page = Gtk.Box()
        self.three_month_case_page.add(three_month_case_canvas)
        self.case_by_day.append_page(self.three_month_case_page,Gtk.Label("3 month"))

        self.total_daily_case_page = Gtk.Box()
        self.total_daily_case_page.add(total_daily_case_canvas)
        self.case_by_day.append_page(self.total_daily_case_page,Gtk.Label("All time"))

        self.death_by_day_box.add(one_month_death_canvas)

        self.three_month_death_page = Gtk.Box()
        self.three_month_death_page.add(three_month_death_canvas)
        self.death_by_day.append_page(self.three_month_death_page,Gtk.Label("3 month"))

        self.total_daily_death_page = Gtk.Box()
        self.total_daily_death_page.add(total_daily_death_canvas)
        self.death_by_day.append_page(self.total_daily_death_page,Gtk.Label("All time"))

        self.webview3 = WebKit2.WebView()
        uri3 = "https://api.ncovtrack.com/covid/vietnam/provinces?metric=cases&showTable=false&showMap=true"
        self.webview3.load_uri(uri3)
        self.cases_map.pack_start(self.webview3,True,True,0)

        self.webview4 = WebKit2.WebView()
        uri4 = "https://api.ncovtrack.com/covid/vietnam/provinces?metric=deaths&showTable=false&showMap=true"
        self.webview4.load_uri(uri4)
        self.death_map.pack_start(self.webview4,True,True,0)

        self.webview5 = WebKit2.WebView()
        uri5 = "https://api.ncovtrack.com/covid/vietnam/provinces?metric=deaths&showTable=true&showMap=false"
        self.webview5.load_uri(uri5)
        # self.webview2.run_javascript_in_world('document.getElementsByClassName("text-lightMode  m-0 p-2")[0].style.display = "none" ','',None,None,None)
        self.cases_table.pack_start(self.webview5,True,True,0)

        recover_progress = float(cases[0]['total_recover'].replace(".",""))/float(cases[0]['total_cases'].replace(".",""))
        self.recover_number.set_text("Recover number: "+ cases[0]['total_recover'])
        self.recover_progess_bar.set_fraction(recover_progress)

        self.top_case_provinces.pack_start(top_case_canvas,True,True,0)
        self.least_case_provinces.pack_start(least_case_canvas,True,True,0)
        # Case

        #News
        self.news_title.set_text("Source:VnExpress "+ cases[0]['date'])

        for i in range(5):
            label = {}
            img = {}
            des = {}
            box_index = f'box{i}'
            self.box = {}


            if i == 0:
                for j in range(i*20, i*20 + 20):
                    index = f'label{j}'
                    label[index] = Gtk.Button()
                    label[index] = label[index].new_with_label(news[j]['title'])
                    label[index].connect("clicked", self.on_news_btn_clicked,news[j]['href'],index)
                    img[index] = Gtk.Image()
                    try:
                        img[index].set_from_file(NEWS_IMG_DIR + news[j]['image_paths'][0])
                    except:
                        print(NEWS_IMG_DIR + str(news[j]['image_paths']))
                    des[index]= Gtk.Label()
                    des[index].set_text(news[j]['description'])
                    self.news_box1.pack_start(label[index],True,True,0)
                    self.news_box1.pack_start(img[index],True,True,0)
                    self.news_box1.pack_start(des[index],True,True,0)
            else:
                # vertical_orientation = Gtk.Orientation(0)
                self.box[box_index] = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
                for j in range(i*20, i*20 + 20):
                    index = f'label{j}'
                    label[index] = Gtk.Button()
                    label[index] = label[index].new_with_label(news[j]['title'])
                    label[index].connect("clicked", self.on_news_btn_clicked,news[j]['href'],index)
                    img[index] = Gtk.Image()
                    try:
                        img[index].set_from_file(NEWS_IMG_DIR + news[j]['image_paths'][0])
                    except:
                        print(NEWS_IMG_DIR + str(news[j]['image_paths']))
                    des[index]= Gtk.Label()
                    des[index].set_text(news[j]['description'])

                    self.box[box_index].pack_start(label[index],True,True,0)
                    self.box[box_index].pack_start(img[index],True,True,0)
                    self.box[box_index].pack_start(des[index],True,True,0)

                self.news_notebook.append_page(self.box[box_index],Gtk.Label(f"PAGE {i+1}"))

        #News
        self.show_all()


    @Gtk.Template.Callback()
    def on_news_btn_clicked(self,button,href,index):
        news_window = {}
        print(href)
        news_window[index] = NewsWindow(href)
        news_window[index].show_all()

class NewsWindow(Gtk.Window):
    def __init__(self,href):
        Gtk.Window.__init__(self,title="News")
        self.news_content_area = Gtk.Box()
        self.news_webview = WebKit2.WebView()
        self.news_webview.load_uri(href)
        self.news_content_area.pack_start(self.news_webview,True,True,0)
        self.add(self.news_content_area)












        
