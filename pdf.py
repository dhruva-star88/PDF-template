from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

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

    # To set Footer, First we need to break the line to add text below
    pdf.ln(262)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    # This is the nested loop, we iterate over the pages to add the particular number of pages as in csv data
    # We subtract from 1, cuz we already have one page in the above parent iteration
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # To set footer for children pages
        pdf.ln(274)
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

pdf.output("notes.pdf")
