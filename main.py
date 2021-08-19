import ds3225
from fastapi import FastAPI
import RPi.GPIO as GPIO

UNLOCKED_DEG = 175

Servo = ds3225.DS3225(18, ZeroOffsetDuty=0, Angle=UNLOCKED_DEG)
app = FastAPI()

@app.get("/servo/{pos}")
def set_pos(pos: int):
   if pos > 180:
      pos = 180
   elif pos < 0:
      pos = 0
   before_pos = Servo.pos
   Servo.SetPos(pos)
   return {
       "before": before_pos,
       "after": Servo.pos
   }
@app.get("/servo/")
def get_pos():
   return {
       "deg": Servo.pos
   }
