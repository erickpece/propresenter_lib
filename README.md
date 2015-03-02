# propresenter_lib

This is a planned Python library designed to help generate ProPresenter files.

## Examples

### Create three slides with labels, colors, and timers

This generates XML suitable for a `.pro5` extension presentation.

```
presentation = Presentation()

presentation.add_slide(
	Slide(
		label = "Slide 1",
		goto_next =
			ControlNext (
				timer = 4
			)
	)
)

presentation.add_slide(
	Slide(
		label = "Slide 2", 
		slide_color = Slide_Color.red,
		transition =
			Transition (
				transition_type = Slide_Transition.default, 
				transition_duration = 4
			),
		goto_next =
			ControlNext (
				timer = 8,
				loop_to_beginning = True
		)
	)
)

presentation.add_slide(
	Slide(
		label = "Slide 3"
	)
)

print(presentation.xml_string())
```