06 - Helpful Hints
===========================

Re-importing module code
++++++++++++++++++++++++
- When troubleshooting your code, sometimes you will want to ``import my_script`` again in the same session.  However, if you've already imported that module in a given session, MicroPython will not import it again.  To resolve this::

    >> import sys
    >> del sys.modules['my_script'] #do not include the .py extension
    >> import my_script

Resetting device into access point mode
+++++++++++++++++++++++++++++++++++++++
- If you lose connection with your device and cannot re-establish it, use Safe Mode boot to re-enable the access point and re-connect to your board: 

    1. Power off the device by unplugging the micro usb cable.
    2. Press **and hold** the blue button on the device.
    3. While continuing to hold the button, power on the device by plugging the micro usb cable back into the device.
    4. Carefully watch the STATUS LED, located above the button.
    5. When the LED blinks rapidly for 5 seconds, your device has entered **safe boot mode**
    6. Release the button
    7. Connect to the device AP and WebREPL using the same steps described in section :doc:`../setup/setup`, starting with the section labelled **Connect to Your Device**
