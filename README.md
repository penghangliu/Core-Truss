# Core-Truss

- 'make' to compile

- './nucleus email-Eu-core.txt 11 NO' to run the core and truss decomposition; this will generate Truss_email-Eu-core.txt, P2_email-Eu-core.txt, and P3_email-Eu-core.txt.
  
- 'python P3.py P3_email-Eu-core.txt' to generate VI plot;

- 'python P2.py P2_email-Eu-core.txt to generate EI plot;

- 'python anomaly_detection.py Truss_email-Eu-core.txt' to do the anomaly detection, which generates the elbow plot, the histogram of core number distributions in clusters, and a .csv file containing the outliers.
