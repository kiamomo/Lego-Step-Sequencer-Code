import rtmidi
import mido
import cv2

#Test für eben gerade
# Midi Ports suchen
print("MIDI output ports: ", mido.get_output_names())
midiOutput = mido.open_output("Microsoft GS Wavetable Synth 0")

def sendControlchange(control, value):
	message = mido.Message('control_change', control=control, value=value)
	midiOutput.send(message)


for value in range(128):
	sendControlchange(7, value)
	cv2.waitKey(500)