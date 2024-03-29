<html>
<head> 
</head>
<body>
<h1>0x19. Postmortem </h1>
<h2>Issue Summary:</h2> 
<p>
<b>Duration:</b> August 10, 2023, 10:00 AM EST - August 10, 2023, 2:00 PM EST
<b>Impact:</b> The EBC Facebook Page experienced a service outage, rendering it inaccessible to users. During this period, users were unable to view or interact with the page. Approximately 95% of the page's followers were affected.
</p>
<h3>Root Cause:</h3> 
<p>
The root cause of the outage was a misconfigured caching mechanism in the backend server of the EBC Facebook Page. This misconfiguration led to an unexpected buildup of cached data, causing the server to become unresponsive.
</p>
<h3>Timeline:</h3> 
<ul>
<li>10:00 AM EST: The outage was detected when an automated monitoring alert indicated a sudden increase in server response times.</li>
<li> 10:15 AM EST: The engineering team began investigating the issue, suspecting a potential problem with the server's performance.</li>
<li> 10:30 AM EST: Initial assumptions pointed towards a potential database bottleneck, prompting a deeper investigation into database performance.</li>
<li> 11:00 AM EST: Database performance was determined to be within acceptable parameters, redirecting the investigation towards the application layer.</li>
<li> 11:30 AM EST: The team identified unusual caching behavior and realized that the cache wasn't being purged properly, leading to a cache overflow.</li>
<li> 12:00 PM EST: Incorrect assumptions about a possible DDoS attack were discarded, and focus shifted to cache management.</li>
<li> 12:30 PM EST: The incident was escalated to the DevOps lead and the System Engineering team for further assistance.</li>
<li> 1:00 PM EST: The misconfigured caching mechanism was isolated as the root cause of the issue.</li>
<li> 2:00 PM EST: The EBC Facebook Page service was successfully restored after reconfiguring the caching system and purging the accumulated cache.
</li>
</ul>
<h3>Root Cause and Resolution:</h3> 
<p>
<b>Root Cause:</b> The misconfigured caching mechanism resulted from an erroneous change to the caching settings, causing cache buildup.
<b>Resolution:</b> The caching mechanism was reconfigured to ensure proper cache purging intervals. The accumulated cache was cleared, and the server's performance was restored.</p>
<h3>Corrective and Preventative Measures:</h3> 
<ul>
<li>Implement stricter version control for server configuration changes to prevent unauthorized or erroneous modifications.</li>
<li> Enhance monitoring alerts to provide more specific details about server performance anomalies, aiding in quicker root cause identification.</li>
<li> Implement automated cache management procedures to ensure timely and effective cache purging.</li>
<li> Develop and maintain a comprehensive documentation repository for server configurations and changes.</li>
</ul>
<h3>Tasks to Address the Issue:</h3> 
<ul>
<li> Review and update the caching configuration to prevent cache overflow.</li>
<li> Implement a regular cache purging schedule to prevent similar incidents.</li>
<li> Enhance monitoring and alerting systems to promptly detect and notify unusual caching behavior.</li>
<li>Conduct a comprehensive review of all server configurations to identify and rectify potential misconfigurations.</li>
<li> Update the incident response plan to include clear escalation paths and responsibilities.</li>
</ul>



