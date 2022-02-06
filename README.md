# storage-object-provision

<span style="font-size:24px"><u><strong>introduction:</strong></u></span></h2>

<h2><span style="font-size:16px">this script will create a storage object also will upload and handle files storage location with only one single command.</span></h2>

<h2><br />
<u><strong><span style="font-size:20px">details</span>:</strong></u></h2>

<h2><span style="font-size:16px">the cycle has many layers and steps will runs</span></h2>

<p><span style="font-size:16px"><strong>step1</strong></span></p>

<p><span style="font-size:16px">your local machine or server (windows, mac, or Linux) we will run vagrant up command to run the script from vagrantfile.&nbsp;</span></p>

<p><span style="font-size:16px"><strong>step2</strong></span></p>

<p><span style="font-size:16px">This script is used to build a pair of Ubuntu-based virtual machines that have the&nbsp;MicroK8S&nbsp;setup of&nbsp;Kubernetes.</span></p>

<p><span style="font-size:16px">It also installs&nbsp;docker, and sets up aliases for kubectl in line with the MicroK8S documentation.</span></p>

<p><strong><span style="font-size:16px">step 3</span></strong></p>

<p><span style="font-size:16px">the script will run shell command in node1 to download and configure Minio server&nbsp;</span></p>

<p><strong><span style="font-size:16px">step4</span></strong></p>

<p><span style="font-size:16px">the script will run a shell command in node2 to download python3.8, pip3 and run a shell script to run python with AWS SDK as Minio client&nbsp;</span></p>

<p><span style="font-size:16px">to connect with Minio server and handle the files storage, in this Example, the python script will run function to present file location if the file size &lt; or = 2 Mb</span></p>

<p><span style="font-size:16px">will&nbsp;be stored in Minio server Bucket,&nbsp;file size &gt;2 Mb will&nbsp;be stored in AWS S3 Bucket.</span></p>

<p><br />
<u><strong><span style="font-size:22px">Prerequisites:</span></strong></u></p>

<p><span style="font-size:16px">Install the latest version of&nbsp;Vagrant.<br />
Install&nbsp;VirtualBox<br />
Up and Running:</span></p>

<p><span style="font-size:16px">1- clone or Download this Repo.</span></p>

<p><span style="font-size:16px">2- open Repo location in the terminal and run &quot;vagrant up&quot; command.</span></p>

<p><span style="font-size:16px">#please note the whole cycle will be automatic, node1 and node2 will work under the bridge network so while node1 and node2 are provisioning you find a message to select the network you want to connect with (just click on your local or host network number).</span></p>

------------------------------------------------------------------------------------------------------------------------


![Slide1](https://user-images.githubusercontent.com/36302233/152698949-c5b99f97-d563-465e-902f-84b0c5cccf5a.jpg)
