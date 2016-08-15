# Some sort of website
Comparing rental cities and stuff.

## Basic Flow 
1. User hits the homepage and are able to select a city they want to view rental data for. Right now I have a text box for city selection, probably need to make that a drop down list initially since supported cities will likely be limited (since we will have to manually populate a DB due to lack of available APIs)
2. Once the user selects a city, they're presented with a summary of the city's rental statistics (statistics TBD) and maybe related visuals. If it makes sense, this summary can also include a "ranking" relative to other cities we've charted
3. Somewhere on the city summary page, a user can select a certain metric to get more detailed information on. For example, the user can choose to get a visualization charting YoY growth of population, or price / sq. ft., or whatever else. 
4. The visualizations should be interactive, so they'll likely be built out with D3 (except in cases where D3 is overkill). 
5. At some point, it would be nice to have the ability to select two cities and compare them along different metrics. 

## Notes
* Treat Issues as a backlog of sorts
* Better architecture document to come# Some sort of website
