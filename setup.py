from distutils.core import setup
setup(
  name = 'pybleno',
  packages = ['pybleno', 'pybleno/hci_socket',  'pybleno/hci_socket/BluetoothHCI'], # this must be the same as the name above
  # v0.11.1:
  #  - 'Fix hci_ufilter struct member alignment padding to pad opcode by 2 bytes. #63'
  # v0.11.2:
  #  - 'HCI: increase maxMtu to 128 for Realtek chips'
  version = '0.11.2',
  description = 'A direct port of the Bleno bluetooth LE peripheral role library to Python2/3',
  author = 'Adam Langley',
  author_email = 'github.com@irisdesign.co.nz',
  url = 'https://github.com/Adam-Langley/pybleno', # use the URL to the github repo
  download_url = 'https://github.com/pseiderer/pybleno/archive/refs/tags/v0.11.2.tar.gz', # I'll explain this in a second
  keywords = ['Bluetooth', 'Bluetooth Smart', 'BLE', 'Bluetooth Low Energy'], # arbitrary keywords
  classifiers=[
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4'
  ]
)
