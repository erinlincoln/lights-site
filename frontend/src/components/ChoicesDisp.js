import React, { useContext } from 'react';
import ColorSelect from './ColorSelect';
import '../style/choicesDisp.css'

export default function ChoicesDisp({choices}) {

  return (
    <div onLoad={() => console.log(choices)} id='choices'>
        {choices.map( (disp, i) => 
            <div key={i}>
                <ColorSelect disp={disp} index={i}/>
            </div> )}
    </div>
  )
}
