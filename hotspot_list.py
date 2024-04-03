

import requests
import pandas as pd
import time
import json


def get_hotspots(subnetwork):
    url = f"https://entities.nft.helium.io/v2/hotspots?subnetwork={subnetwork}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def detailed_hotspot(asset_key):

    url = f"https://entities.nft.helium.io/v2/hotspot/{asset_key}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

if __name__ == "__main__":
    print("started script for fetch and add data to csv...")
    try:
        for subnet in ["iot", "mobile"]:
            hotspot_data = get_hotspots(subnet)
            start = 0
            for i in hotspot_data["items"]:
                data = detailed_hotspot(i["key_to_asset_key"])
                if not start:
                    # Create a DataFrame from the JSON data
                    df = pd.json_normalize(data)

                    # Save the DataFrame to a CSV file (omit index)
                    df.to_csv(f'{subnet}_data.csv', index=False)
                    start += 1
                    # Optional: Append more data to the CSV file
                else:
                    time.sleep(1)  # Sleep for 1 second (adjust as needed)
                    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

            # Save the updated DataFrame to the same CSV file
            df.to_csv(f'{subnet}_data.csv', index=False, mode='a', header=False)
    except Exception as e:
        print(f"Error: {e}")
    print("Data appended to 'iot_data.csv' and 'mobile_data.csv'.")
    