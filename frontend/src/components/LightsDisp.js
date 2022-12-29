import React, {createContext, useState} from 'react';
import RoomDisp from './RoomDisp';
import ModeDisp from './ModeDisp';
import '../style/lightsDisp.css';

export const StateContext = createContext(null);

function LightsDisp() {
    const [ room, setRoom ] = useState();
    const [ mode, setMode ] = useState();
    const [ colors, setColors ] = useState([]);
    const [ pickingRoom, setPickingRoom ] = useState( true );
    const value = { room, setRoom, mode, setMode, colors, setColors, 
        pickingRoom, setPickingRoom };

    return (
        <StateContext.Provider value={ value } >
            <div id='content'>
                { pickingRoom
                    ? <RoomDisp />
                    : <ModeDisp />
                }
            </div>
        </StateContext.Provider>
    )
}

export default LightsDisp;