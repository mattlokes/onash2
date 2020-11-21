# O-NAS-H2+

## Introduction
![Image of ONASH2](https://github.com/mattlokes/onash2/blob/main/docs/onash2_main.jpg?raw=true)

Welcome, My recent Reddit [post](https://www.reddit.com/r/3Dprinting/comments/juqaqa/designed_and_3d_printed_a_home_servernas/) exploded with overwhelming postive comments and requests for documentation on my 3D printed NAS project, so here it is!

This document is in no means fully exhaustive, but hopefully give some idea/pointers of what's required to recreate. I will point out links of useful guides rather than reinvent the wheel wherever i can. If you have any further questions please feel free to send me issues via the github [repo](https://github.com/mattlokes/onash2). I will do my best to answer :)

If anyone does print the parts and make there own ONASH2, you can thank me by sending a photo of it! :)

Oh and why ONASH2.... ODroid - NAS - H2

## Index
 - [Specifications](#Specifications)
 - [Case](#Case)
 - [Electronics](#Electronics)
 - [Software Setup](#Software-Setup)
   - [Auto Start on applying power](#Auto-Start-on-applying-power)
   - [Fan Control](#Fan-Control)
   - [Flashing the OS](#Flashing-the-OS)
   - [Gigabit Ethernet Controller Driver](#Gigabit-Ethernet-Controller-Driver)
   - [Docker](#Docker)
   - [MDADM](#MDADM)
 - [Status OLED](#Status-OLED) 
   - [I2C connections](#I2C-connections)
   - [Python/Docker](#PythonDocker)
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

## Case

### 3D Printed Parts List

All parts pictured were printed in Galaxy Black Prusament PLA on a PRUSA Mini using the 0.2 Quality Presets. ( I did increase my bed temp to 63C to help with bed adhesion). All parts can be found [here](https://github.com/mattlokes/onash2/tree/main/stl)

Part | Number | Print time (@ Above settings) | Required
---- | ------ | ----------------------------- | ---------
[onash2_case_bottom.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_case_bottom.stl) | 1 | ~15 hrs | Yes
[onash2_case_top.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_case_top.stl) | 1 | ~15 hrs | Yes
[onash2_lag_0.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_leg_0.stl) | 1 | ~5 hrs* | Yes
[onash2_lag_1.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_leg_1.stl) | 1 | * | Yes
[onash2_lag_2.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_leg_2.stl) | 1 | * | Yes
[onash2_lag_3.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_leg_3.stl) | 1 | * | Yes
[onash2_2.5_3.5_hdd_adapter.stl](https://github.com/mattlokes/onash2/blob/main/stl/onash2_2.5_3.5_hdd_adapter.stl) | 2 | ~30 mins | No

_*Print Time is the total applied to all legs printed on the same plate_

### Other Parts List

Part | Number | Comment 
---- | ------ | -------
40mm M3 Hex Cap Bolts/Nuts | 2 | For attaching the rear of the case top to bottom. (You will need a hex driver/key longer than 70mm)
20mm M3 Hex Cap Bolts/Nuts | 2 | For attaching the front of the case top to bottom (40mm might also work)
12mm M3 Hex Cap Bolts/Nuts | 12 | 8 - for the case legs, 4 - holding the board to the legs
[Dust Filters](https://www.amazon.co.uk/gp/product/B07HFR2BM5/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) | 2 | The case was designed specifically for these, although any 120x120 dust filter which is no thicker than 2mm should be fine
[9mm Diameter Rubber Feet](https://www.amazon.co.uk/gp/product/B076ND94QV/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) | 4 | Reduce any vibrations / noise

## Electronics

### Parts List

Part | Number | Comment 
---- | ------ | -------
[ODroid H2+](https://www.hardkernel.com/shop/odroid-h2plus) | 1 | None
[60W 15V Power Supply](https://www.hardkernel.com/shop/15v-4a-power-supply-uk-plug/) | 1 | None
[ODroid H2+ SATA Power/Data Cables](https://www.hardkernel.com/shop/sata-data-and-power-cable/) | 2 | The power cables are pretty proprietry as far as i can tell.
[NVME](https://www.amazon.co.uk/gp/product/B07YFF8879/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) | 1 | For your OS Drive, you could use a hardkernel EMMC instead.
[DDR4 RAM](https://www.amazon.co.uk/gp/product/B019FRBHZ0/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) | 1/2 | The maximum the ODroid supports is 32GB, use case dependant how much to get.
SATA 2.5"/3.5" HDD | 1/2 | If you want to create a RAID you will need two (you dont need identical drivers but it helps)
[5V PWM Noctua 120x120 Fan](https://www.amazon.co.uk/gp/product/B07DXDQKZM/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) | 1 | **Make sure its 5V!**
[JST 1.25mm 4 Pin](https://www.ebay.co.uk/itm/302007426719) | 1 | Required to connect the System Fan
[1.5" I2C OLED](https://www.amazon.co.uk/gp/product/B07F3Y984N/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) | 1 | Case is designed for exactly this OLED dimensions.
4k7 Resistor | 2 | Used to pull High the I2C SDA/SCLK lines.
[USB A Socket](https://www.amazon.co.uk/gp/product/B07TVHRH5Q/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) | 1 | Only required if you want the internal USB Port


### Fan wiring

Using the JST Connector, and the Noctua fan extension cable that came in the box I soldered together an adapter to allow connecting it
to the H2+. **Beware your JST Connector may have different coloured wires!**

Signal | JST Wire Colour | Noctua Wire Colour
------ | --------------- | ------------------
GND  |	![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) RED |	![#000000](https://via.placeholder.com/15/000000/000000?text=+) BLACK
+5V  |	![#000000](https://via.placeholder.com/15/000000/000000?text=+) BLACK |	![#ffff00](https://via.placeholder.com/15/ffff00/000000?text=+) YELLOW
TACH |	![#ffff00](https://via.placeholder.com/15/ffff00/000000?text=+) YELLOW |	![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) GREEN
PWM  |	![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) GREEN | ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+)BLUE



### OLED/USB Wiring

_I believe the USB port is only brought to the GPIO expansion header on the H2+ (Not the H2)._

![Wiring](https://github.com/mattlokes/onash2/blob/main/docs/wiring.png?raw=true)


## Software Setup

I'd advise doing all the software setup before you construct the server case.

### Auto Start on applying power
Follow the instructions [here](https://wiki.odroid.com/odroid-h2/application_note/autostart_when_power_applied)

### Fan Control
Follow the instructions [here](https://wiki.odroid.com/odroid-h2/hardware/pwm_fan)

**Tip: If you've printed the case in PLA, i would suggest that you set the low temperature to 40C - RPM 1000, medium to 47C - 1500 and high to 47C - 1500, then set thermal shutdown at 55C. This is to stop thermal runaway if the fan stops working, which could(would) cause the PLA to soften and possible damage** 

### Flashing the OS
Follow the instructions on [Hardkernel](https://wiki.odroid.com/odroid-h2/start#installation) for this. However i picked 
[Ubuntu Server 20.04 LTS](https://releases.ubuntu.com/20.04/ubuntu-20.04.1-live-server-amd64.iso). 

_I picked server edition because it doesnt start up an X server or any Window Manger, i dont want the GUI taking up any resources when I dont plan to use it._

To "Flash" the OS you will need a USB Mouse and keyboard/HDMI cable hooked up to the ODroid so that you can go through the installation steps.

Its pretty straightforward but you will get some fun messages about missing Network Interface. At the time of writing the Gigabit ethernet controller drvier is not part of the Kernel in 20.04 LTS (5.4.0-52-generic). [You can sort this out after OS installation](#Gigabit-Ethernet-Controller-Driver).

### Gigabit Ethernet Controller Driver
#### Compiling the Driver
You can follow the guide on [Hardkernel](https://wiki.odroid.com/odroid-h2/application_note/install_ethernet_driver_on_h2plus). 
The process is very much a chicken and the egg sort of situation, compiling a network driver without a network driver was tricky.

I tried USB tethering, but with an iPhone i just couldnt get it to work without installing packages, which is also tricky without a network connection.

I ended up setting up an QEMU VM running the Ubuntu Server 20.04 LTS image on another machine i have, then compiled the driver on there. It was surprisingly easy to do but probably not for a beginner.

I also see theres [now steps on Hardkernel](https://wiki.odroid.com/odroid-h2/application_note/install_ethernet_driver_on_h2plus) for loading packages onto a USB drive. This looks like the simpliest method. 

#### Using Precompiled Driver

If you are using the an Ubuntu Image with the same kernel (5.4.0-52-generic) as me, i've also [included the driver in the github repo](https://github.com/mattlokes/onash2/tree/main/software/r8125/5.4.0-52-generic) to make it super easy. You can copy this to your board using a USB stick and then load it into your kernel using [**insmod**](https://linux.die.net/man/8/insmod), then to bring up the network interface follow the instructions on [Hardkernel](https://wiki.odroid.com/odroid-h2/application_note/install_ethernet_driver_on_h2plus) 

**Tip: If you do use my Precompiled Driver, as soon as its working i suggest you install properly using the instructions on [Hardkernel](https://wiki.odroid.com/odroid-h2/application_note/install_ethernet_driver_on_h2plus)**

### Docker

I use [Docker](https://docs.docker.com/get-started/) to run all my services, being able to containerize all the dependancies allows for super easy backups and also makes things very easy to manage. I also run [Portainer](https://www.portainer.io/) in a Docker container which gives a fantastic Web UI for managing all the other Docker containers.

I'm not going into how to set these up as theres plenty of information about Docker around, just have a Google :)!

### MDADM

Because i want my main NAS HDDs to be redundant, i set them up in [RAID 1 Mirror](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_1) using MDADM. 

To set up a RAID 1 Array follow [this guide](https://www.digitalocean.com/community/tutorials/how-to-create-raid-arrays-with-mdadm-on-ubuntu-18-04#creating-a-raid-1-array).

**Tip: If your drives are new you can use the follow argument to your mdadm create command [--assume-clean](https://superuser.com/questions/438520/mdadm-raid-fast-setup-with-empty-drives). This stops you wasting resources copying 4TB (in my case) of 0s for 14 hours... **  

## Status OLED 

### I2C connections

I assume you have connected up your I2C Display following the [wiring diagram above](#OLEDUSB-Wiring). I2C 6 on the GPIO header is accessible via ```/dev/i2c-2``` from the linux terminal. The first thing you will need to do is find the address of the Display. I2C supports upto 127 addresses ```0x00 - 0x7F```. On my OLED there was a choice of two addresses based on a resistor soldered between two points that could be swapped (```0x78``` or ```0x7A```). However it turns out the PCB description was lying to me and the address was actaully ```0x3C``` go figure....

Anyway, to be able to find the address/confirm you've got something there, you can use i2c-tools to do a "detect" of the bus. Now theres a few fun caveats here:
1. I2C doesnt strictly support "discovery" so if you run this on an I2C bus thats used for other purposes (CPU Temperature sensors / Clock chips etc) it could potential have bad side effects.
2. By default i2c tools runs SMBus flavour commands which is a subset of I2C commonly used for motherboard components, if you dont use the ```-r``` argument things wont work.

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -a -r 2
```

This should give you something like:

```bash
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
```    

With this setup you are ready to use the code.
   
### Python/Docker

You can get the Docker File/Source to build the image from [here](https://github.com/mattlokes/onash2/tree/main/software/sysinfo_lcd/sysinfo_lcd_dev)

You can build/run the image as a container using the [Docker-compose YAML](https://github.com/mattlokes/onash2/tree/main/software/sysinfo_lcd)

This script uses the Luma Library which does all the hard work, and is based on one of the Luma examples which i modified to work for my use case. There are some hardcoded magic numbers in the python script which are specific to my setup, these must be changed before building the Docker image. These could(probably should) have been added as arguments to make it easier to reuse. Hopefully it will be pretty obvious what to change.


## FAQ
 - **Q: How much did this cost all in all?**
 
   A: It really depends on what you want in terms of RAM/NVME/EMMC/HDD capcity, I spent about £400 all in, but that includes 32GB of RAM which is overkill and 2x4TB 2.5" HDD. So you should be able to tailor to your budget.
 - **Q: I've got a PRUSA Mini and i struggle to get the case parts not to curl, how did you do it?**
 
   A: I had the same problem during the first attempt at printing, then i discovered this excellent mod [Silicon Bed Levelling](https://forum.prusaprinters.org/forum/user-mods-octoprint-enclosures-nozzles/prusa-mini-silicone-bed-leveling-mod/) over on the PRUSA forum. Well worth the fiddling and patience. I've had perfect first layers since!
 - **Q: Is PLA really suitable for this?**
 
   A: If you are asking this question or dont know why this could be an issue, print it in PETG to be safe :)
 - **Q: Well why did you print in PLA then?**
 
   A: Better print quality, easier to print and i understand the risks ( I think / hope ) 
