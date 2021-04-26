import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()

class DS3225:

    def __init__(self, Pin, ZeroOffsetDuty, Angle):
        pi.set_mode(Pin, pigpio.OUTPUT)
        self.mPin = Pin
        self.m_ZeroOffsetDuty = ZeroOffsetDuty
        self.SetPos(Angle)

    def SetPos(self, pos):
        self.pos = pos
        #Duty ratio = 2.5%〜12.0% : 0.5ms〜2.4ms : 0 ～ 180deg
        duty = (12-2.5)*self.pos/180+2.5 + self.m_ZeroOffsetDuty
        pi.hardware_PWM(self.mPin, 50, int(duty * 10000))

    def Cleanup(self):
        pi.hardware_PWM(self.mPin, 50, 0)
        time.sleep(0.5)
        pi.set_mode(self.mPin, pigpio.INPUT)

if __name__ == '__main__':
    Servo = DS3225(Pin=18, ZeroOffsetDuty=0, Angle=0)
    try:
        while True:
            Servo.SetPos(0)
            time.sleep(1)
            Servo.SetPos(90)
            time.sleep(1)
            Servo.SetPos(180)
            time.sleep(1)
            Servo.SetPos(90)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        Servo.Cleanup()
        print("\nexit program")
