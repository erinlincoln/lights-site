import React, {useEffect, useState} from 'react';
import ColorSet from './ColorSet';
import SingleColor from './SingleColor';
import ReactSlider from 'react-slider';
import '../style/colorSelect.css';

export default function ColorSelect({ colors, index, disp }) {
    const [color, setColor] = useState();
    const [dim, setDim] = useState(100);


    useEffect( () => {
        // document.querySelector( `#cs-${index}` ).style.backgroundColor = color;
        colors[ index ] = color;
        sendChange();
    }, [color, dim])

    async function sendChange() {
        let res = await fetch('http://192.168.5.182:3001/lights/', {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({colors, dim: 100-dim})
        })
        .then( res => res.json())
        .catch(err => console.log(err))

        console.log(res)
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
            
            
            <ReactSlider
                className="vertical-slider"
                thumbClassName="example-thumb"
                trackClassName="example-track"
                orientation="vertical"
                sx={{
                    '& input[type="range"]': {
                      WebkitAppearance: 'slider-vertical',
                    },
                  }}
                  value={dim}
                  onChange={setDim}
                // onKeyDown={preventHorizontalKeyboardNavigation}
            />
            
        </div>
        
    )
}
