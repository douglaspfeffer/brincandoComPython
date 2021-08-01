#python -m pip install win10toast

from win10toast import ToastNotifier

import time

#inicialização

toaster=ToastNotifier()

#Exibir notificação sempre que preciso

toaster.show_toast('Notification','Alert! Yes',threaded=True,icon_path=None,duration=3)

#Para verificar se alguma notificação está ativa utilize, 'toaster.notification_active()'

while toaster.notification_active():
    time.sleep(0.1)
