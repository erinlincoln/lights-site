import React, {useEffect, useState, useContext} from 'react';
import ColorSet from './ColorSet';
import SingleColor from './SingleColor';
import { StateContext } from './LightsDisp';
import '../style/colorSelect.css';
import OffToggle from './OffToggle';

export default function ColorSelect({index, disp }) {

    const { room, colors, mode } = useContext( StateContext );
    const [color, setColor] = useState();
    const [dim, setDim] = useState(100);
    const [ lastUpdate, setLastUpdate ] = useState( Date.now() );
    const [ waiting, setWaiting ] = useState( false );


    useEffect( () => {
        colors[ index ] = color;
        if ( color && colors.filter(e => e).length === mode.length ) sendChange();
    }, [color, dim])

    useEffect( () => {
        if (disp.type === 'off') setColor('#000000');
    }, [])

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
        await fetch('http://192.168.0.21:3001/lights/', {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({room, colors, dim: 100-dim})
            })
            .catch(err => console.log(err))
    }
    
    return (
        <div style={{ backgroundColor: color != '#000000' ? color : undefined }} className='choice-container'>
            { disp.type === 'color' && 
                <SingleColor color={color} setColor={setColor} index={index}/> 
                }
            { disp.type === 'color-set' &&
                <ColorSet setColor={setColor} colorArr={disp.colors}/>
                }
            { disp.type === 'off' &&
                <OffToggle setColor={setColor} color={color}/>}
        </div>
        
    )
}
