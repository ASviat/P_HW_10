# Задание 5.

# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
# преобразовать результаты из байтовового в строковый тип на кириллице.

# Подсказки:
# --- используйте модуль chardet, иначе задание не засчитается!!!

import subprocess
import chardet

ARGS = ['ping', 'youtube.com']
I_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
print(I_PING.stdout)
for line in I_PING.stdout:
    result = chardet.detect(line)
    print(line.decode(result['encoding']))
