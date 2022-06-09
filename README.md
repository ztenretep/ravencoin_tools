# Introduction

<p align="justify">To access the Ravencoin Blockchain directly, a node must be installed and connected to the network. Then follow these steps.</p>

<p align="justify">You can use file 'raven-4.3.2.1-x86_64-linux-gnu.zip' for a basic installation. The node is started via './ravend -daemon -maxconnections=10000'.</p> 

<p align="justify">As soon as the node is connected, the blockchain can be accessed via python-ravencoinlib 0.2.2.</p>

<p align="justify">With the first scripts, I am trying to understand how to interact with the blockchain.</p>

# Set up node

<p align="justify">Select a directory for the operation of the node. Open this directory in a terminal window.</p>

<code>mkdir rvn_node</code>

<code>cd rvn_node</code>

<code>wget https://github.com/RavenProject/Ravencoin/releases/download/v4.3.2.1/raven-4.3.2.1-x86_64-linux-gnu.zip</code>

<code>unzip raven-4.3.2.1-x86_64-linux-gnu.zip</code>
  
<code>cd linux</code>
  
<code>gunzip raven-4.3.2.1-x86_64-linux-gnu.tar.gz</code>
  
<code>tar xf raven-4.3.2.1-x86_64-linux-gnu.tar</code>
  
<code>cd raven-4.3.2.1/bin</code> 
  
<p align="justify">Now we are ready to go.</p>
  
<code>./ravend -daemon -maxconnections=10000</code> 

<p align="justify">The wallet is reachable by:</p>

<code>./raven-qt</code> 
