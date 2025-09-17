from PIL import Image, ImageDraw, ImageFont

class WaterMarker:

    def __init__(self, input_filename: str, output_filename: str, watermark_text: str):
        self._input_f = input_filename
        self._output_f = output_filename
        self._font_location = r'font\font.ttf'
        self._font_size = 20
        self._h_spacing = 70
        self._v_spacing = 90
        self._font_opacity = 100
        self._watermarker_text = watermark_text
    
    def add_watermark(self):
        # Load IMG
        image = Image.open(self._input_f)

        # Add Watermark
        output = self.watermark(image, self._watermarker_text, self._font_location, self._font_size,
                                self._h_spacing, self._v_spacing, self._font_opacity)

        # Save Output IMG
        output.save(self._output_f)  # saving file

    @staticmethod
    def watermark(img, watermark_text, font_location, font_size, h_spacing, v_spacing, font_opacity):
        font = ImageFont.truetype(font_location, font_size)
        watermark_text = watermark_text
        im_width, im_height = img.size

        drawing = ImageDraw.Draw(img)
        bbox = drawing.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        im_text = Image.new('RGBA', (int(text_width), int(text_height)), (255, 255, 255, 0))
        drawing = ImageDraw.Draw(im_text)
        drawing.text((0, 0), watermark_text, fill=(255, 255, 255, font_opacity), font=font)

        current_width = im_width
        current_height = im_height

        up_down = +1

        while current_width > text_width + h_spacing:
            new_position = (current_width - text_width) - h_spacing, current_height + (up_down * (v_spacing // 2))
            img.paste(im_text, new_position, im_text)
            current_width, current_height = new_position

            repeat_current_width, repeat_current_height = new_position

            while repeat_current_height > text_height + v_spacing:
                repeat_new_position = repeat_current_width, (repeat_current_height - text_height - v_spacing)
                img.paste(im_text, repeat_new_position, im_text)
                repeat_current_width, repeat_current_height = repeat_new_position

            up_down *= -1

        return img
        