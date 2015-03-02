from slide import Slide, Slide_Color, Slide_Transition
from presentation import Presentation
from shared import Shared


presentation = Presentation()
presentation.add_slide(Slide(label="I am not alone", slide_color=Slide_Color.red))
presentation.add_slide(Slide(label="Fire", slide_color=Slide_Color.green))
print(presentation.xml_string())