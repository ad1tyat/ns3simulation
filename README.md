# Assignment 4 README

**NOTE**: Running ns3 simulation requires **python2**, while the analysis scripts use **python3**. Please ensure both are available on the system.  
## Setup of ns3

Download ns3 3.28.1 : https://www.nsnam.org/release/ns-allinone-3.28.1.tar.bz2

Build ns3 by following these instructions https://www.nsnam.org/docs/release/3.28/tutorial/singlehtml/index.html#building-ns3

In the `ns-3.28.1` directory in the file `waf`, change the first line to `#!/usr/bin/env python2` to ensure it is run using python2.

## Compiling simulation.cc

Modify `simulation.cc` by changing line 37 to "0","256", "512","1000" to run experiment for different RTS Thresholds

Copy the `simulation.cc` file into `ns-allinone-3.28.1/ns-3.28.1/scratch/`

Now in the `ns-3.28.1` directory run the following commands :

```bash
./waf --run scratch/simulation
```

## Analysis

Now there will be 4 files produced in this directory itself :

1. Westwood_256.xml (for threshold=256 we have named this .xml see line 206 )
2. AccessPoint-1-0.pcap
3. Station-0-0.pcap
4. Station-2-0.pcap

### Analysing .xml

All relevant files are in `xmls` folder. or you can find them by below instructions :

Copy the following file `ns-3.28.1/src/flow-monitor/examples/flowmon-parse-results.py` and .xml file produced above, into a common directory

Run

```bash
python2 flowmon-parse-results.py Westwood_256.xml
```

You can see the output on terminal now

**Note** : Please ensure both python2 and python3 are installed on your system. The ns3 core uses python2 whilst the packet analysis is done using python3.
### Analysing .pcap 

Scripts are in `scripts/data` folder in submission 

in that folder make a folder named exactly `assignment-4-data`and 4 subfolders named : "0","256", "512","1000". Copy the pcaps in each subfolder. [Or see note below]

The scripts will be run using python3. We will also need to install `dpkt` package.
```bash
pip install dpkt
```

Now to run the scripts:
```bash
python3 gen_ack.py
python3 gen_cts.py
python3 gen_rts.py
python3 gen_tcp_ack_seg.py
```

Now they will produce .txt files which will have labelled data.

Paste the text file data into graph scripts located in `scripts/graph` folder

```
python3 graph_ack.py
python3 graph_cts.py
python3 graph_rts.py
python3 graph_tcp_ack.py
python3 graph_tcp_seg.py
```

Hence we get output of graphs, you can export them in any image or pdf format. 

We have done the above process and saved the txt files and graphs in `/data` and `/graphs` folder in our submission.

**Note** : The pcap files are 1.2 GB in size per experiment so they are uploaded here : https://iitgoffice-my.sharepoint.com/personal/atrivedi_iitg_ac_in/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fatrivedi%5Fiitg%5Fac%5Fin%2FDocuments%2Fcs342%2Fassign4%2Fdata 

All the outputs and graphs are mentioned in report as well. 
