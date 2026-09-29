# Credits

The generators in this package are Python ports or reconstructions. Credit for
the domains, the original generators and the benchmark sets belongs to the
people below. Where the sources name no author, the entry says so. Nothing here
is guessed.

## Collections

- **PDDL Generators** ([AI-Planning/pddl-generators](https://github.com/AI-Planning/pddl-generators)):
  Jendrik Seipp, Álvaro Torralba and Jörg Hoffmann. *PDDL Generators*, Zenodo
  2022, [doi:10.5281/zenodo.6382173](https://doi.org/10.5281/zenodo.6382173).
  It builds on Jörg Hoffmann's [FF domain collection](http://fai.cs.uni-saarland.de/hoffmann/ff-domains.html).
- **Autoscale** ([AI-Planning/autoscale](https://github.com/AI-Planning/autoscale)):
  Álvaro Torralba, Jendrik Seipp and Silvan Sievers. "Automatic Instance
  Generation for Classical Planning". ICAPS 2021, pp. 376–384. The
  `autoscale/` generators follow the calls in its `autoscale/domains.py`.
- **Reference tasks:** the IPC tasks in `data/classical/downward-benchmarks`
  ([aibasel/downward-benchmarks](https://github.com/aibasel/downward-benchmarks)),
  the IPC 2023 learning-track tasks in `data/classical/ipc2023-learning`, and
  the Autoscale 21.11 tasks in `data/classical/autoscale-benchmarks-main`.

## Domains and generators

The `autoscale/` and `ipc_learning/` packages of a domain credit the same
people as the `ipc/` counterpart; `ipc_learning/` uses the learning track's
domain files ([ipc2023-learning/benchmarks](https://github.com/ipc2023-learning/benchmarks),
Taitler et al., AI Magazine 45(2), 2024). Notes refer to the notices in the next section.

| domain | domain authors | original generator (authors) | notes |
|---|---|---|---|
| agricola | Tomás de la Rosa (IPC 2018) | `GenAgricola.py` (Tomás de la Rosa) | |
| assembly | Drew McDermott (AIPS-1998) | reconstruction from the IPC tasks (`assembly.c` does not produce them; no code used) | |
| barman | IPC 2011; not named in the sources | `barman-generator.py`; not named | |
| blocks_3, blocks_4, blocksworld | Terry Winograd (1972), via the IPP collection | `bwstates` (John Slaney, Sylvie Thiébaux); `2pddl` converters (FF collection) | [Freiburg](#freiburg) |
| cavediving | Nathan Robinson, Christian Muise, Charles Gretton (IPC 2014) | `generator.py` (same authors) | ISC-style notice kept in `generator.py` |
| childsnack | Raquel Fuentetaja, Tomás de la Rosa (IPC 2014) | `child-snack-generator.py` (same authors) | [MIT](#mit) |
| citycar | Mauro Vallati (IPC 2014), modified by Masataro Asai | `generator.py` (Mauro Vallati) | |
| data_network | Manuel Heusner, Florian Pommerening, Álvaro Torralba (IPC 2018) | `generator.py` (Manuel Heusner) | |
| delivery | not named in the sources | `delivery/generate.py` (pddl-generators); not named | |
| depots | Derek Long, Maria Fox (IPC 2002) | `depots.cc`; not named | |
| driverlog | Derek Long, Maria Fox (IPC 2002) | `dlgen` (`generator.cc`); not named | |
| elevators | IPC 2008; not named in the sources | `generate.py`; its README says the author is unknown | |
| ferry | unknown; taken from the IPP domain collection | `ferry.c` (FF collection) | [Freiburg](#freiburg) |
| flashfill | Javier Segovia-Aguas (IPC 2018; Segovia-Aguas, Jiménez, Jonsson, ICAPS 2016) | example generators `gen0*.py`; domains rebuilt from IPC skeletons | |
| floortile | Tomás de la Rosa (IPC 2011) | `floortile-generator.py` (Tomás de la Rosa) | [MIT](#mit) |
| folding | Daniel Fišer (IPC 2023), after the ASP Competition 2011 "Reverse Folding" problem by Agostino Dovier, Andrea Formisano and Enrico Pontelli | `generate.py` (Daniel Fišer) | public domain |
| freecell | Fahiem Bacchus (AIPS-2000), adapted from a TLPLAN domain by Nolan Andres and Robert HillHouse | reconstructed from the IPC tasks; `freecell.c` (Jörg Hoffmann) was used as a reference only | [Freiburg](#freiburg) (`freecell.c`) |
| goldminer | Alan Fern (IPC 2008 learning track) | generator by Madhu Srinivasan | domain: [MIT](#mit); generator: [GPL-2.0-or-later](#goldminer-generator) |
| grid | Drew McDermott (AIPS-1998) | `grid/generate.py` (not named); `grid.c` (FF collection) | [Freiburg](#freiburg) |
| gripper | Jana Koehler (AIPS-1998) | `gripper.c` (FF collection) | [Freiburg](#freiburg) |
| hiking, hiking_binary | Lee McCluskey (IPC 2014) | `generator.py` (Lee McCluskey) | domain file: [Huddersfield](#huddersfield) |
| labyrinth | Rebecca Eifler, Daniel Fišer (IPC 2023) | `instance_generator/` (same authors) | public domain |
| logistics | Manuela Veloso; AIPS-1998 version by Bart Selman and Henry Kautz | `logistics.c` (FF collection) | [Freiburg](#freiburg) |
| maintenance | Jussi Rintanen (IPC 2014) | `maintenance.c` (Jussi Rintanen) | |
| miconic | Jana Koehler (AIPS-2000) | `miconic.c`, the original AIPS-2000 generator (FF collection) | [Freiburg](#freiburg) |
| miconic_fulladl, miconic_fulladl_goal, miconic_simpleadl | Jana Koehler (AIPS-2000) | `miconic.c` (FF collection); fulladl_goal wraps `ipc/miconic_fulladl`; simpleadl re-exports `ipc/miconic` | fulladl and fulladl_goal: [Freiburg](#freiburg) |
| movie | Corin Anderson (AIPS-1998) | `movie.c` (FF collection) | [Freiburg](#freiburg) |
| mprime, mystery | Drew McDermott (AIPS-1998) | McDermott's generator is not public; reconstructed from the IPC tasks, no code from `mprime.c`/`mystery.c` | |
| nomystery | IPC 2011; not named in the sources | `nomystery` (pddl-generators); not named | |
| nurikabe | Álvaro Torralba, Florian Pommerening (IPC 2018) | `generate.py` (same authors) | |
| openstacks | Patrik Haslum (IPC 2006; IPC 2008 ADL cost version); 2006 instances from the 2005 Constraint Modelling Challenge (Barbara Smith, Ian Gent) | matrix generator after Ioannis Refanidis's `generate_problems` (pddl-generators `generator.py`) | |
| parking | IPC 2008; not named in the sources | `parking-generator.pl`; not named | |
| pathways | Yannis Dimopoulos, Alfonso Gerevini, Alessandro Saetti (IPC 2006) | `main.c` (same authors) | |
| pegsol | IPC 2008; not named in the sources | new generator; upstream converts the Solipeg 2.2 library (J Cade Roux, GPL-2.0-or-later), from which no puzzles are included | |
| recharging_robots | Daniel Gnad, Álvaro Torralba, with Daniel Fišer (IPC 2023) | `generator.py` (same authors) | public domain |
| ricochet_robots | Daniel Fišer (IPC 2023), after the board game and the ASP Competition 2015 instances | `generate.py`, `asp-to-pddl.py` (Daniel Fišer) | no license statement in the repository |
| rovers | IPC 2002; not named in the sources | `rovgen.cc`; not named | |
| rubiks_cube | Bharath Muppasani, Biplav Srivastava, Clemens Büchner, Patrick Ferber (IPC 2023) | `generator.py` (same authors) | public domain |
| satellite | Maria Fox, Derek Long (IPC 2002) | `satgen.cc` (Derek Long, Maria Fox) | |
| scanalyzer | Malte Helmert (IPC 2008) | `generator.py`; not named | |
| schedule | Manuela Veloso (Prodigy collection); prepared for AIPS-2000 by Fahiem Bacchus | `schedule.c` (FF collection) | [Freiburg](#freiburg) |
| settlers | Marcel Steinmetz, after Patrik Haslum's IPC 2002 Settlers (IPC 2018) | Autoscale's `settlers` generator (CPLEX step replaced) | |
| slitherlink | IPC 2023; not named in the sources | `generate.hs` (Harald Bögeholz) and `generate-pddl.py` (public domain part only) | [BSD-2-Clause](#slitherlink-generator) |
| snake | Álvaro Torralba, Florian Pommerening (IPC 2018) | `generate.py` (same authors) | |
| sokoban | IPC 2008 | new generator; the IPC tasks are Microban levels by David W. Skinner, converted by `build-problems.py` | |
| spanner | Amanda Coles, Andrew Coles, Maria Fox, Derek Long (IPC 2011) | pddl-generators `spanner`; not named | |
| spider | IPC 2018; not named in the sources | `generate.py`; not named | |
| storage | Alfonso Gerevini, Alessandro Saetti (IPC 2006) | `main.cpp` (same authors) | |
| termes | Sven Koenig, Satish Kumar (IPC 2018) | generator and solver by Álvaro Torralba, Florian Pommerening | |
| tetris | Mauro Vallati (IPC 2014) | generator by Mauro Vallati | |
| tidybot | Bhaskara Marthi (IPC 2011) | `core.clj` (Bhaskara Marthi) | |
| tpp | Alfonso Gerevini, Alessandro Saetti (IPC 2006) | `gen-TPP` (same authors) | |
| transport, transport_fuel | IPC 2008; not named in the sources | city, two-cities and three-cities generators; not named. `misc/transport_fuel` is a variant of our own | |
| trucks | Yannis Dimopoulos, Alfonso Gerevini, Alessandro Saetti (IPC 2006) | `trucks.c` (same authors), lifted ADL version | |
| visitall | Nir Lipovetzky (IPC 2011) | `grid.c` (FF collection), goal-ratio version submitted by Nir Lipovetzky | domain: [MIT](#mit); generator: [Freiburg](#freiburg) |
| woodworking | IPC 2008; not named in the sources | `create_woodworking_instance.py`; not named | |
| zenotravel | IPC 2002; not named in the sources | `zenogenerator.cc`; not named | |

## Notices

These notices come with the upstream sources the ports are based on. They are
reproduced verbatim, as the notices require.

### Freiburg

Carried by the FF-collection generators marked above (`gripper.c`,
`logistics.c`, `grid.c`, `miconic.c`, `schedule.c`, `ferry.c`, `movie.c`,
`freecell.c`, the blocksworld `2pddl` converters, and others).

The following modules derive from those generators. They keep this notice
(`SPDX-License-Identifier: LicenseRef-Freiburg`, see
`LICENSES/LicenseRef-Freiburg.txt`) and may be used for non-commercial research
only; the rest of the package is GPL-3.0-or-later:

- `classical/ipc/{blocks_3,blocks_4,ferry,gripper,logistics,miconic,miconic_fulladl,movie,schedule,visitall}/generator.py`
- `classical/autoscale/{blocksworld,freecell,logistics,mprime}/generator.py`
- `classical/ipc_learning/{blocksworld,ferry,miconic}/generator.py`
- `classical/misc/miconic_fulladl_goal/generator.py`

`ipc/freecell`, `ipc/mprime` and `ipc/mystery` were rebuilt from the IPC tasks
without code from `freecell.c`, `mprime.c` or `mystery.c` (the `autoscale/`
freecell and mprime ports do derive from them, see above), and `ipc/grid` ports
`grid/generate.py`, which carries no notice.

```
(C) Copyright 2001 Albert Ludwigs University Freiburg
    Institute of Computer Science

All rights reserved. Use of this software is permitted for
non-commercial research purposes, and it may be copied only
for that use.  All copies must include this copyright message.
This software is made available AS IS, and neither the authors
nor the  Albert Ludwigs University Freiburg make any warranty
about the software or its performance.
```

### Huddersfield

Carried by the hiking domain file:

```
(c) 2001 Copyright (c) University of Huddersfield
Automatically produced from GIPO from the domain hiking
All rights reserved. Use of this software is permitted for non-commercial
research purposes, and it may be copied only for that use.  All copies must
include this copyright message.  This software is made available AS IS, and
neither the GIPO team nor the University of Huddersfield make any warranty about
the software or its performance.
```

### MIT

Covers childsnack (Copyright (c) 2013 Raquel Fuentetaja and Tomas de la Rosa),
floortile (Copyright (c) 2013 Tomas de la Rosa), the visitall domain
(Copyright (c) 2011 Nir Lipovetzky) and the goldminer domain (Copyright (c)
2008 Alan Paul Fern):

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Goldminer generator

Copyright (C) 2008 by Madhu Srinivasan (srinivma@gmail.com). Distributed under
the GNU General Public License as published by the Free Software Foundation,
either version 2 of the License, or (at your option) any later version.

### Slitherlink generator

`classical/ipc/slitherlink/generator.py` derives from `generate.hs` and keeps
its notice in the file header:

```
Copyright (c) 2012, Harald Bögeholz (bo@ct.de)
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those of the authors and should not be interpreted as representing official policies, either expressed or implied, of the FreeBSD Project.
```

## Numeric domains and generators

Generators in `numeric/ipc/`. Reconstructions contain no upstream code; the
reference tasks are the IPC 2023 and IPC 2026 numeric-track datasets. None of
the domain or task files carries a license notice.

| domain | domain authors | generator | notes |
|---|---|---|---|
| block_grouping | Enrico Scala, Miquel Ramirez | reconstruction | |
| coins | Connor Little | reconstruction | |
| counters | Guillem Francès, Hector Geffner; numeric version by Enrico Scala, Miquel Ramirez | reconstruction | |
| delivery | Alexander Shleyfman, Ryo Kuroiwa | reconstruction | |
| drone | Enrico Scala | reconstruction | |
| expedition | Joan Espasa Arxer, after Ben Pathak | reconstruction | |
| ext_plant_watering | Joan Espasa Arxer, after Plant Watering by Guillem Francès, Hector Geffner (numeric by Scala, Ramirez) | reconstruction | |
| factory_robot | Joan Espasa Arxer | reconstruction | |
| farmland, fo_farmland | Enrico Scala, Miquel Ramirez; fo_ version Enrico Scala, Dongxu Li | port of `farmlandgenerator.py` ([hstairs/planning-numeric-domains-generators](https://github.com/hstairs/planning-numeric-domains-generators), Enrico Scala) | no license statement in the repository |
| fo_counters | Enrico Scala, Dongxu Li | reconstruction | |
| forestfire | Alexander Shleyfman | reconstruction | |
| game_2048 | Christian Muise, Samantha Papais, Ronny Rochwerg | reconstruction | |
| gear_car | not named in the files | reconstruction | |
| hydropower, markettrader, sugar | Amanda Coles, Maria Fox, Derek Long (JAIR 46, 2013) | reconstruction | |
| line_exchange_snp | not named in the files | reconstruction | |
| mprime | Drew McDermott (IPC 1998) | translation of the `classical/ipc/mprime` reconstruction | |
| onlycraft | after Benyamin, Mordoch, Shperberg, Piotrowski, Stern, "Crafting a Pogo Stick in Minecraft with Heuristic Search" | reconstruction | |
| pathwaysmetric | Yannis Dimopoulos, Alfonso Gerevini, Alessandro Saetti (IPC 2006); atemporal version by Amanda Coles, Maria Fox, Derek Long | port of pathways `main.c -N` | |
| petri_net | "Anonymous" | reconstruction | |
| rainbowttles | Alba Gragera | reconstruction | |
| rover | IPC 2002; not named in the sources | port of `rovgen -n` | |
| sailing, fo_sailing | Enrico Scala, Miquel Ramirez; fo_ version Enrico Scala, Dongxu Li | port of `generate_saving.py` (hstairs/planning-numeric-domains-generators, Enrico Scala) | no license statement in the repository |
| sailing_wind | Luigi Bonassi, Carl Hentges | reconstruction | |
| settlers_snp | Enrico Scala, Miquel Ramirez, after Patrik Haslum's IPC 2002 Settlers | reconstruction | |
| settlersnumeric | Maria Fox, Derek Long (IPC 2002); pddl-generators credits Patrik Haslum | reconstruction | |
| tpp | Alfonso Gerevini, Alessandro Saetti (IPC 2006); IPC 2023 tasks by Enrico Scala, Miquel Ramirez | reconstruction | |
| zenotravel | IPC 2002; "Author unknown" | port of `zenogenerator -n` | |
| ztalloc_sum | Christian Muise | reconstruction | |
