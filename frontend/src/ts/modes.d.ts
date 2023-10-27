export enum ModeType {
    SOLID = 'solid',
    MULTI = 'multicolor',
    RANGE = 'range',
    GRADIENT = 'gradient',
    OFF = 'off',
    RUNMULTI = 'runningmulticolor',
    TWINKLE = 'twinkle',
    RAINBOW = 'rainbow'
}

export interface Mode {
    type: string,
    name: ModeType,
    mode: ModeType,
    description: string,
    data?: any
}