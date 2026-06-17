fro import TextClip

clip = TextClip(text="Hello", font_size=70)
clip.duration = 5
clip.write_videofile("output.mp4", fps=24)
