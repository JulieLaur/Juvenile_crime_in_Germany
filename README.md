## Juvenile_crime_in_Germany
This repository shows our final project of the Advanced Data Analytics Bootcamp at neuefische GmbH:  
# Juvenile crime in Germany - current extent, distribution, and development
In this README file, you find an introduction to the topic and a description on the fictitious scenario that we assumed as our assigned task. Furthermore, you find a description of the scope, the sources and the tools we used. <br>

If you would like to see our final delivery directly, click on the following link: https://crime-germany.streamlit.app/.<br> It redirects you to our dashboard that provides at-a-glance views on the current extent, distribution, and recent development of juvenile crime in Germany and its 16 federal states.<br>

This repository provides in several jupyter notebooks the code we used to gather, clean, and prepare the data for our dashboard. Furthermore, you find code on creating some additional charts for the final presentation of our project, which was held on the 21st of August 2023.<br>

The code that runs the dashboard can be viewed in a separate repository: LINK

## What is juvenile crime?
In Germany, offences committed by persons aged between 14 and 20 are classified as juvenile crime. That means juvenile crime not only includes offences by juveniles (persons aged 14 to under 18), but also offences commited by adolescents (persons aged 18 to under 21).

## Scenario (Fictive)
While the implementation competence of preventive action against juvenile crime lies with the 16 federal states of Germany, the research on prevention and the development of preventive strategies is taken over by social science research institutes. Germany is involved in this process in the role of the Bundesministerium für Familie, Senioren, Frauen und Jugend. The BMFSFJ is responsible for stimulating action in the 16 federal states and for allocating funds on research.  

In order to be able to optimally fulfill its competences to stimulate adequate action and to distribute funds appropriately, the BMFSFJ assigned us to provide them with a comprehensive overview of the current extent of juvenile crime in Germany.

They would like to know the current level of juvenile crime, the development over the recent years, the offenses that account for the majority of juvenile crime, and the distribution of the most common offenses.

### Scope

* Time frame: last five years (2018 - 2022)
* Area: Germany and its 16 federal states
* Age groups:
    * 14 < 16
    * 16 < 18
    * 18 < 21
* Selected crimes: <br>
---
|BKA Schluessel|Crime German|Crime English|
---|---|---|
|------|Straftaten insgesamt|Total offences|
|100000|Straftaten gegen die sexuelle Selbstbestimmung insgesamt|Sexual offences|
|210000|Raub, räuberische Erpressung und räuberischer Angriff auf Kraftfahrer §§ 249-252, 255, 316a StGB|Robbery|
|220000|Körperverletzung §§ 223-227, 229, 231 StGB|Assault|
|232100|Freiheitsberaubung § 239 StGB|Deprivation of liberty|
|232200|Nötigung § 240 StGB|Coercion|
|435*00|Wohnungseinbruchdiebstahl §§ 244 Abs. 1 Nr. 3 und Abs. 4, 244a StGB|Residential burglary|
|*26*00|Ladendiebstahl insgesamt|Shoplifting|
|674000|Sachbeschädigung §§ 303-305a StGB|Damage to property|
|730000|Rauschgiftdelikte (soweit nicht bereits mit anderer Schlüsselzahl erfasst)|Drug offences (w/o procurement)|
|891100|direkte Beschaffungskriminalität|Drug procurement crime|
|010000, 020010|Mord § 211 StGB, Totschlag § 212 StGB|Homicide|

## Data Sources

* Police crime statistics: PKS Bundeskriminalamt, 2018 - 2022, Version 2.0

* German federal statistical office (Statistisches Bundesamt - Destatis)
