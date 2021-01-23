from win32com.client import Dispatch

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)

if __name__=='__main__':
    speak(" A VERY VERY HAPPY NEW YEAR EVERYONE.  FROM DIRGH..")