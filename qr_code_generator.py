from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
import segno

img_count = 0

class MainScr(Screen):
    def __init__(self, name="main"):
        super().__init__(name=name)
        self.main_box = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.upper_box = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.lower_box = BoxLayout(orientation="vertical", padding=8, spacing=8)

        self.input = TextInput()

        self.qr_image = Image()

        self.create_btn = Button(text="Create QR code")
        self.create_btn.on_press = self.render_qrcode

        self.upper_box.add_widget(self.qr_image)

        self.lower_box.add_widget(self.input)
        self.lower_box.add_widget(self.create_btn)

        self.main_box.add_widget(self.upper_box)
        self.main_box.add_widget(self.lower_box)

        self.add_widget(self.main_box)
    def render_qrcode(self):
        global img_count
        img_count += 1
        self.qr_image.source = ""
        if self.input.text != "":
            qr = segno.make_qr(self.input.text)
            qr.save("qr_code"  + str(img_count)+".png", scale=10)

        self.qr_image.source = "qr_code" + str(img_count)+".png"
       
class QrCodeGenerator(App):
  def build(self):
    sm = ScreenManager()
    sm.add_widget(MainScr())
    return sm

app = QrCodeGenerator()
app.run()