from random import randbytes
from constants import *



# MODE_SOLID (Off version)
def genData_Off(strip):

    # Construct data
    data = bytearray()
    try:
        data.append(strip) # Strip index
        data.extend(bytearray.fromhex("000000")) # Color data
    except:
        return None

    # Length check
    if len(data) != 4:
        return None
    return data


# MODE_SOLID
def genData_Solid(strip, mode_json):
    # Error checking
    if "colors" not in mode_json["data"] or len(mode_json["data"]["colors"]) != 1:
        return None

    # Construct data
    data = bytearray()
    try:
        data.append(strip) # Strip index
        data.extend(bytearray.fromhex("".join(mode_json["data"]["colors"][0][1:]))) # Color data
    except:
        return None

    # Length check
    if len(data) != 4:
        print("Bad length check. ", data)
        return None
    return data

# MODE_GRADIENT
def genData_Gradient(strip, mode_json):
    # Error checking
    if "colors" not in mode_json["data"] or len(mode_json["data"]["colors"]) != 2:
                return None
    if "center" not in mode_json["data"] or mode_json["data"]["center"] < 0 or mode_json["data"]["center"] > 1:
        return None

    # Construct data
    data = bytearray()
    try:
        data.append(strip) # Strip index
        data.append(int(mode_json["data"]["center"] * 255)) # Center
        data.extend(bytearray.fromhex("".join(mode_json["data"]["colors"][0][1:]))) # Color 1
        data.extend(bytearray.fromhex("".join(mode_json["data"]["colors"][1][1:]))) # Color 2
    except:
        return None

    # Length check
    if len(data) != 8:
        return None
    return data

# MODE_MULTICOLOR
def genData_Multicolor(strip, mode_json):
    # Error checking
    if "colors" not in mode_json["data"]:
        return None

    # Construct data
    data = bytearray()
    try:
        data.append(strip) # Strip index
        for color in mode_json["data"]["colors"]:
            data.extend(bytearray.fromhex("".join(color[1:]))) # Color data
    except:
        return None

    return data

# MODE_RUNNINGMULTICOLOR
def genData_RunningMulticolor(strip, mode_json):
    # Error checking
    if "colors" not in mode_json["data"]:
        return None
    if "speed" not in mode_json["data"] or mode_json["data"]["speed"] < 0 or mode_json["data"]["speed"] > 1 :
        return None

    # Construct data
    data = bytearray()
    try:
        data.append(strip) # Strip index
        data.append(int(mode_json["data"]["speed"] * 32766)) # Speed
        for color in mode_json["data"]["colors"]:
            data.extend(bytearray.fromhex("".join(color[1:]))) # Color data
    except:
        return None

    return data

# MODE_SHIMMER
def genData_Shimmer(strip, mode_json):
    # Error checking
    if "colors" not in mode_json["data"] or len(mode_json["data"]["colors"]) != 1:
        return None
    if "speed" not in mode_json["data"]:
        return None
    if "frequency" not in mode_json["data"]:
        return None

    # Construct data
    data = bytearray()
    try:
        data.append(strip) # Strip index
        data.append(int(mode_json["data"]["speed"] * 32766)) # Speed
        data.append(int(mode_json["data"]["frequency"] * 32766)) # Frequency
    except:
        return None

    # Length check
    if len(data) != 5:
        return None
    return data

# MODE_RAINBOW
def genData_Rainbow(strip, mode_json):
    print("entering rainbow")
    # Error checking
    if "speed" not in mode_json["data"]:
        print("speed not found")
        return None

    # Construct data
    data = bytearray()
    try:
        data.append(strip) # Strip index
        #data.append(int(mode_json["data"]["speed"] * 32766)) # Speed
        data.extend(((int)(mode_json["data"]["speed"] * 32766)).to_bytes(2, 'big')) # Speed
        
    except Exception as e:
        print(e)
        return None

    # Length check
    if len(data) != 3:
        return None
    return data
    
def create_ota_message():
    message = bytearray()
    
        # Message ID: random 4-byte value
    message.extend(randbytes(4))
    message.extend(TASK_OTA.to_bytes(1, 'big'))
    l = (len(message) + 2)
    message.extend(l.to_bytes(2, 'big'))
    return message
    

# Creates the mode data string to send to a satellite as specified in backend_v3_standard.txt
def create_mode_message(strip, mode_json):
    # Previously, the presence of the 'name' and 'data' properties have been verified
    # The only error checking we need to do is the contents of 'data' and the validity of 'name'

    message = bytearray()

    # Message ID: random 4-byte value
    message.extend(randbytes(4))

    task_id = TASK_UNUSED
    data = None

    # Generate data
    match mode_json["name"]:
        case "off":
            task_id = TASK_MODE_SOLID
            data = genData_Off(strip)
        case "solid":
            task_id = TASK_MODE_SOLID
            data = genData_Solid(strip, mode_json)
        case "gradient":
            task_id = TASK_MODE_GRADIENT
            data = genData_Gradient(strip, mode_json)
        case "multicolor":
            task_id = TASK_MODE_MULTICOLOR
            data = genData_Multicolor(strip, mode_json)
        case "runningmulticolor":
            task_id = TASK_MODE_RUNNING_MULTICOLOR
            data = genData_RunningMulticolor(strip, mode_json)
        case "shimmer":
            task_id = TASK_MODE_SHIMMER
            data = genData_Shimmer(strip, mode_json)
        case "rainbow":
            task_id = TASK_MODE_RAINBOW
            data = genData_Rainbow(strip, mode_json)
        case _:
            return None
    
    if data is None:
        return None
    
    message.extend(task_id.to_bytes(1, 'big'))

    l = (len(message) + len(data) + 2)
    if l > MAX_MESSAGE_LENGTH:
        return None
    message.extend(l.to_bytes(2, 'big'))
    message.extend(data)
    return message

