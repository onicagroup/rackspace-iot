02 - IoT `Hello World` on AWS
==============================

The intent of this section is to go from zero to a working IoT project in just a few minutes and a few simple lines of code.  This section emphasizes simplicity and getting your Rackspace IoT DevKit sending IoT data as quickly as possible, without slowing down to examine what is happening under the hood.  In later sections, we will dive deeper into the underlying functionality demonstrated here.

This walkthough assumes you have succesfully completed the assembly setup process for your device in section :doc:`../setup/setup` and you are currently connected to your device via your WiFi and WebREPL session.

----

Add Config Values to `hello_world.py`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- In your Rackspace IoT repository, navigate to ``hello_world.py`` in the root directory, and open that file in a text editor.
- Edit the lines below, replacing the values with the values provided by your lab instructor.  **All values are 100% lower case**::

    # config
    thing_id = 'team_name'                     # choose a team name: all lowercase, _ separator, no special chars
    company_name = 'aws'                       # always use 'aws' here.
    endpoint = 'aws_iot_endpoint_dns_hostname' # find this in labinfo.txt

- **Save** the file, and close the text editor.


Upload files to your Rackspace IoT device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Back in the WebREPL session in your browser, ensure your session is still active. Place your cursor in the REPL console, and press the **Enter** key several times.  If your session is active, each press should return a Python REPL prompt ``>>>``.  If not, click **Disconnect**, refresh the page, and reconnect as before.  Do not proceed until your WebREPL sesssion is active.

- Using the same **Choose File>>Send to device** method that you used during Setup to upload your WiFi connection info, transfer the following three files one at a time to the device:

1. The certificate from your lab zip file, ending in ``-certificate.pem.crt``
2. The private key from your lab zip file, ending in ``-private.pem.key``
3. The ``hello_world.py`` file that you edited above.
    
- Ensure each file uploaded sucessfully, by listing the files in the WebREPL::

    >> import os
    >> os.listdir()
    ['boot.py', 'rackspace_iot_cfg.json', 'ab12345678-certificate.pem.crt', 'ab12345678-private.pem.key', 'hello_world.py']
    >> 

- If any uploaded file is missing from the list of files on the device, upload and list again until all three files are listed on the device.


Send 'Hello World!' to AWS IoT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- In the WebREPL terminal, run the ``hello_world.py`` script, and notice the message publishing logs.  Note: to execute a script manually in Micropython, you ``import`` the script as a module, leaving off the ``.py`` extension as shown below.

::

    >> import hello_world
    published to topic iotsample/company_name/first_last/data: {'message': 'Hello World from <thingId>'}
    published to topic iotsample/company_name/first_last/data: {'message': 'Hello World from <thingId>'}
    ...
    ...

- To stop sending messages, type ``Ctrl+C`` in your WebREPL console terminal, you will see the execution break below, which is normal::

    Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
    KeyboardInterrupt: 
    >> 
