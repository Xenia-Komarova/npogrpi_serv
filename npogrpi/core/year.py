from datetime import datetime


def year(request):
    """
    Добавляет переменную с текущим годом.
    """
    dty = datetime.now().year
    return {'year': dty}