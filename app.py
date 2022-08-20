import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

# A dictionary holding all pins that are gonna be used
pins = {
   23 : {'name' : 'Munt', 'state' : GPIO.LOW},
   24 : {'name' : 'Bieslook en bramen', 'state' : GPIO.LOW}
   }

for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   templateData = {
      'pins' : pins
      }
   return render_template('main.html', **templateData)

@app.route("/<switchPin>/<action>")
def action(switchPin, action):
   switchPin = int(switchPin)
   PlantName = pins[switchPin]['name']
   if action == "on":
      GPIO.output(switchPin, GPIO.HIGH)
      message = "Watering " + PlantName
      time.sleep(15)
      GPIO.output(switchPin, GPIO.LOW)
      message = "Watering " + PlantName
   if action == "off":
      GPIO.output(switchPin, GPIO.LOW)
      message = "Watering " + PlantName

   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)