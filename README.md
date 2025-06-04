# DIY-Macro

DIY-Macro is a 3x3 macropad with a rotary encoder and an OLED display. It was designed as a Starter Project during the Highway event in Hackclub.

## BOM

* 8x White DSA Keycaps
* 8x Cherry MX Switches
* 9x 1N4148 Diodes
* 1x XIAO RP2040 micro-controller
* 4x M3x16mm Screw Bolt
* 4x M3x5x4mm Heatset Inserts
* 1x 0.91 inch OLED display
* 1x EC11 Rotary Encoder
* 1x PCB
* 1x Case(divided into top and bottom, 3d printed)

## Schematic

![Schematic](https://github.com/FabioCastroMorffi/DIY-Macro/blob/main/assets/Screenshot%20from%202025-06-04%2012-45-03.png)

## PCB

![PCB](https://github.com/FabioCastroMorffi/DIY-Macro/blob/main/assets/Screenshot%20from%202025-06-04%2014-27-00.png)

![3D PCB](https://github.com/FabioCastroMorffi/DIY-Macro/blob/main/assets/Screenshot%20from%202025-06-04%2014-27-34.png)

Something to improve in the future would definitely be **track placement** when routing. As the amount of components increases, effective routing becomes essential!

## CAD Model

The model is very similar to the standard one from Hackpad. The case is held in place with 4 heatset inserts that hold the top and the bottom together. My main struggle relied on matching the openings for the top and the bottom together for all components. Having two instances of the top helped me with this due to being able to update the top and directly check whether it matched the pcb and the bottom.

The model was done in Fusion 360 (in the browser unfortunately)

![3D Model](https://github.com/FabioCastroMorffi/DIY-Macro/blob/main/assets/Screenshot%20from%202025-06-04%2015-02-57.png) 

## Firmware

The firmware is done with the kmk library in Python and I will troubleshoot(if necessary) upon the receiving of the kit. 

## Thank you

To the Hackclub Team leading this event, thank you so much for the opportunity. This introduction to hardware has expanded my views on technology and given me the opportunity get a taste of hardware design. I'm truly grateful for that. 
