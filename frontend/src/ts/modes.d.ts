export enum ModeType {
    SINGLE = 'single color',
    MULTI = 'multiple colors',
    GRADIENT = 'gradient'
}

export interface Mode {
    name: string,
    type: ModeType,
    description: string
}