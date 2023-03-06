import { Mode, ModeType } from "../ts/modes.d";

const modes: Mode[] = [
    {
        name: 'Solid',
        type: ModeType.SINGLE,
        description: 'Choose a single color to display'
    },
    {
        name: 'Striped',
        type: ModeType.MULTI,
        description: 'Choose multiple colors to make a striped pattern'
    },
    {
        name: 'Sunlight',
        type: ModeType.GRADIENT,
        description: 'Choose from a set of natural-hued light colors mimicking sunlight',
        data: {
            colors: ['#ffddd2', '#ff5b27']
        }
    }
]

export default modes;