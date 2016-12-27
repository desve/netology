# sudo apt-get update
# sudo apt-get install imagemagick
# Пример запуска
# convert trump_mug.jpg -resize 200 1.jpg

import subprocess

file_name_input = 'trump_mug.jpg'
file_name_output = '1.jpg'

# proc = subprocess.Popen("ping -c2 %s" % ip, shell=True, stdout=subprocess.PIPE)
# out = proc.stdout.readlines()
# или
# out = proc.communicate()
# proc = subprocess.Popen('convert %s -resize 200 %s' % (file_name_input, file_name_output), 
#                         shell = True, stdout = subprocess.PIPE)
                      
proc = subprocess.call('convert trump_mug.jpg -resize 200 1.jpg', shell = True, stdout=subprocess.PIPE)

