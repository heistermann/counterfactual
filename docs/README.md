This page provides a new perspective on flash flood hazards in Germany.

We used DWD's [RADKLIM](https://opendata.dwd.de/climate_environment/CDC/grids_germany/hourly/radolan/reproc/2017_002/)
product to identify the ten most extreme precipitation events in Germany from 2001 to 2022.
We then assumed that *any* of these top 10 events could have happened *anywhere*
in Germany. In other words, these events were shifted around all over Germany.
For all resulting positions of the precipitation fields, we simulated the corresponding
peak discharge for any affected catchment with an area smaller than 750 km². From
all the realisations of this simulation experiment, the maximum peak discharge
was identified for each catchment.

These results might help to reduce the element of surprise in disaster risk management,
by allowing a view on what *could* happen in case certain extreme events occurred
elsewhere. Such scenario analysis is referred to as "counterfactual thinking",
and a "downward counterfactual search" strives to identify constellations with impacts
worse than observed for the actual event itself.

Please find a comprehensive presentation of this approach in 
[our recent preprint](https://doi.org/10.5194/egusphere-egu23-1241):
Voit, P., and Heistermann, M.: Downward counterfactual analysis of historical rainfall 
events in Germany, Nat. Haz. Earth Syst. Sc. Disc., in review.

In the map below, you can compare the **counterfactual maximum peak** to the 
**original maximum peak** that resulted from the *actual* rainfall events 
over a catchment from **2001 to 2022**. We show the **unit peak discharge** which 
normalizes the peak flow by the upstream basin area. The results are presented 
per federal state. When hovering over the map, you can also see which rainfall event
caused the maximum counterfactual peak.

Please use the drop-down menu to select a different state 
and then hit the `Update map` button to update the map. 
**Please be patient, loading data may take a while...**

<iframe src="https://heistermann.github.io/ff-hazard/map.html"
    width="110%"
    height="500"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

This is the list of extreme preciptation events that were analysed:

| ID       | Date               | max. 24 h prec. | federal state |
| -------- | ------------------ | --------------- | ------------- |
| LS/Jul02 | Jul 15-20, 2002    | 138 | Niedersachsen |
| BB/Jun17 | Jun 26-Jul 2, 2017 | 149 | Berlin / Brandenburg |
| SN/Aug02 | Aug 10-15, 2002    | 224 | Sachsen |
| NW/Jul21 | Jul 11-16, 2021    | 136 | NRW, Rheinland-Pfalz |
| LS/Jul17 | Jul 22-27, 2017    | 136 | Niedersachsen |
| BW/May16 | May 27-Jun 1, 2016 | 98  | Baden-Württemberg, Bayern |
| BB/Jun21 | Jun 28-Jul 3, 2021 | 217 | Brandenburg |
| BB/Jun20 | Jun 11-16, 2020    | 93  | Brandenburg |
| HS/May19 | May 18-23, 2019    | 106 | Hessen |
| SN/Jun13 | Jun 18-22, 2013    | 121 | Sachsen |
