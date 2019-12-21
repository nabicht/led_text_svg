"""
This file is part of led_text_svg.

MIT License

Copyright (c) 2016-2017 Peter F. Nabicht

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import json
import svgwrite

class LEDSign(object):

    def __init__(self, font, kerning=2, space=5, point_radius=4, point_space=2):
        assert kerning > 0, "kerning must be greater than 0"
        assert space >= 0, "space must be greater than or equal to 0"
        assert font is not None, "font must be defined"
        assert point_radius > 0, "point_radius must be greater than 0"
        assert point_space >= 0, "point space must be greater than or equal to 0"
        self._font = font
        self._kerning = kerning
        self._space =  space
        self._point_size = point_radius + 2
        self._point_space = space
        self._kerning_width = (self._kerning * self._point_size) + ((self._kerning - 1) * self._point_space)
        self._point_radius = point_radius

    def _generate_character(self, starting_point, svg, char):
        x = starting_point[0]
        y = starting_point[1]
        if char is " ":
            x = x + (self._space * self._point_size) + (self._space * self._point_space)
        else:
            # look up character
            font_char = self._font.character_map.get(char)
            if font_char is None:
                raise "Font %s does not know %s" % (self._font.__class__.__name__, char)
            
            char_y = y
            for line in font_char:  # go through list of lines backwards because want to write the bottom line first
                char_x = x
                for point in line:
                    if point == 1:
                        svg.add(svg.circle(center=(char_x+self._point_radius, char_y+self._point_radius), 
                                           r=self._point_radius, fill='black', stroke='black', stroke_width=1))
                    char_x += self._point_size + self._point_space
                char_y += self._point_size + self._point_space
            font_width = len(font_char[0])
            # kerning applied after a character
            x = x + (font_width * self._point_size) + ((font_width - 1) * self._point_space) + self._kerning_width  # one less space between points than there are points
        return (x, y)

    def generate_sign(self, text, file_name):        
        dwg = svgwrite.Drawing(file_name, profile='tiny')
        starting_point = (0, 0)
        for char in text:
            starting_point = self._generate_character(starting_point, dwg, char)
        dwg.save()

    def settings(self):
        d = {"font": self._font.__class__.__name__,
             "kerning": self._kerning,
             "space": self._space,
             "point_radius": point_radius,
             "point_space": point_space}
        return json.dumps(d)


