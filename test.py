from slide import Slide, Slide_Color, Slide_Transition


slide = Slide(
	label="I am not alone", 
	color=Slide_Color.blue,
	transition=Slide_Transition.dissolve
)

print(slide)
print(slide.xml())