import couch from '../images/relax.png';
import bed from '../images/bed.png';
import computer from '../images/computer.png';


function ZoneDisp({setZone, setPickingZone}) {

    function pickZone( num ) {
        setZone(num); 
        setPickingZone(false);
    }

    return (
        <div>
            <button onClick={ () => pickZone(1)}>
                <img src={couch} alt="living room cartoon"></img>
                <p>living room</p>
            </button>
            <button onClick={ () => pickZone(2)}>
                <img src={bed} alt="bedroom cartoon"></img>
                <p>bedroom</p>
            </button>
            <button onClick={ () => pickZone(3)}>
                <img src={computer} alt="office cartoon"></img>
                <p>office</p>
            </button>
        </div>
    )
}

export default ZoneDisp;