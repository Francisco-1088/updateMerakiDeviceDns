import meraki
import credentials
import pandas as pd

dashboard = meraki.DashboardAPI(api_key=credentials.api_key)
#This is the default inventory structure when exported from Organization - Inventory in Co-term organizations
#If using a PDL organization, comment line 9 and uncomment line 8
#device_serials = pd.read_csv('serials.csv', names = ['Name', 'Type', 'Network', 'Model', 'Serial', 'MAC', 'Tags', 'IP', 'Order', 'Claimed', 'Country', 'Expiration', 'Inventory'])
device_serials = pd.read_csv('serials.csv', names = ['MAC','Serial','Model','Claimed','Order','Country/Region','Network','Name'])
print(device_serials)

#Remove rows with blank network value, that is devices not assigned to a network
device_serials.dropna(subset=['Network'], inplace=True)

serials = device_serials.Serial.to_list()

#Remove column header
serials.pop(0)

print(serials)

for serial in serials:
    device = dashboard.devices.getDeviceManagementInterface(serial=serial)

    #Only affects devices with static IP config
    if device['wan1']['usingStaticIp'] == True:
        #Update your desired DNS here
        static_dns = ['208.67.222.222', '8.8.8.8']
        device['wan1']['staticDns'] = static_dns
        print("This is the previous device configuration.")
        print(device)
        dashboard.devices.updateDeviceManagementInterface(serial=serial, **device)
        device = dashboard.devices.getDeviceManagementInterface(serial=serial)
        print("This is the new device configuration.")
        print(device)