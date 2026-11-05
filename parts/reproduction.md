# Making replacement parts

[Home](../README.md) · [Suppliers](README.md) · [CAD](../cad/README.md) · [Original drawings](../docs/README.md)

Part index for the XA, XB, and AR77XB. A row is a worklist entry, not a drawing.

**Evidence:** *dimensioned* = some dimensions documented; *assembly only* = illustrated or identified; *missing* = no usable source.

## Body and cover

| Part | Possible making method | Evidence | Needed |
| --- | --- | --- | --- |
| Wooden base / plinth | Woodworking or CNC routing | Assembly only; [XA envelope](../models/xa/README.md#dimensions-and-arm-geometry) | Wall sections, rebates, fixing positions, finish |
| Metal top plate | Cut and drill sheet; form | Assembly only; [XB drawing 119](../docs/originals/xb-drawing-119.tif) | Hole pattern, thickness, material, edges |
| Bottom panel | Cut sheet and drill | Assembly only, XB | Outline, thickness, attachment, cable exit |
| Dust cover | Cut, bend, or bond acrylic | Dimensioned in part; [XB hinge detail](../models/xb/README.md#cover-dimensions-and-clearance) | Shape, thickness, lip, corners, clearances by version |
| Hinges and brackets | Form sheet or machine | Dimensioned in part; [XB drawing 114](../docs/originals/xb-drawing-114.tif). Later XB revisions delete hinges | Hinge mechanism, pin fits |
| Feet / pads | Cut or mold | Felt feet on the XB BOM | Footprint, thickness, material |
| Badges / bezels | Engrave, print, or cut | Assembly only | Geometry, artwork, attachment |

## Tonearm and headshell

| Part | Possible making method | Evidence | Needed |
| --- | --- | --- | --- |
| Counterweight | Turn and drill; thread the locking hole | Dimensioned; [XA record](xa-counterweight.md), [preliminary drawing](../cad/exports/xa-counterweight/PRELIMINARY-xa-counterweight.pdf) | Locking hole, tolerances, XB and AR77XB variants |
| Counterweight locking screw | Buy, or turn and thread | Missing | Thread, tip, length |
| Arm tube | Form tube and machine its ends | Assembly only | Bend, wall thickness, material, end features |
| Pivot block / coupling | Machine; make or source inserts | Assembly only | Bore locations, pivot alignment, materials, fits |
| Pivot screws and bearing inserts | Precision turn or grind | Assembly only | Thread, point geometry, contact material |
| Arm spindle and bearing sleeve | Precision turn, grind, hone | Assembly only | Mating dimensions, clearance, material, finish |
| Arm bearing ball and thrust disc | Source a ball; make or source the disc | Identified in the [XA service manual](../docs/originals/xa-service-manual.pdf) | Sizes, grade, thickness, disc material |
| Headshell body and neck | Machine, mold, or print | Missing; [top-mount headshell](../models/xa/mods/headshell-top-mount.md) | Neck, locking geometry, cartridge position, material, mass |
| Headshell contact pins, springs, insulator | Source or make | Missing | Pin layout, spring travel and force, insulation, fits |
| Cartridge screws, bushings, shims | Buy screws; turn bushings; cut shims | Dimensioned; [hardware set](../docs/what-goes-where.md#why-are-there-so-many-cartridge-screws), [drawings](../cad/README.md) | Check on the installed shell |
| Tonearm rest / yoke | Machine or mold | One height; [XA record](xa-counterweight.md#tonearm-rest) | Shape, stem, thread, attachment |
| Cueing lever and linkage | Turn, form, or machine | Assembly only, XB | Component drawings, travel |
| Cueing piston, cylinder, damping parts | Precision machine | Assembly only | Fits, travel, materials, damping medium |

## Platter, drive, and suspension

| Part | Possible making method | Evidence | Needed |
| --- | --- | --- | --- |
| T-bar / subchassis | Machine or fabricate | Assembly only, XB | Bearing centers, parallelism, spring locations, material, mass |
| Inner platter / hub | Turn and machine; fit spindle | Assembly only, XB | Belt surface, shoulders, spindle fit, material, mass, runout |
| Outer platter | Turn and finish; balance | Assembly only, XB | Diameters, section, register, material, mass |
| Platter spindle | Precision turn or grind | Assembly only | Profile, bearing fits, finish, material, thrust end |
| Main bearing housing / liner | Machine and finish | Assembly only | Material, running fit by revision |
| Main bearing ball / thrust spacer | Source a ball; machine or source the spacer | [XB part numbers](../models/xb/README.md#bearings-and-suspension) | Dimensions, material |
| Motor pulley | Turn concentric steps and bore | [XA motor variants](../models/xa/README.md#motor-identification) | Pulley dimensions by motor and mains frequency |
| Motor mounting brackets | Cut, form, or machine | Assembly only, XB | Geometry, mounting, adjustment |
| Main belt | Source or manufacture | Missing; [supplier](README.md#replacement-parts) | Length, section, material, tension |
| Starter belt, early two-motor tables | Source or manufacture | Missing | Full specification |
| Suspension springs | Source, or wind and characterize | Missing | Wire, material, rate, free length |
| Grommets, spring bushings, damping foam and tubes | Cut, mold, or source | Identified on the XA and XB drawings | Dimensions, material properties |
| Suspension studs, nuts, washers | Source, or turn and thread | [XB nut thread](../models/xb/README.md#factory-hardware) | Stud geometry, length |
| Other screws, clips, cable clamps, capacitor straps | Source; form sheet parts | Dimensioned in part; [XB hardware](../models/xb/README.md#factory-hardware), [mounting changes](../models/xb/README.md#wiring-and-mounting-changes) | Remaining sizes |
| Record mat | Cut, mold, or source | Missing | Material, thickness |

## Electrical parts and setup accessories

Motors, switches, capacitors, cables, and connectors belong in each model's electrical section and the [supplier directory](README.md).

A [preliminary overhang gauge](../cad/exports/overhang-gauge/PRELIMINARY-overhang-gauge.pdf) is drawn from the 0.688 in overhang. AR's own gauge outline and a stylus-force gauge drawing are missing.
