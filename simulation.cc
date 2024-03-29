#include "ns3/command-line.h"
#include "ns3/config.h"
#include "ns3/string.h"
#include "ns3/log.h"
#include "ns3/yans-wifi-helper.h"
#include "ns3/ssid.h"
#include "ns3/mobility-helper.h"
#include "ns3/mobility-module.h"
#include "ns3/on-off-helper.h"
#include "ns3/yans-wifi-channel.h"
#include "ns3/mobility-model.h"
#include "ns3/packet-sink.h"
#include "ns3/packet-sink-helper.h"
#include "ns3/tcp-westwood.h"
#include "ns3/internet-stack-helper.h"
#include "ns3/ipv4-address-helper.h"
#include "ns3/ipv4-global-routing-helper.h"
#include "ns3/internet-module.h"
#include "ns3/wifi-module.h"
#include "ns3/flow-monitor.h"
#include "ns3/flow-monitor-module.h"
#include <iostream>
#include <cstdlib>


using namespace ns3;
Ptr<PacketSink> sink;                         /* Pointer to the packet sink application */

int GenerateRandomNumber()
{
  std::srand(time(NULL));
  int x=(std::rand()%5);
  return x+1;
}
void SetDefault(uint32_t payload)
{
  std::string RtsCtsThreshold="256";//there are 4 cases for this
  std::string FragmentationThreshold="1000";
  Config::SetDefault("ns3::WifiRemoteStationManager::RtsCtsThreshold",StringValue(RtsCtsThreshold));
  Config::SetDefault("ns3::WifiRemoteStationManager::FragmentationThreshold",StringValue(FragmentationThreshold));
  Config::SetDefault("ns3::TcpSocket::SegmentSize",UintegerValue(payload));
}
void CalculateThroughput ()
{
  static uint64_t lastTotalRx = 0;
  Time now = Simulator::Now ();                                         /* Return the simulator's virtual time. */
  double cur = (sink->GetTotalRx () - lastTotalRx) * (double) 8 / 1e5;     /* Convert Application RX Packets to MBits. */
  std::cout << now.GetSeconds () << "s: \t" << cur << " Mbit/s" << std::endl;
  lastTotalRx = sink->GetTotalRx ();
  Simulator::Schedule (MilliSeconds (100), &CalculateThroughput);
}

int main(int argc,char *argv[])
{
  uint32_t payload = 1000;                //default 1000bytes in the question
  std::string datarate = "100";           //default taken as 100Mbps
  std::string tcpVariant = "TcpWestwood";
  std::string phyRate = "HtMcs7";
  
  double simulationTime = 50;             //default 50seconds in the question
  SetDefault(payload);
  datarate = datarate + std::string("Mbps");

  Config::SetDefault ("ns3::TcpL4Protocol::SocketType", TypeIdValue (TcpWestwood::GetTypeId ()));
  Config::SetDefault ("ns3::TcpWestwood::ProtocolType", EnumValue (TcpWestwood::WESTWOOD));
  WifiMacHelper mac;
  WifiHelper wifiHelper;
  wifiHelper.SetStandard(WIFI_PHY_STANDARD_80211n_5GHZ);

  // Set up Legacy Channel 
  YansWifiChannelHelper wifichannel;
  wifichannel.SetPropagationDelay("ns3::ConstantSpeedPropagationDelayModel");
  wifichannel.AddPropagationLoss("ns3::FriisPropagationLossModel");

  // Setup Physical Layer 
  YansWifiPhyHelper wifiPhy = YansWifiPhyHelper::Default ();
  wifiPhy.SetChannel (wifichannel.Create ());
  wifiPhy.Set ("TxPowerStart", DoubleValue (100.0));
  wifiPhy.Set ("TxPowerEnd", DoubleValue (100.0));
  wifiPhy.Set ("TxPowerLevels", UintegerValue (1));
  wifiPhy.Set ("TxGain", DoubleValue (0));
  wifiPhy.Set ("RxGain", DoubleValue (0));
  wifiPhy.Set ("RxNoiseFigure", DoubleValue (10));
  wifiPhy.Set ("CcaMode1Threshold", DoubleValue (-79));
  wifiPhy.Set ("EnergyDetectionThreshold", DoubleValue (-79 + 3));
  wifiPhy.SetErrorRateModel ("ns3::YansErrorRateModel");
  wifiHelper.SetRemoteStationManager ("ns3::ConstantRateWifiManager","DataMode", StringValue (phyRate),"ControlMode", StringValue ("HtMcs0"));
  
  NodeContainer apNode,staWifiNode1,staWifiNode2;
  staWifiNode1.Create(1);
  apNode.Create (1);
  staWifiNode2.Create(1);
  Ptr<Node> apWifiNode = apNode.Get(0);
  NodeContainer staWifiNodes;
  staWifiNodes.Add(staWifiNode1);
  staWifiNodes.Add(staWifiNode2);

  // Configure AP 
  Ssid ssid = Ssid ("network");
  mac.SetType ("ns3::ApWifiMac","Ssid", SsidValue (ssid));

  NetDeviceContainer apDevice;
  apDevice = wifiHelper.Install (wifiPhy, mac, apWifiNode);

  // Configure STA 
  mac.SetType ("ns3::StaWifiMac","Ssid", SsidValue (ssid));

  NetDeviceContainer staDevices;
  staDevices = wifiHelper.Install (wifiPhy, mac, staWifiNodes);

  // Mobility model
  MobilityHelper mobility;
  Ptr<ListPositionAllocator> position = CreateObject<ListPositionAllocator> ();
  position->Add (Vector (5.0, 0.0, 0.0));
  position->Add (Vector (5.0, 250.0, 0.0));
  position->Add (Vector (5.0, 500.0, 0.0));
  mobility.SetPositionAllocator(position);
  mobility.SetMobilityModel("ns3::ConstantPositionMobilityModel");
  
  int j=0;
  NodeContainer::Iterator i;
  std::cout<<"Nodes related to mobility in order are:: ";
  for(i= staWifiNodes.Begin(); i!= staWifiNodes.End();++i)
  {
    mobility.Install((*i));
    std::cout<<(*i)<<" ";
    if(j==0)
    {
      mobility.Install(apWifiNode);
      std::cout<<apWifiNode<<" ";
      j++;
    }
    else if(j==1)
    {
      std::cout<<"\n";
    }
  }
  
 // Internet stack 
  InternetStackHelper stack;
  NodeContainer nodes;
  j=0;
  std::cout<<"Nodes related to stack in order are:: ";
  for (i = staWifiNodes.Begin (); i != staWifiNodes.End (); ++i)
  {
    nodes.Add((*i));
    std::cout<<(*i)<<" ";
    if(j==0)
      {
        nodes.Add(apWifiNode);
        std::cout<<apWifiNode<<" ";
        j++;
      }
    else if(j==1)
      std::cout<<"\n";
  }
  stack.Install(nodes);

  Ipv4AddressHelper address;
  address.SetBase ("10.1.1.0", "255.255.255.0");
  Ipv4InterfaceContainer apInterface,staInterface;
  apInterface = address.Assign (apDevice);
  staInterface = address.Assign (staDevices);
  // Populate routing table
  Ipv4GlobalRoutingHelper::PopulateRoutingTables ();

  // Install TCP Receiver on the access point 
  uint16_t portno=9;
  Ipv4Address ipv4=Ipv4Address::GetAny();
  std::string protocol="ns3::TcpSocketFactory";
  Address inetaddress=Address(InetSocketAddress(ipv4,portno));
  PacketSinkHelper sinkHelper (protocol,inetaddress);
  ApplicationContainer sinkApp = sinkHelper.Install (apWifiNode);
  sink = StaticCast<PacketSink> (sinkApp.Get (0));

  // Install TCP Transmitter on the station
  ipv4=apInterface.GetAddress(0);
  inetaddress=Address(InetSocketAddress (ipv4,portno));
  OnOffHelper server (protocol,inetaddress);
  server.SetAttribute ("PacketSize", UintegerValue (payload));
  server.SetAttribute ("OnTime", StringValue ("ns3::ConstantRandomVariable[Constant=1]"));
  server.SetAttribute ("OffTime", StringValue ("ns3::ConstantRandomVariable[Constant=0]"));
  server.SetAttribute ("DataRate", DataRateValue (DataRate (datarate)));
  ApplicationContainer serverApp = server.Install (staWifiNodes);

  //record traffic 
  FlowMonitorHelper fph;
  Ptr<FlowMonitor> fm = fph.InstallAll();

  // Start Applications in random (0,5) create tcp connection between node 1,0/node 2,1
  sinkApp.Start (Seconds (0.0));

  int x= GenerateRandomNumber();
  std::cout<<"Hello!! RandomNumber Generated is:: "<<x<<"\n";
  double x_double=(double)x*1.0;
  serverApp.Start (Seconds (x_double));
  Simulator::Schedule (Seconds (x_double + 0.1), &CalculateThroughput);

  // Using ns3 PCAP for tracing
  wifiPhy.SetPcapDataLinkType (WifiPhyHelper::DLT_IEEE802_11_RADIO);
  wifiPhy.EnablePcap ("AccessPoint", apDevice);
  wifiPhy.EnablePcap ("Station", staDevices);

  Simulator::Stop (Seconds (simulationTime + x_double));
  Simulator::Run ();
  fm->SerializeToXmlFile("Westwood_256.xml",true,true);  
  Simulator::Destroy ();

  return 0;
}