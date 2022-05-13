from common.format import format_date

import datetime

# modelのインスタンスの操作


def delete_instance(model, id_name, pk):

    if(id_name == "id"):
        instances = model.objects.filter(id=pk)
    elif(id_name == "sort"):
        instances = model.objects.filter(sort=pk)

    for instance in instances:
        instance.delete_flg = True
        instance.update_date = format_date(datetime.datetime.now())
        instance.save()
