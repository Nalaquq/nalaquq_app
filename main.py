from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.video import Video
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.lang import Builder
from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapMarkerPopup

#Define different screens

class GridLayout(GridLayout): 
    pass 

class SplashScreen(Screen): 
    pass 

class MainPage(Screen): 
    pass

class Weather(Screen):
    def on_start(self): 
        marker=MapMarkerPopup(lat=60.4297201, lon=-159.156797)
        marker.add_widget(Button)
        self.root.add_widget(marker)
    pass 
    
class Map(Screen): 
    pass

class WindowManager(ScreenManager): 
    pass 
 

class AnchorLayoutExample(AnchorLayout):
    pass

class SAR(Screen):
    pass


class MainWidget(Widget):
    pass


class MainApp(App):
    pass

MainApp().run()
