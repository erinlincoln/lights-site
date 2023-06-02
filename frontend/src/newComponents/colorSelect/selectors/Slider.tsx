import React from 'react';
import ReactSlider from 'react-slider';
import '../../../newStyle/slider.css';

export default function Slider({dim, setDim}: {dim : number, setDim: any}) {
  return (
    <div className='d-flex flex-column align-items-center'>
      <h6 className='text-center'>dim</h6>
        <ReactSlider
                className="vertical-slider"
                thumbClassName="example-thumb"
                trackClassName="example-track"
                orientation="vertical"
                min={0}
                max={100}
                defaultValue={0}
                // sx={{
                //     '& input[type="range"]': {
                //       WebkitAppearance: 'slider-vertical',
                //     },
                //   }}
                  value={dim}
                  onChange={setDim}
                // onKeyDown={preventHorizontalKeyboardNavigation}
            />
    </div>
  )
}
