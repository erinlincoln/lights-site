# Define constants here for global use.

# Task IDs
TASK_UNUSED                     = 0x00
TASK_PING                       = 0x01
TASK_GET_ERROR                  = 0x02
TASK_GET_LAST_MSG               = 0x03
TASK_SYNC_TIME                  = 0x04
TASK_OTA                        = 0x05

TASK_RAW_LED_COMMAND            = 0x10
TASK_MODE_SOLID                 = 0x11
TASK_MODE_GRADIENT              = 0x12
TASK_MODE_MULTICOLOR            = 0x13
TASK_MODE_RUNNING_MULTICOLOR    = 0x14
TASK_MODE_TWINKLE               = 0x15
TASK_MODE_RAINBOW               = 0x16

# Maximum message length
MAX_MESSAGE_LENGTH = 7 + 303

# ip addresses
IP_OFFICE =     '192.168.0.26' # V
IP_HALLWAY =    '192.168.0.19' # IV
IP_LIVINGROOM = '192.168.0.20' # III
IP_BEDROOM =    '192.168.0.23' # II
# unused:       '192.168.0.15' # I