import React, {useEffect, useState} from 'react';
import ColorSet from './ColorSet';
import SingleColor from './SingleColor';
import '../style/colorSelect.css';

export default function ColorSelect({ colors, index, disp }) {
    const [color, setColor] = useState();
    const [dim, setDim] = useState(100);


    useEffect( () => {
        colors[ index ] = color;
        sendChange();
    }, [color, dim])

    useEffect( () => {
        if (disp.type === 'off') setColor('#000000');
    }, [])

    async function sendChange() {
        await fetch('http://192.168.5.182:3001/lights/', {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({colors, dim: 100-dim})
        })
        .catch(err => console.log(err))
    }
    
    return (
        <div id='color-select'>
            <div style={{backgroundColor: color}} id='choice-container'>
                { disp.type === 'color' && 
                    <SingleColor color={color} setColor={setColor} index={index}/> 
                    }
                { disp.type === 'color-set' &&
                    <ColorSet setColor={setColor} colorArr={disp.colors}/>
                    }
            </div>
        </div>
        
    )
}
