import serial, time, subprocess, os.path, os, UIstuff, pygame, DataSorter

pygame.init()

winsize = (150, 220)
win = pygame.display.set_mode(winsize)

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM3'
ser.open()

intensities = ["63", "126", "189", "252"]
colours = ["white", "red", "green", "blue", "far-red"]

count = 1

def sendcol(colour, intensity):
    values = bytearray(colour[0] + str(intensity), "utf-8")
    ser.write(values)

def generate_pickle(count, current_colour, current_intensity):
    generated_save_string = str(count)
    outfile = open("save_name_temp.txt", "w")
    outfile.writelines(generated_save_string)
    outfile.close()

    return generated_save_string

measure_button = UIstuff.Button(item_id="measure", width=150, height=70, passive_colour=(13, 255, 89), active_colour=(0, 212, 66), icon="Start Measure")
stop_button = UIstuff.Button(y=70, item_id="stop", width=150, height=70, passive_colour=(255, 35, 10), active_colour=(212, 22, 0), icon="Finish")
text_id = UIstuff.TextBox(y=160, x=70, text="id", font_colour=(255, 255, 255), font_size=40)

increment_button = UIstuff.Button(y=140, width=40, height=40, icon="+", item_id="increment")
decrement_button = UIstuff.Button(y=180, width=40, height=40, icon="-", item_id="decrement")

success_sound = pygame.mixer.Sound("success.wav")
startup_sound = pygame.mixer.Sound("startup.wav")

outfile = open("current_led_id.txt", "r")
led_id = int(outfile.read())
outfile.close()

led_id += 1

outfile = open("current_led_id.txt", "w")
outfile.writelines(str(led_id))
outfile.close()

startup_sound.play()
stop = False

while not stop:
    win = pygame.display.set_mode(winsize)

    measure_button.passive_colour, measure_button.active_colour = (13, 255, 89), (0, 212, 66)
    stop_button.passive_colour, stop_button.active_colour = (255, 35, 10), (212, 22, 0)
  
    measure_button.icon = "Start Measure"
    stop_button.icon = "Finish"
    paused = True

    while paused:
        win.fill((0, 0, 0))
        text_id.text = ("0"*(3-len(str(led_id)))) + str(led_id)
        text_id.draw(win)

        if measure_button.draw(win) == "measure":
            paused = False

            measure_button.icon = "Working..."
            stop_button.icon = "Working..."

            measure_button.passive_colour, measure_button.active_colour = (204, 204, 204), (204, 204, 204)  
            stop_button.passive_colour, stop_button.active_colour = (204, 204, 204), (204, 204, 204)

            measure_button.draw(win)
            stop_button.draw(win)

        if stop_button.draw(win) == "stop":
            stop = True
            paused = False

            pygame.quit()

        if increment_button.draw(win) == "increment":
            led_id += 1

            outfile = open("current_led_id.txt", "w")
            outfile.writelines(str(led_id))
            outfile.close()

            time.sleep(0.1)

        if decrement_button.draw(win) == "decrement":
            led_id -= 1
            led_id = max(led_id, 1)

            outfile = open("current_led_id.txt", "w")
            outfile.writelines(str(led_id))
            outfile.close()
            
            time.sleep(0.1)

        for event in pygame.event.get():
            pass

        pygame.display.update()

    pygame.display.quit()

    if not stop:
        subprocess.Popen(['java', '-jar', 'sik_sikuli.jar'], creationflags=subprocess.CREATE_NEW_CONSOLE)
 
        for i, intensity in enumerate(range(4)):
            for j, colour in enumerate(range(5)):
                xls_url = generate_pickle(count, colours[j], intensities[i])
                sendcol(colours[j], int(intensities[i]))

                while not os.path.isfile("lighttrigger.txt"):
                    pass

                while os.path.isfile("lighttrigger.txt"):
                    try:
                        os.remove("lighttrigger.txt")

                    except:
                        pass
    
                sendcol(colours[j], 0)
                time.sleep(1)
                count += 1

        time.sleep(3)
        
        DataSorter.XLSHandler(led_id)
        
        success_sound.play()
        led_id += 1
        outfile = open("current_led_id.txt", "w")
        outfile.writelines(str(led_id))
        outfile.close()