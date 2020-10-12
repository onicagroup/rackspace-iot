03 - Rackspace IoT Feature Tour
===============================

ESP32 Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Your Rackspace IoT Development board is built around the powerful Esspresif ESP32 Microcontroller Unit (MCU).  The ESP32 chip is small and affordable, with features that are perfectly suited for a broad range of IoT applications. The ESP32 is equipped with GPIO pins, and includes support for a variety of protocols like SPI, I2C, UART, and more.

One key feature of the ESP32 is that both wireless networking and Bluetooth are included onboard the MCU itself.  This sets the ESP apart from other microcontrollers like those found on boards like Arduino and Rasberry Pi, for which WiFi and Bluetooth require additional onboard components or add on hardware. This means that you can easily control and monitor ESP32-based devices remotely without the need for additional WiFi or Bluetooth components.

.. image:: ../img/esp32-chip.png
    :align: center
    :alt: ../img/esp32-chip.png
    :width: 200px

**Features of the ESP32 MCU:**

- Xtensa Dual-Core 32-bit LX6 with 600 DMIPS @160 MHz
- 802.11 b/g/n Wi-Fi
- Bluetooth 4.2 and BLE
- SRAM and Flash capable
- 36 GPIO pins
- 16 software PWM channels
- Common protocol interfaces: 4 SPI, 2 I2C, 2 I2S, 2 UART
- 12-Bit Analog to Digital Converter (ADC)
- Controller Area Network (CAN) enabled
- Ethernet MAC interface
- Onboard sensors

   - Capacative touch
   - Temperature
   - Hall effect
- Operating temp range: -40ºC to 125ºC

----

Rackspace IoT Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Rackspace IoT Development board expands on the capabilities of the ESP32 chip, by providing additional hardware common to many enterprise IoT development projects.  Below is a diagram of the Rackspace IoT board and its components:

1. ESP32 MCU
2. 3.3V Serial JST connector
3. Barrel jack power connector
4. External battery connector, and onboard charger
5. LTE Cell modem ready
6. STATUS LED
7. Button
8. 3 JST connectors, wired for I2C
9. 30-pin breakout board/breadboard adapter, with pinout diagram
10. Micro-USB port, which provides USB to serial and can power the board (not shown)

.. image:: ../img/rackspace-iot-1.svg
    :align: center
    :alt: ../img/rackspace-iot-1.svg
    :width: 400px

.. image:: ../img/rackspace-iot-2.svg
    :align: center
    :alt: ../img/rackspace-iot-2.svg
    :width: 600px

----

Convenience Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Rackspace IoT boards include a number of convenience functions baked into the ``rackspaceiot`` module of the Micropython firmware.  These functions allow developers to easily interact with the sensors of the ESP32 as well as some hardware
features of the board.  In this section, we will walk through the convenience functions that are available.

This section assumes you have:

- A working Rackspace IoT Developer Kit
- Succesfully completed the setup process for your device in section :doc:`../setup/setup`, and you are currently connected to your device via your WiFi and WebREPL session.

Below are descriptions of the the available convenience functions:

- ``rackspaceiot.led('on')`` - turns the STATUS LED on
- ``rackspaceiot.led('off')`` - turns the STATUS LED off
- ``rackspaceiot.blink(delay_ms, duration_sec)`` - blinks the STATUS LED with a delay in ms and duration in seconds
- ``rackspaceiot.hall()`` - reads the value of the onboard hall effect sensor, which can be used to measure magnetic fields near the ESP32 chip.
- ``rackspaceiot.temp()`` - reads the value of the onboard temperature sensor.
- ``rackspaceiot.touch()`` - reads the value of an onboard capacitive touch sensor, mapped to PIN12 on the Rackspace IoT board.
- ``rackspaceiot.read_all()`` - reads all onboard sensor values above, and returns them in JSON format.

Using the WebREPL console terminal, you can experiment with the different functions above.    Here are some examples::

    >> rackspaceiot.led('on')
    # STATUS LED turns on

    >> rackspaceiot.led('off')
    # STATUS LED turns off

    >> rackspaceiot.blink(500, 10)
    # STATUS LED blinks every 500 milliseconds, for 10 seconds

    >> rackspaceiot.hall()
    73

    >> rackspaceiot.temp()
    131

    >> rackspaceiot.touch()
    375

    >> rackspaceiot.read_all()
    {"touch": 375, "hall": 69, "temp": 131}

Now, try to vary the sensor readings, and run each function again to see the values change.  Examples:

- Place the Rackspace IoT board in a warm place, in direct sunlight, or touch the metal MCU case with your hand to change the ``temp()`` reading.

    - Note: it will change *very* little due to the low resolution of the onboard temp sensor
- Place a magnet near the MCU chip, and see the ``hall()`` reading change.
- Insert a jumper wire into the breadboard next to pin12 on the Rackspace IoT breakout board.  Touch the free end of the jumper with your finger, and see the ``touch()`` reading change.

Next, try to read all the sensor values continuously.  Using the methods described above, you can vary the sensor readings in realtime, and watch them change in the WebREPL output::

    >> from time import sleep
    >> while True:
    ..     rackspaceiot.read_all()
    ..     sleep(1)
    # press Enter 4 times
    {"touch": 382, "hall": 70, "temp": 132}
    {"touch": 382, "hall": 70, "temp": 132}
    {"touch": 382, "hall": 68, "temp": 132}
    {"touch": 382, "hall": 71, "temp": 132}
    ...
    ...

    # Ctrl+C to break
    Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
    KeyboardInterrupt: 
    >> 


Note that on-chip sensor readings are not calibrated to any particular scale, nor are they expected to be terribly consistent from device to device.  For example, the temperature reading is just a raw sensor value, it does not map directly to an actual temperature value.  For more reliable readings, we will use more accurate sensors in the next section.