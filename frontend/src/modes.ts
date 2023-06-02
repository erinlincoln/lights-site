const modeChoices = {
    off: { 
        mode: 'single',
        choices: [ { type: 'off' } ]
    },
    sunlight: {
        mode: 'single',
        choices: [ { type: 'color-slider', colors: ['#FCF9D9', '#D9EEFC'] } ]
    },
    single: {
        mode: 'single',
        choices: [ { type: 'single' } ]
    },
    // rainbow: [],
    striped: {
        mode: 'multi',
        choices: [ { type: 'single' }, { type: 'single' } ]
    }
}

export default modeChoices;