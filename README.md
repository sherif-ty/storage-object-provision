# storage-object-provision
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun Underlined SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">introduction:</span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">This</span><span class="NormalTextRun SCXW79759240 BCX0"> script will create a storage object also will upload and handle files storage location with only one single command.</span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun Underlined SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">details</span></span><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">:</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">The</span><span class="NormalTextRun SCXW79759240 BCX0"> cycle has many layers and steps </span><span class="NormalTextRun SCXW79759240 BCX0">and </span><span class="NormalTextRun SCXW79759240 BCX0">will </span><span class="NormalTextRun SCXW79759240 BCX0">run automatically </span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">step1</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">your local machine or server (windows, mac, or Linux) we will run vagrant up command to run the script from </span><span class="NormalTextRun SpellingErrorV2 SCXW79759240 BCX0">vagrantfile</span><span class="NormalTextRun SCXW79759240 BCX0">. </span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">step2</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">This script is used to build a pair of Ubuntu-based virtual machines that have the MicroK8S setup of Kubernetes.</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">It also installs docker, and sets up aliases for </span><span class="NormalTextRun SpellingErrorV2 SCXW79759240 BCX0">kubectl</span><span class="NormalTextRun SCXW79759240 BCX0"> in line with the MicroK8S documentation.</span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">step 3</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">The</span><span class="NormalTextRun SCXW79759240 BCX0"> script will run shell command in node1 to download and configure Minio server </span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">step4</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">The</span><span class="NormalTextRun SCXW79759240 BCX0"> script will run a shell command in node2 to download python3.8, pip3 and run a shell script to run python with AWS SDK as Minio client </span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">to connect with Minio server and handle the files storage, in this Example, the python script will run function to present file location if the file size &lt; or = 2 Mb</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">will be stored in Minio server Bucket, file size &gt;2 Mb will be stored in AWS S3 Bucket.</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">&nbsp;</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun Underlined SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">Prerequisites:</span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="ListContainerWrapper SCXW79759240 BCX0">
<ul class="BulletListStyle1 SCXW79759240 BCX0">
<li class="OutlineElement Ltr SCXW79759240 BCX0" data-leveltext="" data-font="Symbol" data-listid="1" data-aria-posinset="1" data-aria-level="1">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Install the latest version of Vagrant.</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</li>
<li class="OutlineElement Ltr SCXW79759240 BCX0" data-leveltext="" data-font="Symbol" data-listid="1" data-aria-posinset="2" data-aria-level="1">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Install VirtualBox</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</li>
</ul>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun Underlined SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">Up and Running:</span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">1- clone or Download this Repo.</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">&nbsp;</span><span class="NormalTextRun SCXW79759240 BCX0">2- open Repo location in the terminal and run "vagrant up" command.</span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">&nbsp;</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">#</span><span class="NormalTextRun SCXW79759240 BCX0">Please</span></span><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"> note the whole cycle will be automatic, node1 and node2 will work under the bridge network so while node1 and node2 are provisioning you find a message to select the network you want to connect with (just click on your local or host network number).</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun Underlined SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">Demo Status:</span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<div class="TableContainer SCXW79759240 BCX0">
<div id="{4fadb984-afe4-46f7-82c1-fd3120cb6395}{118}" class="WACAltTextDescribedBy SCXW79759240 BCX0">&nbsp;</div>
<table class="Table  Ltr TableGrid BorderColorBlack TransparentBackgroundColor TableWordWrap SCXW79759240 BCX0" border="1" data-tablestyle="MsoTableGrid" data-tablelook="1696">
<tbody class="SCXW79759240 BCX0">
<tr class="TableRow SCXW79759240 BCX0">
<td class="FirstRow FirstCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Sub task</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="FirstRow SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Status </span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="FirstRow SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">branch</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="FirstRow LastCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">note</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
</tr>
<tr class="TableRow SCXW79759240 BCX0">
<td class="FirstCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Design system and work flow </span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Done</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Master</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="LastCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
</tr>
<tr class="TableRow SCXW79759240 BCX0">
<td class="FirstCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">Configure vagrant </span><span class="NormalTextRun SCXW79759240 BCX0">file (</span><span class="NormalTextRun SCXW79759240 BCX0">OS and network)</span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Done</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Master</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="LastCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
</tr>
<tr class="TableRow SCXW79759240 BCX0">
<td class="FirstCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Configure Kubernetes cluster and node in vagrant file</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Done</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Master</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="LastCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335551550&quot;:2,&quot;335551620&quot;:2,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
</tr>
<tr class="TableRow SCXW79759240 BCX0">
<td class="FirstCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Deploy Minio server script in </span><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="none">Kubernetes node</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">6</span><span class="NormalTextRun SCXW79759240 BCX0">0%</span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Test Branch</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="LastCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="none"><span class="NormalTextRun SCXW79759240 BCX0">Script is Ready but </span><span class="NormalTextRun SCXW79759240 BCX0">needs</span><span class="NormalTextRun SCXW79759240 BCX0"> to insert in vagrant file to run in node </span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
</tr>
<tr class="TableRow SCXW79759240 BCX0">
<td class="FirstCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Deploy python script in </span><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="none"><span class="NormalTextRun SCXW79759240 BCX0">Kubernetes </span><span class="NormalTextRun SCXW79759240 BCX0">node (</span><span class="NormalTextRun SCXW79759240 BCX0">to </span><span class="NormalTextRun SCXW79759240 BCX0">connect</span><span class="NormalTextRun SCXW79759240 BCX0"> s3 and handle files </span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">2</span><span class="NormalTextRun SCXW79759240 BCX0">0</span><span class="NormalTextRun SCXW79759240 BCX0">%</span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Test Branch</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="LastCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
</tr>
<tr class="TableRow SCXW79759240 BCX0">
<td class="FirstCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Create S3 Account to integrate with the system </span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Done</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW79759240 BCX0">Test</span><span class="NormalTextRun SCXW79759240 BCX0"> Branch</span></span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="LastCol SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
</tr>
<tr class="TableRow SCXW79759240 BCX0">
<td class="FirstCol LastRow SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto">Total system integration </span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="LastRow SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"> --- </span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="LastRow SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="TextRun SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"> -----</span><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
<td class="LastCol LastRow SCXW79759240 BCX0" data-celllook="0">
<div class="TableCellContent SCXW79759240 BCX0">
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="OutlineElement Ltr SCXW79759240 BCX0">
<p class="Paragraph SCXW79759240 BCX0" lang="EN-US" xml:lang="EN-US"><span class="EOP SCXW79759240 BCX0" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559739&quot;:160,&quot;335559740&quot;:259}">&nbsp;</span></p>
</div> 
------------------------------------------------------------------------------------------------------------------------


![Slide1](https://user-images.githubusercontent.com/36302233/152698949-c5b99f97-d563-465e-902f-84b0c5cccf5a.jpg)
