# Awesome Space Security

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Check URLs](https://github.com/Peco602/awesome-space-security/actions/workflows/check-urls.yml/badge.svg)](https://github.com/Peco602/awesome-space-security/actions/workflows/check-urls.yml)
[![GitHub Pages](https://github.com/Peco602/awesome-space-security/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/Peco602/awesome-space-security/actions/workflows/gh-pages.yml)

> A curated list of awesome resources about the security of space systems.

If you would like to contribute, please read [CONTRIBUTING.md](https://github.com/Peco602/awesome-space-security/blob/main/CONTRIBUTING.md) first.
It contains a lot of tips and guidelines to help keep things organized.
Just click [README.md](https://github.com/Peco602/awesome-space-security/edit/main/README.md) to submit a pull request.
If this list is not complete, you can contribute to make it so. Here is a great video tutorial to learn how to [contribute on Github](https://egghead.io/lessons/javascript-identifying-how-to-contribute-to-an-open-source-project-on-github).

> **Please**, help organize these resources so that they are _easy to find_ and _understand_ for newcomers.

**_If you see a link here that is not (any longer) a good fit, you can fix it by submitting a [pull request](https://github.com/Peco602/awesome-space-security/edit/main/README.md) to improve this file. Thank you!_**

> Inspired by [awesome-python](https://github.com/vinta/awesome-python).

![Space Security](https://sparta.aerospace.org/theme/images/Threat_Landscape.png)

## Table of contents

<!--TOC-->

- [Table of contents](#table-of-contents)
- [Legend](#legend)
- [Books](#books)
- [Directives](#directives)
- [Papers](#papers)
- [Reports](#reports)
- [Talks](#talks)
- [Threat Modeling](#threat-modeling)
- [Tools](#tools)

<!--TOC-->

<!--LEGEND-->

## Legend

-   Draft :construction:
-   Paid :heavy_dollar_sign:
-   Abandoned :skull:

<!--LEGEND-->

---

<!--CONTENT-->

## Books
- `2020.03.31` [Cybersecurity for Space: Protecting the Final Frontier](https://www.google.it/books/edition/Cybersecurity_for_Space/31DaDwAAQBAJ?hl=it&gbpv=0): The first book focused on the implementation of cybersecurity for space systems :heavy_dollar_sign:

## Directives

### Aerospace Industries Association (AIA)
- `2018.11.29` [NAS9933](https://global.ihs.com/doc_detail.cfm?&csf=AIA&item_s_key=00773721&item_key_date=870400&input_doc_number=NAS9933&input_doc_title=&org_code=AIA%2FNAS): Critical Security Controls for Effective Capability in Cyber Defense :heavy_dollar_sign:

### Committee on National Security Systems (CNSS)
- `2012.11.28` [CNSSP-12](https://www.hsdl.org/?view&did=726945): National Information Assurance Policy for Space Systems used to Support National Security Missions

### Consultative Committee for Space Data Systems (CCSDS)
- `2011.11` [CCSDS 350.6-G-1](https://public.ccsds.org/Pubs/350x6g1.pdf): Space Missions Key Management Concept
- `2012.11` [CCSDS 351.0-M-1](https://public.ccsds.org/Pubs/351x0m1.pdf): Security Architecture for Space Data Systems
- `2014.12` [CCSDS 350.9-G-1](https://public.ccsds.org/Pubs/350x9g1.pdf): CCSDS Cryptographic Algorithms
- `2018.06` [CCSDS 350.5-G-1](https://public.ccsds.org/Pubs/350x5g1.pdf): Space Data Link Security Protocol - Summary of Concept and Rationale
- `2018.06` [CCSDS 356.0-B-1](https://public.ccsds.org/Pubs/356xb1.pdf): Network Layer Security Adaptation Profile
- `2018.06` [CCSDS A13.1-Y-1](https://public.ccsds.org/Pubs/A13x1y1.pdf): CCSDS Recommended Procedures for Cloud-Based Interoperability Testing
- `2019.03` [CCSDS 350.0-G-3](https://public.ccsds.org/Pubs/350x0g3.pdf): The Application of Security to CCSDS Protocols
- `2019.04` [CCSDS 350.4-G-2](https://public.ccsds.org/Pubs/350x4g2.pdf): CCSDS Guide for Secure System Interconnection
- `2019.04` [CCSDS 350.7-G-2](https://public.ccsds.org/Pubs/350x7g2.pdf): Security Guide for Mission Planners
- `2019.07` [CCSDS 357.0-B-1](https://public.ccsds.org/Pubs/357x0b1.pdf): CCSDS Authentication Credentials
- `2019.08` [CCSDS 352.0-B-2](https://public.ccsds.org/Pubs/352x0b2.pdf): CCSDS Cryptographic Algorithms
- `2020.02` [CCSDS 350.8-M-2](https://public.ccsds.org/Pubs/350x8m2.pdf): Information Security Glossary of Terms
- `2020.02` [CCSDS 355.1-B-1](https://public.ccsds.org/Pubs/355x1b1.pdf): Space Data Link Security Protocol - Extended Procedures
- `2022.02` [CCSDS 350.1-G-3](https://public.ccsds.org/Pubs/350x1g3.pdf): Security Threats against Space Missions
- `2022.07` [CCSDS 355.0-B-2](https://public.ccsds.org/Pubs/355x0b2.pdf): Space Data Link Security Protocol

### European Space Agency (ESA)
- `1994.10` [ESA PSS-05-0 Issue 2](http://microelectronics.esa.int/vhdl/pss/PSS-05-0.pdf): ESA software engineering standards
- `2000.03.30` [BSSC(2000)1 Issue 1](http://everyspec.com/ESA/download.php?spec=BSSC_2000-1_I1_2000.029384.pdf): ESA C and C++ Coding Standards
- `2009.03.06` [ECSS-E-ST-40C](https://ecss.nl/standard/ecss-e-st-40c-software-general-requirements/): Software
- `2013.12.11` [ECSS-E-HB-40A](https://ecss.nl/hbstms/ecss-e-hb-40a-software-engineering-handbook-11-december-2013/): Software engineering handbook
- `2017.02.15` [ECSS-Q-ST-80C](https://ecss.nl/standard/ecss-q-st-80c-rev-1-software-product-assurance-15-february-2017/): Software product assurance
- `2017.11.22` [ECSS-Q-HB-80-03A Rev.1](https://ecss.nl/hbstms/20347/): Software dependability and safety
- `2022.05.31` [ECSS-E-ST-10-03C Rev.1](https://ecss.nl/standard/ecss-e-st-10-03c-rev-1-testing-31-may-2022/): Testing

### Federal Office for Information Security (BSI)
- `2022.06.30` [IT baseline protection profile for space infrastructures](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Grundschutz/profiles/Profile_Space-Infrastructures.pdf?__blob=publicationFile&v=2): Minimum Protection for Satellites Covering their Entire Life Cycle

### Ministry of Economy, Trade and Industry (METI)
- `2023.03` [Cybersecurity Guidelines for Commercial Space Systems](https://www.meti.go.jp/shingikai/mono_info_service/sangyo_cyber/wg_seido/wg_uchu_sangyo/pdf/20230331_1e.pdf)

### National Aeronautics and Space Administration (NASA)
- `2011.11` [NASA/SP-2010-580](https://ntrs.nasa.gov/api/citations/20120003291/downloads/20120003291.pdf): NASA System Safety Handbook Volume 1: System Safety Framework and Concepts for Implementation
- `2014.11` [NASA/SP-2014-612](https://ntrs.nasa.gov/api/citations/20150015500/downloads/20150015500.pdf): NASA System Safety Handbook Volume 2: System Safety Concepts, Guidelines, and Implementation Examples
- `2020.09.04` [SPD-5](https://history.nasa.gov/SPD-5.pdf): Cybersecurity Principles for Space Systems
- `2020.12.16` [MRPP.CPS.20201216](https://explorers.larc.nasa.gov/2023APPROBE/pdf_files/NASA13.%20MRPP_CPS_Candidate_Protection_Strategies-v4.5-20201216.pdf): Candidate Protection Strategies
- `2022.07.15` [NASA-STD-1006A](https://standards.nasa.gov/sites/default/files/standards/NASA/A/0/2022-07-15-NASA-STD-1006A-Approved.pdf): Space System Protection Standard

### National Institute of Standards and Technology (NIST)
- `1994.08.01` [SEL-94-003](https://ntrs.nasa.gov/api/citations/19950022400/downloads/19950022400.pdf): NASA C Coding Standard and Style Guide
- `2004.03.31` [NASA-GB-8719.13](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/nasa-gb-8719.13.pdf): NASA Software Safety Guidebook
- `2005.05.24` [SEL-94-003](https://ntrs.nasa.gov/api/citations/20080039927/downloads/20080039927.pdf): NASA C++ Coding Standard and Style Guide
- `2020.09` [NIST SP 800-53 Rev. 5](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf): Security and Privacy Controls for Information Systems and Organizations
- `2021.02` [NIST IR 8323](https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8323.pdf): Foundational PNT Profile: Applying the Cybersecurity Framework for the Responsible Use of Positioning, Navigation, and Timing (PNT) Services
- `2022.02` [NIST IR 8270](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8270-draft2.pdf): Introduction to Cybersecurity for Commercial Satellite Operations :construction:
- `2022.05` [NIST SP 800-161r1](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-161r1.pdf): Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations
- `2022.12` [NIST IR 8401](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8401.pdf): Satellite Ground Segment: Applying the Cybersecurity Framework to Satellite Command and Control

## Papers
- `2016.04.30` [Satellite Network Hacking & Security Analysis](https://www.cscjournals.org/manuscript/Journals/IJCSS/Volume10/Issue1/IJCSS-1200.pdf), International Journal of Computer Science and Security (IJCSS)
- `2018.12` [Cybersecurity Principles for Space Systems](https://2ea998fc-9f95-482a-87f8-dd57460966a8.filesusr.com/ugd/e741d3_daa22cd1e5234b8f9139fa9c7406be29.pdf), Journal of Aerospace Computing, Information and Communication
- `2021.07` [CubeSat Security Attack Tree Analysis](https://www.computer.org/csdl/proceedings-article/smc-it/2021/856000a068/1ANLcp3WNag), 8th IEEE International Conference on Space Mission Challenges for Information Technology (SMC-IT 2021)
- `2023.05.26` [PCspooF: Compromising the Safety of Time-Triggered Ethernet](https://web.eecs.umich.edu/~barisk/public/pcspoof.pdf), IEEE Symposium on Security and Privacy 2023

## Reports
- `2019.11` [Defending Spacecraft in the Cyber Domain](https://aerospace.org/sites/default/files/2019-11/Bailey_DefendingSpacecraft_11052019.pdf)
- `2020.10` [Establishing Space Cybersecurity Policy, Standards, & Risk Management Practices](https://aerospace.org/sites/default/files/2020-10/Bailey%20SPD5_20201010%20V2_formatted.pdf)
- `2021.04.29` [Cybersecurity Protections for Spacecraft: A Threat Based Approach](https://aerospace.org/sites/default/files/2022-07/DistroA-TOR-2021-01333-Cybersecurity%20Protections%20for%20Spacecraft--A%20Threat%20Based%20Approach.pdf)
- `2023.04` [Space Threat Assessment: A Report of the CSIS Aerospace Security Project](https://csis-website-prod.s3.amazonaws.com/s3fs-public/2023-04/230414_Bingen_Space_Assessment.pdf?VersionId=oMsUS8MupLbZi3BISPrqPCKd5jDejZnJ)

## Talks

### Black Hat
- `2009.02.18` [Satellite Hacking for Fun and Profit](https://www.youtube.com/watch?v=PyXZX63etog), Black Hat DC 2009
- `2014.08.06` [SATCOM Terminals: Hacking by Air, Sea, and Land](https://www.youtube.com/watch?v=YeKswEamOl4), Black Hat USA 2014
- `2015.08.05` [Spread Spectrum Satcom Hacking Attacking The Globalstar Simplex Data Service](https://www.youtube.com/watch?v=arPqhHQ-R4o), Black Hat USA 2015
- `2020.08.05` [Whispers Among the Stars: A Practical Look at Perpetrating Satellite Eavesdropping Attacks](https://www.youtube.com/watch?v=d5Sbwlu6f8o), Black Hat USA 2020

### CYSAT
- `2022.04.07` [Cyber range for space a way to optimize the cybersecurity process](https://www.youtube.com/watch?v=Kfwiw-2TkMw), CYSAT 2022

### DEF CON
- `2012.10.31` [Satellite Hacking: An Introduction](https://www.youtube.com/watch?v=xIsG8GpB67A), DEF CON Switzerland 2012
- `2020.08.07` [Exploiting Spacecraft](https://www.youtube.com/watch?v=b8QWNiqTx1c), DEF CON 28 Aerospace Village
- `2021.08.06` [Unboxing the Spacecraft Software BlackBox Hunting for Vulnerabilities](https://www.youtube.com/watch?v=WvKtdXSRvhM), DEF CON 29 Aerospace Village
- `2022.08.13` [Hunting for Spacecraft Zero Days using Digital Twins](https://www.youtube.com/watch?v=t_efCpd2PbM), DEF CON 30 Aerospace Village

### Other conferences
- `2016.07.24` [Iridium Satellite Hacking](https://www.youtube.com/watch?v=cvKaC4pNvck), HOPE XI 2016
- `2016.12.27` [Reverse Engineering Outernet](https://www.youtube.com/watch?v=TCoSRx7DpGY), 33C3
- `2017.01.27` [Reverse Engineering Satellite Based IP Content Distribution](https://www.youtube.com/watch?v=U1WyBP4lKZk), ReCon Brussels 2017
- `2018.10.12` [Hacking Yachts Remotely via Satcom or Maritime Internet Router](https://www.youtube.com/watch?v=mT7dXJ_ob8k)
- `2020.02` [GPS As An Attack Vector](https://www.youtube.com/watch?v=Duxr1yRKRoU), S4 Conference 2020
- `2022.09.10` [Satellite Communications Reverse Engineering](https://www.youtube.com/watch?v=qAiqKHG6uYM&t=17389s), GambiConf EU 2022

## Threat Modeling
- [MITRE ATT&CK® Matrix for ICS](https://attack.mitre.org/matrices/ics/): Knowledge base of adversary tactics and techniques against Industrial Control Systems (ICS) based on real-world observations
- [Space Attack Research & Tactic Analysis (SPARTA)](https://sparta.aerospace.org/): Knowledge base of unclassified information to space professionals about how spacecraft may be compromised via cyber and traditional counterspace means
- [Space Attacks and Countermeasures Engineering Shield (SPACE-SHIELD)](https://spaceshield.esa.int/): A MITRE ATT&CK® like knowledge-base framework for Space Systems. It is a collection of adversary tactics and techniques, and a security tool applicable in the Space environment to strengthen the security level. 

## Tools
- [CITEF](https://www.rheagroup.com/document/citef-pdf-brochure/): Next Generation Cyber-Range Services for space missions :heavy_dollar_sign:
- [CryptoLib](https://github.com/nasa/CryptoLib): Provide a software-only solution using the CCSDS Space Data Link Security Protocol - Extended Procedures (SDLS-EP) to secure communications between a spacecraft running the core Flight System (cFS) and a ground station.
- [QA707](https://www.qascom.it/GNSS-software-simulation.php): Fully configurable GNSS Software Defined Radio (SDR) simulator for flexible generations of GNSS signals, interferences and authentication schemes up to RF level :heavy_dollar_sign:
- [iSAFT](https://www.teletel.eu/products-overview/): Advanced solutions for the validation of satellite/spacecraft on-board data networks including SpaceWire, SpaceFibre, MIL-STD-1553, Time-Triggered Ethernet, CAN/CANOpen, WizardLink and others :heavy_dollar_sign:
<!--CONTENT-->

---

If you have any question about this opinionated list, do not hesitate to contact me [@Peco602](https://twitter.com/peco602) on Twitter or open an issue on GitHub.
