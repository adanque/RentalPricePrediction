# New York Apartment Rental Price Prediction

## _Predicting Rental Prices in NYC - Evaluating Price Factors !!!Under Construction - Currently in progress!!!_

<a href="https://www.linkedin.com/in/alandanque"> Author: Alan Danque </a>

<a href="https://adanque.github.io/">Click here to go back to Portfolio Website </a>

![A remote image](https://adanque.github.io/assets/img/work-analytics.jpg)

Abstract: 

Everyone likes to have a place of their own that they can call home. A place where one can rest, recharge, and relax. A place where a person can safely store their possessions. Finding such a place can be an ordeal no matter if you are a renter, a homeowner, or a landlord. As the price of any type of home is affected by many different factors. The confusing caveats are trying to understand which factors affect the value or rental price. And if the value is credible or just overly bloated to line someone’s pockets. For example, according to investopia.com there are many locations in New York where the price of a 700 square foot apartment can be between $2,900 and $3,500. (Kopp 2019). However, in Chicago, a similar sized apartment can run about $1,708. (Riley 2019). There are many factors to why the rents are so incredulously different. These include location and proximity to a desired destination. Destinations like work, Ivy league schools, or popular and highly rated clustered locations for food, drink, and entertainment. Other factors also include square footage of the space, how many bedrooms, how many bathrooms and more. As a former landlord, and apartment renter who owns his own home and works for a real estate investment trust – which is a large landlord, I hope to reveal which factors are the more directly influencing factors and predict what the rental price should be close to. I believe this will help those looking for apartments or apartment buildings to have a better sense of the cost and value before they commit to signing.

### Project Specific Questions
- 

## Included Project Variables / Factors 

### Top 40 NYC Employers by Distance according to Fortune Magazine - https://fortune.com/best-workplaces-new-york/2020/search/
| Rank | Name | Industry | Employees | World Wide Revenue | 
| ------ | ------ | ------ | ------ | ------ | 
| 40 | The Goldman Sachs Group, Inc. | Financial Services & Insurance | - | $36,616,000,000 | 
| 39 | Adecco Group brands | Professional Services | - | - | 
| 38 | Live Nation Entertainment | Entertainment | 11,277 | $10,787,800,000 | 
| 37 | Zillow | Information Technology | 5,150 | $1,300,000,000 | 
| 36 | Blackstone | Financial Services & Insurance | - | - | 
| 35 | Voya Financial | Financial Services & Insurance | 5,835 | $8,514,000,000 | 
| 34 | Horizon Media | Advertising & Marketing | 1,908 | - | 
| 33 | Ernst & Young LLP | Professional Services | 260,569 | $34,800,000,000 | 
| 32 | Protiviti | Professional Services | 3,520 | $957,716,000 | 
| 31 | Accenture | Professional Services | 477,000 | $39,573,450,000 | 
| 30 | PricewaterhouseCoopers LLP | Professional Services | 250,000 | $41,300,000,000 | 
| 29 | Dechert LLP | Professional Services | 1,966 | $1,021,751,932 | 
| 28 | Mastercard Incorporated | Financial Services & Insurance | 14,800 | $14,950,000,000 | 
| 27 | KPMG LLP | Professional Services | 207,000 | $28,960,000,000 | 
| 26 | Baker Tilly Virchow Krause, LLP | Professional Services | 3,558 | $630,000,000 | 
| 25 | Comcast NBCUniversal | Telecommunications | 184,000 | $94,507,000,000 | 
| 24 | Atlassian | Information Technology | - | $1,210,126,855 | 
| 23 | Citizens Bank | Financial Services & Insurance | - | $160,000,000,000 | 
| 22 | Capital One Financial Corporation | Financial Services & Insurance | 47,500 | $28,100,000,000 | 
| 21 | Deloitte | Professional Services | 109,778 | $43,200,000,000 | 
| 20 | Adobe | Information Technology | 21,163 | $9,030,000,000 | 
| 19 | Cumberland Farms, Inc. | Retail | - | $3,700,000,000 | 
| 18 | Alston & Bird LLP | Professional Services | 1,610 | $816,473,083 | 
| 17 | DHL Express U.S. | Transportation | 102,540 | $18,197,669,000 | 
| 16 | Workiva Inc. | Information Technology | 1,393 | $244,344,000 | 
| 15 | Dropbox | Information Technology | - | $1,391,700,000 | 
| 14 | Cooley LLP | Professional Services | 2,311 | $1,226,149,000 | 
| 13 | Bain & Company | Professional Services | 10,131 | - | 
| 12 | American Express | Financial Services & Insurance | - | $40,338,000 | 
| 11 | Orrick | Professional Services | 2,400 | $1,046,000,000 | 
| 10 | Shawmut Design and Construction | Construction | - | $1,440,600,000 | 
| 9 | Noom, Inc. | Information Technology | 1,323 | $61,000,000 | 
| 8 | The Cheesecake Factory Incorporated | Hospitality | 38,009 | $2,332,331,000 | 
| 7 | Concord Hospitality Enterprises Company | Hospitality | 5,251 | $41,577,989 | 
| 6 | Box, Inc. | Information Technology | 2,053 | $608,400,000 | 
| 5 | West Monroe Partners | Professional Services | 850 | - | 
| 4 | Wegmans Food Markets, Inc. | Retail | - | $9,217,331,000 | 
| 3 | Power Home Remodeling | Construction | - | $695,000,000 | 
| 2 | Hulu | Media | 2,261 | - | 
| 1 | Salesforce | Information Technology | 40,152 | $13,280,000,000 | 

### NYC Attractions
 | name | latitude | longitude | tourism | 
 | ------ | ------ | ------ | ------ | 
 | 1 World Trade Center | 40.7130055 | -74.0131898 | attraction | 
 | 80 South Street | 40.7056076 | -74.0043915 | attraction | 
 | Access High Line Park | 40.7523844 | -74.0018026 | attraction | 
 | American Icon | 40.7172272 | -74.0035301 | attraction | 
 | Anton Kern Gallery | 40.7611132 | -73.9739449 | attraction | 
 | Archibalds Townhouse | 40.7733291 | -73.9656246 | attraction | 
 | Arguably the best location to see evening Manhattan Henge | 40.7471958 | -73.9812647 | attraction | 
 | BAC | 40.7560503 | -73.9973055 | attraction | 
 | Barthmans Sidewalk Clock | 40.7098196 | -74.0099251 | attraction | 
 | big gay ice cream | 40.7264894 | -73.9847678 | attraction | 
 | Bloody Angle | 40.7144199 | -73.9981297 | attraction | 
 | Bryant Park | 40.7535129 | -73.9839079 | attraction | 
 | California Sea Lion | 40.7678191 | -73.9717588 | attraction | 
 | Canal Street | 40.7171153 | -73.9985965 | attraction | 
 | Canal street market | 40.718987 | -74.0008621 | attraction | 
 | Carrie Bradshaw House | 40.7353656 | -74.0038558 | attraction | 
 | Casa di Carrie | 40.735302 | -74.0038435 | attraction | 
 | Chelsea | 40.7458699 | -74.0018779 | attraction | 
 | Chelsea Flea Market | 40.7436929 | -73.9903215 | attraction | 
 | Chelsea Market | 40.7429237 | -74.0069958 | attraction | 
 | Chinatown | 40.7156258 | -73.9984718 | attraction | 
 | Circle line ferrys | 40.7628258 | -74.0015777 | attraction | 
 | Classic Car Club Manhattan | 40.7580807 | -74.0047756 | attraction | 
 | Cocktail Kingdom | 40.7436082 | -73.9907173 | attraction | 
 | Colonnade row | 40.7292801 | -73.9924535 | attraction | 
 | Color Factory | 40.7258445 | -74.0062226 | attraction | 
 | Cortlandt Alley | 40.7177394 | -74.0023028 | attraction | 
 | Couv Led Zepp 5e album | 40.7273462 | -73.9850116 | attraction | 
 | Curry hill | 40.7426274 | -73.9824692 | attraction | 
 | Delacorte Musical Clock | 40.7681148 | -73.9711748 | attraction | 
 | Diamond District | 40.7572421 | -73.9801423 | attraction | 
 | Dream house | 40.7184995 | -74.0048345 | attraction | 
 | Dr Nevilles I Am Legend townhouse | 40.7313957 | -73.9965692 | attraction | 
 | Empire State Building | 40.7481629 | -73.9849958 | attraction | 
 | Explore Chinatown Information Kiosk | 40.7173684 | -73.9992431 | attraction | 
 | Flatiron District | 40.7410723 | -73.9896534 | attraction | 
 | Food Truck Street | 40.7570048 | -73.9814247 | attraction | 
 | Free Kayaking with the Downtown Boathouse | 40.6915007 | -74.0122141 | attraction | 
 | Free Public Stargazing | 40.7725563 | -73.9835751 | attraction | 
 | Free Public Stargazing | 40.7420581 | -74.0077867 | attraction | 
 | Friends Building | 40.7323595 | -74.0052999 | attraction | 
 | Gapstow bridge | 40.7669279 | -73.9738339 | attraction | 
 | Gentoo Penguin | 40.76833 | -73.971457 | attraction | 
 | Glen span arch | 40.7947039 | -73.9591072 | attraction | 
 | Greenwich Village | 40.7335845 | -74.0028172 | attraction | 
 | Grey houndiin bus stop | 40.7575015 | -73.994485 | attraction | 
 | Grizzly Bear | 40.7684112 | -73.971913 | attraction | 
 | Grove Court | 40.7321796 | -74.0057762 | attraction | 
 | Hangmans Elm | 40.7318891 | -73.998611 | attraction | 
 | High Line Access | 40.7467802 | -74.0045942 | attraction | 
 | High Line Park | 40.7451181 | -74.0066972 | attraction | 
 | Huddlestone arch | 40.7958355 | -73.9556352 | attraction | 
 | Kayak Brooklyn | 40.6995561 | -73.997566 | attraction | 
 | La casa de los Tenenbaums | 40.8237943 | -73.9465643 | attraction | 
 | La de forest house | 40.7331991 | -73.9946773 | attraction | 
 | Le Petit Versailles | 40.7210729 | -73.9818662 | attraction | 
 | LES SKATEPARK | 40.7110791 | -73.9933152 | attraction | 
 | Liz Christy Garden | 40.7242411 | -73.9921517 | attraction | 
 | Low Line Park | 40.7203545 | -73.9871259 | attraction | 
 | Mad about you building | 40.7346862 | -73.9946122 | attraction | 
 | Mahayanna Buddhist Center | 40.71641 | -73.995237 | attraction | 
 | Maison sur les toits | 40.72332 | -73.9883555 | attraction | 
 | Mark Twain House | 40.7337058 | -73.9964593 | attraction | 
 | Meatpacking District | 40.7409503 | -74.0075113 | attraction | 
 | NBC Studios | 40.7591425 | -73.9796681 | attraction | 
 | Nicholas Roerich Museum | 40.8027945 | -73.9689522 | attraction | 
 | Nicola Tesla corner | 40.7535873 | -73.9846757 | attraction | 
 | NY Skyride | 40.7483272 | -73.9856549 | attraction | 
 | Original brown stone houses | 40.8230348 | -73.9474058 | attraction | 
 | paparazzi dogman and paparazzi rabbitgirl | 40.7599935 | -73.9806283 | attraction | 
 | Paul Nicklen Gallery | 40.7226903 | -74.0033029 | attraction | 
 | Point de vue 17e rue | 40.7440976 | -74.0069385 | attraction | 
 | Puffin | 40.768196 | -73.9713336 | attraction | 
 | Red Panda | 40.7682914 | -73.9727846 | attraction | 
 | Rockefeller Center | 40.7588448 | -73.9788005 | attraction | 
 | Rowboat rentals | 40.7749309 | -73.9690887 | attraction | 
 | Salmagundi club | 40.7343017 | -73.9945529 | attraction | 
 | Schwartz Luggage Storage | 40.7552442 | -73.9945593 | attraction | 
 | Seal | 40.7683716 | -73.9716059 | attraction | 
 | Sea Lions | 40.767841 | -73.9717654 | attraction | 
 | Sightseeing Pass, LLC | 40.7608187 | -73.9875915 | attraction | 
 | Site of the Beach Pneumatic Subway | 40.7129806 | -74.0065761 | attraction | 
 | Snow Leopard | 40.7686429 | -73.9726493 | attraction | 
 | Snow Monkey | 40.7681797 | -73.9723113 | attraction | 
 | SoHo | 40.7228801 | -73.9987505 | attraction | 
 | South Street Seaport | 40.7057753 | -74.0028376 | attraction | 
 | Spyscape | 40.7650645 | -73.9838591 | attraction | 
 | Statue of Liberty | 40.7219912 | -73.9851473 | attraction | 
 | Stonewall Inn | 40.7338008 | -74.0021484 | attraction | 
 | Textile building | 40.7174627 | -74.0056679 | attraction | 
 | The High Line | 40.753277 | -74.0034424 | attraction | 
 | The High Line North Entrance | 40.7561135 | -74.0033107 | attraction | 
 | The Ride | 40.7549545 | -73.9911128 | attraction | 
 | Times Square | 40.7579511 | -73.9856026 | attraction | 
 | Tortoise | 40.7679979 | -73.9727565 | attraction | 
 | TriBeCa | 40.7223526 | -74.0061043 | attraction | 
 | Tropical Zone | 40.7676312 | -73.9725255 | attraction | 
 | Umpire rock | 40.7693619 | -73.9777798 | attraction | 

### NYC Borough Area Zip 
 | Borough | Area | Zip Code | 
 | ------ | ------ | ------ | 
 | Manhattan | Chelsea and Clinton | 10001 | 
 | Manhattan | Lower East Side | 10002 | 
 | Manhattan | Lower East Side | 10003 | 
 | Manhattan | Lower Manhattan | 10004 | 
 | Manhattan | Lower Manhattan | 10005 | 
 | Manhattan | Lower Manhattan | 10006 | 
 | Manhattan | Lower Manhattan | 10007 | 
 | Manhattan | Lower East Side | 10008 | 
 | Manhattan | Lower East Side | 10009 | 
 | Manhattan | Gramercy Park and Murray Hill | 10010 | 
 | Manhattan | Chelsea and Clinton | 10011 | 
 | Manhattan | Greenwich Village and Soho | 10012 | 
 | Manhattan | Greenwich Village and Soho | 10013 | 
 | Manhattan | Greenwich Village and Soho | 10014 | 
 | Manhattan | Greenwich Village and Soho | 10015 | 
 | Manhattan | Gramercy Park and Murray Hill | 10016 | 
 | Manhattan | Gramercy Park and Murray Hill | 10017 | 
 | Manhattan | Chelsea and Clinton | 10018 | 
 | Manhattan | Chelsea and Clinton | 10019 | 
 | Manhattan | Chelsea and Clinton | 10020 | 
 | Manhattan | Upper East Side | 10021 | 
 | Manhattan | Gramercy Park and Murray Hill | 10022 | 
 | Manhattan | Upper West Side | 10023 | 
 | Manhattan | Upper West Side | 10024 | 
 | Manhattan | Upper West Side | 10025 | 
 | Manhattan | Central Harlem | 10026 | 
 | Manhattan | Central Harlem | 10027 | 
 | Manhattan | Upper East Side | 10028 | 
 | Manhattan | East Harlem | 10029 | 
 | Manhattan | Central Harlem | 10030 | 
 | Manhattan | Inwood and Washington Heights | 10031 | 
 | Manhattan | Inwood and Washington Heights | 10032 | 
 | Manhattan | Inwood and Washington Heights | 10033 | 
 | Manhattan | Inwood and Washington Heights | 10034 | 
 | Manhattan | East Harlem | 10035 | 
 | Manhattan | Chelsea and Clinton | 10036 | 
 | Manhattan | Central Harlem | 10037 | 
 | Manhattan | Lower Manhattan | 10038 | 
 | Manhattan | Central Harlem | 10039 | 
 | Manhattan | Inwood and Washington Heights | 10040 | 
 | Manhattan | Inwood and Washington Heights | 10041 | 
 | Manhattan | Upper East Side | 10044 | 
 | Manhattan | Upper East Side | 10045 | 
 | Manhattan | Upper East Side | 10048 | 
 | Manhattan | Upper East Side | 10055 | 
 | Manhattan | Upper East Side | 10060 | 
 | Manhattan | Upper East Side | 10065 | 
 | Manhattan | Upper East Side | 10069 | 
 | Manhattan | Upper East Side | 10075 | 
 | Manhattan | Upper East Side | 10090 | 
 | Manhattan | Upper East Side | 10095 | 
 | Manhattan | Upper East Side | 10098 | 
 | Manhattan | Upper East Side | 10099 | 
 | Manhattan | Upper East Side | 10103 | 
 | Manhattan | Upper East Side | 10104 | 
 | Manhattan | Upper East Side | 10105 | 
 | Manhattan | Upper East Side | 10106 | 
 | Manhattan | Upper East Side | 10107 | 
 | Manhattan | Upper East Side | 10110 | 
 | Manhattan | Upper East Side | 10111 | 
 | Manhattan | Upper East Side | 10112 | 
 | Manhattan | Upper East Side | 10115 | 
 | Manhattan | Upper East Side | 10118 | 
 | Manhattan | Upper East Side | 10119 | 
 | Manhattan | Upper East Side | 10120 | 
 | Manhattan | Upper East Side | 10121 | 
 | Manhattan | Upper East Side | 10122 | 
 | Manhattan | Upper East Side | 10123 | 
 | Manhattan | Upper East Side | 10128 | 
 | Manhattan | Upper East Side | 10128 | 
 | Manhattan | Upper East Side | 10151 | 
 | Manhattan | Upper East Side | 10152 | 
 | Manhattan | Upper East Side | 10153 | 
 | Manhattan | Upper East Side | 10154 | 
 | Manhattan | Upper East Side | 10155 | 
 | Manhattan | Upper East Side | 10158 | 
 | Manhattan | Upper East Side | 10161 | 
 | Manhattan | Upper East Side | 10162 | 
 | Manhattan | Upper East Side | 10165 | 
 | Manhattan | Upper East Side | 10166 | 
 | Manhattan | Upper East Side | 10167 | 
 | Manhattan | Upper East Side | 10168 | 
 | Manhattan | Upper East Side | 10169 | 
 | Manhattan | Upper East Side | 10170 | 
 | Manhattan | Upper East Side | 10171 | 
 | Manhattan | Upper East Side | 10172 | 
 | Manhattan | Upper East Side | 10173 | 
 | Manhattan | Upper East Side | 10174 | 
 | Manhattan | Upper East Side | 10175 | 
 | Manhattan | Upper East Side | 10176 | 
 | Manhattan | Upper East Side | 10177 | 
 | Manhattan | Upper East Side | 10178 | 
 | Manhattan | Upper East Side | 10199 | 
 | Manhattan | Upper East Side | 10270 | 
 | Manhattan | Upper East Side | 10271 | 
 | Manhattan | Upper East Side | 10275 | 
 | Manhattan | Upper East Side | 10278 | 
 | Manhattan | Upper East Side | 10279 | 
 | Manhattan | Lower Manhattan | 10280 | 
 | Manhattan | Lower Manhattan | 10281 | 
 | Manhattan | Lower Manhattan | 10282 | 
 | Staten Island | Stapleton and St. George | 10301 | 
 | Staten Island | Port Richmond | 10302 | 
 | Staten Island | Port Richmond | 10303 | 
 | Staten Island | Port Richmond | 10303 | 
 | Staten Island | Stapleton and St. George | 10304 | 
 | Staten Island | Stapleton and St. George | 10305 | 
 | Staten Island | South Shore | 10306 | 
 | Staten Island | South Shore | 10307 | 
 | Staten Island | South Shore | 10308 | 
 | Staten Island | South Shore | 10309 | 
 | Staten Island | Port Richmond | 10310 | 
 | Staten Island | Port Richmond | 10311 | 
 | Staten Island | South Shore | 10312 | 
 | Staten Island | Mid-Island | 10314 | 
 | Bronx | High Bridge and Morrisania | 10451 | 
 | Bronx | High Bridge and Morrisania | 10452 | 
 | Bronx | Central Bronx  | 10453 | 
 | Bronx | Hunts Point and Mott Haven | 10454 | 
 | Bronx | Hunts Point and Mott Haven | 10455 | 
 | Bronx | High Bridge and Morrisania | 10456 | 
 | Bronx | Central Bronx  | 10457 | 
 | Bronx | Bronx Park and Fordham | 10458 | 
 | Bronx | Hunts Point and Mott Haven | 10459 | 
 | Bronx | Central Bronx  | 10460 | 
 | Bronx | Southeast Bronx | 10461 | 
 | Bronx | Southeast Bronx | 10462 | 
 | Bronx | Kingsbridge and Riverdale | 10463 | 
 | Bronx | Southeast Bronx | 10464 | 
 | Bronx | Southeast Bronx | 10465 | 
 | Bronx | Northeast Bronx  | 10466 | 
 | Bronx | Bronx Park and Fordham | 10467 | 
 | Bronx | Bronx Park and Fordham | 10468 | 
 | Bronx | Northeast Bronx  | 10469 | 
 | Bronx | Northeast Bronx  | 10470 | 
 | Bronx | Kingsbridge and Riverdale | 10471 | 
 | Bronx | Southeast Bronx | 10472 | 
 | Bronx | Southeast Bronx | 10473 | 
 | Bronx | Hunts Point and Mott Haven | 10474 | 
 | Bronx | Northeast Bronx  | 10475 | 
 | Queens | Southeast Queens | 11004 | 
 | Queens | Southeast Queens | 11005 | 
 | Queens | Northwest Queens | 11101 | 
 | Queens | Northwest Queens | 11102 | 
 | Queens | Northwest Queens | 11103 | 
 | Queens | Northwest Queens | 11104 | 
 | Queens | Northwest Queens | 11105 | 
 | Queens | Northwest Queens | 11106 | 
 | Queens | Northwest Queens | 11109 | 
 | Brooklyn | Northwest Brooklyn | 11201 | 
 | Brooklyn | Flatbush | 11203 | 
 | Brooklyn | Borough Park | 11204 | 
 | Brooklyn | Northwest Brooklyn | 11205 | 
 | Brooklyn | Bushwick and Williamsburg | 11206 | 
 | Brooklyn | East New York and New Lots | 11207 | 
 | Brooklyn | East New York and New Lots | 11208 | 
 | Brooklyn | Southwest Brooklyn | 11209 | 
 | Brooklyn | Flatbush | 11210 | 
 | Brooklyn | Greenpoint | 11211 | 
 | Brooklyn | Central Brooklyn | 11212 | 
 | Brooklyn | Central Brooklyn | 11213 | 
 | Brooklyn | Southwest Brooklyn | 11214 | 
 | Brooklyn | Northwest Brooklyn | 11215 | 
 | Brooklyn | Central Brooklyn | 11216 | 
 | Brooklyn | Northwest Brooklyn | 11217 | 
 | Brooklyn | Borough Park | 11218 | 
 | Brooklyn | Borough Park | 11219 | 
 | Brooklyn | Sunset Park | 11220 | 
 | Brooklyn | Bushwick and Williamsburg | 11221 | 
 | Brooklyn | Greenpoint | 11222 | 
 | Brooklyn | Southern Brooklyn | 11223 | 
 | Brooklyn | Southern Brooklyn | 11224 | 
 | Brooklyn | Flatbush | 11225 | 
 | Brooklyn | Flatbush | 11226 | 
 | Brooklyn | Southwest Brooklyn | 11228 | 
 | Brooklyn | Southern Brooklyn | 11229 | 
 | Brooklyn | Borough Park | 11230 | 
 | Brooklyn | Northwest Brooklyn | 11231 | 
 | Brooklyn | Sunset Park | 11232 | 
 | Brooklyn | Central Brooklyn | 11233 | 
 | Brooklyn | Canarsie and Flatlands | 11234 | 
 | Brooklyn | Southern Brooklyn | 11235 | 
 | Brooklyn | Canarsie and Flatlands | 11236 | 
 | Brooklyn | Bushwick and Williamsburg | 11237 | 
 | Brooklyn | Central Brooklyn | 11238 | 
 | Brooklyn | Canarsie and Flatlands | 11239 | 
 | Brooklyn | Canarsie and Flatlands | 11241 | 
 | Brooklyn | Canarsie and Flatlands | 11242 | 
 | Brooklyn | Canarsie and Flatlands | 11243 | 
 | Brooklyn | Canarsie and Flatlands | 11249 | 
 | Brooklyn | Canarsie and Flatlands | 11252 | 
 | Brooklyn | Canarsie and Flatlands | 11256 | 
 | Queens | Canarsie and Flatlands | 11351 | 
 | Queens | North Queens | 11354 | 
 | Queens | North Queens | 11355 | 
 | Queens | North Queens | 11356 | 
 | Queens | North Queens | 11357 | 
 | Queens | North Queens | 11358 | 
 | Queens | North Queens | 11359 | 
 | Queens | North Queens | 11360 | 
 | Queens | Northeast Queens | 11361 | 
 | Queens | Northeast Queens | 11362 | 
 | Queens | Northeast Queens | 11363 | 
 | Queens | Northeast Queens | 11364 | 
 | Queens | Central Queens | 11365 | 
 | Queens | Central Queens | 11366 | 
 | Queens | Central Queens | 11367 | 
 | Queens | West Queens | 11368 | 
 | Queens | West Queens | 11369 | 
 | Queens | West Queens | 11370 | 
 | Queens | West Queens | 11371 | 
 | Queens | West Queens | 11372 | 
 | Queens | West Queens | 11373 | 
 | Queens | West Central Queens | 11374 | 
 | Queens | West Central Queens | 11375 | 
 | Queens | West Queens | 11377 | 
 | Queens | West Queens | 11378 | 
 | Queens | West Central Queens | 11379 | 
 | Queens | West Central Queens | 11385 | 
 | Queens | Southeast Queens | 11411 | 
 | Queens | Jamaica | 11412 | 
 | Queens | Southeast Queens | 11413 | 
 | Queens | Southwest Queens | 11414 | 
 | Queens | Southwest Queens | 11415 | 
 | Queens | Southwest Queens | 11416 | 
 | Queens | Southwest Queens | 11417 | 
 | Queens | Southwest Queens | 11418 | 
 | Queens | Southwest Queens | 11419 | 
 | Queens | Southwest Queens | 11420 | 
 | Queens | Southwest Queens | 11421 | 
 | Queens | Southeast Queens | 11422 | 
 | Queens | Jamaica | 11423 | 
 | Queens | Southeast Queens | 11426 | 
 | Queens | Southeast Queens | 11427 | 
 | Queens | Southeast Queens | 11428 | 
 | Queens | Southeast Queens | 11429 | 
 | Queens | Southeast Queens | 11430 | 
 | Queens | Jamaica | 11432 | 
 | Queens | Jamaica | 11433 | 
 | Queens | Jamaica | 11434 | 
 | Queens | Jamaica | 11435 | 
 | Queens | Jamaica | 11436 | 
 | Queens | Rockaways | 11691 | 
 | Queens | Rockaways | 11692 | 
 | Queens | Rockaways | 11693 | 
 | Queens | Rockaways | 11694 | 
 | Queens | Rockaways | 11695 | 
 | Queens | Rockaways | 11697 | 


### Distance to Highly Rated and Priced Businesses recorded by Yelp
| Yelp Rating | Latitudes | Longitudes | 
| ------ | ------ | ------ | 
 | Yelp_Highest_Priced_0 -Cluster Center | 40.71360594 | -74.00834961 |  
 | Yelp_Highest_Priced_1 -Cluster Center | 40.76068284 | -73.97826484 | 
 | Yelp_Highest_Priced_2 -Cluster Center | 40.73287131 | -73.99541715 | 
 | Yelp_Highest_Rated_0 -Cluster Center | 40.71570017 | -74.00162143 | 
 | Yelp_Highest_Rated_1 -Cluster Center | 40.80175434 | -73.94419938 | 
 | Yelp_Highest_Rated_2 -Cluster Center | 40.76213922 | -73.98069774 | 

### Apartment Description 
- Length of the apartment description

### Apartment Amenities
- bathrooms
- bedrooms
- latitude
- longitude
- price
- interest_level
- elevator
- cats_allowed
- hardwood_floors
- dogs_allowed
- doorman
- dishwasher
- no_fee
- laundry_in_building
- fitness_center
- laundry_in_unit
- roof_deck
- outdoor_space
- dining_room
- high_speed_internet
- balcony
- swimming_pool
- new_construction
- terrace
- exclusive
- loft
- garden_patio
- wheelchair_access
- common_outdoor_space


## Pythonic Libraries Used in this project
Package               Version
--------------------- ---------
- async-generator       1.10
- asyncio               3.4.3
- certifi               2020.12.5
- decorator             4.4.2
- defusedxml            0.7.1
- folium                0.12.1
- geojson               2.5.0
- geopy                 2.1.0
- gmaps                 0.9.0
- gmplot                1.4.1
- greenlet              1.0.0
- htmlmin               0.1.12
- html-parser           0.2
- ImageHash             4.2.0
- imgkit                1.1.0
- importlib-metadata    2.1.1
- joblib                1.0.1
- jsonschema            3.2.0
- MarkupSafe            1.1.1
- matplotlib            3.3.4
- mplleaflet            0.0.5
- networkx              2.5
- notebook              6.3.0
- numpy                 1.20.1
- packaging             20.9
- pandas                1.2.3
- pandas-profiling      2.11.0
- pandasql              0.7.3
- piianalyzer           0.1.0
- pygeohash             1.2.0
- pyodbc                4.0.30
- PyYAML                5.4.1
- requests              2.25.1
- scikit-learn          0.24.1
- scipy                 1.6.1
- seaborn               0.11.1
- Shapely               1.7.1
- simplejson            3.17.2
- sklearn               0.0
- SQLAlchemy            1.4.2
- threadpoolctl         2.1.0
- typing-extensions     3.7.4.3
- urllib3               1.26.4
- websockets            8.1

## Repo Folder Structure

└───Datasets

└───Scripts

└───Results

## Python Files 

| File Name  | Description |
| ------ | ------ |
| JsonYelpDatay.py | Yelp Data Extraction |
| LoopJson.py | Json Data Conversion to Central CSV |
| LoopJsonFiles.py | Loop through JSON files, transform and create consolidated CSV | 
| Pandas_Profiling_Generate_EDA_Reports.py | Quick Descriptive Statistics | 
| RentHop_EDA_Reviews.py | Preliminary Data Wrangling and EDA review | 
| TopNYCEmployerMap.py | Map Top NYC Employers | 
| DistancesToTopNYCEmployers.py | Updates Renthop Apartments with geohashes of the Latitudes and Longitudes | 
| CalculateDistancesToTopNYCEmployers.py | Updates Distances from the Renthop Apartments to the top employers | 
| ClusterNYCYelpRatedBusinesses.py | Creates clusters and gets the centers for these kmeans clusters. Using Yelp Highest Ratings and Yelp Most Expensive Restaurants | 
| NYC_RentHop_ApartmentLocations_Map | Create Map of the locations of the apartments in my master dataset |
| GetZipCode.py | Created to get zipcodes from lat and long so to remove non NYC apartments from the NYC RentHop dataset using a list of valid Zip Codes |
| GetZipCodeLow.py | Created to get zipcodes from lat and long so to remove non NYC apartments from the NYC RentHop dataset using a list of valid Zip Codes / partitioned by interest level due to larger base recordset causing session timeout with Nominatim |
| GetZipCodeMedium.py | Created to get zipcodes from lat and long so to remove non NYC apartments from the NYC RentHop dataset using a list of valid Zip Codes / partitioned by interest level due to larger base recordset causing session timeout with Nominatim |
| GetZipCodeHigh.py | Created to get zipcodes from lat and long so to remove non NYC apartments from the NYC RentHop dataset using a list of valid Zip Codes / partitioned by interest level due to larger base recordset causing session timeout with Nominatim |
| Combine_RentHop_InterestFiles.py | Combines the resulting csv files from GetZipCodeHigh/Medium/Low.py files |
| NYCAttractionsMap.py | Creates Maps of the NYC Attractions | 
| CalculateDistancesToNYCAttractions.py | Generates the geohash for these attractions using the Latitudes and Longitudes | 
| RemoveNonNYCRecords.py | Removes Non NYC apartments from master analytics dataset |
| BoroughZips.py | Updates the Borough along with Borough Area Name using ZipCode. Adds numeric code for each. | 

| FinalDataWranglingEDA.py | Final Data Wrangling, strips html, punctuation and cleans up non NYC Zipcode related apartments. | 
| VariableCorrelationReview.py | Variable Correlation Analysis using the master analytics dataset | 
| RandomForest.py | Model review and testing. Features Analysis and parameter tuning. | 


## Datasets
| NYCEmployers.csv | NYC Top Employers - https://fortune.com/best-workplaces-new-york/2020/search/ | 
| yelp_business_data.csv | NYC Yelp Businesses  | 
| renthopNYC_Final.csv | FinalDataSet |  


## Results
Under construction

## Maps

### Top NYC Employers - https://fortune.com/best-workplaces-new-york/2020/search
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Top_Employers_Heatmap.png?raw=true)
Heatmap Location for Top Employers In NYC

### RentHop Inventoried Apartments
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_ApartmentLocations_Map.png?raw=true)
Apartment locations contained in my NYC RentHop dataset. Note: the outliers outside of NYC - these will be removed from my final cleaned dataset.
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_ApartmentLocations_Heatmap.png?raw=true)
Above is a heatmap of the apartments located in NYC

### NYC Attractions
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Attractions.png?raw=true)
NYC Attraction locations.
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Attractions_Heatmap.png?raw=true)
Above is a heatmap of the attractions located in NYC


### Yelp Top Pricing and Highest Rating
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Highest_Priced_Yelp_Businesses_KMeans_Cluster.png?raw=true)
Plot of the KMeans clusters of Yelp Rated High Priced Businesses

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Top_Rated_Yelp_Businesses_KMeans_Cluster_Centers.png?raw=true)
Map of the centers of each of the KMeans clusters of Yelp Rated High Priced Businesses

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Highest_Priced_Yelp_Businesses_KMeans_Cluster_Centers.png?raw=true)
Plot of the KMeans clusters of the Highest Yelp Rated Businesses 

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Highest_Rated_Yelp_Businesses_KMeans_Cluster.png?raw=true)
Plot of the KMeans clusters of the Highest Yelp Rated Businesses 

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Map_Highest_Priced_Yelp_Businesses_KMeans_Cluster_Centers.png?raw=true)
Map of the centers of each of the KMeans clusters of the Yelp Rated Highest Priced Businesses 

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Map_Highest_Rated_Yelp_Businesses_KMeans_Cluster_Centers.png?raw=true)
Map of the centers of each of the KMeans clusters of the Highest Yelp Rated Businesses 

## Amenities Review
Interest Levels
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Interest_Level_Pie.png?raw=true)
RentHop Apartment Review Level Breakdown

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Interest_Level_Review.png?raw=true)
RentHop Apartment Review Level Distribution

### Bedrooms
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Bedrooms_Breakdown_by_Interest.png?raw=true)
RentHop Apartment Bedroom Distribution Breakdown

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Bedrooms_Breakdown_by_Interest_Frequency.png?raw=true)
RentHop Apartment Bedroom Distribution Frequency

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Bedrooms_Occurences_Histogram.png?raw=true)
RentHop Apartment Bedroom Distribution by Interest Level

### Bathrooms
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Bathrooms_Occurences_Histogram.png?raw=true)
RentHop Apartment Bathroom Distribution 

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Bathrooms_Occurences_Violin_Chart.png?raw=true)
RentHop Apartment Violin plot of bathroom by Interest Level

### Pricing Reviews
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Price_Outlier_Detection_Review.png?raw=true)
Pricing Outlier Detection
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Price_w90_pct_Max_Price_Excluded.png?raw=true)
Apartment Pricing Distribution

## Data Sources
| RentHop | NYC Apartments Inventory | https://www.kaggle.com/c/two-sigma-connect-rental-listing-inquiries/data | 
| Yelp | Collection of NYC Business Ratings and Prices | https://www.yelp.com/dataset | 
| Fortune | NYC List of top 40 Employers | https://fortune.com/best-workplaces-new-york/2020/search/ | 
| Pluto | NYC Borough Location Area Information | https://www1.nyc.gov/ | 
| Mygeodata | NYC Location of Attractions | https://mygeodata.cloud/ | 
| Zip Codes | NYC Zip Codes | https://worldpostalcode.com/united-states/new-york/new-york-city | 
| Boroughs Area Names | Borough by Zip Code | https://www.nycbynatives.com/nyc_info/new_york_city_zip_codes.php & https://storage.googleapis.com/plos-corpus-prod/10.1371/journal.pone.0194799/1/pone.0194799.s001.pdf?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=wombat-sa%40plos-prod.iam.gserviceaccount.com%2F20210328%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210328T203603Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&X-Goog-Signature=91b1ec1a775a9e750bc63a5cd5d7bc1e36ebba6f7271f16239ef3bf4fb44a025c106d9737e6bc6b88a4e1402ece330e70790ec33e25622be67c35e409e637a4b763cb2461a5b037bf23bc3ab415791fd625225cffbeac605de27991074666cf5a8acb1a0b428e2e7f71d383dfdfc3aaabada40e2aadd923a3ae48fc4da6e4e42fec97bc62ac32a84e05b9cfb9f269c10e600859b0f0a6ce5ac4cf04c7eef0e57d47ba99eac61b04a70ccdeff079a33ee0156343794d022edad687477934124d775295d416026a1bd31d0fd44da85820a2758b6034cd284f1bbbcc6e565918cb2cbbf35441ba1d0221691732c2047bb7d11d53f0ac5309ea2616c5adab80dff96 |

##References: 

Kopp, C. (November 2019). How Expensive is it to Live in New York City? Retrieved from: https://www.investopedia.com/articles/personal-finance/012315/how-expensive-new-york-city-really.asp

Riley, E. (July 2019). Cost of Living in Chicago vs. NYC: Which Big City Is Cheaper? Retrieved from: https://streeteasy.com/blog/cost-of-living-in-chicago-vs-nyc/#:~:text=Median%20rent%20for%20a%201,That's%20nothing%20to%20scoff%20at.

TIMOTHY102, (October 2020). Predicting NYC AirBnB Rental Prices with TensorFlow. Retrieved from  https://www.analyticsvidhya.com/blog/2020/10/predicting-nyc-airbnb-rental-prices-tensorflow/

Carmody, B. (February 2021). Best Rental Listing Sites. Retrieved from  https://www.investopedia.com/best-rental-listing-sites-5075293

RentCafe. (n.d.). RentCafe is a listing site that can be used for comparable pricing with my predicted values. Retrieved from https://www.rentcafe.com/

Mastroeni, T. (October 2020). How is Artificial Intelligence Used in Real Estate? Retrieved from https://www.fool.com/millionacres/real-estate-market/real-estate-innovation/how-is-artificial-intelligence-used-in-real-estate/

Barzilay, O. (March 2017). Property Management May Be The Next Frontier For AI. Retrieved from https://www.forbes.com/sites/omribarzilay/2017/03/14/property-management-may-be-the-next-frontier-for-ai/?sh=3ba8d5f66fb3

McLaughlin, K. (November 2019). Robots Are Taking Over (the Rental Screening Process). Retrieved from https://www.wsj.com/articles/robots-are-taking-over-the-rental-screening-process-11574332200

Devanesan, J. (October 2019). What happens when AI enters the rental market? Retrieved from https://techhq.com/2019/10/what-happens-when-ai-enters-the-rental-market/

Antony, V. (May 2020) Predicting Apartment Rental Prices in Germany. Retrieved from https://towardsdatascience.com/predicting-apartment-rental-prices-in-germany-d5635197ab00

Villar, B. (April 2020). Machine Learning and RealState: Predicting Rental Prices in Amsterdam. Retrieved from https://towardsdatascience.com/ai-and-real-state-renting-in-amsterdam-part-1-5fce18238dbc

Najera, C. Hunter, T. Zhan, D. Bialer, J. (March 2017). Predicting Interest for NYC Apartment Rental Listings - A Guideline For Landlors and Agents. Retrieved from https://nycdatascience.com/blog/student-works/predicting-interest-nyc-apartments-rent-guideline-landlords/



