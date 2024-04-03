
import requests
import pandas as pd


def oui_info():

    url = "https://entities.nft.helium.io/v2/oui/all"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

if __name__ == "__main__":
    print("started script for fetch and add data to csv...")
    try:
        oui_data = oui_info()
        # Create a DataFrame from the JSON data
        df = pd.json_normalize(oui_data)
        # Save the DataFrame to a CSV file (omit index)
        df.to_csv(f'oui_data.csv', index=False)
    except Exception as e:
        print(f"Error: {e}")
    print("Data appended to 'oui_data.csv'.")
    