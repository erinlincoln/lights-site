import couch from '../images/relax.png';
import bed from '../images/bed.png';
import computer from '../images/computer.png';
import '../style/zoneDisp.css'


function ZoneDisp({setZone, setPickingZone}) {

    function pickZone( number, name ) {
        setZone({number, name }); 
        setPickingZone(false);
    }

    return (
        <div id='zone-disp'>
            <button onClick={ () => pickZone(1, "living room")}>
                <img src={couch} alt="living room cartoon"></img>
                <p>living room</p>
            </button>
            <button onClick={ () => pickZone(2, "bedroom")}>
                <img src={bed} alt="bedroom cartoon"></img>
                <p>bedroom</p>
            </button>
            <button onClick={ () => pickZone(3, "office")}>
                <img src={computer} alt="office cartoon"></img>
                <p>office</p>
            </button>
        </div>
    )
}

export default ZoneDisp;