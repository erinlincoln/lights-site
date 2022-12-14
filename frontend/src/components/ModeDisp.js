import Restart from "./Restart";
import ModeSelect from "./ModeSelect";
import React, {useState} from "react";
import ChoicesDisp from "./ChoicesDisp";

export default function ModeDisp({mode, setMode, colors, setColors, zone, setPickingZone}) {
    const [choices, setChoices] = useState();

  return (
    <div>
        <Restart zone={zone.name} setPickingZone={setPickingZone}/>
        <ModeSelect setColors={setColors} setMode={setMode} setChoices={setChoices}/>
        { choices && 
            <ChoicesDisp choices={choices} colors={colors}/>   
        }
    </div>
  )
}
