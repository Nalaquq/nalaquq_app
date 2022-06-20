from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.video import Video
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.lang import Builder
from kivy_garden.mapview import MapView

#Define different screens

class SplashScreen(Screen): 
    pass 

class MainPage(Screen): 
    pass

class Map(Screen): 
    pass

class WindowManager(ScreenManager): 
    pass 
 

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass


class MainApp(App):
    pass


MainApp().run()
