from propresenter_lib.slide import Slide, Slide_Color, Slide_Transition
from propresenter_lib.presentation import Presentation
from propresenter_lib.shared import Shared


presentation = Presentation()
presentation.add_slide(Slide(label="Black", slide_color=Slide_Color.black))
presentation.add_slide(Slide(label="Blue", slide_color=Slide_Color.blue))
presentation.add_slide(Slide(label="Brown", slide_color=Slide_Color.brown))
presentation.add_slide(Slide(label="Cyan", slide_color=Slide_Color.cyan))
presentation.add_slide(Slide(label="Green", slide_color=Slide_Color.green))
presentation.add_slide(Slide(label="Magenta", slide_color=Slide_Color.magenta))
presentation.add_slide(Slide(label="Orange", slide_color=Slide_Color.orange))
presentation.add_slide(Slide(label="Purple", slide_color=Slide_Color.purple))
presentation.add_slide(Slide(label="Red", slide_color=Slide_Color.red))
presentation.add_slide(Slide(label="Yellow", slide_color=Slide_Color.yellow))
presentation.add_slide(Slide(label="White", slide_color=Slide_Color.white))

print(presentation.xml_string())