# Making replacement parts

[Home](../README.md) · [Suppliers](README.md) · [Original drawings](../docs/README.md)

Use this as the part-by-part drawing index for **XA, XB, and AR77XB**. It starts with the evidence already collected, plus a measured XA counterweight. A row means the part is on the worklist; it does not mean a manufacturing drawing is available.

**Evidence:** *dimensioned* = some dimensions are documented; *assembly only* = illustrated or identified, with manufacturing details missing; *missing* = no usable part drawing verified. None of the repository's replacement designs has yet been made and fit-tested.

Parts with some dimensions also have an OpenSCAD model, a drawing, and export files in [cad](../cad/README.md). The making methods below are **our workshop assessment**, based on the kind of geometry involved. They are not claims about AR's original manufacturing processes. Model and revision differences still need checking.

## Body and cover

| Part | Possible making method | Drawing evidence / next information needed |
| --- | --- | --- |
| Wooden base / plinth | Woodworking or CNC routing | Assembly only; [XA envelope](../models/xa/README.md#dimensions-and-arm-geometry) is not a joinery plan. Need wall sections, rebates, fixing positions, and finish. |
| Metal top plate | Cut/drill sheet; form where required | [XB assembly](../docs/originals/xb-drawing-119.tif); need a complete dimensioned hole pattern, thickness, material, and edge details. |
| Bottom panel | Cut sheet and drill | XB assembly only; need outline, thickness, attachment, and cable-exit details. |
| Dust cover | Cut, bend, or bond acrylic | [Older XB hinge detail](../models/xb/README.md#cover-dimensions-and-clearance) has partial dimensions. Need overall shape, thickness, lip, corner geometry, and clearances by version. |
| Hinges and brackets | Form sheet or machine components | [XB sheet 2](../docs/originals/xb-drawing-114.tif) gives partial mounting dimensions; hinge mechanism and pin fits remain missing. Later XB revisions delete hinges. |
| Feet / pads | Cut or mold compliant material | XB BOM identifies felt feet; need footprint, thickness, and material specification. |
| Badges / bezels | Engrave, print, or cut/form | Assembly only; need geometry, artwork, and attachment by model. |

## Tonearm and headshell

| Part | Possible making method | Drawing evidence / next information needed |
| --- | --- | --- |
| Counterweight | Turn and drill; thread the locking hole | [XA owner measurements](xa-counterweight.md): external size, bore, material, and mass reported for one table; locking-hole details and tolerances missing. [Preliminary drawing](../cad/exports/xa-counterweight/PRELIMINARY-xa-counterweight.pdf). XB/AR77XB variants need separate records. |
| Counterweight locking screw | Buy a matching fastener, or turn/thread | Missing confirmed thread, tip form, and length for that location. Do not assign a screw from a different assembly. |
| Arm tube | Form tube and machine its ends | Assembly only; need bend geometry, wall thickness, material, end features, and relation to the stylus/pivots. |
| Pivot block / coupling | Machine body; make or source inserts | Assembly only; need bore locations, pivot alignment, materials, and fits. |
| Pivot screws and bearing inserts | Precision turn/grind; machine inserts | Assembly only; need thread, point geometry, contact material, and adjustment requirements. |
| Arm spindle and bearing sleeve | Precision turn/grind/hone as required | Assembly only; need mating dimensions, clearance, material, finish, and alignment. |
| Arm bearing ball and thrust disc | Source a suitable ball; make or source thrust material | Components identified in the [XA service manual](../docs/originals/xa-service-manual.pdf), which calls the disc Teflon on p. 1 and nylon in the p. 4 parts list. Sizes, grade, thickness, and confirmed material by revision remain missing. |
| Headshell body and neck | Machine suitable material, or mold/print a prototype | [Headshell reference](../docs/headshells.md): full body and connector drawing missing. Need locking geometry, cartridge position, material, and finished mass. A [PMMA top-mount concept](../cad/exports/headshell-pmma-top-mount/PRELIMINARY-headshell-pmma-top-mount.pdf) exists, with those dimensions as placeholders. |
| Headshell contact pins, springs, and insulator | Source contacts or make an assembly | Missing dimensioned pin layout, spring travel/force, insulation, and connector fits. |
| Cartridge screws, bushings, shims | Buy screws; turn bushings; cut shims | [Dimensioned community hardware drawing](../docs/headshells.md#mounting-screws-and-spacers), explicitly XA/XB. Verify the installed shell. [Models and drawings](../cad/README.md) for all sizes. |
| Tonearm rest / yoke | Machine or mold a suitable part | The [same XA owner report](xa-counterweight.md#tonearm-rest) supplies one height; full shape, stem, thread, and attachment remain missing. |
| Cueing lever and linkage | Turn, form, or machine pieces | XB assembly identifies the mechanism; component drawings and travel remain missing. Do not assume every model has this arrangement. |
| Cueing piston / cylinder / damping parts | Precision machine mating parts | Assembly only; need fits, travel, materials, damping medium, and operation by revision. |

## Platter, drive, and suspension

| Part | Possible making method | Drawing evidence / next information needed |
| --- | --- | --- |
| T-bar / subchassis | Machine or fabricate a replacement | XB assembly only; need bearing-center geometry, parallelism, spring locations, material, and mass. |
| Inner platter / hub | Turn and machine; fit spindle | XB assembly only; need belt surface, shoulder dimensions, spindle fit, material, mass, and runout requirements. |
| Outer platter | Turn and finish; check balance | XB assembly only; need all diameters, section, mating register, material, and mass. |
| Platter spindle | Precision turn/grind | Assembly only; need full profile, bearing fits, surface finish, material, and thrust-end geometry. |
| Main bearing housing / liner | Machine and finish mating surfaces | Assembly only; need material and running fit for the actual revision. Historical bearing materials changed. |
| Main bearing ball / thrust spacer | Source precision ball; machine or source spacer | [XB part identifiers](../models/xb/README.md#bearings-and-suspension) exist; dimensions and material remain missing. |
| Motor pulley | Turn concentric steps and bore | [XA shaft/motor variants](../models/xa/README.md#motor-identification) established; complete pulley dimensions and tolerances by motor and mains frequency missing. |
| Motor mounting brackets | Cut/form or machine | XB assembly only; need geometry and mounting/adjustment details. |
| Main belt | Source or manufacture elastomer belt | No verified manufacturing specification; length alone does not establish material, section, or tension. [Supplier evidence](README.md#replacement-parts). |
| Starter belt, early two-motor tables | Source or manufacture elastomer belt | Separate XA variant; complete verified specification missing. |
| Suspension springs | Source or wind and characterize | Complete drawing, wire/material specification, spring rate, free length, and loaded behavior missing. |
| Grommets, spring bushings, damping foam/tubes | Cut, mold, or source suitable materials | XA service drawing and XB assembly identify components; dimensions and material properties by revision missing. |
| Suspension studs, nuts, washers | Source hardware or turn/thread studs | [XB nut thread documented](../models/xb/README.md#factory-hardware); complete stud geometry and original length missing. |
| Other screws, clips, cable clamps, capacitor straps | Source hardware; form sheet parts | [XB hardware](../models/xb/README.md#factory-hardware) and [mounting changes](../models/xb/README.md#wiring-and-mounting-changes) provide partial specifications. |
| Record mat | Cut, mold, or source | Complete original material/thickness specification by revision missing. |

## Electrical parts and setup accessories

Motor internals, switches, capacitors, cables, and connectors need their own specifications and sources. Machining their housings does not reproduce their electrical behavior. Keep these in the model's electrical section and [supplier directory](README.md), linked from any future mechanical drawing.

Overhang gauges and stylus-force gauges also belong in the part index when usable drawings are found. Their geometry or calibration must be established before treating a reproduction as a setup tool. A [preliminary overhang gauge](../cad/exports/overhang-gauge/PRELIMINARY-overhang-gauge.pdf) is drawn from the documented 0.688 in dimension; AR's own gauge outline has not been found.

## What makes a drawing usable

For each part, collect **dimensions, material, critical fits/finish, model/revision, and evidence**. Preserve a factory value separately from a measurement of an aged part. Add a fit result once a replacement has actually been made; an attractive CAD model alone leaves that question open.

Roy Allison's firsthand AR history describes early bearing bores shrinking and seizing, followed by a change to steel-jacketed Babbitt inserts. It also describes the difficulty of producing consistent belts. These are useful examples of why copying the visible shape may leave important manufacturing details unresolved. [Allison's account](https://vinylnirvana.com/ar-turntable-resources/ar-turntable-history/acoustic-research-inc-the-golden-years-by-roy-allison)

Start with the counterweight, rest, shims, and simple brackets as candidates for measurement and drawings. Keep bearing, platter, pulley, and arm-geometry work tied to measured functional requirements. This ordering is a workshop judgment, not a claim that any existing drawing is production-ready.
