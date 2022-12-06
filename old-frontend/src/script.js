let zone;
let zoneName;
let mode;

window.onload = () => {
    // attach event listeners to zone buttons
    for ( let i = 1; i < 4; i++ ) {
        document.querySelector( `#zone-${i}`).addEventListener( 'click', ( e ) => zoneSelect( e, i ) );
    }
    
    
}

function zoneSelect( e, num ) {
    // set zone they selected
    zone = num;
    zoneName = e.target.textContent;

    // reset button container
    document.querySelector( '.btn-container' ).replaceChildren( back() );

}

function reset() {
    window.location.href = '';
}

function back() {
    let btn = document.createElement( 'button' );
    btn.textContent = `${zoneName}`;
    btn.id = 'back';

    btn.addEventListener( 'click', reset );

    return btn;
}