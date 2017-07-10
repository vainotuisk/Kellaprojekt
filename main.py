# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.clock import Clock
from time import strftime
import urllib.request
import datetime
import json
linn = "Pärnu"
address_param = urllib.parse.urlencode({'address': linn})
target = "http://api.openweathermap.org/data/2.5/weather?q="+address_param+"&appid=312148cec8dfac78058217072b44201e"
connection = urllib.request.urlopen(target)
raw_data = connection.read()
print ("Retrieved {0} characters".format(len(raw_data)))
parsed_data = json.loads(raw_data)
temperatuurC = int(parsed_data['main']['temp'] - 273)
print(temperatuurC)
tuul = int(parsed_data['wind']['speed'])
d = datetime.date.today().strftime("%A %d. %B %Y")
try:
    suund = int(parsed_data['wind']['deg'])
except:
    suund = '-'
kirjeldus = parsed_data['weather'][0]['description']
class KellApp(App):
    def update_time(self,nap):
        self.root.ids.time.text= strftime('%H:[b]%M:%S[/b]')
    def on_start(self):
        Clock.schedule_interval(self.update_time,1)
        Clock.schedule_interval(self.update_temperatuur,6)
        Clock.schedule_interval(self.update_tuul,6)
        Clock.schedule_interval(self.update_suund,6)
        Clock.schedule_interval(self.update_suund,6)
        self.root.ids.kuup.text = str(d)
    def update_temperatuur(self,nap):
        self.root.ids.temperatuur.text = str(temperatuurC) + '[b]\xb0 C [/b]'
    def update_tuul(self,nap):
        self.root.ids.tuul.text= str(tuul) + '[b] m/s[/b]'
    def update_suund(self,nap):
        self.root.ids.suund.text= str(suund) + '[b]\xb0[/b]'
if __name__ == '__main__':

    LabelBase.register(name='Aino',fn_regular='Aino-Regular.ttf',fn_bold='Aino-Headline.ttf',fn_bolditalic='Aino-Bold.ttf')
    KellApp().run()
