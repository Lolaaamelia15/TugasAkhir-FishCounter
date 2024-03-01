import requests
import json
import newCounter
from time import sleep
from servo import Servo
from waterpump import Waterpump
from buzzer import Buzzer
import lcd
import cProfile

servo = Servo()
waterpump = Waterpump()
buzzer = Buzzer()

while(True):
    try:
        print("getting status..")
        x = requests.get('https://fishcounterta.000webhostapp.com/status.php')
        response_json = x.json()

        # Mengekstrak nilai dari JSON
        # id_value = response_json['id']
        hitung_status = response_json['hitung']

        if hitung_status == 'true':
            jumlah_value = 15
            harga_value = 500
            # jumlah_value = int(response_json['jumlah'])
            # harga_value = int(response_json['harga'])

        jumlah_ikan = 0
        while (jumlah_ikan < jumlah_value):
            servo.close()    # Tutup servo
            jumlah_ikan += newCounter.count(interval=10) # call hitung
            print("jumlah ikan : " +str(jumlah_ikan))
            servo.open()                # Hidupkan servo
            # time.sleep(10) # waktu untuk mengeluarkan ikan        # Matikan waterpump
        newCounter.stopProgram( )   
        lcd.tampil(jumlah_value,harga_value*jumlah_value)
        # lcd.tampil(10,10*10)
        buzzer.turn_on_buzzer()
            
        print(jumlah_value, jumlah_value*harga_value) # Print harga total di terminal

            # reset table status
            # x = requests.post('https://fishcounterta.000webhostapp.com/status.php') 
            # print(x.json())

    except KeyboardInterrupt:
        waterpump.turn_off_waterpump()
        waterpump.stop()
        servo.close()
        servo.stop()
        # lcd_display.stop()
        break

    except Exception as e:
        waterpump.turn_off_waterpump()
        servo.close()
        # lcd_display.stop()
        print(e.args)
    #     print(traceback.format)
        
    finally:
        sleep(3)

