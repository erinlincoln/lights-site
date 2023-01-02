import React, { useContext } from 'react';
import ColorSelect from './ColorSelect';
import '../style/choicesDisp.css'
import { StateContext } from './Main';

export default function ChoicesDisp() {

  const { choices } = useContext( StateContext );

  return (
    <div onLoad={() => console.log(choices)} id='choices'>
        {choices.map( (disp, i) => 
            <div key={i}>
                <ColorSelect disp={disp} index={i}/>
            </div> )}
    </div>
  )
}
