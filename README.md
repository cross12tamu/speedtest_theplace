# The Place and Speed Test
* Run the following script to record speed metrics for ISPs
# Header for CSV:
* `server_name,server_id,latency,jitter,packet_loss,download,upload,download_bytes,upload_bytes,share_url`
* Download column is most interesting, divide by 125000 to have Mbps speed
# Running
When in the scripts directory:
`python run_speedtest.py >> ../log/speedtest_log.csv`
