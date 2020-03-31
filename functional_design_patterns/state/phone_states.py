from abc import ABC, abstractmethod


class PhoneState(ABC):
    @abstractmethod
    def ring(self):
        pass


class PlaneState(PhoneState):
    def ring(self):
        pass


class SilentState(PhoneState):
    def ring(self):
        print('Shine the screen.')


class VibrationState(PhoneState):
    def ring(self):
        print('Vibrate')


class NormalState(PhoneState):
    def ring(self):
        print('Ring the ringtone.')
