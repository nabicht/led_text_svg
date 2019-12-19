# led_text_svg
Converts text to LED, or "Scoreboard" font. And saves it as an SVG. Can be used as the image alone but is also now useable with CNC Routers, Laser cutters, etc.

# Requirements
pip install svgwrite

# Example Usage
*code can be found/run in example.py*
`import led_sign
import standard_font
standard_font.validate_font()
sign_gen = led_sign.LEDSign(standard_font)
sign_gen.generate_sign("A Test", "test.svg")`

