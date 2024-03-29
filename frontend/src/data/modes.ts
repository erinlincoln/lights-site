import { Mode, ModeType } from "../ts/modes.d";

const modes: Mode[] = [
    {
        type: 'Solid',
        name: ModeType.SOLID,
        mode: ModeType.SOLID,
        description: 'Choose a single color to display'
    },
    {
        type: 'Striped',
        name: ModeType.MULTI,
        mode: ModeType.MULTI,
        description: 'Choose multiple colors to make a striped pattern'
    },
    {
        type: 'Sunlight',
        name: ModeType.RANGE,
        mode: ModeType.SOLID,
        description: 'Choose from a set of natural-hued light colors mimicking sunlight',
        data: {
            colors: ['#ffddd2', '#ff5b27']
        }
    }
]

export default modes;