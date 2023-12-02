import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

coil_A_1_pin = 13 # 4 pink
coil_A_2_pin = 26 # 17 orange
coil_B_1_pin = 6  # 23 blue
coil_B_2_pin = 19 # 24 yellow

StepCount=8
Seq = [
    [0,1,0,0],
    [0,1,0,1],
    [0,0,0,1],
    [1,0,0,1],
    [1,0,0,0],
    [1,0,1,0],
    [0,0,1,0],
    [0,1,1,0]
]


GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)


def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

def doThing():
    forward(int(1) / 1000.0, int(30))
    backwards(int(1) / 1000.0, int(30))


if __name__ == '__main__':
    doThing()
    time.sleep(1)