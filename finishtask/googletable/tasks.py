import datetime

from googletable.models.data import Data
from googletable.utils.utils import kurs_uah, google_read, telegram_sender
from finishtask.celery import app


@app.task
def update_orders():
    table_values = google_read()
    for el in table_values:
        massage_to_telegram = False
        if el[3] < datetime.date.today():
            massage_to_telegram = True
        up = Data.objects.update_or_create(
            ex_id=el[0],
            defaults={
                'order_id': el[1],
                'price_usd': el[2],
                'delivery_date': el[3],
                'price_uah': float(el[2]) * float(kurs_uah()),
                'massage_to_telegram': massage_to_telegram
            }
        )


@app.task
def massage_to_telegram():
    queryset = Data.objects.get(massage_to_telegram=True)
    for el in queryset:
        order_id = getattr(el, 'order_id')
        telegram_sender(order_id)
        el.delete()
