import React from 'react';
import ColorSelect from './ColorSelect';

export default function ChoicesDisp({choices, colors}) {

  return (
    <div onLoad={() => console.log(choices)}>
        {choices.map( (disp, i) => 
            <div key={i}>
                <ColorSelect disp={disp} index={i} colors={colors}/>
            </div> )}
    </div>
  )
}
