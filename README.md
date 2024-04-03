# helium_hotspot
This project fetched data from helium hotspot API and added into csv file.

# Hotspot Data Processing Scripts

This repository contains Python scripts for processing hotspot data related to IoT and mobile subnetworks. The scripts generate clean CSV files with relevant information. Below are the deliverables:

## 1. Hotspot List by Subnetwork

### Description
The `hotspot_list.py` script retrieves hotspot data for both IoT and mobile subnetworks. It collects relevant details and organizes them into a clean CSV file.

### Usage
1. Run the `hotspot_list.py` script.
2. fetched the response and give data for next step.

## 2. Hotspot Info by Key to Asset Key

### Description
The `hotspot_info.py` script uses the key-to-asset key obtained from Hotspot List by Subnetwork. based oon fethed key_to_asset_key from above REST call now we fetches detailed hotspot information, including location, activity status, and ownership and ase.

### Usage
1. The output will be saved in `iot_data.csv` and `mobile_data.csv`.

## 3. OUI Organization List

### Description
The `oui_list.py` Oscript lists UI (Organizationally Unique Identifier) information associated with hotspots. It provides insights into the organizations behind these hotspots.

### Usage
1. Run the `oui_list.py` script.
2. The output will be saved in `oui_data.csv` that include OUI organization details.
