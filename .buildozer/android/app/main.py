from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


class TutorialApp(App):

    def build(self):
        layout = FloatLayout()
        scatter = Scatter()
        label = Label(text='Hello',
                      font_size=150)
        layout.add_widget(scatter)
        scatter.add_widget(label)
        return layout

if __name__ == '__main__':
    TutorialApp().run()
