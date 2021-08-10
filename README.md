# updateMerakiDeviceDns
Update DNS config for Meraki devices from a list of serials in a CSV file

Clone github repo and install the python libraries.

-git clone https://github.com/Francisco-1088/updateMerakiDeviceDns.git

-pip install -r requirements.txt

Go to your Meraki organization, go to Organization - Inventory and download the list of devices with the Export to CSV button, and replace the serials.csv file in the folder with this.

If your organization is in Co-term, use as is. If your organization is in PDL, uncommend line 8 and comment line 9.

Remove any devices you don't wish to update DNS to from the serials.csv file.

Update line 28 with your desired DNS to be updated. (If only one DNS is to be used, it should be written as ['8.8.8.8']).

Run with python main.py
