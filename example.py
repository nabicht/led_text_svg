import led_sign
import standard_font
standard_font.validate_font()
sign_gen = led_sign.LEDSign(standard_font)
sign_gen.generate_sign("A Test", "test.svg")
