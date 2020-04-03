from functional_design_patterns.state.phone import *

normal_state = NormalState()
vibration_state = VibrationState()
silent_state = SilentState()
plane_state = PlaneState()

phone = Phone()

phone.ring()
phone.set_state(silent_state)
phone.ring()
phone.set_state(plane_state)
phone.ring()
phone.ring()
phone.set_state(vibration_state)
phone.ring()
phone.set_state(normal_state)
phone.ring()
