const modeChoices = {
    off: { 
        mode: 'single-color',
        choices: [ { type: 'off' } ]
    },
    sunlight: {
        mode: 'single-color',
        choices: [ { type: 'color-slider', colors: ['#FCF9D9', '#D9EEFC'] } ]
    },
    single: {
        mode: 'single-color',
        choices: [ { type: 'single-color' } ]
    },
    // rainbow: [],
    striped: {
        mode: 'multi-color',
        choices: [ { type: 'single-color' }, { type: 'single-color' } ]
    }
}

export default modeChoices;