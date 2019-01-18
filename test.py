from openpyxl.chart import (
    Reference, Series,
    ScatterChart
)
import openpyxl

book = openpyxl.Workbook()
sheet = book.active

rows = [
    ['Size', 'Batch 1', 'Batch 2'],
    [2, 40, 30],
    [3, 40, 25],
    [4, 50, 30],
    [5, 30, 25],
    [6, 25, 35],
    [7, 20, 40],
]
for row in rows:
    sheet.append(row)

chart = ScatterChart()
chart.style = 13
chart.x_axis.title = 'Size'
chart.y_axis.title = 'Percentage'

xvalues = Reference(sheet, min_col=1,
			 min_row=2, max_row=7)

for i in range(2, 4):
    values = Reference(sheet, 
				min_col=i, 
				min_row=1, 
				max_row=7)
    series = Series(values, xvalues, 
				title_from_data=True)
    chart.series.append(series)

sheet.add_chart(chart, "A10")

book.save("./scraping/results/data/test.xlsx")
