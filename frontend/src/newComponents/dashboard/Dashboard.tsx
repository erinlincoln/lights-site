import React from 'react'
import '../../newStyle/dashboard.css';
import { Color } from '../../ts/style.enum';
import Apt from '../icons/Apt';
import DashboardItem from './DashboardItem';
import { useLightsContext } from '../../contexts/lightsContext';
import { Preset } from '../../ts/user';

export default function Dashboard() {
    const {user} = useLightsContext();

  return (
    <div className='body-component' id='dashboard'>
        <Apt 
            lines={Color.DR5} 
            livingroom={Color.O4} 
            livingroomHover={Color.O6}
            bedroom={Color.R4} 
            bedroomHover={Color.R6}
            hallway={Color.Y5} 
            hallwayHover={Color.Y7}
            office={Color.YO4} 
            officeHover={Color.YO7}
            none={Color.DR4}
            couch={Color.O9}
            couchHover={Color.O1}
            bed={Color.R9}
            bedHover={Color.R1}
            door={Color.Y9}
            doorHover={Color.Y3}
            laptop={Color.YO9}
            laptopHover={Color.YO2}
            />
        {
            user.presets && 
            <div>
                <h1>Presets</h1>
                {user.presets.map((preset: Preset) => <DashboardItem id={`preset-${preset.name}`} text={preset.name}/>)}
            </div>
            
        }
    </div>
  )
}
