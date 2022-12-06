import React, {useState} from 'react';
import ZoneDisp from './ZoneDisp';
import ModeDisp from './ModeDisp';

function LightsDisp() {
    const [ zone, setZone ] = useState();
    const [ mode, setMode ] = useState();
    const [ colors, setColors ] = useState();
    const [ pickingZone, setPickingZone ] = useState( true );

    if ( pickingZone ) {
        return <ZoneDisp setZone={setZone} setPickingZone={setPickingZone}/>
    } else {
        return <ModeDisp setMode={setMode} setColors={setColors} zone={zone}/>
    }
}

export default LightsDisp;