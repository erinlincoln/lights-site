import React, {useEffect, useState, useContext, createContext} from 'react';
import ColorSlider from './selectors/ColorSlider';
import SingleColor from './selectors/SingleColor';
import { StateContext } from './Main';
import '../style/colorSelect.css';
import OffToggle from './selectors/OffToggle';
import ChoicesDisp from './ChoicesDisp';

export const ColorContext = createContext();

export default function ColorSelect({index, disp }) {

    const { data, choices } = useContext( StateContext );
    const [color, setColor] = useState();
    const [dim, setDim] = useState(100);
    const [ lastUpdate, setLastUpdate ] = useState( Date.now() );
    const [ waiting, setWaiting ] = useState( false );
    const value = { index, color, setColor };
    const mode = data.mode.type;

    // if display is off, turn off lights
    useEffect( () => {
        if (disp.type === 'off') setColor('#000000');
    }, [])


    // send change if all colors are set
    useEffect( () => {
        // if the color is set
        if ( mode === 'single-color' || 'off' && color ) {
            sendChange();

        // if all colors are set
        } else if ( mode === 'multi-color' && data.data.colors && !data.data.colors.includes( undefined ) ) {
            sendChange();
        }
    }, [ color ])

    

    function sendChange() {
        if ( Date.now() - lastUpdate > 40 && !waiting ) {
            setLastUpdate( Date.now() );
            setWaiting( false );
            sendData();
        } else if ( !waiting ) {
            setWaiting( true );
            setTimeout( sendChange, 40 );
        }
        
    }

    async function sendData() {
        await fetch('http://localhost:3001/lights/', {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify( data )
            })
            .catch(err => console.log(err))
    }
    
    return (
        <ColorContext.Provider value={value}>
            <div style={{ backgroundColor: color != '#000000' ? color : undefined }} className='choice-container'>
                { disp.type === 'single-color' && 
                    <SingleColor color={color} setColor={setColor} index={index}/> 
                    }
                { disp.type === 'color-slider' &&
                    <ColorSlider colors={ choices[ index ].colors }/>
                    }
                { disp.type === 'off' &&
                    <OffToggle setColor={setColor} color={color}/>}
            </div>
        </ColorContext.Provider>
    )
}
