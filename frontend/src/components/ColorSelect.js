import React, {useEffect, useState} from 'react';
import ColorSet from './ColorSet';
import SingleColor from './SingleColor';
import ReactSlider from 'react-slider';
import '../style/colorSelect.css';

export default function ColorSelect({ colors, index, disp }) {
    const [color, setColor] = useState();


    useEffect( () => {
        // document.querySelector( `#cs-${index}` ).style.backgroundColor = color;
        colors[ index ] = color;
    }, [color])
    
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
                // onKeyDown={preventHorizontalKeyboardNavigation}
            />
            
        </div>
        
    )
}
