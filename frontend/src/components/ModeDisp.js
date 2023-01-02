import Restart from "./Restart";
import ModeSelect from "./ModeSelect";
import React, {useContext, useState} from "react";
import ChoicesDisp from "./ChoicesDisp";
import { StateContext } from "./Main";

export default function ModeDisp() {

  const { choices } = useContext( StateContext );

  return (
    <div>
        <Restart/>
        <ModeSelect />
        { choices && 
            <ChoicesDisp />   
        }
    </div>
  )
}
