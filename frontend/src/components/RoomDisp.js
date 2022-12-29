import couch from '../images/relax.png';
import bed from '../images/bed.png';
import computer from '../images/computer.png';
import '../style/zoneDisp.css'
import { useContext } from 'react';
import { StateContext } from './LightsDisp';


function RoomDisp() {
    const { setRoom, setPickingRoom } = useContext( StateContext );

    function pickRoom( name ) {
        setRoom( name ); 
        setPickingRoom(false);
    }

    return (
        <div id='zone-disp'>
            <button onClick={ () => pickRoom( "livingRoom" )}>
                <img src={couch} alt="living room cartoon"></img>
                <p>living room</p>
            </button>
            <button onClick={ () => pickRoom( "bedroom" )}>
                <img src={bed} alt="bedroom cartoon"></img>
                <p>bedroom</p>
            </button>
            <button onClick={ () => pickRoom( "office" )}>
                <img src={computer} alt="office cartoon"></img>
                <p>office</p>
            </button>
        </div>
    )
}

export default RoomDisp;