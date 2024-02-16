from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

data = pd.read_csv("pdf_topics.csv")

# The following for loop gives the access to every row of the csv file
for index, row in data.iterrows():
    # add_page adds the page
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    # Here args of text_color is codes of RGB
    pdf.set_text_color(100, 100, 100)
    # With the help of cell only we can write the data into pdf, so we should call that function
    # Here align="L" means txt will start from left side of the pdf page
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # Here arguments of line are x1,y1,x2,y2 => x1,y1 represents starting point and x2,y2, represents ending point
    pdf.line(10, 21, 200, 21)


pdf.output("notes.pdf")
