import os, glob
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

F = r"C:\Users\HP\Downloads\docs\docs_statement"
COLS, ROWS = 3, 2
M = 30   # 0.5 inch = 36 points
G = 11   # ~20px gap between images

files = sorted(set(f for e in ["*.jpg","*.jpeg","*.png","*.webp"]
                   for f in glob.glob(os.path.join(F, e))))
print(len(files), "images found")

pw, ph = A4
cw = (pw - 2*M - G*(COLS-1)) / COLS
ch = (ph - 2*M - G*(ROWS-1)) / ROWS

c = canvas.Canvas("screenshots_grid.pdf", pagesize=(pw, ph))

for i in range(0, len(files), COLS*ROWS):
    chunk = files[i:i+COLS*ROWS]
    for idx, f in enumerate(chunk):
        col = idx % COLS
        row = idx // COLS
        cx = M + col*(cw+G)
        cy = ph - M - (row+1)*ch - row*G
        c.drawImage(f, cx, cy, cw, ch, mask="auto")
    c.showPage()

c.save()
print("Done! screenshots_grid.pdf saved")
