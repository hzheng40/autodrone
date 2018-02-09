# Autodrone

## Part I: Build List
**Quadrotor platform**: custom platform with 130mm X-plate, 1306(?) brushless motors, 4-in-1 ESC, PDB, Crazyflie 2.0 with BigQuad deck, Rpi zero w with pi camera v2.

**Video capture pipeline**: Gstreamer with gst-rpicamsrc on rpi, gstreamer and OpenCV built with gstreamer on PC.
PC side example code: `capture_test.py`
Pi Zero side example code: `cap.sh`
Install script and dependecies will come later.