# Introduction

<p align="justify">An API interface is provided by Ravencoin to make queries. More information can be found here:</p>
https://rvn.cryptoscope.io/api<p><a href="https://rvn.cryptoscope.io/api"></a></p>

<p align="justify">To access the Ravencoin Blockchain directly, a node must be installed and connected to the Ravencoin Mainnet.</p>

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

<h2>Donation</h2>

<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="RNi9cTpobtVErv8H9uijhcafcT4VgEaDUL"><pre><code>RNi9cTpobtVErv8H9uijhcafcT4VgEaDUL</code></pre></div>
