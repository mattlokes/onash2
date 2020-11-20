# O-NAS-H2+

## Introduction
![Image of ONASH2](https://github.com/mattlokes/onash2/blob/main/docs/onash2_main.jpg?raw=true)

Welcome, My recent Reddit [post](https://www.reddit.com/r/3Dprinting/comments/juqaqa/designed_and_3d_printed_a_home_servernas/) exploded with overwhelming postive comments and requests for documentation on my 3D printed NAS project, so here it is!

This document is in no means fully exhaustive, but hopefully give some idea/pointers of what's required to recreate. If you have any further questions please feel free to send me issues via the github [repo](https://github.com/mattlokes/onash2). I will do my best to answer :)

If anyone does print the parts and make there own ONASH2, you can thank me by sending a photo of it! :)

Oh and why ONASH2.... ODroid - NAS - H2

## Index
 - [Specifications](#Specifications)
 - [3D Printed Parts](#3D-Printed-Parts)
 - [Electronics](#Electronics)
 - [Software Setup](#Software-Setup)
   - [Flashing the OS](#Flashing-the-OS)
   - [Compiling the Gigabit Ethernet Controller Driver](#Compiling-the-Gigabit-Ethernet-Controller-Driver)
   - [Docker](#Docker)
   - [MDADM](#MDADM)
 - [Status OLED](#Status-OLED) 
   - [I2C connection](#I2C-connections)
   - [Docker File](#Docker-File)
 - [FAQ](#FAQ)

## Specifications

ONASH2 is designed to use:
- The [ODroid H2/H2+](https://www.hardkernel.com/shop/odroid-h2plus/)
- 2x 3.5" HDDs, although 2.5" HDD can be used with the [printable included adapters](https://github.com/mattlokes/onash2/blob/main/stl/onash2_2.5_3.5_hdd_adapter.stl)
- One Large 120mm Cooling Fan (**REQUIRED when using PLA**)
- No power button ( You must set the Default Power State to S0 in the BIOS so that it will boot when power is applied )
- [Status OLED](https://www.amazon.co.uk/gp/product/B07F3Y984N/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- Internal Mounting Point for a USB Port
- Only M3 Screws (unless using 3.5" HDD which required different screws)
- To be printed within a build volume of 180x180x120mm
- No Supports (Although it helps around HDD mounting screw slots in the legs)
- **Dimensions 175x175x134mm**

## 3D Printed Parts

All parts pictured were printed in Galaxy Black Prusament PLA on a PRUSA Mini using the 0.2 Quality Presets. ( I did increase my bed temp to 63C to help with bed adhesion). All parts can be found [here](https://github.com/mattlokes/onash2/tree/main/stl)

### Required Prints

Part | Number | Print time (@ Above settings) 
---- | ------ | -----------------------------
[onash2_case_bottom.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_case_bottom.stl)| 1 | ~15 hours
[onash2_case_top.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_case_top.stl)| 1 | ~15 hours
[onash2_lag_0.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_leg_0.stl)| 1 | ~5hours*
[onash2_lag_1.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_leg_1.stl)| 1 | *
[onash2_lag_2.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_leg_2.stl)| 1 | *
[onash2_lag_3.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_leg_3.stl)| 1 | *
_*Print Time is the total applied to all legs printed on the same plate_

### Optional Prints

Part | Number | Print time (@ Above settings) 
---- | ------ | -----------------------------
[onash2_2.5_3.5_hdd_adapter.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_2.5_3.5_hdd_adapter.stl)| 2 | ~30 minutes

## Electronics
## Software Setup
### Flashing the OS
### Compiling the Gigabit Ethernet Controller Driver
### Docker
### MDADM
## Status OLED 
### I2C connections
### Docker File
## FAQ
 - **Q: How much did this cost all in all?**
 
   A: It really depends on what you want in terms of RAM/NVME/EMMC/HDD capcity, I spent about £400 all in, but that includes 32GB of RAM which is overkill and 2x4TB 2.5" HDD. So you should be able to tailor to your budget.
 - **Q: I've got a PRUSA Mini and i struggle to get the case parts not to curl, how did you do it?**
 
   A: I had the same problem during the first attempt at printing, then i discovered this excellent mod [Silicon Bed Levelling](https://forum.prusaprinters.org/forum/user-mods-octoprint-enclosures-nozzles/prusa-mini-silicone-bed-leveling-mod/) over on the PRUSA forum. Well worth the fiddling and patience. I've had perfect first layers since!
 - **Q: Is PLA really suitable for this?**
 
   A: If you are asking this question or dont know why this could be an issue, print it in PETG to be safe :)
 - **Q: Well why did you print in PLA then?**
 
   A: Better print quality, easier to print and i understand the risks ( I think / hope )


```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/mattlokes/onash2/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
