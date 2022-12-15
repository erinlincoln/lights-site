import React from 'react';
import ReactSlider from 'react-slider';
import '../style/slider.css';

export default function Slider() {
  return (
    <div>
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
