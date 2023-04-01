export enum ModeType {
    SOLID = 'solid',
    MULTI = 'multicolor',
    GRADIENT = 'gradient',
    OFF = 'off',
    RUNMULTI = 'runningmulticolor',
    TWINKLE = 'twinkle',
    RAINBOW = 'rainbow'
}

export interface Mode {
    type: string,
    name: ModeType,
    description: string,
    data?: any
}