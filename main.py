from kivy.app import App
from kivy.uix.screenmanager import Screen
class PhotoGalleryApp(App):
    pass

class Display(Screen):
    def display_image(self):
        return images[index]
    def advance_image(self):
        global index
        if index < len(images):
            index +=1
        else:
            index = 0
        self.ids.image.source = self.display_image()


images = ["car_stare.png","funny_skyweb","per8_RGillion_MoviePoster.png"]
index = 0

PhotoGalleryApp().run()