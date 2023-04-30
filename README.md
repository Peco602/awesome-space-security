# Awesome Space Security [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

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

<!--TOC-->

- [Legend](#legend)
- [Threat Modeling](#threat-modeling)
- [Standards](#standards)
  - [Aerospace Industries Association (AIA)](#aerospace-industries-association-aia)
  - [Consultative Committee for Space Data Systems (CCSDS)](#consultative-committee-for-space-data-systems-ccsds)
  - [National Institute of Standards and Technology (NIST)](#national-institute-of-standards-and-technology-nist)
  - [National Aeronautics and Space Administration (NASA)](#national-aeronautics-and-space-administration-nasa)
  - [Ministry of Economy, Trade and Industry (METI)](#ministry-of-economy-trade-and-industry-meti)
  - [Federal Office for Information Security (BSI)](#federal-office-for-information-security-bsi)
  - [Committee on National Security Systems (CNSS)](#committee-on-national-security-systems-cnss)
- [Papers](#papers)
- [Books](#books)
- [Software](#software)

<!--TOC-->
---

## Legend

-   Abandoned :skull:
-   Draft :construction:
-   Monetized :heavy_dollar_sign:

## Threat Modeling

- [Space Attack Research & Tactic Analysis (SPARTA)](https://sparta.aerospace.org/) - SPARTA is intended to provide unclassified information to space professionals about how spacecraft may be compromised via cyber and traditional counterspace means

## Standards

### Aerospace Industries Association (AIA)

- [NAS9933](https://global.ihs.com/doc_detail.cfm?&csf=AIA&item_s_key=00773721&item_key_date=870400&input_doc_number=NAS9933&input_doc_title=&org_code=AIA%2FNAS) - Critical Security Controls for Effective Capability in Cyber Defense :heavy_dollar_sign:

### Consultative Committee for Space Data Systems (CCSDS)

- [CCSDS 350.0-G-3](https://public.ccsds.org/Pubs/350x0g3.pdf) - The Application of Security to CCSDS Protocols
- [CCSDS 350.1-G-3](https://public.ccsds.org/Pubs/350x1g3.pdf) - Security Threats against Space Missions
- [CCSDS 350.4-G-2](https://public.ccsds.org/Pubs/350x4g2.pdf) - CCSDS Guide for Secure System Interconnection
- [CCSDS 350.5-G-1](https://public.ccsds.org/Pubs/350x5g1.pdf) - Space Data Link Security Protocol - Summary of Concept and Rationale
- [CCSDS 350.6-G-1](https://public.ccsds.org/Pubs/350x6g1.pdf) - Space Missions Key Management Concept
- [CCSDS 350.7-G-2](https://public.ccsds.org/Pubs/350x7g2.pdf) - Security Guide for Mission Planners
- [CCSDS 350.8-M-2](https://public.ccsds.org/Pubs/350x8m2.pdf) - Information Security Glossary of Terms
- [CCSDS 350.9-G-1](https://public.ccsds.org/Pubs/350x9g1.pdf) - CCSDS Cryptographic Algorithms
- [CCSDS 351.0-M-1](https://public.ccsds.org/Pubs/351x0m1.pdf) - Security Architecture for Space Data Systems
- [CCSDS 352.0-B-2](https://public.ccsds.org/Pubs/352x0b2.pdf) - CCSDS Cryptographic Algorithms
- [CCSDS 355.0-B-2](https://public.ccsds.org/Pubs/355x0b2.pdf) - Space Data Link Security Protocol
- [CCSDS 355.1-B-1](https://public.ccsds.org/Pubs/355x1b1.pdf) - Space Data Link Security Protocol - Extended Procedures
- [CCSDS 356.0-B-1](https://public.ccsds.org/Pubs/356xb1.pdf) - Network Layer Security Adaptation Profile
- [CCSDS 357.0-B-1](https://public.ccsds.org/Pubs/357x0b1.pdf) - CCSDS Authentication Credentials
- [CCSDS A13.1-Y-1](https://public.ccsds.org/Pubs/A13x1y1.pdf) - CCSDS Recommended Procedures for Cloud-Based Interoperability Testing

### National Institute of Standards and Technology (NIST)

- [NIST IR 8270](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8270-draft2.pdf) - Introduction to Cybersecurity for Commercial Satellite Operations :construction:
- [NIST IR 8323](https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8323.pdf) - Foundational PNT Profile: Applying the Cybersecurity Framework for the Responsible Use of Positioning, Navigation, and Timing (PNT) Services
- [NIST IR 8401](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8401.pdf) - Satellite Ground Segment (*Applying the Cybersecurity Framework to Satellite Command and Control*)
- [NIST SP 800-161](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-161.pdf) - Supply Chain Risk Management Practices for Federal Information Systems and Organizations
- [NIST SP 800-53 Rev. 5](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) - Security and Privacy Controls for Information Systems and Organizations

### National Aeronautics and Space Administration (NASA)

- [MRPP.CPS.20201216](https://explorers.larc.nasa.gov/2023APPROBE/pdf_files/NASA13.%20MRPP_CPS_Candidate_Protection_Strategies-v4.5-20201216.pdf) - Candidate Protection Strategies
- [NASA-STD-1006A](https://standards.nasa.gov/sites/default/files/standards/NASA/A/0/2022-07-15-NASA-STD-1006A-Approved.pdf) - Space System Protection Standard
- [NASA-STD-8719.13C](https://standards.nasa.gov/sites/default/files/standards/NASA/C-Change-2/0/nasa-std-871913c_with_change_2.docx) - Software Safety Standard
- [NASA/SP-2010-580](https://ntrs.nasa.gov/api/citations/20120003291/downloads/20120003291.pdf) - NASA System Safety Handbook Volume 1, System Safety Framework and Concepts for Implementation
- [NASA/SP-2014-612](https://ntrs.nasa.gov/api/citations/20150015500/downloads/20150015500.pdf) - NASA System Safety Handbook Volume 2: System Safety Concepts, Guidelines, and Implementation Examples

### Ministry of Economy, Trade and Industry (METI)

- [Cybersecurity Guidelines for Commercial Space Systems](https://www.meti.go.jp/shingikai/mono_info_service/sangyo_cyber/wg_seido/wg_uchu_sangyo/pdf/20230331_1e.pdf)

### Federal Office for Information Security (BSI)

- [IT baseline protection profile for space infrastructures](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Grundschutz/profiles/Profile_Space-Infrastructures.pdf?__blob=publicationFile&v=2) - Minimum Protection for Satellites Covering their Entire Life Cycle

### Committee on National Security Systems (CNSS)

- [CNSSP-12](https://www.hsdl.org/?view&did=726945) - National Information Assurance Policy for Space Systems used to Support National Security Missions


## Papers

- [Cybersecurity Protections for Spacecraft: A Threat Based
Approach](https://aerospace.org/sites/default/files/2022-07/DistroA-TOR-2021-01333-Cybersecurity%20Protections%20for%20Spacecraft--A%20Threat%20Based%20Approach.pdf), April 2021
- [PCspooF: Compromising the Safety of
Time-Triggered Ethernet](https://web.eecs.umich.edu/~barisk/public/pcspoof.pdf), 2023 IEEE Symposium on Security and Privacy (SP)

## Books

- [Cybersecurity for Space](https://link.springer.com/book/10.1007/978-1-4842-5732-6) - The first book focused on the implementation of cybersecurity for space systems :heavy_dollar_sign:

## Software

- [CryptoLib](https://github.com/nasa/CryptoLib) - Provide a software-only solution using the CCSDS Space Data Link Security Protocol - Extended Procedures (SDLS-EP) to secure communications between a spacecraft running the core Flight System (cFS) and a ground station.
- [CITEF](https://www.rheagroup.com/document/citef-pdf-brochure/) - Next Generation Cyber-Range Services for space missions :heavy_dollar_sign:
- [QA707](https://www.qascom.it/GNSS-software-simulation.php) - Fully configurable GNSS Software Defined Radio (SDR) simulator for flexible generations of GNSS signals, interferences and authentication schemes up to RF level :heavy_dollar_sign:
---

If you have any question about this opinionated list, do not hesitate to contact me [@Peco602](https://twitter.com/peco602) on Twitter or open an issue on GitHub.
