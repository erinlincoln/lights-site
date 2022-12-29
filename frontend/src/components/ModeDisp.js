import Restart from "./Restart";
import ModeSelect from "./ModeSelect";
import React, {useContext, useState} from "react";
import ChoicesDisp from "./ChoicesDisp";

export default function ModeDisp() {
    const [choices, setChoices] = useState();

  return (
    <div>
        <Restart/>
        <ModeSelect setChoices={setChoices}/>
        { choices && 
            <ChoicesDisp choices={choices}/>   
        }
    </div>
  )
}
