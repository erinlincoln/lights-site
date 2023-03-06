import React, { useState } from 'react'
import Bed from './Bed';
import Couch from './Couch';
import Laptop from './Laptop';
import '../../newStyle/apt.css';
import Door from './Door';
import { useSequenceContext } from '../../contexts/sequenceContext';
import { lightsSequence } from '../../ts/lightsSequence.enums';

export default function Apt(props: 
    {lines: string, 
        hallway: string, 
        hallwayHover: string,
        livingroom: string, 
        livingroomHover: string,
        office: string, 
        officeHover: string,
        bedroom: string, 
        bedroomHover: string,
        none: string,
        bed: string,
        bedHover: string,
        couch: string,
        couchHover: string,
        laptop: string,
        laptopHover: string,
        door: string,
        doorHover: string
    }) {
    const  {lines, hallway, hallwayHover, livingroom, livingroomHover, office, officeHover, bedroom, bedroomHover, none, bed, bedHover, couch, couchHover, laptop, laptopHover, door, doorHover} = props;
    const {setStage, setRoom} = useSequenceContext();
    
    const [isBedHover, setBedHover] = useState(false);
    const [isCouchHover, setCouchHover] = useState(false);
    const [isDoorHover, setDoorHover] = useState(false);
    const [isLaptopHover, setLaptopHover] = useState(false);

    const bedroomColor = isBedHover ? bedroomHover : bedroom;
    const livingroomColor = isCouchHover ? livingroomHover : livingroom;
    const hallwayColor = isDoorHover ? hallwayHover : hallway;
    const officeColor = isLaptopHover ? officeHover : office;

    const bedHandleMouseEnter = () => setBedHover(true);
    const bedHandleMouseLeave = () => setBedHover(false);
    const couchHandleMouseEnter = () => setCouchHover(true);
    const couchHandleMouseLeave = () => setCouchHover(false);
    const doorHandleMouseEnter = () => setDoorHover(true);
    const doorHandleMouseLeave = () => setDoorHover(false);
    const laptopHandleMouseEnter = () => setLaptopHover(true);
    const laptopHandleMouseLeave = () => setLaptopHover(false);

    const handleClick = (room: any) => {setRoom(room); setStage(lightsSequence.MODESELECT)}

    return (
        <div id='apt-container'>
            <Bed color={bed} hoverColor={bedHover} isBedHover={isBedHover} handleMouseEnter={bedHandleMouseEnter} handleMouseLeave={bedHandleMouseLeave} handleClick={() => handleClick('bedroom')}/>
            <Couch color={couch} hoverColor={couchHover} isCouchHover={isCouchHover} handleMouseEnter={couchHandleMouseEnter} handleMouseLeave={couchHandleMouseLeave} handleClick={() => handleClick('livingroom')}/>
            <Laptop color={laptop} hoverColor={laptopHover} isLaptopHover={isLaptopHover} handleMouseEnter={laptopHandleMouseEnter} handleMouseLeave={laptopHandleMouseLeave} handleClick={() => handleClick('office')}/>
            <Door color={door} hoverColor={doorHover} isDoorHover={isDoorHover} handleMouseEnter={doorHandleMouseEnter} handleMouseLeave={doorHandleMouseLeave} handleClick={() => handleClick('hallway')}/>
            <svg id='apt-icon' width="580" height="550" viewBox='70 25 640 560' xmlns="http://www.w3.org/2000/svg">
                <g onClick={() => handleClick('bedroom')} onMouseEnter={bedHandleMouseEnter} onMouseLeave={bedHandleMouseLeave}>
                    <rect stroke={bedroomColor} id="svg_72" height="55.32832" width="47.13156" y="490.99041" x="191.39855" stroke-width="5" fill={bedroomColor}/>
                    <rect stroke={bedroomColor} id="svg_71" height="79.5089" width="172.54248" y="493.44946" x="235.25138" stroke-width="5" fill={bedroomColor}/>
                    <rect stroke={bedroomColor} id="svg_70" height="223.36258" width="191.3951" y="303.28388" x="87.70913" stroke-width="5" fill={bedroomColor}/>
                </g>
                <g onClick={() => handleClick('livingroom')} onMouseEnter={couchHandleMouseEnter} onMouseLeave={couchHandleMouseLeave}>
                    <rect stroke={livingroomColor} id="svg_57" height="75.17242" width="63.69689" y="289.34406" x="285.09466" stroke-width="5" fill={livingroomColor}/>
                    <rect stroke={livingroomColor} id="svg_56" height="75.17242" width="189.5035" y="268.69887" x="284.77208" stroke-width="5" fill={livingroomColor}/>
                    <rect stroke={livingroomColor} id="svg_55" height="75.17242" width="182.08413" y="22.24694" x="251.22365" stroke-width="5" fill={livingroomColor}/>
                    <rect stroke={livingroomColor} id="svg_53" height="75.17242" width="244.34228" y="44.82761" x="188.9655" stroke-width="5" fill={livingroomColor}/>
                    <rect stroke={livingroomColor} id="svg_52" height="35.86207" width="344.18903" y="89.6552" x="87.58618" stroke-width="5" fill={livingroomColor}/>
                    <rect stroke={livingroomColor} id="svg_51" height="191.72414" width="385.51727" y="109.65521" x="88.27584" stroke-width="5" fill={livingroomColor}/>
                </g>
                <g onClick={() => handleClick('office')} onMouseEnter={laptopHandleMouseEnter} onMouseLeave={laptopHandleMouseLeave}>
                    <rect stroke={officeColor} id="svg_60" height="91.0252" width="215.38357" y="286.32193" x="477.77348" stroke-width="5" fill={officeColor}/>
                    <rect stroke={officeColor} id="svg_58" height="188.28189" width="199.25943" y="379.12387" x="494.80169" stroke-width="5" fill={officeColor}/>
                    <rect id="svg_59" height="20.94007" width="165.38381" y="570.50858" x="470.93591" stroke-width="5" stroke={officeColor} fill={officeColor}/>
                </g>
                <g>
                    <rect stroke={none} id="svg_66" height="43.61931" width="124.65603" y="349.06836" x="350.67069" stroke-width="5" fill={none}/>
                    <rect stroke={none} id="svg_69" height="77.22611" width="7.44192" y="496.20078" x="409.6876" stroke-width="5" fill={none}/>
                    <rect stroke={none} id="svg_67" height="144.84965" width="79.16384" y="422.83949" x="415.01551" stroke-width="5" fill={none}/>
                    <rect stroke={none} id="svg_68" height="144.84965" width="54.16362" y="447.42987" x="416.24503" stroke-width="5" fill={none}/>
                    <rect stroke={none} id="svg_65" height="123.94786" width="188.18116" y="369.97017" x="287.55539" stroke-width="5" fill={none}/>
                    <rect id="svg_61" height="174.35813" width="131.62329" y="107.26297" x="476.49144" stroke-width="5" stroke={none} fill={none}/>
                </g>
                <g onClick={() => handleClick('hallway')} onMouseEnter={doorHandleMouseEnter} onMouseLeave={doorHandleMouseLeave}>
                    <rect stroke={hallwayColor} id="svg_64" height="143.50931" width="68.31726" y="138.54148" x="612.15303" stroke-width="5" fill={hallwayColor}/>
                    <rect stroke={hallwayColor} id="svg_63" height="98.8368" width="81.02229" y="41.40949" x="612.97271" stroke-width="5" fill={hallwayColor}/>
                    <rect stroke={hallwayColor} id="svg_62" height="81.62354" width="247.00735" y="21.36596" x="436.74804" stroke-width="5" fill={hallwayColor}/>
                </g>
                <g>
                    <line stroke={lines} stroke-width="5" stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_2" y2="18.66667" x2="687.48959" y1="18.66667" x1="243.92614" fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_3" y2="17.54284" x2="246.39047" y1="46.00087" x1="246.39047" stroke-width="5" fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_4" y2="43.61991" x2="187.97188" y1="43.61991" x1="248.65079" stroke-width="5" fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_6" y2="41.06898" x2="188.3355" y1="89.07228" x1="188.3355" stroke-width="5" fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_7" y2="86.52695" x2="84.97778" y1="86.52695" x1="190.88083" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_8" y2="530.68816" x2="86.15813" y1="84.1635" x1="86.15813" stroke-width="5" fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_9" y2="528.57116" x2="191.91532" y1="528.57116" x1="83.67332" stroke-width="5" fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_10" y2="527.28945" x2="189.38757" y1="550.61197" x1="189.38757" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_11" y2="549.38748" x2="186.87245" y1="549.38748" x1="235.51001" stroke-width="5" fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_12" y2="549.48818" x2="233.06103" y1="576.73441" x1="233.06103" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_13" y2="575.50992" x2="230.84009" y1="575.50992" x1="417.95892" stroke-width="5" fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_14" y2="574.6782" x2="415.50995" y1="596.32624" x1="415.50995" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_15" y2="595.50991" x2="413.26401" y1="595.50991" x1="639.99964" stroke-width="5" fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_16" y2="597.96177" x2="469.79565" y1="567.75482" x1="469.79565" stroke-width="5" fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_17" y2="570.2038" x2="467.26829" y1="570.2038" x1="493.87727" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_18" y2="572.53004" x2="494.28544" y1="375.10182" x1="494.28544" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_19" y2="421.63242" x2="493.99423" y1="421.63242" x1="407.75485" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_20" y2="419.10323" x2="409.79567" y1="503.26504" x1="409.79567" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_21" y2="493.87729" x2="281.21258" y1="493.87729" x1="345.30589" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_22" y2="496.029" x2="283.67326" y1="303.67327" x1="283.67326" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_23" y2="305.71408" x2="286.17596" y1="305.71408" x1="155.91819" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_24" y2="366.53039" x2="351.84572" y1="366.53039" x1="283.67326" stroke-width="5" fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_25" y2="347.75489" x2="347.82398" y1="347.75489" x1="477.95891" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_26" y2="345.40439" x2="349.38752" y1="366.93856" x1="349.38752" stroke-width="5" fill="none"/>
                    <rect stroke={lines} id="svg_28" height="44.48978" width="17.55102" y="377.14264" x="476.73442" stroke-width="5" fill={lines}/>
                    <line id="svg_29" y2="386.53068" x2="476.73442" y1="104.48966" x1="476.73442" stroke-width="5" stroke={lines} fill="none"/>
                    <line id="svg_31" y2="106.53047" x2="545.35665" y1="106.53047" x1="433.87729" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke={lines} id="svg_32" y2="104.15906" x2="543.67318" y1="175.91821" x1="543.67318" stroke-width="5" fill="none"/>
                    <line id="svg_33" y2="173.46923" x2="544.75928" y1="173.46923" x1="612.24458" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke={lines} id="svg_34" y2="379.16091" x2="609.7956" y1="104.89782" x1="609.7956" stroke-width="5" fill="none"/>
                    <line stroke={lines} id="svg_35" y2="106.53047" x2="550.21101" y1="106.53047" x1="543.26501" stroke-width="5" fill="none"/>
                    <line stroke={lines} id="svg_37" y2="107.3468" x2="607.35385" y1="107.3468" x1="600.40785" stroke-width="5" fill="none"/>
                    <line id="svg_38" y2="377.14263" x2="495.70519" y1="377.14263" x1="512.24461" stroke-width="5" stroke={lines} fill="none"/>
                    <line id="svg_39" y2="376.73447" x2="588.6696" y1="376.73447" x1="610.61193" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_40" y2="564.88665" x2="637.5507" y1="595.10175" x1="637.5507" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_41" y2="567.34666" x2="697.46433" y1="567.34666" x1="636.73437" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_42" y2="286.07997" x2="695.50986" y1="569.79563" x1="695.50986" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_43" y2="285.71409" x2="697.8389" y1="285.71409" x1="674.28538" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_44" y2="285.30593" x2="478.19622" y1="285.30593" x1="619.18336" stroke-width="5" stroke={lines} fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_46" y2="284.85978" x2="682.04048" y1="138.77536" x1="682.04048" stroke-width="5" fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_47" y2="141.22434" x2="698.51156" y1="141.22434" x1="682.04048" stroke-width="5" fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_48" y2="143.67327" x2="696.32619" y1="38.36722" x1="696.32619" stroke-width="5" fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_49" y2="39.99988" x2="698.86559" y1="39.99988" x1="683.67313" stroke-width="5" fill="none"/>
                    <line stroke={lines} stroke-linecap="undefined" stroke-linejoin="undefined" id="svg_50" y2="42.33506" x2="685.71395" y1="16.32642" x1="685.71395" stroke-width="5" fill="none"/>
                </g>
            </svg>
        </div>
    )
}
