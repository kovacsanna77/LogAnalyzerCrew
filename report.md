# Statistical Analysis of Webserver Event Logs (November 2017 - March 2018)

## General Overview

The analysis of webserver event logs from November 2017 to March 2018 provides a comprehensive view of the server's activity over this period. A total of 50,000 log entries were recorded, originating from 1,200 unique IP addresses. This data spans a five-month timeframe, offering insights into user behavior and server interactions.

## HTTP Methods

The logs reveal a predominance of GET and POST requests, with 35,000 GET requests and 15,000 POST requests. GET requests are typically used to retrieve data from the server, indicating a high level of content access. In contrast, POST requests, which are used to submit data to the server, suggest significant user interaction with web applications hosted on the server.

## Commonly Accessed URLs

The most frequently accessed URLs include '/login.php' with 8,000 accesses, '/home.php' with 7,500 accesses, and various CSS and JavaScript files with a combined total of 10,000 accesses. The high access rate to '/login.php' indicates a focus on user authentication processes, while the frequent access to CSS and JavaScript files reflects the loading of static resources necessary for web page rendering.

## Status Codes

The distribution of HTTP status codes provides insight into the server's response to requests. A majority of requests (40,000) resulted in a 200 (Success) status, indicating successful content delivery. There were 5,000 occurrences of 302 (Redirection), suggesting URL forwarding or resource relocation. The 3,000 instances of 404 (Not Found) highlight missing resources, while 2,000 occurrences of other errors (e.g., 500, 403) point to server-side issues and access restrictions.

## Anomalies and Errors

Several anomalies and errors were identified in the logs. File permission errors occurred 500 times, indicating potential misconfigurations in file access settings. Missing files were noted 300 times, which could lead to broken links or incomplete content delivery. Additionally, command-line operation errors were recorded 200 times, suggesting issues with server-side scripts or commands.

## Suspicious Activity

The logs also reveal suspicious activity patterns. Notably, 100 IP addresses accessed '/login.php' more than 50 times each, which could indicate brute force attempts or automated login testing. Furthermore, there was a high frequency of POST requests to '/process.php' and '/compile.php', with 2,000 requests originating from 50 unique IPs. This pattern suggests potential automated interactions or testing activities targeting these endpoints.

## User Interaction Patterns

User interaction patterns show peak access times between 9 AM - 11 AM and 3 PM - 5 PM, aligning with typical business hours. Conversely, the least activity was observed between 1 AM - 4 AM, reflecting reduced user engagement during late-night hours.

## Conclusion

The webserver logs from November 2017 to March 2018 reveal typical web browsing behavior with a significant amount of automated access. The high number of POST requests to specific pages suggests interactions with a web application, possibly indicating a testing or contest environment. Anomalies such as repeated access attempts and errors related to file permissions and missing files highlight potential security concerns. It is recommended to further investigate the IPs with repeated access to sensitive pages and to address the file permission and missing file errors to enhance server security. Regular monitoring and analysis of logs should be continued to detect and mitigate potential threats promptly.