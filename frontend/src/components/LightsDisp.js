import React, {useState} from 'react';
import ZoneDisp from './ZoneDisp';
import ModeDisp from './ModeDisp';
import '../style/lightsDisp.css';

function LightsDisp() {
    const [ zone, setZone ] = useState();
    const [ mode, setMode ] = useState();
    const [ colors, setColors ] = useState([]);
    const [ pickingZone, setPickingZone ] = useState( true );

    return (
        <div id='content'>
            { pickingZone
                ? <ZoneDisp setZone={setZone} setPickingZone={setPickingZone}/>
                : <ModeDisp mode={mode} setMode={setMode} colors={colors} setColors={setColors} zone={zone} setPickingZone={setPickingZone}/>
            }
        </div>
        
    )
}

export default LightsDisp;