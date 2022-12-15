const modeChoices = {
    off: [ {type: 'off' }],
    sunlight: [ {type: 'color-set', colors: ['#FCF9D9', '#D9EEFC']}],
    single: [ { type: 'color'} ],
    // rainbow: [],
    stripped:[ { type: 'color'}, { type: 'color'}, { type: 'color'}]
}

export default modeChoices;