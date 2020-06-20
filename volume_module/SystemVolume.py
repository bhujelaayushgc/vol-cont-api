from ctypes import POINTER, cast

from comtypes import CLSCTX_ALL, CoInitialize, CoUninitialize

from pycaw.pycaw import (AudioUtilities, IAudioEndpointVolume)


class SystemVolume():
    def __init__(self):
        CoInitialize()
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))
        self.current_vol = self.volume.GetMasterVolumeLevelScalar()
        CoUninitialize()

    def get_vol(self):
        return round(self.current_vol * 100)

    def __update_vol(self):
        self.volume.SetMasterVolumeLevelScalar(self.current_vol, None)

    def vol_up(self):
        self.current_vol += 0.02
        self.__update_vol()

    def vol_down(self):
        self.current_vol -= 0.02
        self.__update_vol()
