import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


IR_SENSOR_PILL = 3  # Sensor for low pill notification
IR_SENSOR_MEDICATION = 4  # Sensor for medication dispense
IR_SENSOR_HAND_DETECTION = 5  # Sensor for hand detection
LED_PIN = 6
BUZZER_PIN = 7

# Set up the GPIO pins
GPIO.setup(IR_SENSOR_PILL, GPIO.IN)
GPIO.setup(IR_SENSOR_MEDICATION, GPIO.IN)
GPIO.setup(IR_SENSOR_HAND_DETECTION, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def dispense_pills():
    # Replace this function with your pill dispensing mechanism
    print("Pills dispensed")

try:
    while True:
        # Check for low pill notification
        if GPIO.input(IR_SENSOR_PILL) == 1:
            # Send a notification through Wi-Fi
            print("Low pill notification via Wi-Fi")
        
        # Check if it's time for medication
        if GPIO.input(IR_SENSOR_MEDICATION) == 1:
            # Medication time, trigger the medication process
            GPIO.output(LED_PIN, GPIO.HIGH)
            GPIO.output(BUZZER_PIN, GPIO.HIGH) 
            dispense_pills()  
            GPIO.output(LED_PIN, GPIO.LOW)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
        
        # Check for hand detection
        if GPIO.input(IR_SENSOR_HAND_DETECTION) == 1:
            # Hand detected, dispense pills and send a notification
            dispense_pills()  # 
            print("Pill Dispensed")
            # Send a notification via Wi-Fi
            
        else:
            # No hand detected, set a reminder
            GPIO.output(LED_PIN, GPIO.HIGH)
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(5 * 60)  # Wait for 5 minutes (300 seconds)
            GPIO.output(LED_PIN, GPIO.LOW)
            GPIO.output(BUZZER_PIN, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()x