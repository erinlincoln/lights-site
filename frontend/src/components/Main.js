import React, {createContext, useEffect, useReducer, useState} from 'react';
import RoomDisp from './RoomDisp';
import ModeDisp from './ModeDisp';
import '../style/lightsDisp.css';

export const StateContext = createContext(null);

function updateData ( state, action ) {
    switch ( action.type ) {
        case 'room':
            return { ...state, area: { ...state.area, room: action.room }};
        case 'zone':
            return { ...state, area: { ...state.area, zone: action.zone }};
        case 'strip':
            return { ...state, area: { ...state.area, strip: action.strip }};
        case 'mode':
            return { ...state, mode: action.mode, data: {} };
        case 'data':
            return { ...state, data: action.data };
        default: 
            console.log('ERROR: invalid action type');
    }
}

function LightsDisp() {
    const [ pickingRoom, setPickingRoom ] = useState( true );
    const [ choices, setChoices ] = useState();
    const [ data, setData ] = useReducer( updateData, { mode: {}, area: {}, data: {} } );
    const value = { pickingRoom, setPickingRoom, choices, setChoices, data, setData };

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