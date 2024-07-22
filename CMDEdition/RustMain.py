from pymem import Pymem
import pymem.exception as exc
import pymem.process as proc
import os
import time
import PyLibBass_Python as pylib
import threading
readedfile = bytes("SpazeRev.mp3", "UTF-8")
def Main():
    print("RustClientInjector by RiritoNinigaya")
    print("This is My First Injector for GAME Rust(Unity3D)")
    pylib.bass_library.BASS().BASS_INIT(device=-1, freq=44100, flags=0, win=0, dsguid=0)
    pylib.bass_library.BASS().BASS_START()
    stream_spazerev = pylib.bass_library.BASS().BASS_StreamCreateFile(mem=0, filename=readedfile, offset=0, length=0, flags=0x4)
    pylib.bass_library.BASS().BASS_ChannelPlay(stream_spazerev, False)
    time.sleep(8)
    try:
        rustclient = Pymem("RustClient.exe")
        superiority = bytes("superity2553.dll", "UTF-8")
        proc.inject_dll(rustclient.process_handle, superiority)
        time.sleep(45)
        print("This DLL Is Founded And Injected Successfully")
        time.sleep(3)
        print("Thank you for Choosing This Injector!!!")
        time.sleep(35)
        exit(445)
    except(exc.CouldNotOpenProcess, exc.PymemError, exc.WinAPIError):
        print("Failed to Find RustClient Process")
        time.sleep(13)
        exit(554)

if __name__ == "__main__":
    Main()