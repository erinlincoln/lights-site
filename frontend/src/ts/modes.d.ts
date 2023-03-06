export enum ModeType {
    SINGLE = 'single',
    MULTI = 'multiple',
    GRADIENT = 'gradient'
}

export interface Mode {
    name: string,
    type: ModeType,
    description: string,
    data?: any
}