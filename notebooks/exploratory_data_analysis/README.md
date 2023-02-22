# Exploratory Data Analysis

As explained in the introductory [README.md](README.md), the main objective of this analysis is to explore Hurb's flexible date package cancellations. The following information helps to better understand the data used.

#### Columns:
- operation_id (numerical) - Unique identifier of a single operation. It only exists if the operation process was initiated before cancellation. Otherwise, it is null.
- order_id (numerical) - Unique identifier of an order.
- order_date (DateTime) - Date of the order in the 'Sao Paulo/Brazil' time zone.
- origin_city (string) - Origin city of the flight.
- order_origin_city (string) - Origin city of the flight.
- origin_state (string) - Origin city of the flight.
- origin_country (string) - Origin country of the flight.
- destination_type (string) - Destination type of the travel: national (Brazil) or international destination.
- destination_city (string) - Destination city of the traveler.
- destination_state (string) - Destination state of the traveler.
- destination_country (string) - Destination country of the traveler.
- qty_people (numerical) - Quantity of persons of the order.
- qty_dailies (numerical) - Room nights quantity.
- accommodation_type (string) - Accommodation type: single, double, triple, etc.
- filled_form (string) - Information on whether the traveler completed the form informing the wished dates to travel or not.
- first_form_fill_date (DateTime) - The first date on which the traveler filled up the form.
- last_form_fill_date (DateTime) - The last date on which the traveler filled up the form.
- first_valid_date (DateTime) - The first valid date of the package.
- last_valid_date (DateTime) - The last valid date of the package.


## General questions

- **Which questions are you trying to answer?**
  - Are international travels more canceled than national ones?
  - Is the number of status changes related to the cancellation process?
  - Which are the features that have the most impact on cancellation?
