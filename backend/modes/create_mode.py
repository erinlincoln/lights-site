from modes.basic_modes import *

# Import custom modes here
from modes.twinkle import LEDMode_Twinkle
from modes.rainbow import LEDMode_Rainbow


# Creates a mode from the json received from an API request
def create_mode(length, mode_json):
    # Previously, the presence of the 'name' and 'data' properties have been verified
    # The only error checking we need to do is the contents of 'data' and the validity of 'name'

    match mode_json["name"]:
        case "off":
            return LEDMode_Solid(length, ["#000000"])
        case "solid":
            if "colors" not in mode_json["data"] or len(mode_json["data"]["colors"]) != 1:
                return None
            return LEDMode_Solid(length, [mode_json["data"]["colors"][0]])
        case "gradient":
            # TODO let gradient support more than 2 colors
            if "colors" not in mode_json["data"] or len(mode_json["data"]["colors"]) != 2:
                return None
            if "center" not in mode_json["data"] or mode_json["data"]["center"] < 0 or mode_json["data"]["center"] > 1:
                return None
            return LEDMode_Gradient(length, mode_json["data"]["colors"], mode_json["data"]["center"])
        case "multicolor":
            if "colors" not in mode_json["data"] or len(mode_json["data"]["colors"]) > length:
                return None
            return LEDMode_MultiColor(length, mode_json["data"]["colors"])
        case "runningmulticolor":
            if "colors" not in mode_json["data"]:
                return None
            if "speed" not in mode_json["data"]:
                return None
            return LEDMode_RunningMultiColor(length, mode_json["data"]["colors"], mode_json["data"]["speed"])
        
        # Append custom modes here
        case "twinkle":
            if "colors" not in mode_json["data"] or len(mode_json["data"]["colors"]) != 1:
                return None
            if "speed" not in mode_json["data"]:
                return None
            if "frequency" not in mode_json["data"]:
                return None
            return LEDMode_Twinkle(length, mode_json["data"]["colors"], mode_json["data"]["speed"], mode_json["data"]["frequency"])
        case "rainbow":
            if "speed" not in mode_json["data"]:
                return None
            return LEDMode_Rainbow(length, mode_json["data"]["speed"])
            
        # TODO implement others
        
    return None