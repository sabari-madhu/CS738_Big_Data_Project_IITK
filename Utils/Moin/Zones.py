state_to_zone = {
    "HIMACHAL PRADESH": "NORTH ZONE",
    "PUNJAB": "NORTH ZONE",
    "UTTARAKHAND": "NORTH ZONE",
    "UTTAR PRADESH": "NORTH ZONE",
    "HARYANA": "NORTH ZONE",
    "BIHAR": "EAST ZONE",
    "ODISHA": "EAST ZONE",
    "JHARKHAND": "EAST ZONE",
    "WEST BENGAL": "EAST ZONE",
    "RAJASTHAN": "WEST ZONE",
    "GUJARAT": "WEST ZONE",
    "GOA": "WEST ZONE",
    "MAHARASHTRA": "WEST ZONE",
    "ANDHRA PRADESH": "SOUTH ZONE",
    "TELANGANA": "SOUTH ZONE",
    "KARNATAKA": "SOUTH ZONE",
    "KERALA": "SOUTH ZONE",
    "TAMIL NADU": "SOUTH ZONE",
    "MADHYA PRADESH": "CENTRAL ZONE",
    "CHHATTISGARH": "CENTRAL ZONE",
    "ASSAM": "NORTH EAST ZONE",
    "SIKKIM": "NORTH EAST ZONE",
    "NAGALAND": "NORTH EAST ZONE",
    "MEGHALAYA": "NORTH EAST ZONE",
    "MANIPUR": "NORTH EAST ZONE",
    "MIZORAM": "NORTH EAST ZONE",
    "TRIPURA": "NORTH EAST ZONE",
    "ARUNACHAL PRADESH": "NORTH EAST ZONE",
    "ANDAMAN & NICOBAR ISLANDS": "UNION TERRITORY",
    "CHANDIGARH": "UNION TERRITORY",
    "DADRA & NAGAR HAVELI": "UNION TERRITORY",
    "DAMAN & DIU": "UNION TERRITORY",
    "NCT OF DELHI": "UNION TERRITORY",
    "JAMMU & KASHMIR": "UNION TERRITORY",
    "LADAKH": "UNION TERRITORY",
    "LAKSHADWEEP": "UNION TERRITORY",
    "PUDUCHERRY": "UNION TERRITORY"
}

# Function to get area based on state name
def get_area(STATE):
    return state_to_zone.get(STATE, "Unknown")

