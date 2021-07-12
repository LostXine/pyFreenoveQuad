# Format:  [transStart] [order] [data 0] [data 1] ... [data n] [transEnd]
#          [x] is byte type and the range of [order] and [data x] is 0~127
# Process: The requesting party send the order, then the responding party respond the order.
#          The non blocking order will be responded immediately, and the blocking order will
#          be responded orderStart immediately, then respond orderDone after completion.

# Data stream control orders, range is 128 ~ 255
# These orders are used to control data stream.

transStart = 128;
transEnd = 129;


# Orders, range is 0 ~ 127
# Orders are used to control target.
# Some orders have proprietary response orders, others use orderStart and orderDone.
# The even orders is sent by the requesting party, and the odd orders is sent by the responding party.

# Non blocking orders, range is 0 ~ 63

# Connection
# Request echo, to confirm the target
requestEcho = 0;                # [order]
# Respond echo
echo = 1;                       # [order]

# Function
# Request supply voltage
requestSupplyVoltage = 10;      # [order]
# Respond supply voltage
supplyVoltage = 11;             # [order] [voltage * 100 / 128] [voltage * 100 % 128]
# Request change I/O port state
requestChangeIO = 20;           # [order] [IOindex] [1/0]

# Installation
requestMoveLeg = 30;            # [order] [leg] [64 + dx] [64 + dy] [64 + dz]
requestCalibrate = 32;          # [order]

# Blocking orders, range is 64 ~ 127

# Installation
requestInstallState = 64;       # [order]
requestCalibrateState = 66;     # [order]
requestBootState = 68;          # [order]
requestCalibrateVerify = 70;    # [order]

# Simple action
requestCrawlForward = 80;       # [order]
requestCrawlBackward = 82;      # [order]
#requestCrawlLeft = 84;          # [order]
#requestCrawlRight = 86;         # [order]
requestTurnLeft = 88;           # [order]
requestTurnRight = 90;          # [order]
requestActiveMode = 92;         # [order]
requestSleepMode = 94;          # [order]
requestSwitchMode = 96;         # [order]

# Complex action
#requestCrawl = 110;             # [order] [64 + x] [64 + y] [64 + angle]
#requestChangeBodyHeight = 112;  # [order] [64 + height]
requestMoveBody = 114;          # [order] [64 + x] [64 + y] [64 + z]
requestRotateBody = 116;        # [order] [64 + x] [64 + y] [64 + z]
requestTwistBody = 118;         # [order] [64 + xMove] [64 + yMove] [64 + zMove] [64 + xRotate] [64 + yRotate] [64 + zRotate]

# Universal responded orders, range is 21 ~ 127
# These orders are used to respond orders without proprietary response orders.

orderStart = 21;                # [order]
orderDone = 23;                 # [order]
