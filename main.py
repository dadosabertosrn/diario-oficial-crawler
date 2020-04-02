from datetime import date, timedelta
from helpers import check_output_path, get_pdf_by_date


current_date = date.today()
check_output_path()

while True:
    get_pdf_by_date(current_date)
    current_date = current_date - timedelta(days=1)
