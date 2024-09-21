from  kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main'):
        super().__init__()
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainScreen(Screen):
    def __init__(self,**kwards):
        super().__init__(**kwards)
        v1 = BoxLayout(orientation = 'vertical',padding = 8,spacing = 8)
        h1 = BoxLayout()
        txt = Label('Choose screen')
        h1.add_widget(txt)
        h1.add_widget(v1)
        self.add_widget(h1)
        
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name ='main'))
        return sm
        

app = MyApp()
app.run()
    