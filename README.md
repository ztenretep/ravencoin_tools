# Introduction

<p align="justify">
Ravencoin is different from Tron and Tezos, which I have examined so far. With the latter, access to the blockchain is possible without further problems. In order to access the blockchain of Ravencoin, the operation of a Ravencoin node is necessary. Installation is simple and operation is possible on a standard personal computer. However, some time is needed to synchronise the complete blockchain. In the meantime, 4 years of data have to be synchronised. With the help of raven-qt, the progress can be easily displayed. 
</p>

<p align="justify">
While I am currently testing the RPC interface, I am installing a Ravencoin mining pool in parallel to test if and how mining is possible on a personal computer via the Ravencoin node. The installation and setup has already worked so far. The node, mining pool and miner still need to be made to work together.
</p>

# Programming Requirements

<p align="justify">Following PyPi library is used for the Python scripts:</p>

<code>python-ravencoinlib 0.2.2</code>

# Set Up Ravencoin Node

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

<p align="justify">The QT Ravencoin wallet is reachable by:</p>

<code>./raven-qt -server</code> 

<p align="justify">Finally, set symbolic links:</p>

<pre><code>ln -s ~/rvn_node/linux/raven-4.3.2.1/bin/ravend /usr/bin/ravend
ln -s ~/rvn_node/linux/raven-4.3.2.1/bin/raven-qt /usr/bin/raven-qt</code></pre>

<p align="justify">Run raven-qt detached from terminal window:</p>

<code>nohup ~/rvn_node/linux/raven-4.3.2.1/bin/raven-qt & > /dev/null 2>&1</code>

<p align="justify">Up to this, you do not have to take care about the content of <code>raven.conf</code>.</p>

# References

https://ravencoin.org/

https://raven.wiki/

https://www.ravennodes.com/

# Donation

<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="RNi9cTpobtVErv8H9uijhcafcT4VgEaDUL"><pre><code>RNi9cTpobtVErv8H9uijhcafcT4VgEaDUL</code></pre></div>
