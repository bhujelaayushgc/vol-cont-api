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
        self.current_vol = self.volume.GetMasterVolumeLevelScalar()
        return round(self.current_vol * 100)

    def set_vol(self, vol_level):
        self.current_vol = vol_level / 100
        self.__update_vol()

    def mute(self):
        self.volume.SetMute(1, None)
    
    def unmute(self):
        self.volume.SetMute(0, None)

    def __update_vol(self):
        self.volume.SetMasterVolumeLevelScalar(self.current_vol, None)

    def vol_up(self):
        self.current_vol += 0.01
        self.__update_vol()

    def vol_down(self):
        self.current_vol -= 0.01
        self.__update_vol()
